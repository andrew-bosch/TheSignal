#!/usr/bin/env python3
"""
04-n183 (part 1) — scaffold value_rating=None onto every CA/PA card spec.
value_rating moved from Modifier-subclass-only to base Card() class (S143).
Modifier subclass cards (ModActionCard/ModBattleCard/ModReactCard) already
carry value_rating elsewhere in their block — this sweep only touches plain
`= Card(` blocks (CA/PA), inserting the field right after `doctrine_mod=`,
matching its declared position in the base class (Part1_Core.md).

Idempotent: skips any block that already contains value_rating.

Usage:
  python3 value_rating_sweep.py --dry-run   # report counts, no file write
  python3 value_rating_sweep.py             # apply changes
"""

import re
import sys

DRY_RUN = '--dry-run' in sys.argv
FILES = [
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part2_Standard.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part4a_Guild.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part4b_Ghost.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part4c_Directorate.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part4d_Network.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part4e_Syndicate.md',
]

BLOCK_START = re.compile(r'^\w[\w.]*\s*=\s*Card\(\s*$')
BLOCK_END = re.compile(r'^\)\s*$')
DOCTRINE_LINE = re.compile(r'^\s+.*\bdoctrine_mod\s*=')

total_inserted = 0
total_skipped_already_present = 0

for path in FILES:
    with open(path, 'r') as f:
        lines = f.readlines()

    result = []
    in_block = False
    block_has_value_rating = False
    block_lines_buffer = []  # buffered lines of current block, flushed at block end
    inserted_this_file = 0
    skipped_this_file = 0
    fallback_this_file = 0

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        if not in_block and BLOCK_START.match(line):
            in_block = True
            block_has_value_rating = False
            block_already_had_it = False
            block_lines_buffer = [line]
            i += 1
            continue

        if in_block:
            if 'value_rating' in line:
                block_has_value_rating = True
                block_already_had_it = True

            if BLOCK_END.match(line):
                # Fallback: no doctrine_mod line matched in this block (older/fossil
                # cards missing the field entirely) — insert as last field before close.
                if not block_has_value_rating:
                    block_lines_buffer.append('    value_rating = None,  # scaffolded, not addressed\n')
                    block_has_value_rating = True
                    inserted_this_file += 1
                    fallback_this_file += 1
                result.extend(block_lines_buffer)
                result.append(line)
                if block_already_had_it:
                    skipped_this_file += 1
                in_block = False
                block_lines_buffer = []
                i += 1
                continue

            block_lines_buffer.append(line)

            if not block_has_value_rating and DOCTRINE_LINE.match(line):
                indent_match = re.match(r'^(\s+)', line)
                indent = indent_match.group(1) if indent_match else '    '
                block_lines_buffer.append(f'{indent}value_rating = None,  # scaffolded, not addressed\n')
                block_has_value_rating = True
                inserted_this_file += 1

            i += 1
            continue

        result.append(line)
        i += 1

    print(f"{path.split('/')[-1]}: +{inserted_this_file} inserted ({fallback_this_file} via no-doctrine_mod fallback), {skipped_this_file} already had it")
    total_inserted += inserted_this_file
    total_skipped_already_present += skipped_this_file

    if not DRY_RUN:
        with open(path, 'w') as f:
            f.writelines(result)

print(f"\nTotal: +{total_inserted} inserted, {total_skipped_already_present} already present")
if DRY_RUN:
    print("[DRY RUN — no changes written]")
else:
    print("Files written.")
