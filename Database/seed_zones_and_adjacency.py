def main():
    print("SET FOREIGN_KEY_CHECKS=0;")
    print("DELETE FROM district_adjacency;")
    print("DELETE FROM game_zones;")
    print("SET FOREIGN_KEY_CHECKS=1;")
    
    # 1. Insert Core Meta Zones
    print("INSERT INTO game_zones (id, zone_name, parent_zone_id) VALUES (1, 'Game Box', NULL);")
    print("INSERT INTO game_zones (id, zone_name, parent_zone_id) VALUES (2, 'Chairs', NULL);")
    print("INSERT INTO game_zones (id, zone_name, parent_zone_id) VALUES (3, 'Table', NULL);")
    
    # Insert P1-P6 Areas (Parent = Table)
    for i in range(1, 7):
        print(f"INSERT INTO game_zones (id, zone_name, parent_zone_id) VALUES ({3+i}, 'P{i} Area', 3);")
        
    # Insert Central Area (10) and City (11) hierarchy
    print("INSERT INTO game_zones (id, zone_name, parent_zone_id) VALUES (10, 'Central Area', 3);")
    print("INSERT INTO game_zones (id, zone_name, parent_zone_id) VALUES (11, 'City', 10);")

    # 2. Insert Rings (Parent = City (11), IDs = 500-503)
    rings = ['Ring 0', 'Ring 1', 'Ring 2', 'Ring 3']
    ring_ids = {r: 500+i for i, r in enumerate(rings)}
    for r, rid in ring_ids.items():
        print(f"INSERT INTO game_zones (id, zone_name, parent_zone_id) VALUES ({rid}, '{r}', 11);")

    # 3. Insert Districts (Parent = Rings, IDs = 600+)
    nodes = {
        21: (0, 0, "Chorus Node", 1),
        18: (1, 0, "Military Installation", 2),
        17: (1, 1, "Government Citadel", 5),
        19: (1, 2, "Chorus Research", 1),
        20: (1, 3, "Financial Sanctum", 3),
        16: (2, 0, "Regulatory District", 5),
        10: (2, 1, "Power Grid", 4),
        14: (2, 2, "Logistics Center", 4),
        15: (2, 3, "Research Institute", 1),
        12: (2, 4, "Data Exchange", 1),
        13: (2, 5, "Communications Hub", 2),
        11: (2, 6, "Financial Clearinghouse", 3),
        4:  (3, 0, "Industrial Fringe", 4),
        6:  (3, 1, "Transit Hub", 4),
        7:  (3, 2, "Civic Center", 5),
        3:  (3, 3, "Residential Quarter", 5),
        1:  (3, 4, "University Perimeter", 1),
        2:  (3, 5, "Media District", 2),
        8:  (3, 6, "Broadcast Tower", 2),
        9:  (3, 7, "Observation Post", 2),
        5:  (3, 8, "Commercial Strip", 3)
    }

    curr_id = 600
    district_db_ids = {}
    
    for old_id, (ring, pos, name, res_id) in nodes.items():
        parent_id = ring_ids[f"Ring {ring}"]
        print(f"INSERT INTO game_zones (id, zone_name, parent_zone_id, position, resource_type_id) VALUES ({curr_id}, '{name}', {parent_id}, {pos}, {res_id});")
        district_db_ids[old_id] = curr_id
        curr_id += 1

    # 4. Insert Adjacencies
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
    
    for origin_old, neighbors in adj.items():
        origin_db = district_db_ids[origin_old]
        for n_old in neighbors:
            n_db = district_db_ids[n_old]
            print(f"INSERT IGNORE INTO district_adjacency (district_id, adjacent_district_id, allow_ingress, allow_egress) VALUES ({origin_db}, {n_db}, 1, 1);")

if __name__ == "__main__":
    main()
