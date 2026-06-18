#!/usr/bin/env python3
"""
Art 04 sweeps: 04-n30/31 (persistence_condition/effect=None),
04-n78 (Card Story blocks), 04-n69 (checklist rows).
Safe to re-run: all insertions check for existing content first.

Usage:
  python3 art04_sweep.py --dry-run   # report counts, no file write
  python3 art04_sweep.py             # apply changes
"""

import re
import sys

DRY_RUN = '--dry-run' in sys.argv
INPUT = '/home/abosch/Projects/TheSignal/V1/04___Card_System.md'

with open(INPUT, 'r') as f:
    lines = f.readlines()

result = []
i = 0
n = len(lines)

# ── State ─────────────────────────────────────────────────────────────────
card_has_story        = False   # set by #### Card Story, reset at **Design checklist:**
in_python_block       = False   # inside ```python ... ```
in_checklist_context  = False   # True from **Design checklist:** until table ends
in_checklist_table    = False   # True while processing | rows
checklist_has_data_schema    = False
checklist_has_card_narrative = False
past_preamble = False           # True after line 550 (card specs start ~598)

stats = {
    'persistence_pairs_added': 0,
    'card_stories_added':      0,
    'data_schema_rows_added':  0,
    'card_narrative_rows_added': 0,
}

# ── Main loop ─────────────────────────────────────────────────────────────
while i < n:
    line = lines[i]
    stripped = line.rstrip('\n').rstrip()

    if not past_preamble and i > 550:
        past_preamble = True

    # ── Python block boundaries ──────────────────────────────────────────
    if stripped == '```python':
        in_python_block = True
        result.append(line)
        i += 1
        continue

    if stripped == '```' and in_python_block:
        in_python_block = False
        result.append(line)
        i += 1
        continue

    # ── Inside python block: handle persistence fields (n30 + n31) ───────
    if in_python_block:
        m = re.match(r'^(\s+)persistence\b\s*=\s*(.+)', line)
        if m:
            indent     = m.group(1)
            value_raw  = m.group(2).rstrip().rstrip(',')
            is_permanent = value_raw.startswith('Permanent')

            # Look ahead: is next non-blank line already persistence_condition?
            j = i + 1
            while j < n and lines[j].strip() == '':
                j += 1
            already_done = j < n and 'persistence_condition' in lines[j]

            result.append(line)
            i += 1

            if not is_permanent and not already_done:
                result.append(f'{indent}persistence_condition = None,\n')
                result.append(f'{indent}persistence_effect    = None,\n')
                stats['persistence_pairs_added'] += 1
            continue

        result.append(line)
        i += 1
        continue

    # ── Preamble (§1–§5): pass through unchanged ─────────────────────────
    if not past_preamble:
        result.append(line)
        i += 1
        continue

    # ── Card Story detection ─────────────────────────────────────────────
    if stripped == '#### Card Story':
        card_has_story = True
        result.append(line)
        i += 1
        continue

    # ── Design checklist header ──────────────────────────────────────────
    if stripped == '**Design checklist:**':
        if not card_has_story:
            result.append('#### Card Story\n')
            result.append('⚠ Story pending 04-n79.\n')
            result.append('\n')
            card_has_story = True
            stats['card_stories_added'] += 1

        # Reset for next card
        card_has_story = False

        # Set up checklist tracking
        in_checklist_context         = True
        in_checklist_table           = False
        checklist_has_data_schema    = False
        checklist_has_card_narrative = False

        result.append(line)
        i += 1
        continue

    # ── Checklist table rows ─────────────────────────────────────────────
    if in_checklist_context and line.startswith('|'):
        in_checklist_table = True

        if '| Data schema validation |' in line:
            checklist_has_data_schema = True
        if '| Card narrative |' in line:
            checklist_has_card_narrative = True

        result.append(line)
        i += 1
        continue

    # ── End of checklist table (non-| line after | rows have started) ────
    if in_checklist_table and not line.startswith('|'):
        if not checklist_has_data_schema:
            result.append('| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |\n')
            checklist_has_data_schema = True
            stats['data_schema_rows_added'] += 1
        if not checklist_has_card_narrative:
            result.append('| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |\n')
            checklist_has_card_narrative = True
            stats['card_narrative_rows_added'] += 1
        in_checklist_table  = False
        in_checklist_context = False

    result.append(line)
    i += 1

# ── Final flush (safety net) ──────────────────────────────────────────────
if in_checklist_table:
    if not checklist_has_data_schema:
        result.append('| Data schema validation | ⚠ | Pending 04-n70 | Art 04 §6.1–§6.3 |\n')
        stats['data_schema_rows_added'] += 1
    if not checklist_has_card_narrative:
        result.append('| Card narrative | ⚠ | Pending 04-n79 | Art 04 §5 P26 |\n')
        stats['card_narrative_rows_added'] += 1

# ── Report ────────────────────────────────────────────────────────────────
print(f"Input:  {n} lines")
print(f"Output: {len(result)} lines")
print(f"Delta:  +{len(result) - n} lines")
print(f"\nStats:")
for k, v in stats.items():
    print(f"  {k}: {v}")

if not DRY_RUN:
    with open(INPUT, 'w') as f:
        f.writelines(result)
    print("\n✓ File written.")
else:
    print("\n[DRY RUN — no changes written]")
