import re
import os

def main():
    print("SET FOREIGN_KEY_CHECKS=0;")
    print("DELETE FROM district_adjacency;")
    print("DELETE FROM game_zones;")
    print("SET FOREIGN_KEY_CHECKS=1;")
    
    zones = [
        (1, 'Game Box', 'NULL'),
        (2, 'Chairs', 'NULL'),
        (3, 'Table', 'NULL'),
        (4, 'P1-P5 Areas', 3), # simplified for DB seeding
        (5, 'ARBITER Area', 3),
        (6, 'Central Area', 3),
        (7, 'Supply', 6),
        (8, 'Accord Placement Area', 6),
        (9, 'Session Timeline Area', 6),
        (10, 'Initiative Strip Area', 6),
        (11, 'Chorus Activity Track Area', 6),
        (12, 'Situation Report Area', 6),
        (13, 'Public Standing Track Area', 6),
        (14, 'City', 6),
        (15, 'Ring 0', 14),
        (16, 'Ring 1', 14),
        (17, 'Ring 2', 14),
        (18, 'Ring 3', 14),
        (19, 'Ring 1 Modifier Area', 6), # User explicitly noted not on city map
        (20, 'Ring 2 Modifier Area', 6),
        (21, 'Ring 3 Modifier Area', 6)
    ]
    
    for zid, zname, zparent in zones:
        print(f"INSERT INTO game_zones (id, zone_name, parent_zone_id) VALUES ({zid}, '{zname}', {zparent});")
        
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
        parent_id = 15 + ring
        print(f"INSERT INTO game_zones (id, zone_name, parent_zone_id, position, resource_type_id) VALUES ({curr_id}, '{name}', {parent_id}, {pos}, {res_id});")
        district_db_ids[old_id] = curr_id
        curr_id += 1

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

    # Update Markdown for Modifiers
    md_file = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(md_file, "r") as f:
        content = f.read()
    
    # Change parent_zone_id of Modifiers to `zone_central_area`
    content = content.replace("`zone_ring_1` | `Public` |", "`zone_central_area` | `Public` |")
    content = content.replace("`zone_ring_2` | `Public` |", "`zone_central_area` | `Public` |")
    content = content.replace("`zone_ring_3` | `Public` |", "`zone_central_area` | `Public` |")
    
    with open(md_file, "w") as f:
        f.write(content)

if __name__ == "__main__":
    main()
