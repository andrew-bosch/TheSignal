#!/usr/bin/env python3
"""
schema_cleanup_log #66 (S157) — rebuild `card_effect_component` from .md (SOT).

`card_effect_component` decomposes each card's outcome fields into priced units.
`v_card_pair_uvm_cost.total_pair_cost` is computed from it, and every
`value_rating` tier in the corpus is derived from that — so this table is the
foundation of the cost model. It had NO extractor: it was populated once by an
ad-hoc script that was not kept, and by S157 a third of its rows still carried
the retired `+=`/`-=` syntax swept out of the corpus months earlier.

Reads `card_body` (itself rebuilt from .md by extract_card_body.py), so run
this AFTER that. Writes Database/card_effect_load.sql; does not load it.

Usage:
  python3 tools/extract_card_effects.py            # write load SQL
  python3 tools/extract_card_effects.py --compare  # diff vs current DB, no write
"""
import re, subprocess, sys, os

TIERS = ['success', 'successcrit', 'fail', 'failcrit']

# Classification is ordered — first match wins. Specific before generic, because
# e.g. arbiter.remove(IntelToken, ...) must read as token_delta, not resource.
CATEGORY_RULES = [
    ('reveal',          [r'\breveal', r'reveal_private', r'\bannounce\(']),
    # target_object.alter(type=NamedParty|Terms|TermRemoval) mutates an Accord without
    # the word appearing anywhere in the expression — SYN.CA.10/11, SYN.MOD.1.
    ('accord_action',   [r'accord', r'AccordForm', r'AccordAgreement',
                         r'target_object\.alter', r'NamedParty', r'TermRemoval',
                         r'declared_clause']),
    ('token_delta',     [r'IntelToken', r'intel_token', r'DebriefActionCard', r'\bDA-0']),
    ('standing_delta',  [r'standing', r'StandingMarker', r'\bps\b']),
    ('presence_delta',  [r'presence', r'PresenceToken', r'DeploymentMarker',
                         r'deployment_marker', r'influence_tier', r'presence_chip']),
    ('board_condition', [r'board_condition', r'world_condition', r'\bblock\(',
                         r'apply_modifier', r'StructureBlock', r'structure_block',
                         r'set_flag', r'resolution_grid', r'\bcancel\(', r'\bcorrupt\(',
                         r'\bstructure\(', r'threshold', r'\bVM_', r'_obligation',
                         r'\bactivate\(']),
    ('resource_delta',  [r'\bnative\b', r'\bcapacity\b', r'\bcapital\b', r'\bmandate\b',
                         r'\bexposure\b', r'\bfindings\b', r'resource', r'\bgrant\(']),
]

def classify(expr):
    low = expr.lower()
    for cat, pats in CATEGORY_RULES:
        for p in pats:
            if re.search(p, expr) or re.search(p, low):
                return cat
    return 'other'

def find_target(expr):
    if re.search(r'faction\(target|target_faction|\(target\)|faction\(trigger', expr):
        return 'target'
    if re.search(r'faction\(acting|\bacting\b|faction\(holding|\bholder\b', expr):
        return 'acting'
    if re.search(r'district', expr):
        return 'district'
    return 'other'

def find_magnitude(expr):
    """Signed integer magnitude, or None when the expression is not a plain count."""
    if re.search(r'n_boost|declared\(|count\(|\.each\(|n_declared', expr):
        return None                      # variable — priced via has_boost, not magnitude
    neg = bool(re.search(r'\.remove\(|\bremove\(|\bcancel\(|\bblock\(', expr))
    m = (re.search(r'\.(?:add|remove)\(\s*(\d+)', expr)
         or re.search(r'count\s*=\s*(\d+)', expr)
         or re.search(r'\.(?:add|remove)\([^,)]*,\s*(\d+)\s*\)', expr)
         or re.search(r'[-+]?\s*(\d+)\s*$', expr.strip()))
    if not m:
        return None
    v = int(m.group(1))
    return -v if neg else v

