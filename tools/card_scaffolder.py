#!/usr/bin/env python3
"""
Art 04 stub scaffolder (S136, PM05 09-16 step 1 prep).

Inserts EMPTY structural blocks — Design Rationale header, Card Story
placeholder, Design Checklist skeleton, Status table — for cards missing
them entirely. Every Pass cell is ⚠ and every Note/Artifact-ref cell is
blank, except the two rows with an established pending-ticket convention
(Data schema validation -> 04-n70, Card narrative -> 04-n79), cited
verbatim to match tools/art04_sweep.py's precedent. This script NEVER
writes a verdict, NEVER rewrites or moves existing prose (including each
stub's current italic design note, which is left exactly where it is,
now trailing the new empty scaffold) — Step 2 (design review) supplies
content, this script only supplies structure.

Scope (v1): only handles cards missing ALL 4 blocks — the stub norm
surfaced by card_completeness_audit.py (all 133 Ring Modifiers, most
per-faction stubs). Cards missing SOME but not all blocks (e.g.
GUI.MOD.9/10, missing only the checklist) are reported and left
untouched — inserting into an unfamiliar partial structure needs
case-by-case judgment, not a blanket rule. Re-run the completeness
audit after scaffolding to confirm coverage and see what's left.

Usage:
  python3 tools/card_scaffolder.py <part-file-name> --dry-run
  python3 tools/card_scaffolder.py <part-file-name>

Example:
  python3 tools/card_scaffolder.py 04___Card_System___Part3_Ring_Modifiers.md --dry-run
"""
import os
import re
import sys

V1_DIR = os.path.join(os.path.dirname(__file__), '..', 'V1')

MAIN_CHECKLIST_ROWS = [
    "Action fit", "Voice fit", "Doctrine alignment", "Card type fit",
    "Taxonomy fit", "Balance", "Effect duration", "Persistence",
    "Trigger validity", "Portrait validity", "Supported by zones",
    "Supported by components", "Supported by game procedure",
]
# (name, pass, note, artifact ref) - only these two rows have an established
# pending-ticket convention (art04_sweep.py precedent); cite verbatim.
DATA_SCHEMA_ROW = ("Data schema validation", "⚠", "Pending 04-n70", "Art 04 §6.1–§6.3")
CARD_NARRATIVE_ROW = ("Card narrative", "⚠", "Pending 04-n79", "Art 04 §5 Card Story")
TAIL_ROWS = ["Outcome determinacy", "Resource cost positioning"]
MODREACT_ADDENDUM_ROWS = [
    "Trigger frequency", "Firing window", "Automatic vs. d100",
    "Stack behavior", "Ring constraint",
]

DESIGN_RATIONALE_BLOCK = (
    "#### Design Rationale\n"
    "⚠ Pending design review (09-16). See stub design note below.\n"
    "\n"
)
CARD_STORY_BLOCK = (
    "#### Card Story\n"
    "⚠ Story pending 04-n79.\n"
    "\n"
)
STATUS_BLOCK = (
    "#### Status\n"
    "\n"
    "| | Design Pass | Issues Resolved | Signed off |\n"
    "|--|-------------|-----------------|------------|\n"
    "| Status |  |  |  |\n"
    "\n"
)


def build_checklist_block(is_modreact):
    lines = ["**Design checklist:**\n", "\n",
             "| Category | Pass | Note | Artifact ref |\n",
             "|----------|------|------|--------------|\n"]
    for row in MAIN_CHECKLIST_ROWS:
        lines.append(f"| {row} | ⚠ |  |  |\n")
    lines.append(f"| {DATA_SCHEMA_ROW[0]} | {DATA_SCHEMA_ROW[1]} | {DATA_SCHEMA_ROW[2]} | {DATA_SCHEMA_ROW[3]} |\n")
    lines.append(f"| {CARD_NARRATIVE_ROW[0]} | {CARD_NARRATIVE_ROW[1]} | {CARD_NARRATIVE_ROW[2]} | {CARD_NARRATIVE_ROW[3]} |\n")
    for row in TAIL_ROWS:
        lines.append(f"| {row} | ⚠ |  |  |\n")
    if is_modreact:
        for row in MODREACT_ADDENDUM_ROWS:
            lines.append(f"| {row} (ModReactCard) | ⚠ |  |  |\n")
    lines.append("\n")
    return "".join(lines)


