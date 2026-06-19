#!/usr/bin/env python3
"""
verify_matrix.py
THE SIGNAL — Compare v_comp_verb_matrix output against V1/02___Components.md applicable_verbs.
"""

import sys
import re
import subprocess
from pathlib import Path

DB = "the_signal_db"
COMPONENTS_FILE = Path("/home/abosch/Projects/TheSignal/V1/02___Components.md")

header_re = re.compile(r'^###\s+(.+?)\s+\(DB:\s*(\d+)\)')
table_row_re = re.compile(r'^\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|')

def query(sql):
    result = subprocess.run(
        ["mysql", DB, "-B", "-e", sql],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"DB query failed: {result.stderr.strip()}")
    
    lines = result.stdout.strip().splitlines()
    if not lines:
        return []
    
    headers = lines[0].split("\t")
    rows = []
    for line in lines[1:]:
        rows.append(dict(zip(headers, line.split("\t"))))
    return rows

def parse_markdown_verbs():
    with open(COMPONENTS_FILE, "r") as f:
        lines = f.readlines()

    components = {}
    current_comp = None

    for line in lines:
        line = line.strip()
        h_match = header_re.match(line)
        if h_match:
            current_comp = int(h_match.group(2))
            components[current_comp] = {
                "name": h_match.group(1).strip(),
                "verbs": set()
            }
            continue

        if current_comp is not None:
            row_match = table_row_re.match(line)
            if row_match:
                field = row_match.group(1).strip(" `*")
                val = row_match.group(2).strip()
                if field.lower() in ("field", "------", "value", ":---", "---:"):
                    continue
                if field.lower() == "applicable_verbs":
                    verbs = [v.strip() for v in val.split(";")]
                    for v in verbs:
                        v_clean = v.strip("`*_ ")
                        if v_clean and v_clean.upper() != "N/A":
                            # Ignore comments like "N/A — agent, not a physical component"
                            if "N/A" not in v_clean:
                                components[current_comp]["verbs"].add(v_clean)

    return components

def main():
    db_rows = query("SELECT c.id, c.name, m.* FROM v_comp_verb_matrix m JOIN component c ON m.component = c.name")
    db_matrix = {int(row["id"]): row for row in db_rows}

    md_comps = parse_markdown_verbs()

    mismatches = 0
    checked_count = 0

    print(f"Comparing {len(db_rows)} database components with Markdown entries...\n")

    for db_id, md_info in md_comps.items():
        name = md_info["name"]
        
        if db_id not in db_matrix:
            print(f"Warning: Component '{name}' (ID {db_id}) in markdown but not in database view v_comp_verb_matrix (likely actionable=0)")
            continue

        db_row = db_matrix[db_id]
        checked_count += 1

        # Check verbs: Add, Remove, Move, Reveal, Conceal, Flip, Corrupt
        verb_mapping = {
            "Add": int(db_row.get("Add", 0)),
            "Remove": int(db_row.get("Remove", 0)),
            "Move": int(db_row.get("Move", 0)),
            "Reveal": int(db_row.get("Reveal", 0)),
            "Conceal": int(db_row.get("Conceal", 0)),
            "Flip": int(db_row.get("Flip", 0)),
            "Corrupt": int(db_row.get("Corrupt", 0))
        }

        md_verbs = md_info["verbs"]

        # Special case: in v_comp_verb_matrix, Add and Remove are hardcoded to 1 for all actionable components
        # Let's see if there are mismatches between MD and DB
        diff_db_only = []
        diff_md_only = []

        for verb, val in verb_mapping.items():
            db_has = (val == 1)
            md_has = (verb in md_verbs)

            if db_has and not md_has:
                # Add/Remove are hardcoded in the view, so expect some of those to be DB-only
                if verb in ("Add", "Remove"):
                    continue
                diff_db_only.append(verb)
            elif md_has and not db_has:
                diff_md_only.append(verb)

        if diff_db_only or diff_md_only:
            print(f"Mismatch for component '{name}' (ID {db_id}):")
            print(f"  Markdown verbs: {sorted(list(md_verbs))}")
            print(f"  Database verbs: {[v for v, val in verb_mapping.items() if val == 1]}")
            if diff_db_only:
                print(f"  DB-only (not in MD): {diff_db_only}")
            if diff_md_only:
                print(f"  MD-only (not in DB): {diff_md_only}")
            print()
            mismatches += 1

    print(f"Verification complete. Checked {checked_count} components. Found {mismatches} mismatches.")

if __name__ == "__main__":
    main()
