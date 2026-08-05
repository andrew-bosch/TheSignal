#!/usr/bin/env python3
"""Corpus-wide Card() completeness + taxonomy audit (schema_cleanup_log #4 D/E/F).

Parses every `<ID> = Card(...)` block in V1/04___Card_System.md directly
(source of truth, not the DB mirror) and reports:
  D1 — missing fields that are always-None for this card's subclass per Art 04
       §6.2's Modifier Subclass Field Constraints table — mechanical `=None`
       backfill, no design judgment needed (Phase 0 step 2 sweep candidates)
  D2 — missing fields that are live/per-card-design for this card's subclass
       (or any field on a non-Modifier card, which has no exemptions) — real
       gaps, needs the Phase 0 step 3 checklist pass, not a script
  D3 — missing fields the schema marks Required for this subclass (currently
       only ModReactCard.trigger) — schema violation, not just incompleteness
  E  — type=ModReactCard cards with layer left at None (missing taxonomy)
  F  — any card using the retired subject=PublicStanding value

`is_unique`/`deck_limit` are intentionally excluded (Andy, S154): both are a
post-cross-faction-review decision item, not resolvable per-card — flagging
them here would just be noise until that decision happens (09-16 steps 4-5).

Subclass constraint data transcribed from Art 04 §6.2 "Modifier Subclass
Field Constraints" (Part1_Core.md) — re-verify against source if that table
changes; this script does not read it live.

Also emits a card_id -> mod_subtype (Action|Battle|React|None) map for the
card_status DB backfill, since the corpus's own `type` field already carries
that distinction directly.
"""
import re
import sys
from pathlib import Path

MONOLITH = Path(__file__).resolve().parent.parent / "V1" / "04___Card_System.md"

# Excluded entirely — deferred fields, not part of any completeness sweep until
# the post-cross-faction-review decision lands (see project_card_schema_db_strategy memory).
EXCLUDED_FIELDS = {"is_unique", "deck_limit"}

BASE_FIELDS = [f for f in [
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
] if f not in EXCLUDED_FIELDS]

# Fields added by the 3 Modifier subclasses (on top of the base Card fields above).
# `effect` is Required for ModActionCard/ModBattleCard only — ModReactCard uses the
# inherited success/fail fields instead (§6.2: "— " i.e. live, not `effect`).
MOD_ADDED_REQUIRED = {
    "ModActionCard": {"effect", "ring_constraint"},
    "ModBattleCard":  {"effect", "ring_constraint"},
    "ModReactCard":   {"ring_constraint"},
}
# `acquisition` and `generating_card` are deliberately NOT in the unconditional
# required set — §6.2 states "Deck by default — omit unless Issued" for
# acquisition, and "None unless acquisition=Issued" for generating_card. Omitting
# both is the documented-correct default for the ~260 Deck-sourced cards. They're
# checked conditionally below instead (real gap only if the two fields disagree
# with each other), and `ring_origin` is required only for the non-Issued case.

# Base-Card fields that are always None for a given Modifier subclass, per Art 04
# §6.2 "Modifier Subclass Field Constraints" — missing here is a mechanical `=None`
# backfill (D1), not a design gap.
MOD_ALWAYS_NONE = {
    "ModActionCard": {
        "layer", "function", "subject",
        "beat", "resolution", "threshold", "ring_mod", "doctrine_mod",
        "trigger", "resolution_type", "outcome_type",
        "persistence", "persistence_condition", "persistence_clearing_trigger", "persistence_effect",
        "target_district", "target_faction", "target_object", "target_freeform",
        "boost", "cost",
        "success", "successcrit", "fail", "failcrit", "on_accept", "on_decline", "on_discard",
        "ps_framing",
    },
    "ModBattleCard": {
        "layer", "function", "subject",
        "beat", "resolution", "threshold", "ring_mod", "doctrine_mod",
        "trigger", "resolution_type", "outcome_type",
        "persistence", "persistence_condition", "persistence_clearing_trigger", "persistence_effect",
        "target_district", "target_faction", "target_object", "target_freeform",
        "affinity", "restriction",
        "boost", "cost",
        "success", "successcrit", "fail", "failcrit", "on_accept", "on_decline", "on_discard",
        "ps_framing",
        "perspectives", "design_note",
    },
    "ModReactCard": {
        "beat",  # "ModReactCard: only `beat` is always None. All other `—` fields are live" (§6.2)
    },
}

