#!/usr/bin/env python3
"""Regenerate V1/04___Card_System.md from its 8 Part files (S136 split).

The Part files are source of truth. The monolith is a generated build
artifact kept around for legacy scripts that expect a single file
(parse_mods.py, count_md.py, count_all_ids.py, diff_all.py, diff_db_md.py,
parse_costs.py, parse_costs_full.py, count_classes.py, tools/art04_sweep.py,
tools/art04_target_taxonomy_sweep.py) and for build_wiki.py's nav.

Run after editing any Part file. Safe to re-run — pure concatenation.
"""

import os

V1_DIR = os.path.join(os.path.dirname(__file__), '..', 'V1')

PARTS = [
    '04___Card_System___Part1_Core.md',
    '04___Card_System___Part2_Standard.md',
    '04___Card_System___Part3_Ring_Modifiers.md',
    '04___Card_System___Part4a_Guild.md',
    '04___Card_System___Part4b_Ghost.md',
    '04___Card_System___Part4c_Directorate.md',
    '04___Card_System___Part4d_Network.md',
    '04___Card_System___Part4e_Syndicate.md',
]

OUTPUT = '04___Card_System.md'


def main():
    chunks = []
    for part in PARTS:
        path = os.path.join(V1_DIR, part)
        with open(path, 'r', encoding='utf-8') as f:
            chunks.append(f.read())

    out_path = os.path.join(V1_DIR, OUTPUT)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(''.join(chunks))

    print(f"Wrote {out_path} from {len(PARTS)} parts.")


if __name__ == '__main__':
    main()