def split_components(raw):
    """Split a MutationExpr into components across the three coexisting
    multi-mutation notations (#58): bare tuple, bare list, list([...])."""
    s = raw.strip()
    if s.startswith('list(') and s.endswith(')'):
        s = s[5:-1].strip()
    if (s.startswith('(') and s.endswith(')')) or (s.startswith('[') and s.endswith(']')):
        s = s[1:-1]
    parts, depth, cur = [], 0, ''
    for ch in s:
        if ch in '([{':
            depth += 1
        elif ch in ')]}':
            depth -= 1
        if ch == ',' and depth == 0:
            parts.append(cur); cur = ''
        else:
            cur += ch
    parts.append(cur)
    out = []
    for p in parts:
        p = ' '.join(p.split())
        p = re.sub(r'\s*#.*$', '', p).strip()       # strip trailing inline comment
        # A bare identifier with no call and no operator is a marker/flag in a list
        # (e.g. DIR.CA.5's `Discovery`), not a mutation — it prices nothing.
        if p and p != 'None' and not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', p):
            out.append(p)
    return out

def q(v):
    if v is None:
        return 'NULL'
    return "'" + str(v).replace('\\', '\\\\').replace("'", "\\'") + "'"

def fetch_rows():
    # on_accept/on_decline carry the whole effect on ElectPlayer cards (SYN.CA.7,
    # DIR.PA.8, SYN.PA.1 ...), and persistence_effect carries it on card-as-condition
    # PAs. Omitting them prices those cards at 0. The `tier` column is an ENUM that
    # cannot hold their names, so they are recorded as the tier they resolve at with
    # the source field prefixed onto raw_expr — the original table's own convention.
    sql = ("SELECT card_id, field_name, raw_value FROM card_body "
           "WHERE field_name IN ('success','successcrit','fail','failcrit',"
           "'on_accept','on_decline','persistence_effect') "
           "AND raw_value <> 'None';")
    out = subprocess.run(['mariadb', 'the_signal_db', '-N', '-B', '-e', sql],
                         capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        parts = line.split('\t')
        if len(parts) >= 3:
            rows.append((parts[0], parts[1], '\t'.join(parts[2:]).replace('\\n', '\n')))
    return rows

AUX_FIELDS = {'on_accept': 'success', 'on_decline': 'fail', 'persistence_effect': 'success'}

def build():
    comps, prose = [], []
    for card_id, field, raw in fetch_rows():
        if raw.lstrip().startswith('"'):
            prose.append((card_id, field))      # bare-prose outcome — 04-n218/n220
            continue
        tier = AUX_FIELDS.get(field, field)
        prefix = f'{field}: ' if field in AUX_FIELDS else ''
        for expr in split_components(raw):
            comps.append((card_id, tier, classify(expr), find_target(expr),
                          find_magnitude(expr), prefix + expr))
    return comps, prose

def main():
    comps, prose = build()
    if '--compare' in sys.argv:
        cur = subprocess.run(['mariadb', 'the_signal_db', '-N', '-B', '-e',
                              'SELECT COUNT(*) FROM card_effect_component;'],
                             capture_output=True, text=True).stdout.strip()
        print(f"current DB rows : {cur}")
        print(f"extracted rows  : {len(comps)}")
        print(f"cards covered   : {len({c[0] for c in comps})}")
        print(f"skipped (prose) : {len(prose)}  {[p[0] for p in prose]}")
        from collections import Counter
        print("\nby category:")
        for k, v in Counter(c[2] for c in comps).most_common():
            print(f"  {k:<16} {v}")
        print("\nunclassified sample ('other'):")
        for c in [c for c in comps if c[2] == 'other'][:8]:
            print(f"  {c[0]:<11} {c[5][:70]}")
        return

    lines = ['DELETE FROM card_effect_component;']
    for card_id, tier, cat, tgt, mag, expr in comps:
        lines.append(
            "INSERT INTO card_effect_component (card_id, tier, category, target, magnitude, raw_expr) "
            f"VALUES ({q(card_id)}, {q(tier)}, {q(cat)}, {q(tgt)}, "
            f"{'NULL' if mag is None else mag}, {q(expr)});")
    os.makedirs('Database', exist_ok=True)
    with open('Database/card_effect_load.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"card_effect_component rows: {len(comps)}  (cards: {len({c[0] for c in comps})})")
    print(f"skipped — bare-prose outcome fields (04-n218/n220): {len(prose)}")
    for cid, tier in prose:
        print(f"  {cid} ({tier})")

if __name__ == '__main__':
    main()
