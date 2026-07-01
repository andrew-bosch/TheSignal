import re

def main():
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
    
    md_file = "/home/abosch/Projects/TheSignal/V1/01___Game_Board_New_Meridian.md"
    with open(md_file, "r") as f:
        content = f.read()

    for old_id, (ring, pos, name, res_id) in nodes.items():
        new_db_id = curr_id
        
        # Replace the header: ##### Chorus Node (DB: 21) -> ##### Chorus Node (DB: 600)
        content = re.sub(
            rf"(##### {re.escape(name)} \(DB:\s*){old_id}(\))", 
            rf"\g<1>{new_db_id}\g<2>", 
            content
        )
        
        # Replace the table row immediately following the header:
        # Match from the new header down to the db_id row
        pattern = rf"(##### {re.escape(name)} \(DB: {new_db_id}\).*?\|\s*`db_id`\s*\|\s*){old_id}(\s*\|)"
        content = re.sub(pattern, rf"\g<1>{new_db_id}\g<2>", content, flags=re.DOTALL)
        
        curr_id += 1
        
    with open(md_file, "w") as f:
        f.write(content)
        
    print("Markdown file updated successfully.")

if __name__ == "__main__":
    main()
