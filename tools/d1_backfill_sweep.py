#!/usr/bin/env python3
"""Phase 0 step 2 — D1 mechanical backfill sweep (PM05, S154).

Adds explicit `field = None,  # scaffolded, not addressed` declarations for
every base-Card field that Art 04 §6.2's Modifier Subclass Field Constraints
table marks always-None for ModActionCard/ModBattleCard, but which the card's
own Card() block currently omits entirely. Purely mechanical — no field this
script touches carries any design judgment; the always-None status is a
schema fact, not a per-card decision.

Edits the live Part*.md files directly (never the generated monolith).
Inserts a single appended block, in canonical §6.1 field order, immediately
before each Card(...) block's closing paren — does not touch or reflow any
existing hand-formatted lines, to avoid corrupting card-specific structure.

Usage:
  python3 tools/d1_backfill_sweep.py --dry-run     # report only, no writes
  python3 tools/d1_backfill_sweep.py                # apply to Part*.md files
"""
import re
import sys
from pathlib import Path

V1 = Path(__file__).resolve().parent.parent / "V1"
PART_FILES = sorted(V1.glob("04___Card_System___Part*.md"))
PART_FILES = [f for f in PART_FILES if "Part1_Core" not in f.name]

BASE_FIELDS = [
    "card_id", "id", "version", "name", "tagline", "type", "subtype", "faction",
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
}

KEY_RE = re.compile(r'(?<![\w.])([a-zA-Z_][a-zA-Z0-9_]*)\s*=(?!=)')
CARD_START_RE = re.compile(r'^([A-Za-z0-9_.]+)\s*=\s*Card\(\s*$', re.MULTILINE)


def find_card_blocks_with_offsets(text):
    """Yield (card_id_guess, content_start, close_paren_idx, block_text)."""
    blocks = []
    for m in CARD_START_RE.finditer(text):
        start = m.end()
        depth = 1
        i = start
        while depth > 0 and i < len(text):
            if text[i] == '(':
                depth += 1
            elif text[i] == ')':
                depth -= 1
            i += 1
        close_idx = i - 1  # index of the matching ')'
        blocks.append((m.group(1), start, close_idx, text[start:close_idx]))
    return blocks


def declared_keys_and_type(block):
    keys = set()
    type_val = ""
    depth = 0
    for line in block.split('\n'):
        code = line.split('#', 1)[0]
        for m in KEY_RE.finditer(code):
            pos = m.start()
            local_depth = depth + code[:pos].count('(') - code[:pos].count(')')
            local_depth += code[:pos].count('[') - code[:pos].count(']')
            local_depth += code[:pos].count('{') - code[:pos].count('}')
            if local_depth == 0:
                key = m.group(1)
                keys.add(key)
                if key == "type" and not type_val:
                    rest = code[m.end():].strip()
                    type_val = rest.split(',')[0].strip()
        depth += code.count('(') - code.count(')')
        depth += code.count('[') - code.count(']')
        depth += code.count('{') - code.count('}')
    return keys, type_val


def build_insertion(missing_fields, indent="    "):
    lines = [""]  # blank line separating from prior content
    for f in missing_fields:
        lines.append(f"{indent}{f} = None,  # scaffolded, not addressed")
    return "\n".join(lines) + "\n"


def process_file(path, dry_run):
    text = path.read_text()
    blocks = find_card_blocks_with_offsets(text)
    edits = []  # (content_start, close_idx, insertion_text, card_id)
    for card_id, start, close_idx, block in blocks:
        keys, type_val = declared_keys_and_type(block)
        if type_val not in MOD_ALWAYS_NONE:
            continue
        always_none = MOD_ALWAYS_NONE[type_val]
        missing = [f for f in BASE_FIELDS if f in always_none and f not in keys]
        if not missing:
            continue
        edits.append((start, close_idx, missing, card_id))

    if not edits:
        return 0, 0

    if dry_run:
        for _, _, missing, card_id in edits:
            print(f"  {path.name}: {card_id} — {len(missing)} fields: {', '.join(missing)}")
        return len(edits), sum(len(m) for _, _, m, _ in edits)

    # apply edits back-to-front so earlier offsets stay valid
    new_text = text
    for start, close_idx, missing, card_id in sorted(edits, key=lambda e: e[0], reverse=True):
        insertion = build_insertion(missing)
        new_text = new_text[:close_idx] + insertion + new_text[close_idx:]
    path.write_text(new_text)
    return len(edits), sum(len(m) for _, _, m, _ in edits)


def main():
    dry_run = "--dry-run" in sys.argv
    total_cards = 0
    total_fields = 0
    for path in PART_FILES:
        n_cards, n_fields = process_file(path, dry_run)
        if n_cards:
            print(f"{path.name}: {n_cards} cards, {n_fields} fields{' (dry-run)' if dry_run else ''}")
        total_cards += n_cards
        total_fields += n_fields
    print()
    print(f"TOTAL: {total_cards} cards, {total_fields} fields{' (dry-run — no files written)' if dry_run else ' written'}")


if __name__ == "__main__":
    main()
