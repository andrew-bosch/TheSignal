#!/usr/bin/env python3
"""
seed_comp_verbs.py
THE SIGNAL — Seed comp_verb_phase and comp_verb_role for DB-41 / DB-40 additions.
"""

import sys
import subprocess

DB = "the_signal_db"

def execute_sql(sql):
    result = subprocess.run(
        ["mysql", DB],
        input=sql, text=True, capture_output=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"DB execution failed:\n{result.stderr.strip()}")
    return result.stdout

def main():
    sql = []
    sql.append("START TRANSACTION;")

    # Helper function to generate INSERT statements
    def add_phase(comp_id, verb_id, phase_id, note=""):
        note_val = f"'{note}'" if note else "NULL"
        sql.append(f"INSERT IGNORE INTO comp_verb_phase (component_id, verb_id, phase_id, notes) VALUES ({comp_id}, {verb_id}, {phase_id}, {note_val});")

    def add_role(comp_id, verb_id, role_id, phase_id, note=""):
        note_val = f"'{note}'" if note else "NULL"
        sql.append(f"INSERT IGNORE INTO comp_verb_role (component_id, verb_id, role_id, phase_id, notes) VALUES ({comp_id}, {verb_id}, {role_id}, {phase_id}, {note_val});")

    def seed_standard_roles(comp_id, verb_id, is_arbiter_only=False):
        if is_arbiter_only:
            add_role(comp_id, verb_id, 2, 1) # ARBITER initiator
            add_role(comp_id, verb_id, 2, 2) # ARBITER executor
            add_role(comp_id, verb_id, 2, 3) # ARBITER fulfiller
        else:
            add_role(comp_id, verb_id, 1, 1) # Faction initiator
            add_role(comp_id, verb_id, 1, 2) # Faction executor
            add_role(comp_id, verb_id, 2, 3) # ARBITER fulfiller

    # 1. d10 (id 119) — Add, Remove, Move, Flip
    # rolled/used during covert resolution (8, 14), political resolution (17), Battlefield Strength (19)
    for verb in [1, 2, 15, 16]: # Add, Remove, Flip, Move
        for phase in [8, 14, 17, 19]:
            add_phase(119, verb, phase)
        seed_standard_roles(119, verb, is_arbiter_only=True)

    # 2. Modifier token (id 47) — Flip
    # flipped in modifier resolution (7, 13)
    add_phase(47, 15, 7)
    add_phase(47, 15, 13)
    seed_standard_roles(47, 15, is_arbiter_only=True)

    # 3. ARBITER Threshold Slider (id 106) — Add, Remove, Move, Corrupt
    # Corrupt in 8, 14, 17. Add in 1, Remove in 20, Move in 8, 14, 17
    add_phase(106, 1, 1) # Add
    add_phase(106, 2, 20) # Remove
    for phase in [8, 14, 17]:
        add_phase(106, 16, phase) # Move
        add_phase(106, 13, phase) # Corrupt
    for verb in [1, 2, 16, 13]:
        seed_standard_roles(106, verb, is_arbiter_only=True)

    # 4. Faction Threshold Slider (id 107) — Add, Remove, Move, Corrupt
    add_phase(107, 1, 1) # Add
    add_phase(107, 2, 20) # Remove
    for phase in [8, 14, 17]:
        add_phase(107, 16, phase) # Move
        add_phase(107, 13, phase) # Corrupt
    for verb in [1, 2, 16, 13]:
        seed_standard_roles(107, verb, is_arbiter_only=False)

    # 5. Faction hand (id 94) — Add, Remove, Move, Reveal, Conceal, Corrupt
    # Add, Remove, Move, Reveal, Conceal across active phases
    hand_phases = [1, 3, 4, 8, 9, 10, 14, 15, 16, 17, 20]
    for verb in [1, 2, 16, 10, 14]:
        for phase in hand_phases:
            add_phase(94, verb, phase)
        seed_standard_roles(94, verb, is_arbiter_only=False)
    # Corrupt in covert/political resolution (8, 14, 17)
    for phase in [8, 14, 17]:
        add_phase(94, 13, phase)
    seed_standard_roles(94, 13, is_arbiter_only=False)

    # 6. Operative Pool (id 116) — Add, Remove, Move, Reveal, Conceal, Corrupt
    # init-only verbs in phase 1
    for verb in [1, 2, 16, 10, 14]:
        add_phase(116, verb, 1)
        seed_standard_roles(116, verb, is_arbiter_only=False)
    # Corrupt in 8, 14, 17
    for phase in [8, 14, 17]:
        add_phase(116, 13, phase)
    seed_standard_roles(116, 13, is_arbiter_only=False)

    # 7. Card containers (decks, discards)
    # Ring 1/2/3 modifier decks (53, 54, 55): Add(1), Remove(20), Move(7, 13), Reveal(7, 13), Conceal(1)
    for deck_id in [53, 54, 55]:
        add_phase(deck_id, 1, 1)
        add_phase(deck_id, 2, 20)
        for phase in [7, 13]:
            add_phase(deck_id, 16, phase)
            add_phase(deck_id, 10, phase)
        add_phase(deck_id, 14, 1)
        for verb in [1, 2, 16, 10, 14]:
            seed_standard_roles(deck_id, verb, is_arbiter_only=True)

    # Broadcast Deck (86), Broadcast Effect Deck (87), Broadcast Discard (109), Broadcast Effect Discard (110)
    # Add(1), Remove(20), Move(1, 18), Reveal(1, 18), Conceal(1)
    for deck_id in [86, 87, 109, 110]:
        add_phase(deck_id, 1, 1)
        add_phase(deck_id, 2, 20)
        for phase in [1, 18]:
            add_phase(deck_id, 16, phase)
            add_phase(deck_id, 10, phase)
        add_phase(deck_id, 14, 1)
        for verb in [1, 2, 16, 10, 14]:
            seed_standard_roles(deck_id, verb, is_arbiter_only=True)

    # Faction modifier deck (89)
    # Add(1), Remove(20), Move(7, 13, 17), Reveal(7, 13, 17), Conceal(1)
    add_phase(89, 1, 1)
    add_phase(89, 2, 20)
    for phase in [7, 13, 17]:
        add_phase(89, 16, phase)
        add_phase(89, 10, phase)
    add_phase(89, 14, 1)
    for verb in [1, 2, 16, 10, 14]:
        seed_standard_roles(89, verb, is_arbiter_only=False)

    # Covert operation deck (92), Covert operation discard (93)
    # Add(1), Remove(20), Move(8, 14), Reveal(8, 14), Conceal(1)
    for deck_id in [92, 93]:
        add_phase(deck_id, 1, 1)
        add_phase(deck_id, 2, 20)
        for phase in [8, 14]:
            add_phase(deck_id, 16, phase)
            add_phase(deck_id, 10, phase)
        add_phase(deck_id, 14, 1)
        for verb in [1, 2, 16, 10, 14]:
            seed_standard_roles(deck_id, verb, is_arbiter_only=False)

    # Political act deck (90), Political act discard (91)
    # Add(1), Remove(20), Move(15, 17), Reveal(15, 17), Conceal(1)
    for deck_id in [90, 91]:
        add_phase(deck_id, 1, 1)
        add_phase(deck_id, 2, 20)
        for phase in [15, 17]:
            add_phase(deck_id, 16, phase)
            add_phase(deck_id, 10, phase)
        add_phase(deck_id, 14, 1)
        for verb in [1, 2, 16, 10, 14]:
            seed_standard_roles(deck_id, verb, is_arbiter_only=False)

    # Covert Operation Card Set (114), Political Act Card Set (115), Classified Directives Pool (118)
    # Add(1), Remove(1), Move(1), Reveal(1), Conceal(1)
    for deck_id in [114, 115, 118]:
        for verb in [1, 2, 16, 10, 14]:
            add_phase(deck_id, verb, 1)
            seed_standard_roles(deck_id, verb, is_arbiter_only=False)

    # Apex Ability Pool (117)
    for verb in [1, 2, 16, 10, 14]:
        add_phase(117, verb, 1)
        seed_standard_roles(117, verb, is_arbiter_only=True)

    # 8. DB-40 / DB-41 components
    # DebriefActionCard (100) — Add, Remove, Move, Reveal, Conceal, Corrupt
    # Add in 8, 14. Remove in 20. Move in 8, 14, 20. Reveal in 20. Conceal in 8, 14. Corrupt in 8, 14, 20
    for phase in [8, 14]:
        add_phase(100, 1, phase)
        add_phase(100, 14, phase)
    add_phase(100, 2, 20)
    add_phase(100, 10, 20)
    for phase in [8, 14, 20]:
        add_phase(100, 16, phase)
        add_phase(100, 13, phase)
    for verb in [1, 2, 16, 10, 14, 13]:
        seed_standard_roles(100, verb, is_arbiter_only=True)

    # Intel Delivery Slip (96) — Reveal(10) in 20, Conceal(14) in 8, 14
    add_phase(96, 10, 20)
    for phase in [8, 14]:
        add_phase(96, 14, phase)
    # Roles for 96 are already seeded, but adding standard ones is safe
    seed_standard_roles(96, 10, is_arbiter_only=False)
    seed_standard_roles(96, 14, is_arbiter_only=False)

    # Notification Slip (95) — Reveal(10) in 8, 14, Conceal(14) in 8, 14
    for phase in [8, 14]:
        add_phase(95, 10, phase)
        add_phase(95, 14, phase)
    seed_standard_roles(95, 10, is_arbiter_only=True)
    seed_standard_roles(95, 14, is_arbiter_only=True)

    # Grant Deed (113) — Reveal(10) in 20, Conceal(14) in 20
    add_phase(113, 10, 20)
    add_phase(113, 14, 20)
    seed_standard_roles(113, 10, is_arbiter_only=False)
    seed_standard_roles(113, 14, is_arbiter_only=False)

    sql.append("COMMIT;")
    sql_text = "\n".join(sql)

    try:
        execute_sql(sql_text)
        print("Successfully seeded comp_verb_phase and comp_verb_role entries!")
    except Exception as e:
        print(f"Error executing SQL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
