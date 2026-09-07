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

FACTIONS = ('Syndicate', 'Guild', 'Ghost', 'Network', 'Directorate')

# --- `target` semantics (rewritten S160, PM05 04-n234) --------------------------
# `target` names THE ENTITY WHOSE HOLDINGS THIS ROW CHANGES.
#
# It used to name "whichever entity a four-rule regex cascade mentioned first",
# which is a different question and disagreed with this one on 108 of 355 rows
# (30%). Four defect classes, all fixed here: `faction(Syndicate)`-style hardcoded
# names were invisible to the acting test; the `district` test fired before
# anything read `faction=`; type/currency qualifiers (`IntelToken(faction=X)`,
# `source=faction(X).supply`) read as possession; and there was no value at all
# for a named faction that is neither acting nor the target.
#
# Vocabulary: acting | target | third_party | district | none | other.
# Downstream, value-to-acting derives as  magnitude x (+1 if acting else -1).

# Calls whose ARGUMENTS name a type/currency/key rather than a possessor. Only the
# arguments are blanked -- the accessor survives, so `faction(holder).native(...).add(1)`
# still exposes `faction(holder)...add(` as the receiver.
_QUAL_CALLS = [
    r'IntelToken\s*\(', r'PhantomRecord\s*\(',
    r'AccordForm\s*\(', r'GrantDeed\s*\(', r'DebriefActionCard\s*\(',
    r'\.native\s*\(', r'\.resource\s*\(', r'presence_count\s*\(',
    r'count_attributed_actions\s*\(', r'resource_generation\s*\(',
    r'active_permanents\s*\(',
]

def _blank_args(expr):
    for pat in _QUAL_CALLS:
        rx, pos = re.compile(pat), 0
        while True:
            m = rx.search(expr, pos)
            if not m:
                break
            i = m.end() - 1                       # the '('
            depth, j = 0, i
            while j < len(expr):
                if expr[j] == '(':
                    depth += 1
                elif expr[j] == ')':
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            if j >= len(expr):                    # unbalanced — leave it alone
                pos = m.end()
                continue
            expr = expr[:i + 1] + '_' + expr[j:]
            pos = i + 3
    # a source/origin is never the beneficiary (STD.CA.15: source=faction(target).supply)
    expr = re.sub(r'\bsource\s*=\s*[\w().\[\]]+', ' ', expr)
    expr = re.sub(r'\bfrom_?\s*=\s*[\w().\[\]]+', ' ', expr)
    return expr

# Ordered: an explicit destination outranks a mutation receiver, which outranks a
# bare `faction=` argument.
_RECEIVER = [
    r'\btransfer\s*\(\s*faction\(\s*(\w+)\s*\)',
    r'game\.transfer\s*\([^,]*,[^,]*,\s*faction\(\s*(\w+)\s*\)',
    r'\b(?:to|recipient|with_faction)\s*=\s*faction\(\s*(\w+)\s*\)',
    r'\b(?:to|recipient|with_faction)\s*=\s*(\w+)',
    r'faction\(\s*([\w.]+)\s*\)[\w.\[\]()]*\.(?:add|remove|sub|gain|lose)\s*\(',
    r'\bfaction\s*=\s*(\w+)',
    r'(?:arbiter|game)\.(?:deliver|dispatch|grant)\s*\(\s*faction\(\s*(\w+)\s*\)',
    r'(?:arbiter|game)\.(?:deliver|dispatch|grant)\s*\(\s*(\w+)',
    r'(?:arbiter|game)\.(?:deliver|dispatch|discard_hand)\s*\(.*,\s*(\w+)\s*\)',
    r'\brecipient\s*=\s*faction\(\s*([\w.]+)\s*\)',
    r'faction\(\s*([\w.]+)\s*\)',
]

def _role_of(tok, card_faction):
    if not tok:
        return None
    t = tok.strip()
    if t in ('acting', 'holder', 'holding', 'submitter'):
        return 'acting'
    if t in ('target_district', 'trigger.district'):
        return 'district'
    if t.startswith('target') or t.startswith('trigger') or t == 'named_opponent':
        return 'target'
    if t in FACTIONS:
        # On a faction card the card's own name IS the acting faction. On a
        # Standard/Ring card (faction=All) a named faction can only be someone else.
        return 'acting' if t == card_faction else 'third_party'
    if t.startswith('district') or t in ('board', 'target_district'):
        return 'district'
    return None

# Rows that change nobody's holdings: pure information, flag- and threshold-setting.
_NO_HOLDINGS = re.compile(
    r'\breveal|announce\(|set_flag|\.threshold|apply_modifier|\bblocked_at\(|'
    r'board_condition\(|world_condition\(', re.I)

