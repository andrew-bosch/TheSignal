#!/usr/bin/env python3
"""Extract every Art 04 Card() block into a faithful, re-syncable DB projection.

Companion to extract_card_checklist.py. `.md` stays source of truth; this script
regenerates the DB tables from the Card() blocks so Art 04 card *bodies* (not just
their checklists) are queryable.

Design (hybrid, per Andy S156):
  * card_body            — EAV mirror: one row per (card_id, field_name), raw_value
                           verbatim. Faithful & future-proof across the heterogeneous
                           CA / PA / MOD field sets (a fixed wide table would be 40+
                           mostly-NULL columns). This is the literal "all the Card()".
  * card_restriction_clause — the one logic field decomposed now: restriction split
                           into top-level and/or clauses, each parsed to
                           subject/operator/value where cleanly parseable; raw_clause
                           always kept so nothing is lost.
  * v_card_body (view, defined in the DDL) pivots the common/promoted fields
                           (name, type, trigger, persistence, value_rating, narrative,
                           restriction, cost, ...) into columns for convenient querying.

card_id resolution: the `card_id="..."` field inside the block is ground truth
(same lesson as the checklist extractor — headings collided distinct cards, S155).
A resolved id with no '.' (bare word / "Ghost-ext-TBD" placeholder) means the block
has no real FAC.TYPE.n id — those are the deferred/blocked fossils; they're reported
and skipped, matching card_status's exclusion of them.
"""
import re
import sys
import os

FILES_TO_PARSE = [
    "V1/04___Card_System___Part1_Core.md",
    "V1/04___Card_System___Part2_Standard.md",
    "V1/04___Card_System___Part3_Ring_Modifiers.md",
    "V1/04___Card_System___Part4a_Guild.md",
    "V1/04___Card_System___Part4b_Ghost.md",
    "V1/04___Card_System___Part4c_Directorate.md",
    "V1/04___Card_System___Part4d_Network.md",
    "V1/04___Card_System___Part4e_Syndicate.md",
]

# LHS = Card(  at (indent-0) column, capturing the python var name before it.
CARD_OPEN_RE = re.compile(r'^([A-Za-z0-9_.\-]+)\s*=\s*Card\(', re.MULTILINE)

# Accept dotted deck ids (FAC.TYPE.n) and GD-nn/DA-nn hyphen ids. Rejects the blocked
# fossils' "Ghost-ext-TBD" placeholder (not 2-letter+digits) and bare python var names.
HYPHEN_ID_RE = re.compile(r'^[A-Z]{2}-\d+$')

OPEN = {'(': ')', '[': ']', '{': '}'}
CLOSE = {')', ']', '}'}


def find_block_end(text, open_paren_idx):
    """Given index of the '(' after Card, return index just past its matching ')'.
    Tracks only paren depth for the outer match, but is string- and comment-aware."""
    depth = 0
    i = open_paren_idx
    n = len(text)
    in_str = None  # quote char when inside a string
    while i < n:
        c = text[i]
        if in_str:
            if c == '\\':
                i += 2
                continue
            if c == in_str:
                in_str = None
            i += 1
            continue
        if c in ('"', "'"):
            in_str = c
        elif c == '#':
            nl = text.find('\n', i)
            i = n if nl == -1 else nl
            continue
        elif c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return -1


def split_top_level_fields(body):
    """Split the interior of Card(...) into raw 'key = value' segments at depth-0 commas,
    string- and comment-aware. Returns list of raw segment strings."""
    segments = []
    depth = 0
    in_str = None
    cur = []
    i = 0
    n = len(body)
    while i < n:
        c = body[i]
        if in_str:
            cur.append(c)
            if c == '\\' and i + 1 < n:
                cur.append(body[i + 1])
                i += 2
                continue
            if c == in_str:
                in_str = None
            i += 1
            continue
        if c in ('"', "'"):
            in_str = c
            cur.append(c)
        elif c == '#':
            nl = body.find('\n', i)
            i = n if nl == -1 else nl
            continue
        elif c in OPEN:
            depth += 1
            cur.append(c)
        elif c in CLOSE:
            depth -= 1
            cur.append(c)
        elif c == ',' and depth == 0:
            seg = ''.join(cur).strip()
            if seg:
                segments.append(seg)
            cur = []
        else:
            cur.append(c)
        i += 1
    seg = ''.join(cur).strip()
    if seg:
        segments.append(seg)
    return segments


