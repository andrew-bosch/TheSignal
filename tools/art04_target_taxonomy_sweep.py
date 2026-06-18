#!/usr/bin/env python3
"""
Art 04 sweep: 04-n32 — add target_taxonomy=None to all Card() blocks missing it.

Insertion point: the line containing `affinity=` inside a Card() python block,
immediately preceded by target_taxonomy=None if not already present.

Cards that already have target_taxonomy are left untouched.
C21 Invoke Jurisdiction (the only non-None candidate) must be set manually after.

Usage:
  python3 art04_target_taxonomy_sweep.py --dry-run   # report counts, no write
  python3 art04_target_taxonomy_sweep.py             # apply changes
"""

import re
import sys

DRY_RUN = '--dry-run' in sys.argv
INPUT = '/home/abosch/Projects/TheSignal/V1/04___Card_System.md'

with open(INPUT, 'r') as f:
    lines = f.readlines()

result = []
in_python_block = False
in_card_block   = False
block_has_tt    = False   # target_taxonomy seen in current Card() block
added = 0
skipped = 0

for i, line in enumerate(lines):
    stripped = line.rstrip('\n').rstrip()

    # Track python block boundaries
    if stripped == '```python':
        in_python_block = True
        in_card_block   = False
        block_has_tt    = False
        result.append(line)
        continue

    if stripped == '```' and in_python_block:
        in_python_block = False
        in_card_block   = False
        block_has_tt    = False
        result.append(line)
        continue

    if not in_python_block:
        result.append(line)
        continue

    # Inside python block: detect Card( opening
    if re.match(r'^(\w+\s*=\s*)?Card\(', stripped):
        in_card_block = True
        block_has_tt  = False

    # Track whether this block already has target_taxonomy
    if in_card_block and 'target_taxonomy' in line:
        block_has_tt = True

    # Insertion point: affinity= line (primary) or portrait= line (fallback for stub cards)
    is_affinity = bool(re.match(r'\s+affinity\s*=', line))
    is_portrait = bool(re.match(r'\s+portrait\s*=', line))

    if in_card_block and not block_has_tt and (is_affinity or is_portrait):
        indent = re.match(r'(\s+)', line).group(1)
        result.append(f'{indent}target_taxonomy=None,\n')
        added += 1
        block_has_tt = True  # prevent double-insert
    elif in_card_block and block_has_tt and is_affinity:
        skipped += 1

    result.append(line)

print(f"Input:  {len(lines)} lines")
print(f"Output: {len(result)} lines")
print(f"Delta:  +{len(result) - len(lines)} lines")
print(f"\nInserted target_taxonomy=None: {added}")
print(f"Skipped (already present):     {skipped}")

if not DRY_RUN:
    with open(INPUT, 'w') as f:
        f.writelines(result)
    print("\n✓ File written.")
else:
    print("\n[DRY RUN — no changes written]")