_IS_MOVE = re.compile(r'\btransfer\s*\(|\.move\s*\(|\bredirect\s*\(')

def _move_destination(e, card_faction):
    """For a transfer/move, `target` names WHERE THE THING ENDS UP -- so a single-row
    transfer says whether the acting faction received it or gave it away. An explicit
    `to=` wins, but only when it names a faction: `to=district(target)` is a place,
    not a holder (DIR.CA.4 relocates its OWN presence), so that falls through to the
    last faction reference, which is the mover."""
    m = re.search(r'\b(?:to|recipient)\s*=\s*(?:faction\(\s*(\w+)\s*\)|(\w+))', e)
    if m:
        role = _role_of(next((g for g in m.groups() if g), None), card_faction)
        if role and role != 'district':
            return role
    fac = re.findall(r'faction\(\s*(\w+)\s*\)', e)
    if fac:
        role = _role_of(fac[-1], card_faction)
        if role:
            return role
    eq = re.findall(r'\bfaction\s*=\s*(\w+)', e)
    if eq:
        role = _role_of(eq[-1], card_faction)
        if role:
            return role
    return None


def find_target(expr, card_faction=None):
    e = _blank_args(expr)
    if _IS_MOVE.search(e):
        role = _move_destination(e, card_faction)
        if role:
            return role
    for pat in _RECEIVER:
        m = re.search(pat, e)
        if m:
            role = _role_of(m.group(1), card_faction)
            if role:
                return role
    if re.search(r'\bdistrict\b', e):
        return 'district'
    if _NO_HOLDINGS.search(e):
        return 'none'
    # Corpus convention: an unattributed GAIN (`IntelToken(...).add(1)`) is the acting
    # faction receiving. Deliberately not extended to removals — an unresolved
    # `arbiter.remove(X, from=...)` is the acting faction acting ON something else, and
    # defaulting it to 'acting' would flip the value sign. Those stay 'other'.
    if re.search(r'\.add\s*\(', e):
        return 'acting'
    if re.search(r'\b(?:remove|discard|cancel|destroy)\b', e):
        return 'target' if re.search(r'\btarget|\btrigger', e) else 'other'
    return 'other'

def find_magnitude(expr):
    """Signed integer magnitude, or None when the expression is not a plain count."""
    if re.search(r'n_boost|declared\(|count\(|\.each\(|n_declared', expr):
        return None                      # variable — priced via has_boost, not magnitude
    neg = bool(re.search(r'\.remove\(|\bremove\(|\bcancel\(|\bblock\(', expr))
    m = (re.search(r'\.(?:add|remove)\(\s*(\d+)', expr)
         or re.search(r'count\s*=\s*(\d+)', expr)
         # S160 (04-n235): a fixed multiplier on a TYPE reference is a real magnitude
         # that was being read as the 1-unit floor. Restricted to `.native * N` and
         # `IntelToken(...) * N` on purpose — `structure * 1` (GUI.PA.4) and
         # `trigger.amount * 2` (GHO.MOD.5) multiply a *counted* thing, so reading
         # those would hide genuine variability rather than recover a magnitude.
         or re.search(r'\.native\s*\*\s*(\d+)', expr)
         or re.search(r'IntelToken\([^()]*\)\s*\*\s*(\d+)', expr)
         # a `min(N, ...)` cap is the designed ceiling, not a variable (STD.PA.6)
         or re.search(r'\bmin\(\s*(\d+)\s*,', expr)
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

def fetch_factions():
    """card_id -> faction, from card_body (.md is SOT). find_target needs it to tell
    a card naming its OWN faction (the acting faction) from one naming another's."""
    out = subprocess.run(['mariadb', 'the_signal_db', '-N', '-B', '-e',
                          "SELECT card_id, raw_value FROM card_body "
                          "WHERE field_name = 'faction';"],
                         capture_output=True, text=True).stdout
    return dict(l.split('\t', 1) for l in out.splitlines() if '\t' in l)


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
    factions = fetch_factions()
    for card_id, field, raw in fetch_rows():
        if raw.lstrip().startswith('"'):
            prose.append((card_id, field))      # bare-prose outcome — 04-n218/n220
            continue
        tier = AUX_FIELDS.get(field, field)
        prefix = f'{field}: ' if field in AUX_FIELDS else ''
        for expr in split_components(raw):
            comps.append((card_id, tier, classify(expr),
                          find_target(expr, factions.get(card_id)),
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