def split_key_value(segment):
    """Split a segment on its first depth-0 '=' that is not part of '==' / '>=' etc.
    Returns (key, raw_value) or None if no assignment found."""
    depth = 0
    in_str = None
    i = 0
    n = len(segment)
    while i < n:
        c = segment[i]
        if in_str:
            if c == '\\':
                i += 2
                continue
            if c == in_str:
                in_str = None
            i += 1
            continue
        if c in ('"', "'"):
            in_str = c
        elif c in OPEN:
            depth += 1
        elif c in CLOSE:
            depth -= 1
        elif c == '=' and depth == 0:
            prev = segment[i - 1] if i > 0 else ''
            nxt = segment[i + 1] if i + 1 < n else ''
            if nxt == '=' or prev in ('=', '!', '<', '>'):
                i += 1
                continue
            key = segment[:i].strip()
            val = segment[i + 1:].strip()
            return key, val
        i += 1
    return None


def strip_wrapping_parens(s):
    s = s.strip()
    while s.startswith('(') and s.endswith(')'):
        # verify the leading '(' matches the trailing ')'
        depth = 0
        matched_at_end = False
        in_str = None
        for j, c in enumerate(s):
            if in_str:
                if c == '\\':
                    continue
                if c == in_str:
                    in_str = None
                continue
            if c in ('"', "'"):
                in_str = c
            elif c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    matched_at_end = (j == len(s) - 1)
                    break
        if matched_at_end:
            s = s[1:-1].strip()
        else:
            break
    return s


CLAUSE_SPLIT_RE = None  # split handled manually below

CLAUSE_OP_RE = re.compile(r'\s*(>=|<=|==|!=|>|<|=)\s*')


def split_restriction_clauses(raw):
    """Split a restriction expression into top-level 'and'/'or' clauses.
    Returns list of (connector, raw_clause). connector is the word joining to the
    previous clause ('and'/'or'), None for the first."""
    if raw is None:
        return []
    r = raw.strip()
    if r in ('None', ''):
        return []
    r = strip_wrapping_parens(r)
    clauses = []
    depth = 0
    in_str = None
    cur = []
    connector = None
    i = 0
    n = len(r)
    tokens_lower = r
    while i < n:
        c = r[i]
        if in_str:
            cur.append(c)
            if c == '\\' and i + 1 < n:
                cur.append(r[i + 1]); i += 2; continue
            if c == in_str:
                in_str = None
            i += 1
            continue
        if c in ('"', "'"):
            in_str = c; cur.append(c); i += 1; continue
        if c in OPEN:
            depth += 1; cur.append(c); i += 1; continue
        if c in CLOSE:
            depth -= 1; cur.append(c); i += 1; continue
        if depth == 0:
            # look for whitespace-delimited 'and'/'or'
            for kw in ('and', 'or'):
                end = i + len(kw)
                before_ok = (i == 0) or r[i - 1].isspace() or r[i - 1] in ')'
                after_ok = (end >= n) or r[end].isspace()
                if tokens_lower[i:end].lower() == kw and before_ok and after_ok and i > 0:
                    clause = ''.join(cur).strip()
                    if clause:
                        clauses.append((connector, clause))
                    connector = kw
                    cur = []
                    i = end
                    break
            else:
                cur.append(c); i += 1
            continue
        cur.append(c); i += 1
    clause = ''.join(cur).strip()
    if clause:
        clauses.append((connector, clause))
    return clauses


def parse_clause(raw_clause):
    """Try to split a single clause into (subject, operator, value). Returns
    (subject, op, value) with None where it can't be cleanly parsed."""
    depth = 0
    in_str = None
    i = 0
    n = len(raw_clause)
    while i < n:
        c = raw_clause[i]
        if in_str:
            if c == in_str:
                in_str = None
            i += 1; continue
        if c in ('"', "'"):
            in_str = c; i += 1; continue
        if c in OPEN:
            depth += 1; i += 1; continue
        if c in CLOSE:
            depth -= 1; i += 1; continue
        if depth == 0 and c in '<>=!':
            m = CLAUSE_OP_RE.match(raw_clause, i)
            if m:
                op = m.group(1)
                subject = raw_clause[:i].strip()
                value = raw_clause[m.end():].strip()
                return subject or None, op, value or None
        i += 1
    return None, None, None


