#!/usr/bin/env python3
"""
register_component.py
THE SIGNAL — Register a new component across the full 5-table tmp_ cascade.

Usage:
  python3 register_component.py component.yaml             # dry run: prints SQL only
  python3 register_component.py component.yaml --execute   # runs against the_signal_db

YAML format — see Database/component_template.yaml for a working example.
"""

import sys
import yaml
import subprocess
import textwrap
from pathlib import Path

DB = "the_signal_db"


# ── DB helpers ────────────────────────────────────────────────────────────────

def query(sql):
    """Run a SELECT and return list of row dicts."""
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


def load_lookup(sql, key_col=1, val_col=0):
    """Return {name: id} dict from a two-column query result."""
    return {row[key_col]: int(row[val_col]) for row in query(sql)}


def execute_sql(sql):
    result = subprocess.run(
        ["mysql", DB],
        input=sql, text=True, capture_output=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"DB execution failed:\n{result.stderr.strip()}")
    return result.stdout


# ── Lookup tables ─────────────────────────────────────────────────────────────

def load_lookups():
    verbs      = load_lookup("SELECT id, name FROM verb")
    beats      = load_lookup("SELECT id, name FROM quarter_phase")
    roles      = load_lookup("SELECT id, name FROM player_role")
    phases     = load_lookup("SELECT id, name FROM role_phase")
    components = load_lookup("SELECT id, name FROM component")

    # trigger_type: key = "type.subtype" or "type" if subtype is NULL
    trigger_rows = query("SELECT id, type, subtype FROM trigger_type")
    triggers = {}
    for row in trigger_rows:
        tid, ttype, tsub = int(row[0]), row[1], row[2] if row[2] != "NULL" else None
        key = f"{ttype}.{tsub}" if tsub else ttype
        triggers[key] = tid

    return {
        "verbs":      verbs,
        "beats":      beats,
        "roles":      roles,
        "phases":     phases,
        "components": components,
        "triggers":   triggers,
    }



# ── Validation ────────────────────────────────────────────────────────────────

def resolve(name, lookup, label):
    if name not in lookup:
        available = sorted(lookup.keys())
        raise ValueError(
            f"Unknown {label}: '{name}'\n"
            f"  Available: {available}"
        )
    return lookup[name]


def bool_to_int(val):
    if isinstance(val, bool):
        return 1 if val else 0
    if isinstance(val, str):
        if val.lower() in ("true", "yes", "1"):
            return 1
        if val.lower() in ("false", "no", "0"):
            return 0
        raise ValueError(f"Cannot convert to bool: {val!r}")
    return int(val)


# ── SQL generation ────────────────────────────────────────────────────────────

def esc(s):
    """Minimal SQL string escape."""
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"


