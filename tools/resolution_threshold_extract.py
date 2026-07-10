#!/usr/bin/env python3
"""
Extract resolution/threshold per card_id, generate SQL UPDATEs against
card_status (resolution_type_raw, threshold_val, base_success_pct).
Read-only against the markdown; writes only a SQL file, not the .md files.
"""

import re
import glob

FILES = sorted(glob.glob('/home/abosch/Projects/TheSignal/V1/04___Card_System___Part*.md'))
FILES = [f for f in FILES if 'Card_System.md' not in f]  # skip generated monolith if glob catches it

BLOCK_START = re.compile(r'^(\S+)\s*=\s*Card\(\s*$')
BLOCK_END = re.compile(r'^\)\s*$')
CARD_ID_LINE = re.compile(r'card_id\s*=\s*"([^"]+)"')
RESOLUTION_LINE = re.compile(r'\bresolution\s*=\s*(\w+)')
THRESHOLD_LINE = re.compile(r'\bthreshold\s*=\s*(None|\d+)')

rows = []  # (card_id, resolution, threshold)

for path in FILES:
    with open(path) as f:
        lines = f.readlines()
    in_block = False
    card_id = None
    resolution = None
    threshold = None
    for line in lines:
        start_m = BLOCK_START.match(line)
        if not in_block and start_m:
            in_block = True
            card_id = None
            var_name = start_m.group(1)  # fallback if no explicit card_id= field inside block
            resolution = None
            threshold = None
            continue
        if in_block:
            m = CARD_ID_LINE.search(line)
            if m:
                card_id = m.group(1)
            m = RESOLUTION_LINE.search(line)
            if m:
                resolution = m.group(1)
            m = THRESHOLD_LINE.search(line)
            if m:
                threshold = m.group(1)
            if BLOCK_END.match(line):
                effective_id = card_id if card_id else var_name
                if effective_id:
                    rows.append((effective_id, resolution, threshold))
                in_block = False

print(f"Found {len(rows)} card blocks with card_id across {len(FILES)} files")
missing_resolution = [r for r in rows if r[1] is None]
print(f"Missing resolution field: {len(missing_resolution)} -> {[r[0] for r in missing_resolution]}")

sql_path = '/tmp/claude-1000/-home-abosch/0f3a7b58-9ba5-4020-9f49-d485266c1287/scratchpad/resolution_threshold_updates.sql'
with open(sql_path, 'w') as out:
    for card_id, resolution, threshold in rows:
        res_sql = 'NULL' if resolution is None else f"'{resolution}'"
        if threshold is None or threshold == 'None':
            thr_sql = 'NULL'
        else:
            thr_sql = threshold
        if resolution == 'Automatic':
            pct_sql = '100'
        elif resolution == 'd100' and thr_sql != 'NULL':
            pct_sql = thr_sql
        else:
            pct_sql = 'NULL'
        cid_escaped = card_id.replace("'", "''")
        out.write(
            f"UPDATE card_status SET resolution_type_raw={res_sql}, threshold_val={thr_sql}, "
            f"base_success_pct={pct_sql} WHERE card_id='{cid_escaped}';\n"
        )

print(f"SQL written to {sql_path}")
