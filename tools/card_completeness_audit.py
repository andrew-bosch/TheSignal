#!/usr/bin/env python3
"""
Art 04 completeness audit (S136, PM05 09-16 step 1 prep).

Read-only. Scans all 7 card-bearing Part files and classifies each card
into one of 3 states:

  no_structure  - missing one or more of the 4 full-spec blocks (Design
                  Rationale, Card Story, Design checklist, Status). The
                  raw stub state, pre-scaffold.
  scaffolded    - all 4 blocks present, but content is still the empty
                  placeholder tools/card_scaffolder.py writes (Design
                  Rationale reads its stock "Pending design review
                  (09-16)" line, and no checklist row has been marked
                  with a real "✓" Pass value). Structure exists; content
                  doesn't yet.
  reviewed      - all 4 blocks present with real content (at least one
                  checklist row actually marked ✓, or Design Rationale
                  isn't the scaffold placeholder).

This 3-state model mirrors card_status's structure_pass/design_pass
columns (added S136, db_update_session136.sql) - structure_pass tracks
scaffolded-or-better, design_pass tracks reviewed-or-better. Keep this
script and the DB column in sync: whenever card_scaffolder.py runs,
db_update_session136.sql's UPDATE pattern (or an equivalent one) needs
to run too.

The *(stub)* header marker is checked against this state, not used as
ground truth - flagged as a real disagreement only when a card marked
stub is actually 'reviewed', or a card NOT marked stub is 'no_structure'
or 'scaffolded' (i.e. still unreviewed despite the header looking done).
A stub-marked card that's merely 'scaffolded' is the expected, correct
combination and is not flagged.

A "card" is any ### chunk containing a ```python Card(...)``` block.
Section sub-headers (e.g. "### Standard — Covert Operations") have no
python block and are skipped.

Usage:
  python3 tools/card_completeness_audit.py            # summary only
  python3 tools/card_completeness_audit.py --detail    # every card, one row
  python3 tools/card_completeness_audit.py --missing   # only non-'reviewed' cards
"""
import os
import re
import sys

V1_DIR = os.path.join(os.path.dirname(__file__), '..', 'V1')

PARTS = [
    '04___Card_System___Part2_Standard.md',
    '04___Card_System___Part3_Ring_Modifiers.md',
    '04___Card_System___Part4a_Guild.md',
    '04___Card_System___Part4b_Ghost.md',
    '04___Card_System___Part4c_Directorate.md',
    '04___Card_System___Part4d_Network.md',
    '04___Card_System___Part4e_Syndicate.md',
]

DETAIL = '--detail' in sys.argv
MISSING_ONLY = '--missing' in sys.argv

SCAFFOLD_RATIONALE_MARKER = 'Pending design review (09-16)'


