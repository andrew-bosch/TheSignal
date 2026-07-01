import os

def main():
    # Define the connections. Note that the table in MD is usually symmetric, or just lists all outward/inward for each origin.
    # The existing table had a row for every directed edge, e.g. 21->17, 21->18 etc. And also 18->21, 18->17 etc.
    # Let's build the full set of bidirectional edges.
    
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
        4: ("Ring 3", "Industrial Fringe"),
        6: ("Ring 3", "Transit Hub"),
        7: ("Ring 3", "Civic Center"),
        3: ("Ring 3", "Residential Quarter"),
        1: ("Ring 3", "University Perimeter"),
        2: ("Ring 3", "Media District"),
        8: ("Ring 3", "Broadcast Tower"),
        9: ("Ring 3", "Observation Post"),
        5: ("Ring 3", "Commercial Strip")
    }

    # Order of origin nodes from original MD (for consistency, mostly Ring 0 -> Ring 1 -> Ring 2 -> Ring 3, grouped)
    origin_order = [21, 18, 17, 19, 20, 16, 10, 14, 15, 12, 13, 11, 4, 6, 7, 3, 1, 2, 8, 9, 5]

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

    lines = []
    lines.append("| Ring | Origin # | Origin District | Adjacent # | Adjacent Ring | Allow Ingress | Allow Egress |")
    lines.append("|------|---------|----------------|-----------|--------------|--------------|-------------|")
    
    for origin in origin_order:
        o_ring, o_name = nodes[origin]
        neighbors = adj[origin]
        # sort neighbors by ring, then by ID to look neat, or leave as is. Let's just output them as they are in the lists or sort them.
        # Actually let's sort by adjacent ring (0 to 3) then by adjacent number to be deterministic and tidy.
        def sort_key(n):
            ring_num = int(nodes[n][0].split(" ")[1])
            return (ring_num, n)
        
        neighbors.sort(key=sort_key)
        
        for n in neighbors:
            n_ring, n_name = nodes[n]
            lines.append(f"| {o_ring} | {origin} | {o_name} | {n} | {n_ring} | TRUE | TRUE |")

    with open("/home/abosch/Projects/TheSignal/Whiteboard/scratch/new_table.md", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("Table written to /home/abosch/Projects/TheSignal/Whiteboard/scratch/new_table.md")

if __name__ == "__main__":
    main()
