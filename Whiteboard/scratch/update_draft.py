import sys

def main():
    addresses = {
        21: "0.0", 
        18: "1.0", 17: "1.1", 19: "1.2", 20: "1.3", 
        16: "2.0", 10: "2.1", 14: "2.2", 15: "2.3", 12: "2.4", 13: "2.5", 11: "2.6", 
        4:  "3.0", 6:  "3.1", 7:  "3.2", 3:  "3.3", 1:  "3.4", 2:  "3.5", 8:  "3.6", 9:  "3.7", 5:  "3.8"
    }
    
    nodes = {
        21: ("Ring 0", "Chorus Node"),
        18: ("Ring 1", "Military Installation"),
        17: ("Ring 1", "Government Citadel"),
        19: ("Ring 1", "Chorus Research"),
        20: ("Ring 1", "Financial Sanctum"),
        16: ("Ring 2", "Regulatory District"),
        10: ("Ring 2", "Power Grid"),
        14: ("Ring 2", "Logistics Center"),
        15: ("Ring 2", "Research Institute"),
        12: ("Ring 2", "Data Exchange"),
        13: ("Ring 2", "Communications Hub"),
        11: ("Ring 2", "Financial Clearinghouse"),
        4:  ("Ring 3", "Industrial Fringe"),
        6:  ("Ring 3", "Transit Hub"),
        7:  ("Ring 3", "Civic Center"),
        3:  ("Ring 3", "Residential Quarter"),
        1:  ("Ring 3", "University Perimeter"),
        2:  ("Ring 3", "Media District"),
        8:  ("Ring 3", "Broadcast Tower"),
        9:  ("Ring 3", "Observation Post"),
        5:  ("Ring 3", "Commercial Strip")
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
    
    for origin in origin_order:
        o_ring, o_name = nodes[origin]
        o_addr = addresses[origin]
        neighbors = adj[origin]
        
        def sort_key(n):
            ring_num = int(nodes[n][0].split(" ")[1])
            return (ring_num, n)
        
        neighbors.sort(key=sort_key)
        
        for n in neighbors:
            n_ring, n_name = nodes[n]
            n_addr = addresses[n]
            lines.append(f"| {o_ring} | {o_addr} | {o_name} | {n_addr} | {n_name} | {n_ring} | TRUE | TRUE |")

    with open("/home/abosch/Projects/TheSignal/Whiteboard/scratch/draft_table.md", "w") as f:
        f.write("\n".join(lines) + "\n")
        
    print("Draft updated in scratch folder.")

if __name__ == "__main__":
    main()