def escape_sql(text):
    if text is None:
        return 'NULL'
    mapping = {'\\': '\\\\', "'": "\\'", '"': '\\"', '\n': '\\n', '\r': '\\r', '\0': '\\0'}
    return "'" + ''.join(mapping.get(c, c) for c in text) + "'"


def main():
    body_rows = []          # (card_id, field_name, raw_value, source_file)
    clause_rows = []        # (card_id, clause_index, connector, raw_clause, subject, op, value)
    per_file_counts = {}
    skipped_no_id = []      # (var_name, source_file)
    dup_ids = []            # card_id seen more than once
    seen_ids = set()

    for filepath in FILES_TO_PARSE:
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found.", file=sys.stderr)
            continue
        source_file = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        count = 0
        for m in CARD_OPEN_RE.finditer(text):
            var_name = m.group(1)
            open_paren = text.index('(', m.start())
            end = find_block_end(text, open_paren)
            if end == -1:
                print(f"Warning: unterminated Card( for {var_name} in {source_file}", file=sys.stderr)
                continue
            body = text[open_paren + 1:end - 1]

            fields = {}
            order = []
            for seg in split_top_level_fields(body):
                kv = split_key_value(seg)
                if kv is None:
                    continue
                key, val = kv
                if key and key not in fields:
                    fields[key] = val
                    order.append(key)

            card_id = fields.get('card_id') or fields.get('id') or var_name
            card_id = card_id.strip().strip('"').strip("'")

            if '.' not in card_id and not HYPHEN_ID_RE.match(card_id):
                skipped_no_id.append((var_name, source_file))
                continue
            if card_id in seen_ids:
                dup_ids.append(card_id)
                continue
            seen_ids.add(card_id)
            count += 1

            for key in order:
                body_rows.append((card_id, key, fields[key], source_file))

            restriction_raw = fields.get('restriction')
            for idx, (connector, raw_clause) in enumerate(split_restriction_clauses(restriction_raw)):
                subj, op, value = parse_clause(raw_clause)
                clause_rows.append((card_id, idx, connector, raw_clause, subj, op, value))

        per_file_counts[source_file] = count

    # Emit load SQL
    out = ["DELETE FROM card_restriction_clause;", "DELETE FROM card_body;"]
    for card_id, field_name, raw_value, source_file in body_rows:
        out.append(
            "INSERT INTO card_body (card_id, field_name, raw_value, source_file) VALUES ("
            f"{escape_sql(card_id)}, {escape_sql(field_name)}, {escape_sql(raw_value)}, {escape_sql(source_file)});"
        )
    for card_id, idx, connector, raw_clause, subj, op, value in clause_rows:
        out.append(
            "INSERT INTO card_restriction_clause (card_id, clause_index, connector, raw_clause, subject, operator, value) VALUES ("
            f"{escape_sql(card_id)}, {idx}, {escape_sql(connector)}, {escape_sql(raw_clause)}, "
            f"{escape_sql(subj)}, {escape_sql(op)}, {escape_sql(value)});"
        )

    os.makedirs('Database', exist_ok=True)
    with open('Database/card_body_load.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')

    print("(1) Cards parsed per file:")
    total = 0
    for fp, c in per_file_counts.items():
        print(f"  {fp}: {c}")
        total += c
    print(f"  TOTAL: {total}")
    print(f"\n(2) card_body field rows: {len(body_rows)}")
    print(f"(3) card_restriction_clause rows: {len(clause_rows)}")
    print(f"\n(4) Skipped (no real FAC.TYPE.n card_id — deferred/blocked fossils): {len(skipped_no_id)}")
    for var_name, sf in skipped_no_id:
        print(f"  {var_name} ({sf})")
    print(f"\n(5) Duplicate card_ids skipped: {len(dup_ids)}")
    for cid in dup_ids:
        print(f"  {cid}")


if __name__ == '__main__':
    main()