def build_sql(cfg, lk):
    lines = ["START TRANSACTION;", ""]

    name = cfg["name"]
    actionable          = bool_to_int(cfg.get("actionable", 1))
    transformable       = bool_to_int(cfg.get("transformable", 0))
    receivable          = bool_to_int(cfg.get("receivable", 0))
    transform_visibility = bool_to_int(cfg.get("transform_visibility", 0))
    transform_orientation = bool_to_int(cfg.get("transform_orientation", 0))
    transform_data      = bool_to_int(cfg.get("transform_data", 0))

    parent_id = "NULL"
    if "parent_component" in cfg:
        parent_id = resolve(cfg["parent_component"], lk["components"], "parent component")

    # Step 1 — component
    lines.append("-- Step 1: Register component")
    lines.append(
        f"INSERT INTO component "
        f"(name, parent_component_id, actionable, transformable, receivable, "
        f"transform_visibility, transform_orientation, transform_data) VALUES "
        f"({esc(name)}, {parent_id}, {actionable}, {transformable}, {receivable}, "
        f"{transform_visibility}, {transform_orientation}, {transform_data});"
    )
    lines.append("SET @comp_id = LAST_INSERT_ID();")
    
    # Step 1b — component_dim & component_type
    lines.append("-- Step 1b: Register metadata")
    desc = cfg.get("description", "No description provided")
    ctype = cfg.get("component_type", "other")
    lines.append(f"INSERT INTO component_dim (component_id, description) VALUES (@comp_id, {esc(desc)});")
    lines.append(f"INSERT INTO component_type (component_id, component_type) VALUES (@comp_id, {esc(ctype)});")
    lines.append("")

    # Step 2 — comp_verb_phase
    verb_beats = cfg.get("verbs", [])
    if verb_beats:
        lines.append("-- Step 2: Seed phase coverage (comp_verb_phase)")
        for entry in verb_beats:
            verb_id = resolve(entry["verb"], lk["verbs"], "verb")
            for beat_name in entry["beats"]:
                beat_id = resolve(beat_name, lk["beats"], "beat")
                note = esc(entry.get("notes"))
                lines.append(
                    f"INSERT INTO comp_verb_phase (component_id, verb_id, phase_id, notes) "
                    f"VALUES (@comp_id, {verb_id}, {beat_id}, {note});"
                )
        lines.append("")

    # Step 3 — comp_verb_role
    role_assignments = cfg.get("roles", [])
    if role_assignments:
        lines.append("-- Step 3: Seed role assignments (comp_verb_role)")
        for entry in role_assignments:
            verb_id  = resolve(entry["verb"], lk["verbs"], "verb")
            role_id  = resolve(entry["player_role"], lk["roles"], "player_role")
            phase_id = resolve(entry["phase"], lk["phases"], "phase")
            note     = esc(entry.get("notes"))
            lines.append(
                f"INSERT INTO comp_verb_role (component_id, verb_id, role_id, phase_id, notes) "
                f"VALUES (@comp_id, {verb_id}, {role_id}, {phase_id}, {note});"
            )
        lines.append("")

    # Step 4 — action
    primitives = cfg.get("primitives", [])
    if primitives:
        lines.append("-- Step 4: Seed action primitives (action)")
        for prim in primitives:
            beat_id    = resolve(prim["beat"], lk["beats"], "beat")
            subject_id = resolve(prim["subject"], lk["roles"], "subject (player_role)")
            verb_id    = resolve(prim["verb"], lk["verbs"], "verb")
            trigger_id = resolve(prim["trigger"], lk["triggers"], "trigger")
            bt         = esc(prim.get("beat_trigger", "during"))
            notes      = esc(prim.get("notes"))
            lines.append(
                f"INSERT INTO action "
                f"(phase_id, beat_trigger, trigger_type_id, subject_id, verb_id, component_id, notes) "
                f"VALUES ({beat_id}, {bt}, {trigger_id}, {subject_id}, {verb_id}, @comp_id, {notes});"
            )
        lines.append("")

    # Step 5 — subject_target
    targets = cfg.get("targets", [])
    if targets:
        lines.append("-- Step 5: Seed placement targets (subject_target)")
        for target_name in targets:
            target_id = resolve(target_name, lk["components"], "target component")
            lines.append(
                f"INSERT INTO subject_target (subject_id, target_id) "
                f"VALUES (@comp_id, {target_id});"
            )
        lines.append("")

    lines.append("COMMIT;")
    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    yaml_path = Path(args[0])
    execute = "--execute" in args

    if not yaml_path.exists():
        print(f"Error: file not found: {yaml_path}", file=sys.stderr)
        sys.exit(1)

    with open(yaml_path) as f:
        cfg = yaml.safe_load(f)

    print(f"Loading lookups from {DB}...")
    try:
        lk = load_lookups()
    except RuntimeError as e:
        print(f"Error connecting to DB: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Building SQL for: {cfg['name']}")
    try:
        sql = build_sql(cfg, lk)
    except ValueError as e:
        print(f"\nValidation error:\n  {e}", file=sys.stderr)
        sys.exit(1)

    print()
    print("─" * 60)
    print(sql)
    print("─" * 60)
    print()

    if execute:
        confirm = input(f"Execute against {DB}? (yes/N): ").strip()
        if confirm != "yes":
            print("Aborted.")
            sys.exit(0)
        try:
            execute_sql(sql)
            print(f"Done. '{cfg['name']}' registered successfully.")
        except RuntimeError as e:
            print(f"Execution failed:\n{e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Dry run — SQL printed above. Pass --execute to run.")


if __name__ == "__main__":
    main()
