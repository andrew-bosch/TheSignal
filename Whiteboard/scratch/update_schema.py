import sys
import datetime

def main():
    file_path = "/home/abosch/Projects/TheSignal/Database/schema_reference.md"
    
    with open(file_path, "r") as f:
        lines = f.readlines()
        
    # We will find the line for ### component and insert our schema definition before it.
    insert_idx = -1
    for i, line in enumerate(lines):
        if line.startswith("### component") and "### component_metadata" not in line and "### component_dim" not in line:
            insert_idx = i
            break
            
    schema_block = """### district_adjacency
Defines the bidirectional connectivity rules between physical district zones, utilizing a native composite key of the district's structural ring and orbital position.

| Column | Type | Description |
|---|---|---|
| `origin_ring` | TINYINT | The Ring level (0-3) of the starting district. |
| `origin_position` | TINYINT | The orbital index of the starting district within its ring. |
| `origin_district_name` | VARCHAR | String name of the origin district. |
| `adjacent_ring` | TINYINT | The Ring level (0-3) of the connected district. |
| `adjacent_position` | TINYINT | The orbital index of the connected district within its ring. |
| `adjacent_district_name` | VARCHAR | String name of the connected district. |
| `allow_ingress` | BOOLEAN | Whether movement is allowed INTO adjacent. |
| `allow_egress` | BOOLEAN | Whether movement is allowed FROM adjacent. |

**Primary Key:** (`origin_ring`, `origin_position`, `adjacent_ring`, `adjacent_position`)

"""

    if insert_idx != -1:
        lines.insert(insert_idx, schema_block)
        
    # Also append a changelog entry to the DB list at the bottom.
    changelog_idx = -1
    for i in range(len(lines)-1, -1, -1):
        if "- **DB-09**" in lines[i]:
            changelog_idx = i
            break
            
    if changelog_idx != -1:
        log_entry = "- **DB-27** ✅ (agy): `district_adjacency` migrated to composite (`ring`, `position`) schema. Dropped reliance on arbitrary 1-21 IDs in favor of intrinsic location identifiers. Re-seeded from updated Art 01 rules.\n"
        lines.insert(changelog_idx + 1, log_entry)

    with open(file_path, "w") as f:
        f.writelines(lines)
        
    print(f"Updated {file_path}")

if __name__ == "__main__":
    main()
