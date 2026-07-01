import sys

def main():
    addresses = {
        21: "0.0", 
        18: "1.0", 17: "1.1", 19: "1.2", 20: "1.3", 
        16: "2.0", 10: "2.1", 14: "2.2", 15: "2.3", 12: "2.4", 13: "2.5", 11: "2.6", 
        4:  "3.0", 6:  "3.1", 7:  "3.2", 3:  "3.3", 1:  "3.4", 2:  "3.5", 8:  "3.6", 9:  "3.7", 5:  "3.8"
    }
    
    nodes = {
        21: (0, "Chorus Node"),
        18: (1, "Military Installation"),
        17: (1, "Government Citadel"),
        19: (1, "Chorus Research"),
        20: (1, "Financial Sanctum"),
        16: (2, "Regulatory District"),
        10: (2, "Power Grid"),
        14: (2, "Logistics Center"),
        15: (2, "Research Institute"),
        12: (2, "Data Exchange"),
        13: (2, "Communications Hub"),
        11: (2, "Financial Clearinghouse"),
        4:  (3, "Industrial Fringe"),
        6:  (3, "Transit Hub"),
        7:  (3, "Civic Center"),
        3:  (3, "Residential Quarter"),
        1:  (3, "University Perimeter"),
        2:  (3, "Media District"),
        8:  (3, "Broadcast Tower"),
        9:  (3, "Observation Post"),
        5:  (3, "Commercial Strip")
    }

    adj = {
        21: [18, 17, 19, 20],
        18: [21, 17, 16, 10],
        17: [21, 18, 19, 10, 14, 15],
        19: [21, 17, 20, 15, 12, 13],
        20: [21, 19, 13, 11],
        16: [18, 10, 4, 6],
        10: [18, 17, 16, 14, 6, 7],
        14: [17, 10, 15, 7, 3],
        15: [17, 19, 14, 12, 3, 1, 2],
        12: [19, 15, 13, 2, 8],
        13: [19, 20, 12, 11, 8, 9],
        11: [20, 13, 9, 5],
        4: [16, 6],
        6: [16, 10, 4, 7],
        7: [10, 14, 6, 3],
        3: [14, 15, 7, 1],
        1: [15, 3, 2],
        2: [15, 12, 1, 8],
        8: [12, 13, 2, 9],
        9: [13, 11, 8, 5],
        5: [11, 9]
    }
    
    origin_order = [21, 18, 17, 19, 20, 16, 10, 14, 15, 12, 13, 11, 4, 6, 7, 3, 1, 2, 8, 9, 5]

    lines = []
    lines.append("| Ring | Address | Origin District | Adjacent Address | Adjacent District | Adjacent Ring | Allow Ingress | Allow Egress |")
    lines.append("|------|---------|----------------|-----------------|-------------------|--------------|--------------|-------------|")
    
    sql_lines = []
    sql_lines.append("DROP TABLE IF EXISTS district_adjacency;")
    sql_lines.append("""
CREATE TABLE district_adjacency (
    origin_ring TINYINT NOT NULL,
    origin_position TINYINT NOT NULL,
    origin_district_name VARCHAR(255) NOT NULL,
    adjacent_ring TINYINT NOT NULL,
    adjacent_position TINYINT NOT NULL,
    adjacent_district_name VARCHAR(255) NOT NULL,
    allow_ingress BOOLEAN DEFAULT TRUE,
    allow_egress BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (origin_ring, origin_position, adjacent_ring, adjacent_position)
);
""")

    for origin in origin_order:
        o_ring, o_name = nodes[origin]
        o_addr = addresses[origin]
        o_pos = int(o_addr.split(".")[1])
        neighbors = adj[origin]
        
        def sort_key(n):
            return (nodes[n][0], n)
        
        neighbors.sort(key=sort_key)
        
        for n in neighbors:
            n_ring, n_name = nodes[n]
            n_addr = addresses[n]
            n_pos = int(n_addr.split(".")[1])
            
            lines.append(f"| Ring {o_ring} | {o_addr} | {o_name} | {n_addr} | {n_name} | Ring {n_ring} | TRUE | TRUE |")
            
            sql_lines.append(f'INSERT INTO district_adjacency (origin_ring, origin_position, origin_district_name, adjacent_ring, adjacent_position, adjacent_district_name, allow_ingress, allow_egress) VALUES ({o_ring}, {o_pos}, "{o_name}", {n_ring}, {n_pos}, "{n_name}", 1, 1);')

    new_table_str = "\n".join(lines) + "\n"
    
    with open("/home/abosch/Projects/TheSignal/Whiteboard/scratch/migrate_adjacency.sql", "w") as f:
        f.write("\n".join(sql_lines) + "\n")
    print("Generated SQL migration script.")

    # UPDATE MD FILE
    file_path = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(file_path, "r") as f:
        md_lines = f.readlines()
        
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(md_lines):
        if line.startswith("| Ring | Origin # | Origin District |"):
            start_idx = i
        if start_idx != -1 and i > start_idx and line.strip() == "":
            end_idx = i
            break
            
    if start_idx != -1 and end_idx != -1:
        new_md_lines = md_lines[:start_idx] + [new_table_str + "\n"] + md_lines[end_idx:]
        with open(file_path, "w") as f:
            f.writelines(new_md_lines)
        print(f"Updated table in {file_path}")
    else:
        print("Error: Could not find table to replace in MD file!")

    # UPDATE SVG FILE
    svg_path = "/home/abosch/Projects/TheSignal/V1/NM_Overlay.svg"
    with open(svg_path, "r") as f:
        svg_content = f.read()

    replacements = [
        ("Military Inst.</tspan><tspan x=\"461\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 1</tspan>", "Military Inst.</tspan><tspan x=\"461\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 1.0</tspan>"),
        ("Govmt. Citadel</tspan><tspan x=\"542\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 1</tspan>", "Govmt. Citadel</tspan><tspan x=\"542\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 1.1</tspan>"),
        ("Chorus Research.</tspan><tspan x=\"658\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 1</tspan>", "Chorus Research.</tspan><tspan x=\"658\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 1.2</tspan>"),
        ("Fin. Sanctum</tspan><tspan x=\"739\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 1</tspan>", "Fin. Sanctum</tspan><tspan x=\"739\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 1.3</tspan>"),
        ("Regulatory</tspan><tspan x=\"323\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 2</tspan>", "Regulatory</tspan><tspan x=\"323\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 2.0</tspan>"),
        ("Power Grid</tspan><tspan x=\"383\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 2</tspan>", "Power Grid</tspan><tspan x=\"383\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 2.1</tspan>"),
        ("Logistics Ctr.</tspan><tspan x=\"481\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 2</tspan>", "Logistics Ctr.</tspan><tspan x=\"481\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 2.2</tspan>"),
        ("Research Inst.</tspan><tspan x=\"600\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 2</tspan>", "Research Inst.</tspan><tspan x=\"600\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 2.3</tspan>"),
        ("Data Exchange</tspan><tspan x=\"719\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 2</tspan>", "Data Exchange</tspan><tspan x=\"719\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 2.4</tspan>"),
        ("Comms Hub</tspan><tspan x=\"817\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 2</tspan>", "Comms Hub</tspan><tspan x=\"817\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 2.5</tspan>"),
        ("Fin. Clearinghouse</tspan><tspan x=\"876\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 2</tspan>", "Fin. Clearinghouse</tspan><tspan x=\"876\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 2.6</tspan>"),
        ("Industrial Fringe</tspan><tspan x=\"147\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 3</tspan>", "Industrial Fringe</tspan><tspan x=\"147\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 3.0</tspan>"),
        ("Transit Hub</tspan><tspan x=\"216\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 3</tspan>", "Transit Hub</tspan><tspan x=\"216\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 3.1</tspan>"),
        ("Civic Center</tspan><tspan x=\"321\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 3</tspan>", "Civic Center</tspan><tspan x=\"321\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 3.2</tspan>"),
        ("Residential</tspan><tspan x=\"454\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 3</tspan>", "Residential</tspan><tspan x=\"454\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 3.3</tspan>"),
        ("Univ. Perimeter</tspan><tspan x=\"600\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 3</tspan>", "Univ. Perimeter</tspan><tspan x=\"600\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 3.4</tspan>"),
        ("Media Dist.</tspan><tspan x=\"746\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 3</tspan>", "Media Dist.</tspan><tspan x=\"746\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 3.5</tspan>"),
        ("Broadcast Tower</tspan><tspan x=\"878\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 3</tspan>", "Broadcast Tower</tspan><tspan x=\"878\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 3.6</tspan>"),
        ("Observation Post</tspan><tspan x=\"983\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 3</tspan>", "Observation Post</tspan><tspan x=\"983\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 3.7</tspan>"),
        ("Commerce Strip</tspan><tspan x=\"1052\" dy=\"16\" font-size=\"9\" fill=\"#e0e6ed\">GEN: 3</tspan>", "Commerce Strip</tspan><tspan x=\"1052\" dy=\"16\" font-size=\"8\" fill=\"#e0e6ed\">ADD: 3.8</tspan>"),
        ("<tspan x=\"600\" dy=\"16\" font-size=\"9\">GEN: 0</tspan>", "<tspan x=\"600\" dy=\"16\" font-size=\"8\">ADD: 0.0</tspan>")
    ]
    
    new_svg = svg_content
    for old, new in replacements:
        if old not in new_svg:
            print(f"Warning: could not find {old}")
        new_svg = new_svg.replace(old, new)
        
    with open(svg_path, "w") as f:
        f.write(new_svg)
    print(f"Updated SVG in {svg_path}")

if __name__ == "__main__":
    main()
