#!/usr/bin/env python3
"""Corpus-wide Card() completeness + taxonomy audit (schema_cleanup_log #4 D/E/F).

Parses every `<ID> = Card(...)` block in V1/04___Card_System.md directly
(source of truth, not the DB mirror) and reports:
  D — fields never declared as a kwarg at all (vs. explicitly set to None)
  E — type=ModReactCard cards with layer left at None (missing taxonomy)
  F — any card using the retired subject=PublicStanding value

Also emits a card_id -> mod_subtype (Action|Battle|React|None) map for the
card_status DB backfill, since the corpus's own `type` field already carries
that distinction directly.
"""
import re
import sys
from pathlib import Path

MONOLITH = Path(__file__).resolve().parent.parent / "V1" / "04___Card_System.md"

BASE_FIELDS = [
    "card_id", "id", "version", "name", "tagline", "type", "subtype", "faction",
    "is_unique", "deck_limit",
    "layer", "function", "subject",
    "beat", "resolution", "threshold", "ring_mod", "doctrine_mod", "value_rating",
    "trigger", "resolution_type", "outcome_type",
    "persistence", "persistence_condition", "persistence_clearing_trigger", "persistence_effect",
    "target_district", "target_faction", "target_object", "target_freeform",
    "affinity", "restriction", "cost", "boost",
    "success", "successcrit", "fail", "failcrit", "on_accept", "on_decline", "on_discard",
    "portrait",
    "ps_framing",
    "narrative", "perspectives", "design_note", "arbiter_note",
]

MOD_SUBTYPE_FIELDS = ["effect", "ring_constraint", "ring_origin", "acquisition", "generating_card"]

MOD_SUBTYPE_BY_TYPE = {
    "ModActionCard": "Action",
    "ModBattleCard": "Battle",
    "ModReactCard": "React",
}

KEY_RE = re.compile(r'(?<![\w.])([a-zA-Z_][a-zA-Z0-9_]*)\s*=(?!=)')


def find_card_blocks(text):
    """Yield (card_id_guess, block_text) for every `<LHS> = Card(...)` call."""
    blocks = []
    for m in re.finditer(r'^([A-Za-z0-9_.]+)\s*=\s*Card\(\s*$', text, re.MULTILINE):
        start = m.end()
        depth = 1
        i = start
        while depth > 0 and i < len(text):
            if text[i] == '(':
                depth += 1
            elif text[i] == ')':
                depth -= 1
            i += 1
        blocks.append((m.group(1), text[start:i - 1]))
    return blocks


def top_level_keys(block):
    """Return the set of kwarg names declared at paren-depth 0 within the block,
    plus a dict of a few raw single-line values we care about (type/layer/subject/card_id)."""
    keys = set()
    values = {}
    depth = 0
    i = 0
    n = len(block)
    # strip comments naively per line for key scanning, but keep raw text for value extraction
    lines = block.split('\n')
    depth = 0
    for line in lines:
        code = line.split('#', 1)[0]
        # track paren depth contributed by this line, but scan keys only when depth==0 at line start
        # (fields are typically one per top-level comma segment; nested exprs increase depth)
        for m in KEY_RE.finditer(code):
            pos = m.start()
            local_depth = depth + code[:pos].count('(') - code[:pos].count(')')
            local_depth += code[:pos].count('[') - code[:pos].count(']')
            local_depth += code[:pos].count('{') - code[:pos].count('}')
            if local_depth == 0:
                key = m.group(1)
                keys.add(key)
                if key in ("type", "layer", "subject", "card_id"):
                    rest = code[m.end():].strip()
                    val = rest.split(',')[0].strip().rstrip(',').strip()
                    values.setdefault(key, val)
        depth += code.count('(') - code.count(')')
        depth += code.count('[') - code.count(']')
        depth += code.count('{') - code.count('}')
    return keys, values


def main():
    text = MONOLITH.read_text()
    blocks = find_card_blocks(text)

    d_findings = []   # (card_id, missing_fields)
    e_findings = []   # (card_id,)
    f_findings = []   # (card_id,)
    subtype_map = {}  # card_id -> Action|Battle|React

    for lhs, block in blocks:
        keys, values = top_level_keys(block)
        card_id = values.get("card_id", lhs).strip('"\'')
        type_val = values.get("type", "")
        layer_val = values.get("layer", "")
        subject_val = values.get("subject", "")

        expected = list(BASE_FIELDS)
        if type_val in MOD_SUBTYPE_BY_TYPE:
            expected += MOD_SUBTYPE_FIELDS
            subtype_map[card_id] = MOD_SUBTYPE_BY_TYPE[type_val]

        missing = [f for f in expected if f not in keys]
        if missing:
            d_findings.append((card_id, missing))

        if type_val == "ModReactCard" and layer_val == "None":
            e_findings.append(card_id)

        if "PublicStanding" in subject_val:
            f_findings.append(card_id)

    print(f"Total Card() instances parsed: {len(blocks)}")
    print()
    print(f"=== D: undeclared fields ({len(d_findings)} cards affected) ===")
    total_missing = sum(len(m) for _, m in d_findings)
    print(f"Total missing field-declarations across corpus: {total_missing}")
    field_counts = {}
    for _, missing in d_findings:
        for f in missing:
            field_counts[f] = field_counts.get(f, 0) + 1
    for f, c in sorted(field_counts.items(), key=lambda x: -x[1]):
        print(f"  {f}: {c}")
    print()
    print(f"=== E: ModReactCard with layer=None ({len(e_findings)}) ===")
    for cid in e_findings:
        print(f"  {cid}")
    print()
    print(f"=== F: subject=PublicStanding ({len(f_findings)}) ===")
    for cid in f_findings:
        print(f"  {cid}")
    print()
    print(f"=== mod_subtype map ({len(subtype_map)} MOD-type cards) ===")
    from collections import Counter
    print(Counter(subtype_map.values()))

    if "--dump-d" in sys.argv:
        print()
        print("=== D detail (card_id: missing fields) ===")
        for cid, missing in d_findings:
            print(f"  {cid}: {', '.join(missing)}")

    if "--dump-subtype-sql" in sys.argv:
        print()
        print("=== mod_subtype UPDATE statements ===")
        for cid, sub in sorted(subtype_map.items()):
            print(f"UPDATE card_status SET mod_subtype='{sub}' WHERE card_id='{cid}';")


if __name__ == "__main__":
    main()