def split_cards(text):
    """Split a Part file's text into (header, body) chunks at each '### ' line."""
    lines = text.split('\n')
    chunks = []
    current_header = None
    current_lines = []
    for line in lines:
        if line.startswith('### '):
            if current_header is not None:
                chunks.append((current_header, '\n'.join(current_lines)))
            current_header = line[4:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_header is not None:
        chunks.append((current_header, '\n'.join(current_lines)))
    return chunks


def extract_card_id(body):
    m = re.search(r'\bcard_id\s*=\s*"([^"]+)"', body)
    if m:
        return m.group(1)
    m = re.search(r'^\s*id\s*=\s*"([^"]+)"', body, re.MULTILINE)
    if m:
        return m.group(1)
    m = re.search(r'^\s*id\s*=\s*(\d+)', body, re.MULTILINE)
    if m:
        return f"id={m.group(1)}"
    return "???"


def has_real_checklist_pass(body):
    """True if any checklist row's Pass column is a real ✓, not just the ⚠ scaffold mark."""
    checklist_start = body.find('**Design checklist:**')
    if checklist_start == -1:
        return False
    status_start = body.find('#### Status', checklist_start)
    region = body[checklist_start:status_start] if status_start != -1 else body[checklist_start:]
    return bool(re.search(r'^\|[^|]*\|\s*✓\s*\|', region, re.MULTILINE))


def extract_signed_off(body):
    m = re.search(r'\|\s*Status\s*\|([^|]*)\|([^|]*)\|([^|]*)\|', body)
    if not m:
        return None
    cell = m.group(3).strip()
    return cell if cell else None


def classify(body):
    has_rationale = '#### Design Rationale' in body
    has_story = '#### Card Story' in body
    has_checklist = '**Design checklist:**' in body
    has_status = '#### Status' in body
    has_structure = has_rationale and has_story and has_checklist and has_status

    if not has_structure:
        return 'no_structure', {'rationale': has_rationale, 'story': has_story,
                                 'checklist': has_checklist, 'status': has_status}

    is_placeholder_rationale = SCAFFOLD_RATIONALE_MARKER in body
    real_pass = has_real_checklist_pass(body)

    state = 'scaffolded' if (is_placeholder_rationale and not real_pass) else 'reviewed'
    return state, {'rationale': True, 'story': True, 'checklist': True, 'status': True}


def audit_file(path, filename):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    results = []
    for header, body in split_cards(text):
        if '```python' not in body or 'Card(' not in body:
            continue  # section sub-header, not a card
        state, blocks = classify(body)
        results.append({
            'file': filename,
            'header': header.replace(' *(stub)*', ''),
            'id': extract_card_id(body),
            'stub_marker': '*(stub)*' in header,
            'state': state,
            'signed_off': extract_signed_off(body),
            **blocks,
        })
    return results


def main():
    all_results = []
    for part in PARTS:
        path = os.path.join(V1_DIR, part)
        if os.path.exists(path):
            all_results.extend(audit_file(path, part))

    total = len(all_results)
    counts = {'no_structure': 0, 'scaffolded': 0, 'reviewed': 0}
    for r in all_results:
        counts[r['state']] += 1

    print(f"Total cards found: {total}")
    print(f"  no_structure (raw stub):        {counts['no_structure']}")
    print(f"  scaffolded (structure, no content): {counts['scaffolded']}")
    print(f"  reviewed (real content):         {counts['reviewed']}")
    print()

    print(f"{'File':45} {'Total':>6} {'no_struct':>10} {'scaffold':>9} {'reviewed':>9}")
    for part in PARTS:
        file_results = [r for r in all_results if r['file'] == part]
        fc = {'no_structure': 0, 'scaffolded': 0, 'reviewed': 0}
        for r in file_results:
            fc[r['state']] += 1
        print(f"{part:45} {len(file_results):>6} {fc['no_structure']:>10} {fc['scaffolded']:>9} {fc['reviewed']:>9}")
    print()

    mismatches = [r for r in all_results
                  if (r['stub_marker'] and r['state'] == 'reviewed')
                  or (not r['stub_marker'] and r['state'] in ('no_structure', 'scaffolded'))]
    if mismatches:
        print(f"Note: {len(mismatches)} cards where the *(stub)* header marker disagrees with review state:")
        for r in mismatches[:20]:
            status = ("marked stub but fully reviewed" if r['stub_marker']
                      else f"not marked stub but state={r['state']}")
            print(f"  {r['id']:20} {r['file']:42} {status}")
        if len(mismatches) > 20:
            print(f"  ... and {len(mismatches) - 20} more")
        print()

    if MISSING_ONLY or DETAIL:
        for r in all_results:
            if MISSING_ONLY and r['state'] == 'reviewed':
                continue
            missing = [b for b in ('rationale', 'story', 'checklist', 'status') if not r[b]]
            print(f"{r['id']:20} {r['file']:42} [{r['state']:12}] missing: {', '.join(missing) if missing else '-'}")


if __name__ == '__main__':
    main()
