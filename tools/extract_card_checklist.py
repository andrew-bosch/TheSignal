#!/usr/bin/env python3
"""Extract Art 04 per-card Design Checklist tables into card_checklist SQL.

Card headings are NOT always a reliable card_id source: a handful of cards
(e.g. STD.CA.11/12/13/14 "Disinformation Campaign" etc.) use a literal
"### STANDARD — <NAME>" heading with no real ID in the heading text itself —
the true ID only exists as `card_id="..."` inside the card's own `Card(...)`
python block later in the same section. Trusting the heading alone collided
4+ distinct cards onto a single fake "STANDARD" card_id (caught via a UNIQUE
constraint violation on load, S155). Ground truth is always the `card_id=`
field inside the Card() block if present; the heading text is only a fallback
for the (rare) card that has no such field.
"""
import re
import sys
import os

FILES_TO_PARSE = [
    "V1/04___Card_System___Part2_Standard.md",
    "V1/04___Card_System___Part3_Ring_Modifiers.md",
    "V1/04___Card_System___Part4a_Guild.md",
    "V1/04___Card_System___Part4b_Ghost.md",
    "V1/04___Card_System___Part4c_Directorate.md",
    "V1/04___Card_System___Part4d_Network.md",
    "V1/04___Card_System___Part4e_Syndicate.md",
]

CARD_ID_FIELD_RE = re.compile(r'\bcard_id\s*=\s*"([^"]+)"')

def escape_sql_mysql(text):
    if text is None:
        return 'NULL'
    mapping = {
        '\\': '\\\\',
        "'": "\\'",
        '"': '\\"',
        '\n': '\\n',
        '\r': '\\r',
        '\0': '\\0',
    }
    escaped = ''.join(mapping.get(c, c) for c in text)
    return f"'{escaped}'"

def main():
    total_headers_per_file = {}
    grand_total_rows = 0
    zero_row_cards = []
    failed_rows = []
    id_overrides = []  # (heading_id, real_card_id) where they differ
    skipped_collisions = []  # real_id already used by an earlier card with real rows (e.g. shared "Ghost-ext-TBD" placeholder)
    no_id_cards = []  # (heading_text, row_count) — real checklist content but no resolvable FAC.TYPE.n card_id
    seen_ids_with_rows = set()

    sql_statements = ["DELETE FROM card_checklist;"]

    for filepath in FILES_TO_PARSE:
        total_headers_per_file[filepath] = 0
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found.", file=sys.stderr)
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        source_file = os.path.basename(filepath)
        heading_card_id = None
        section_lines = []       # all lines since current heading, for card_id= lookup
        rows_buffer = []         # (category, verdict, note, artifact_ref) for current card
        checklist_active = False
        in_table = False

        def flush_section():
            nonlocal grand_total_rows
            if heading_card_id is None:
                return
            section_text = ''.join(section_lines)
            m = CARD_ID_FIELD_RE.search(section_text)
            real_id = m.group(1) if m else heading_card_id
            if real_id != heading_card_id:
                id_overrides.append((heading_card_id, real_id))

            if not rows_buffer:
                zero_row_cards.append(real_id)
                return

            # A resolved id with no '.' is a bare heading word (e.g. "Ghost"), not a
            # real FAC.TYPE.n card_id — means no `card_id=` field was found in the
            # Card() block at all (known case: Backdate/Field Verification share the
            # placeholder id="Ghost-ext-TBD", same gap already excluded from
            # card_status per schema_reference.md). Don't mislabel real content under
            # a fake bare-word id — skip and report explicitly instead.
            if '.' not in real_id:
                no_id_cards.append((heading_card_id, len(rows_buffer)))
                return

            if real_id in seen_ids_with_rows:
                skipped_collisions.append(real_id)
                return
            seen_ids_with_rows.add(real_id)

            for category, verdict, note, artifact_ref in rows_buffer:
                grand_total_rows += 1
                sql = "INSERT INTO card_checklist (card_id, category, verdict, note, artifact_ref, source_file) VALUES ("
                sql += f"{escape_sql_mysql(real_id)}, "
                sql += f"{escape_sql_mysql(category)}, "
                sql += f"{escape_sql_mysql(verdict)}, "
                sql += f"{escape_sql_mysql(note)}, "
                sql += f"{escape_sql_mysql(artifact_ref)}, "
                sql += f"{escape_sql_mysql(source_file)});"
                sql_statements.append(sql)

        for line in lines:
            line_stripped = line.strip()

            header_match = re.match(r'^### ([A-Za-z0-9_.]+) —', line)
            if header_match:
                flush_section()

                heading_card_id = header_match.group(1)
                total_headers_per_file[filepath] += 1
                section_lines = [line]
                rows_buffer = []
                checklist_active = False
                in_table = False
                continue

            if heading_card_id is None:
                continue

            section_lines.append(line)

            if '**Design checklist:**' in line:
                checklist_active = True
                continue

            if checklist_active:
                if not in_table:
                    if line_stripped.startswith('|'):
                        in_table = True

                if in_table:
                    if not line_stripped.startswith('|'):
                        checklist_active = False
                        in_table = False
                        continue

                    if 'Category | Pass | Note' in line_stripped:
                        continue
                    if re.match(r'^\|[-|\s]+\|$', line_stripped):
                        continue

                    raw_row = line_stripped
                    if raw_row.startswith('|'): raw_row = raw_row[1:]
                    if raw_row.endswith('|'): raw_row = raw_row[:-1]

                    parts = re.split(r'(?<!\\)\|', raw_row)
                    parts = [p.strip().replace('\\|', '|') for p in parts]

                    if len(parts) != 4:
                        failed_rows.append((heading_card_id, line_stripped))
                    else:
                        rows_buffer.append(tuple(parts))

        flush_section()

    os.makedirs('Database', exist_ok=True)
    with open('Database/card_checklist_load.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sql_statements) + '\n')

    print(f"(1) Total card headers found per file:")
    for fp, count in total_headers_per_file.items():
        print(f"  {fp}: {count}")

    print(f"\n(2) Total checklist rows extracted: {grand_total_rows}")

    print(f"\n(3) Card IDs with zero checklist rows:")
    if not zero_row_cards:
        print("  None")
    else:
        for cid in zero_row_cards:
            print(f"  {cid}")

    print(f"\n(4) Failed rows (did not parse into 4 fields):")
    if not failed_rows:
        print("  None")
    else:
        for cid, line in failed_rows:
            print(f"  {cid}: {line}")

    print(f"\n(5) Heading-vs-card_id= overrides applied ({len(id_overrides)}):")
    for heading_id, real_id in id_overrides:
        print(f"  heading said '{heading_id}' -> using '{real_id}'")

    print(f"\n(6) Skipped — real_id collided with an already-loaded card ({len(skipped_collisions)}):")
    if not skipped_collisions:
        print("  None")
    else:
        for cid in skipped_collisions:
            print(f"  {cid} (no real card_id= field; shares a placeholder id= with another card — needs manual ID assignment before it can be loaded)")

    print(f"\n(7) Skipped — no resolvable card_id at all ({len(no_id_cards)}):")
    if not no_id_cards:
        print("  None")
    else:
        for heading, n in no_id_cards:
            print(f"  heading '{heading}' section, {n} checklist rows dropped — no card_id= field found")

if __name__ == '__main__':
    main()
