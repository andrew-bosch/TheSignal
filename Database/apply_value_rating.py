#!/usr/bin/env python3
"""
04-n178/04-n183 (S145) — apply value_rating tiers (1-4) to Card() blocks in
the Art 04 Part files, sourced live from v_card_pair_uvm_cost.total_pair_cost.

CAVEAT (see schema_reference.md §6.7 for full detail): total_pair_cost is
built on uvm_assumptions/uvm_pair_assumptions base rates, which are
calibrated by averaging *existing designed card costs*, not validated by
playtesting. A tier assigned by this script is a self-consistency read
against the current corpus, not an external correctness check. Re-run only
after re-examining whether the underlying UVM rates still hold, not as a
blind "resync" operation.

Tier boundaries (natural-break on the 201-card S145 distribution, not
equal-population -- see Whiteboard/cost_baseline_recommendations.md §5):
    total_pair_cost <  3.0  -> 1 (floor)
    total_pair_cost <  5.0  -> 2 (standard)
    total_pair_cost <  7.0  -> 3 (advanced)
    total_pair_cost >= 7.0  -> 4 (ceiling)

Behavior:
  - Only touches Card() blocks whose value_rating is still literally `None`
    -- either the line-anchored scaffold form
    (`value_rating = None,  # scaffolded, not addressed`) or the inline
    ModReactCard form sharing a line with other `= None` fields
    (`ring_constraint = None,  ring_origin = None,  value_rating = None,`).
  - Never touches a card whose value_rating is already a number -- e.g. the
    separate S132/S134 ring-modifier "mirrors magnitude" convention. If that
    convention and this pricing model disagree, decide by hand (see PM02
    L284 for the S145 precedent: 9 STD.MOD cards, pricing model won).
  - Cards with value_rating = None but no matching card_id in the DB tier
    map (no computable total_pair_cost -- typically blocked/TBD cards) are
    left untouched and reported, not silently skipped.
  - Idempotent and safe to re-run: matched blocks are counted 1:1 against a
    plain `= Card(` grep count before every run (see verify_block_integrity)
    to catch any nested-bare-paren edge case truncating a match early.

Usage:
    python3 apply_value_rating.py --dry-run   # report only, no writes
    python3 apply_value_rating.py             # apply

Requires: `mysql` CLI configured for passwordless connection to
the_signal_db (matches every other tool in this directory).
"""

import re
import subprocess
import sys

DRY_RUN = '--dry-run' in sys.argv

FILES = [
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part2_Standard.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part3_Ring_Modifiers.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part4a_Guild.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part4b_Ghost.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part4c_Directorate.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part4d_Network.md',
    '/home/abosch/Projects/TheSignal/V1/04___Card_System___Part4e_Syndicate.md',
]

TIER_QUERY = """
SELECT card_id,
  CASE
    WHEN total_pair_cost < 3.0 THEN 1
    WHEN total_pair_cost < 5.0 THEN 2
    WHEN total_pair_cost < 7.0 THEN 3
    ELSE 4
  END AS tier
FROM v_card_pair_uvm_cost
WHERE card_id NOT IN ('GHO.CA.11')
ORDER BY card_id;
"""


def load_tier_map():
    result = subprocess.run(
        ['mysql', 'the_signal_db', '-N', '-e', TIER_QUERY],
        capture_output=True, text=True, check=True,
    )
    tier_map = {}
    for line in result.stdout.splitlines():
        parts = line.strip().split('\t')
        if len(parts) == 2:
            tier_map[parts[0]] = int(parts[1])
    return tier_map


BLOCK_RE = re.compile(r'^\w[\w.]*\s*=\s*Card\(\s*$.*?^\)\s*$', re.MULTILINE | re.DOTALL)
BLOCK_START_RE = re.compile(r'^\w[\w.]*\s*=\s*Card\(\s*$', re.MULTILINE)
ID_LINE = re.compile(r'^\s*id\s*=\s*"([^"]+)"', re.MULTILINE)
VALUE_RATING_NONE = re.compile(
    r'value_rating(?P<eq1>\s*)=(?P<eq2>\s*)None(?P<comma>\s*,)?(?P<comment>[ \t]*#[^\n]*)?'
)


def verify_block_integrity(raw, path):
    starts = len(BLOCK_START_RE.findall(raw))
    matches = len(BLOCK_RE.findall(raw))
    if starts != matches:
        raise RuntimeError(
            f'{path}: block-start count ({starts}) != matched-block count '
            f'({matches}) -- a nested bare-paren line is truncating a match. '
            f'Do not proceed until this is resolved (see script docstring).'
        )


def main():
    tier_map = load_tier_map()

    applied_total = 0
    skipped_no_data = []
    already_set_total = 0

    for path in FILES:
        with open(path, 'r') as f:
            raw = f.read()

        verify_block_integrity(raw, path)

        applied_this_file = 0
        out_parts = []
        pos = 0
        for match in BLOCK_RE.finditer(raw):
            block = match.group(0)
            out_parts.append(raw[pos:match.start()])

            id_m = ID_LINE.search(block)
            card_id = id_m.group(1) if id_m else None

            vr_m = VALUE_RATING_NONE.search(block)
            if vr_m and card_id:
                if card_id in tier_map:
                    tier = tier_map[card_id]
                    comma = vr_m.group('comma') or ','
                    new_text = f'value_rating{vr_m.group("eq1")}={vr_m.group("eq2")}{tier}{comma}'
                    block = block[:vr_m.start()] + new_text + block[vr_m.end():]
                    applied_this_file += 1
                    applied_total += 1
                else:
                    skipped_no_data.append(card_id)
            elif not vr_m:
                already_set_total += 1

            out_parts.append(block)
            pos = match.end()
        out_parts.append(raw[pos:])
        new_raw = ''.join(out_parts)

        print(f"{path.split('/')[-1]}: applied {applied_this_file}")

        if not DRY_RUN and new_raw != raw:
            with open(path, 'w') as f:
                f.write(new_raw)

    print(f"\nTotal applied: {applied_total}")
    print(f"Total already-set (untouched): {already_set_total}")
    print(f"Skipped, value_rating=None but no pricing data ({len(skipped_no_data)}): {skipped_no_data}")


if __name__ == '__main__':
    main()
