#!/usr/bin/env python3
"""
seed_component_metadata.py
THE SIGNAL — Parse components from V1/02___Components.md and seed component_metadata table.

Usage:
  python3 seed_component_metadata.py             # dry run: prints SQL statements
  python3 seed_component_metadata.py --execute   # executes against the_signal_db
"""

import sys
import re
import subprocess
from pathlib import Path

DB = "the_signal_db"
COMPONENTS_FILE = Path("/home/abosch/Projects/TheSignal/V1/02___Components.md")

header_re = re.compile(r'^###\s+(.+?)\s+\(DB:\s*(\d+)\)')
table_row_re = re.compile(r'^\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|')
int_re = re.compile(r'\d+')

def query(sql):
    result = subprocess.run(
        ["mysql", DB, "-B", "--skip-column-names", "-e", sql],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"DB query failed: {result.stderr.strip()}")
    rows = []
    for line in result.stdout.strip().splitlines():
        if line:
            rows.append(line.split("\t"))
    return rows

def load_existing_components():
    rows = query("SELECT id FROM component")
    return {int(row[0]) for row in rows}

def clean_val(val):
    val = val.strip()
    val = val.strip("`'*_")
    if val.upper() in ("N/A", "NONE", "NULL", ""):
        return None
    return val

def parse_max_placement_ref(val):
    val = clean_val(val)
    if not val:
        return None
    db_match = re.search(r'DB:\s*(\d+)', val, re.IGNORECASE)
    if db_match:
        return int(db_match.group(1))
    return None

def parse_max_placement_count(val):
    val = clean_val(val)
    if not val:
        return None
    int_match = int_re.search(val)
    if int_match:
        return int(int_match.group(0))
    return None

def parse_visibility(val):
    val = clean_val(val)
    if not val:
        return 'Public'
    val_lower = val.lower()
    if 'player-private' in val_lower or 'private' in val_lower:
        return 'Player-private'
    if 'arbiter-only' in val_lower or 'arbiter' in val_lower:
        return 'ARBITER-only'
    if 'variable' in val_lower:
        return 'Variable'
    return 'Public'

def parse_faction_keyed(val):
    val = clean_val(val)
    if not val:
        return 'N/A'
    val_lower = val.lower()
    if val_lower.startswith('yes'):
        return 'Yes'
    if val_lower.startswith('no'):
        return 'No'
    return 'N/A'

def parse_privacy_model(val):
    val = clean_val(val)
    if not val:
        return None
    val_lower = val.lower()
    if 'arbiter-private' in val_lower:
        return 'ARBITER-private'
    if 'faction-private' in val_lower:
        return 'Faction-private'
    if 'open' in val_lower:
        return 'Open'
    return None

def parse_back_design(val):
    val = clean_val(val)
    if not val:
        return None
    val_lower = val.lower()
    if 'faction-keyed' in val_lower:
        return 'Faction-keyed'
    if 'arbiter-keyed' in val_lower:
        return 'ARBITER-keyed'
    if 'neutral' in val_lower:
        return 'Neutral'
    return None

def parse_card_source(val):
    val = clean_val(val)
    if not val:
        return None
    val_lower = val.lower()
    if 'deck' in val_lower:
        return 'Deck'
    if 'hand' in val_lower:
        return 'Hand'
    if 'arbiter supply' in val_lower or 'arbiter' in val_lower:
        return 'ARBITER supply'
    if 'sealed' in val_lower:
        return 'Sealed'
    return None

def esc(s):
    if s is None:
        return "NULL"
    escaped = str(s).replace("\\", "\\\\").replace("'", "''")
    return "'" + escaped + "'"