# Fields the schema marks Required (must be non-None) for a subclass — missing is
# a schema violation, distinct from ordinary incompleteness.
MOD_REQUIRED = {
    "ModReactCard": {"trigger"},
}

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
                if key in ("type", "layer", "subject", "card_id", "acquisition"):
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

    d1_findings = []  # (card_id, subclass, missing_always_none_fields) — scriptable backfill
    d2_findings = []  # (card_id, subclass_or_None, missing_live_fields) — real gaps, needs review
    d3_findings = []  # (card_id, missing_required_fields) — schema violation
    e_findings = []   # (card_id,)
    f_findings = []   # (card_id,)
    acquisition_findings = []  # (card_id, reason) — acquisition/generating_card/ring_origin disagreement
    subtype_map = {}  # card_id -> Action|Battle|React

    for lhs, block in blocks:
        keys, values = top_level_keys(block)
        card_id = values.get("card_id", lhs).strip('"\'')
        type_val = values.get("type", "")
        layer_val = values.get("layer", "")
        subject_val = values.get("subject", "")

        subclass = type_val if type_val in MOD_SUBTYPE_BY_TYPE else None
        if subclass:
            subtype_map[card_id] = MOD_SUBTYPE_BY_TYPE[subclass]

        if subclass:
            always_none = MOD_ALWAYS_NONE[subclass]
            required = MOD_REQUIRED.get(subclass, set())
            added = MOD_ADDED_REQUIRED[subclass]
            expected_live = [f for f in BASE_FIELDS if f not in always_none] + sorted(added)
        else:
            always_none = set()
            required = set()
            expected_live = list(BASE_FIELDS)

        missing_always_none = sorted(f for f in always_none if f not in keys)
        missing_live = [f for f in expected_live if f not in keys]
        missing_required = sorted(f for f in required if f not in keys)

        # acquisition/generating_card/ring_origin conditional check (§6.2: "Deck by
        # default — omit unless Issued" / "None unless acquisition=Issued"). Only
        # flag real disagreements, not the documented-correct Deck-default omission.
        if subclass:
            acq_val = values.get("acquisition", "")
            is_issued = "Issued" in acq_val
            if is_issued and "generating_card" not in keys:
                acquisition_findings.append((card_id, "declared Issued but no generating_card"))
            if not is_issued and "ring_origin" not in keys:
                acquisition_findings.append((card_id, "Deck-default, missing explicit ring_origin"))
            if "generating_card" in keys and not is_issued:
                acquisition_findings.append((card_id, "generating_card set but acquisition not declared Issued"))

        if missing_always_none:
            d1_findings.append((card_id, subclass, missing_always_none))
        if missing_live:
            d2_findings.append((card_id, subclass, missing_live))
        if missing_required:
            d3_findings.append((card_id, missing_required))

        if type_val == "ModReactCard" and layer_val == "None":
            e_findings.append(card_id)

        if "PublicStanding" in subject_val:
            f_findings.append(card_id)

    print(f"Total Card() instances parsed: {len(blocks)}")
    print(f"(is_unique/deck_limit excluded from all buckets — deferred, S154)")
    print()

    print(f"=== D3: REQUIRED field missing — schema violation ({len(d3_findings)} cards) ===")
    for cid, missing in d3_findings:
        print(f"  {cid}: {', '.join(missing)}")
    print()

    print(f"=== D1: scriptable `=None` backfill ({len(d1_findings)} cards affected) ===")
    total_d1 = sum(len(m) for _, _, m in d1_findings)
    print(f"Total missing always-None declarations: {total_d1}")
    field_counts = {}
    for _, _, missing in d1_findings:
        for f in missing:
            field_counts[f] = field_counts.get(f, 0) + 1
    for f, c in sorted(field_counts.items(), key=lambda x: -x[1]):
        print(f"  {f}: {c}")
    print()

    print(f"=== D2: needs design/checklist review, not a script ({len(d2_findings)} cards affected) ===")
    total_d2 = sum(len(m) for _, _, m in d2_findings)
    print(f"Total missing live-field declarations: {total_d2}")
    field_counts = {}
    for _, _, missing in d2_findings:
        for f in missing:
            field_counts[f] = field_counts.get(f, 0) + 1
    for f, c in sorted(field_counts.items(), key=lambda x: -x[1]):
        print(f"  {f}: {c}")
    print()

    print(f"=== D-acquisition: acquisition/generating_card/ring_origin disagreements ({len(acquisition_findings)}) ===")
    for cid, reason in acquisition_findings:
        print(f"  {cid}: {reason}")
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
        print("=== D1 detail (card_id [subclass]: missing always-None fields) ===")
        for cid, subclass, missing in d1_findings:
            print(f"  {cid} [{subclass}]: {', '.join(missing)}")
        print()
        print("=== D2 detail (card_id [subclass]: missing live fields) ===")
        for cid, subclass, missing in d2_findings:
            print(f"  {cid} [{subclass or 'base'}]: {', '.join(missing)}")

    if "--dump-subtype-sql" in sys.argv:
        print()
        print("=== mod_subtype UPDATE statements ===")
        for cid, sub in sorted(subtype_map.items()):
            print(f"UPDATE card_status SET mod_subtype='{sub}' WHERE card_id='{cid}';")


if __name__ == "__main__":
    main()
