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
    
    # Generate all rows
    rows = []
    
    for origin, neighbors in adj.items():
        o_ring, o_name = nodes[origin]
        o_addr = addresses[origin]
        o_pos = int(o_addr.split(".")[1])
        
        for n in neighbors:
            n_ring, n_name = nodes[n]
            n_addr = addresses[n]
            n_pos = int(n_addr.split(".")[1])
            
            rows.append({
                'o_ring': o_ring,
                'o_pos': o_pos,
                'o_addr': o_addr,
                'o_name': o_name,
                'n_ring': n_ring,
                'n_pos': n_pos,
                'n_addr': n_addr,
                'n_name': n_name,
            })
            
    # Sort by origin_ring, origin_position, adjacent_ring, adjacent_position
    rows.sort(key=lambda r: (r['o_ring'], r['o_pos'], r['n_ring'], r['n_pos']))
    
    lines = []
    lines.append("| Ring | Address | Origin District | Adjacent Address | Adjacent District | Adjacent Ring | Allow Ingress | Allow Egress |")
    lines.append("|------|---------|----------------|-----------------|-------------------|--------------|--------------|-------------|")
    
    for r in rows:
        lines.append(f"| Ring {r['o_ring']} | {r['o_addr']} | {r['o_name']} | {r['n_addr']} | {r['n_name']} | Ring {r['n_ring']} | TRUE | TRUE |")

    new_table_str = "\n".join(lines) + "\n"

    # UPDATE MD FILE
    file_path = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(file_path, "r") as f:
        md_lines = f.readlines()
        
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(md_lines):
        if line.startswith("| Ring | Address | Origin District | Adjacent Address | Adjacent District |"):
            start_idx = i
        if start_idx != -1 and i > start_idx and line.strip() == "":
            end_idx = i
            break
            
    if start_idx != -1 and end_idx != -1:
        new_md_lines = md_lines[:start_idx] + [new_table_str + "\n"] + md_lines[end_idx:]
        with open(file_path, "w") as f:
            f.writelines(new_md_lines)
        print(f"Successfully reordered and updated table in {file_path}")
    else:
        print("Error: Could not find table to replace in MD file!")

if __name__ == "__main__":
    main()
