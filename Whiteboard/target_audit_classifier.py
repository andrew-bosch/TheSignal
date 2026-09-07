"""
S160 audit instrument for PM05 04-n234 — `card_effect_component.target` semantics.

STATUS:   Reference only. NOT wired into any tool or sync path, and deliberately so.
PURPOSE:  Implements the *proposed* definition of `target` (the entity whose holdings
          a row changes) and diffs it against the stored values, to size the defect.
          Result at S160: 179 agree, 108 confirmed misclassified, 21 mixed,
          45 unresolved by this classifier (its own limitation, not the DB's --
          the six toll cards are the clearest example: it over-strips
          `native(faction=...)` and loses the receiver, where stored `acting` is right).
TRIGGER:  Whoever implements 04-n234 should start from this and fix the three known
          weaknesses: over-stripping in QUAL, no source-vs-destination handling for
          `.move(from, to)`, and no `none` value for board-level rows that belong to
          no faction.
DELETE:   when 04-n234 is closed and a corrected find_target() ships in
          tools/extract_card_effects.py. This file is not the fix.
"""

import re, subprocess, csv, io, collections

FACTIONS = ('Syndicate','Guild','Ghost','Network','Directorate')

q = ("SELECT e.id, e.card_id, s.faction, e.tier, e.category, e.target, "
     "COALESCE(e.magnitude,'NULL'), REPLACE(REPLACE(e.raw_expr,'\\t',' '),'\\n',' ') "
     "FROM card_effect_component e JOIN card_status s ON s.card_id=e.card_id ORDER BY e.id;")
out = subprocess.run(['mysql','the_signal_db','-N','-B','-e',q],
                     capture_output=True, text=True).stdout
rows=[l.split('\t') for l in out.strip().split('\n')]

# --- strip contexts where a faction name is a TYPE/KEY qualifier, not a possessor ---
QUAL = [
    r'IntelToken\s*\([^)]*\)',            # IntelToken(faction=X) / IntelToken(X)
    r'PhantomRecord\s*\([^)]*\)',
    r'target_profile[\w.]*',
    r'if_acting_faction\s*=\s*\w+',
    r'\.native\b(?!\s*\.)',               # "faction(target).native" as a currency type
    r'native\s*\(\s*faction\s*=[^)]*\)',
    r'count_attributed_actions\s*\([^)]*\)',
    r'resource_generation\s*\([^)]*\)',
    r'presence_count\s*\([^)]*\)',
    r'active_permanents\s*\([^)]*\)',
]
def strip_quals(e):
    for p in QUAL: e = re.sub(p,' ',e)
    return e

def acted_on(expr, card_faction):
    """Who does this row's holdings actually change? Returns a role token."""
    e = strip_quals(expr)

    # explicit destination wins over any source mention
    dest = re.search(r'(?:to|recipient|with_faction|action\s*=\s*transfer)\s*=?\s*\(?\s*'
                     r'faction\(\s*(\w+)\s*\)|(?:to|recipient)\s*=\s*(\w+)', e)
    # receiver of a mutation: X.add( / X.remove( / X.sub(
    mut = re.search(r'faction\(\s*(\w+)\s*\)[\w.()=]*\.(?:add|remove|sub)\s*\(', e)
    # arbiter.place/remove/deliver/dispatch(..., faction=X ...) or (X, ...)
    plc = re.search(r'arbiter\.(?:place|remove)\s*\([^)]*?faction\s*=\s*(\w+)', e)
    dlv = re.search(r'(?:arbiter|game)\.(?:deliver|dispatch|grant|transfer)\s*\(\s*'
                    r'(?:faction\(\s*(\w+)\s*\)|(\w+))', e)
    xfr = re.search(r'game\.transfer\s*\([^,]*,[^,]*,\s*faction\(\s*(\w+)\s*\)', e)

    who=None
    for m in (xfr, mut, plc, dlv, dest):
        if m:
            who = next((g for g in m.groups() if g), None)
            if who: break
    if not who:
        if re.search(r'\bdistrict\b', e): return 'district'
        return 'unresolved'

    if who in ('acting','holder','holding'): return 'acting'
    if who in ('target','target_faction','trigger'): return 'opponent'
    if who in FACTIONS:
        return 'acting' if who == card_faction else 'third_party'
    if who.startswith('district') or who=='board': return 'district'
    return 'unresolved'

MAP = {'acting':'acting','opponent':'target','district':'district',
       'third_party':'other','unresolved':'other'}

dis=collections.Counter(); byclass=collections.defaultdict(list); total=0
for r in rows:
    if len(r)<8: continue
    _id,cid,cf,tier,cat,stored,mag,expr = r[:8]
    total+=1
    corrected = acted_on(expr, cf)
    if MAP[corrected] != stored:
        dis[(stored,corrected)] += 1
        byclass[(stored,corrected)].append((cid,cat,mag,expr[:95]))

print(f"rows audited: {total}")
agree = total - sum(dis.values())
print(f"agree: {agree}   disagree: {sum(dis.values())}  ({100*sum(dis.values())/total:.1f}%)\n")
print("stored -> corrected            n")
for (s,c),n in dis.most_common():
    print(f"  {s:9} -> {c:12} {n:4}")
import json
json.dump({f"{k[0]}->{k[1]}":v for k,v in byclass.items()}, open('disagree.json','w'), indent=1)