def is_modreact_card(body):
    return bool(re.search(r'\btype\s*=\s*ModReactCard\b', body))


def scaffold_file(path, dry_run):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    out = []
    stats = {'scaffolded': 0, 'already_complete': 0, 'partial_skipped': 0, 'not_a_card': 0}
    partial_ids = []

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if not line.startswith('### '):
            out.append(line)
            i += 1
            continue

        # Collect this card's full chunk (header through line before next '### ' or EOF)
        header_line = line
        j = i + 1
        chunk_lines = []
        while j < n and not lines[j].startswith('### '):
            chunk_lines.append(lines[j])
            j += 1
        body = ''.join(chunk_lines)

        has_python_card = '```python' in body and 'Card(' in body
        if not has_python_card:
            out.append(header_line)
            out.extend(chunk_lines)
            stats['not_a_card'] += 1
            i = j
            continue

        has_rationale = '#### Design Rationale' in body
        has_story = '#### Card Story' in body
        has_checklist = '**Design checklist:**' in body
        has_status = '#### Status' in body
        all_missing = not (has_rationale or has_story or has_checklist or has_status)
        all_present = has_rationale and has_story and has_checklist and has_status

        header_id_match = re.match(r'### ([A-Za-z0-9\.\-]+)', header_line)
        card_id = header_id_match.group(1) if header_id_match else header_line.strip()

        if all_present:
            out.append(header_line)
            out.extend(chunk_lines)
            stats['already_complete'] += 1
            i = j
            continue

        if not all_missing:
            # Partial completeness - do not touch, report instead (see module docstring).
            out.append(header_line)
            out.extend(chunk_lines)
            stats['partial_skipped'] += 1
            partial_ids.append((card_id, has_rationale, has_story, has_checklist, has_status))
            i = j
            continue

        # All 4 missing: insert the empty scaffold right after the header
        # (and after an immediately-following nav back-link line, if present).
        out.append(header_line)
        k = 0
        if k < len(chunk_lines) and chunk_lines[k].startswith('[↑'):
            out.append(chunk_lines[k])
            k += 1
        # Ensure exactly one blank line before the scaffold
        if k < len(chunk_lines) and chunk_lines[k].strip() == '':
            k += 1
        out.append('\n')
        out.append(DESIGN_RATIONALE_BLOCK)
        out.append(CARD_STORY_BLOCK)
        out.append(build_checklist_block(is_modreact_card(body)))
        out.append(STATUS_BLOCK)
        out.extend(chunk_lines[k:])
        stats['scaffolded'] += 1
        i = j

    print(f"{os.path.basename(path)}:")
    print(f"  Scaffolded (was missing all 4 blocks): {stats['scaffolded']}")
    print(f"  Already complete (untouched):          {stats['already_complete']}")
    print(f"  Partial - skipped, needs manual review: {stats['partial_skipped']}")
    print(f"  Non-card section headers (untouched):  {stats['not_a_card']}")
    if partial_ids:
        print("\n  Partial-completeness cards (skipped):")
        for card_id, r, s, c, st in partial_ids:
            missing = [n for n, v in (('rationale', r), ('story', s), ('checklist', c), ('status', st)) if not v]
            print(f"    {card_id:20} missing: {', '.join(missing)}")

    if dry_run:
        print("\n[DRY RUN - no file written]")
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(out)
        print(f"\n✓ File written: {path}")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry_run = '--dry-run' in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)
    for name in args:
        path = name if os.path.isabs(name) else os.path.join(V1_DIR, name)
        if not os.path.exists(path):
            print(f"Not found: {path}")
            continue
        scaffold_file(path, dry_run)


if __name__ == '__main__':
    main()