def parse_metadata():
    with open(COMPONENTS_FILE, "r") as f:
        lines = f.readlines()

    components = []
    current_comp = None

    for line in lines:
        line = line.strip()
        h_match = header_re.match(line)
        if h_match:
            if current_comp:
                components.append(current_comp)
            current_comp = {
                "name": h_match.group(1).strip(),
                "id": int(h_match.group(2)),
                "fields": {}
            }
            continue

        if current_comp:
            row_match = table_row_re.match(line)
            if row_match:
                field = row_match.group(1).strip(" `*")
                val = row_match.group(2).strip()
                if field.lower() in ("field", "------", "value", ":---", "---:"):
                    continue
                current_comp["fields"][field] = val

    if current_comp:
        components.append(current_comp)

    return components

def main():
    execute = "--execute" in sys.argv
    existing_ids = load_existing_components()
    comps = parse_metadata()

    sql_statements = ["START TRANSACTION;", "DELETE FROM component_metadata;"]

    for c in comps:
        db_id = c["id"]
        if db_id not in existing_ids:
            print(f"-- Skip parsed component {db_id} ({c['name']}) - not registered in component table")
            continue

        fields = c["fields"]

        # Universal fields
        # Note: quantity_expr and physical_form are NOT NULL; if value is N/A/empty, write 'N/A'
        physical_form = clean_val(fields.get("physical_form", "")) or 'N/A'
        quantity_expr = clean_val(fields.get("quantity", "")) or 'N/A'
        visibility = parse_visibility(fields.get("visibility", ""))
        states = clean_val(fields.get("states", ""))
        faction_keyed = parse_faction_keyed(fields.get("faction_keyed", ""))
        max_placement_count = parse_max_placement_count(fields.get("max_placement_count", ""))
        max_placement_ref = parse_max_placement_ref(fields.get("max_placement_ref", ""))

        # Ensure max_placement_ref points to an existing component
        if max_placement_ref and max_placement_ref not in existing_ids:
            print(f"-- Warning: Component {db_id} placement ref {max_placement_ref} not found in DB. Set to NULL.")
            max_placement_ref = None

        # Group-specific fields
        privacy_model = parse_privacy_model(fields.get("privacy_model", ""))
        display_fields = clean_val(fields.get("display_fields", ""))
        back_design = parse_back_design(fields.get("back_design", ""))
        card_source = parse_card_source(fields.get("card_source", ""))
        recorded_fields = clean_val(fields.get("recorded_fields", ""))
        function_prose = clean_val(fields.get("function", ""))
        scale_prose = clean_val(fields.get("scale", ""))
        init_value_prose = clean_val(fields.get("init_value", ""))

        stmt = (
            f"INSERT INTO component_metadata ("
            f"component_id, physical_form, quantity_expr, visibility, states, faction_keyed, "
            f"max_placement_count, max_placement_ref, privacy_model, "
            f"display_fields, back_design, card_source, recorded_fields, function_prose, "
            f"scale_prose, init_value_prose"
            f") VALUES ("
            f"{db_id}, {esc(physical_form)}, {esc(quantity_expr)}, {esc(visibility)}, {esc(states)}, {esc(faction_keyed)}, "
            f"{esc(max_placement_count)}, {esc(max_placement_ref)}, {esc(privacy_model)}, "
            f"{esc(display_fields)}, {esc(back_design)}, {esc(card_source)}, {esc(recorded_fields)}, {esc(function_prose)}, "
            f"{esc(scale_prose)}, {esc(init_value_prose)}"
            f");"
        )
        sql_statements.append(stmt)

    sql_statements.append("COMMIT;")
    sql_text = "\n".join(sql_statements)

    if execute:
        print(f"Executing {len(sql_statements) - 3} metadata insertions against {DB}...")
        result = subprocess.run(
            ["mysql", DB],
            input=sql_text, text=True, capture_output=True
        )
        if result.returncode != 0:
            print("Execution failed!")
            print(result.stderr)
            sys.exit(1)
        print("Success!")
    else:
        print(sql_text)
        print(f"\nDry run complete. Found {len(comps)} components parsed from Markdown.")
        print("Run with --execute to commit to the database.")

if __name__ == "__main__":
    main()
