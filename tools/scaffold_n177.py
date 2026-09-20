#!/usr/bin/env python3
"""04-n177 schema scaffolding sweep.

NOTE: SKIP_FIELDS/SKIP_CARDS encode the S163 rulings (PM02 L381), not permanent
truth. `is_unique`/`deck_limit` are skipped only because they are blocked on
04-n136 (PM05 04-n238) — revisit this script when that rules.

Inserts every §6.1 field a Card() block omits, per the S163 ruling
(PM02): explicit value on every card, absence is always a defect.

 - None-default fields  -> inserted as `= None`
 - persistence (ModReact) -> `= Immediate`, §6.1's documented class default
 - subtype              -> derived from faction (All->Standard, else FactionSpecific);
                           correlation verified 332/332, zero exceptions
 - acquisition / generating_card -> NOT touched; §6.2's S133 omit-unless-Issued
                           default stands
 - is_unique / deck_limit -> NOT touched; blocked on 04-n136
 - id / card_id         -> NOT touched; identity values, not placeholders

Placement: insertion-sort against §6.1 class order — a missing field is
written after the last canonically-preceding field present in the block,
so blocks move toward canonical order without wholesale reordering.
"""
import re, sys, glob, os

CANON = """card_id id version name tagline type subtype faction layer function subject
effect beat resolution threshold ring_mod doctrine_mod value_rating trigger resolution_type
outcome_type persistence persistence_condition persistence_clearing_trigger persistence_effect
target_district target_faction target_object target_freeform
affinity restriction cost boost success successcrit fail failcrit on_accept on_decline on_discard
portrait ps_framing ring_constraint ring_origin narrative perspectives design_note
arbiter_note""".split()
RANK = {f: i for i, f in enumerate(CANON)}

BASE = [f for f in CANON if f not in ("effect", "ring_constraint", "ring_origin")]
EXPECT = {
    "CovertOperation": BASE,
    "PublicAct":       BASE,
    "ModActionCard":   BASE + ["effect", "ring_constraint", "ring_origin"],
    "ModBattleCard":   BASE + ["effect", "ring_constraint", "ring_origin"],
    "ModReactCard":    BASE + ["ring_constraint", "ring_origin"],
}
SKIP_FIELDS = {"id", "card_id", "acquisition", "generating_card", "is_unique", "deck_limit"}
# pre-known exceptions: GD-01 template + two 🚫 BLOCKED deferred-design cards
SKIP_CARDS  = {"Grant Deed", "Backdate", "Field Verification"}

def field_spans(code):
    """{field: (start_line, end_line)} for TOP-LEVEL fields of the Card( call only.

    Depth-aware: a `field =` inside a nested constructor (PSFraming(...),
    game.board_condition(...), a parenthesised multi-line value) is an argument,
    not a Card field, and must never be treated as an anchor. Inserting against a
    line-number-only map puts the new field inside the nested expression.
    """
    k = code.index("= Card(") + len("= Card(")
    depth, line = 1, code[:k].count("\n")
    spans, cur = {}, None
    i = k
    while i < len(code):
        ch = code[i]
        if ch == "\n":
            line += 1
            nxt = code.find("\n", i + 1)
            text = code[i + 1: nxt if nxt > 0 else len(code)]
            if depth == 1:
                m = re.match(r"\s*([a-z_]+)\s*=", text)
                if m:
                    if cur:
                        spans[cur][1] = line - 1
                    cur = m.group(1)
                    spans.setdefault(cur, [line, line])
        elif ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
            if depth == 0:
                if cur:
                    spans[cur][1] = line - 1
                break
        i += 1
    # packed same-line fields: `a = 1,  b = 2,`
    for f, (st, en) in list(spans.items()):
        pass
    return {f: tuple(v) for f, v in spans.items()}


def fields_present(code):
    """Top-level field -> the line its value ENDS on (safe insertion anchor)."""
    spans = field_spans(code)
    out = {f: en for f, (st, en) in spans.items()}
    # also catch fields packed onto an already-counted top-level line
    for i, line in enumerate(code.split("\n")):
        seg = line.split("#")[0]
        names = re.findall(r"(?:^|,)\s*([a-z_]+)\s*=", seg)
        if len(names) > 1 and names[0] in out:
            for n in names[1:]:
                out.setdefault(n, out[names[0]])
    return out

def scaffold(block):
    """block = raw text between ```python and ```. Returns (new_block, added)."""
    lines = block.split("\n")
    code  = "\n".join(l.split("#")[0] for l in lines)
    tm = re.search(r"\btype\s*=\s*(\w+)", code)
    if not tm or tm.group(1) not in EXPECT:
        return block, []
    typ = tm.group(1)
    nm  = re.search(r"\bname\s*=\s*\"?([^\",\n]+)", code)
    if nm and nm.group(1).strip() in SKIP_CARDS:
        return block, []
    fam = re.search(r"(?:^|,)\s*faction\s*=\s*(\w+)", code, re.M)
    faction = fam.group(1) if fam else None

    pres = fields_present(code)
    missing = [f for f in EXPECT[typ] if f not in pres and f not in SKIP_FIELDS]
    if not missing:
        return block, []

    # value for each inserted field
    def value(f):
        if f == "subtype":
            return "Standard" if faction == "All" else "FactionSpecific"
        if f == "persistence" and typ == "ModReactCard":
            return "Immediate"
        return "None"

    # closing paren line of the Card( ... ) call
    close = next((i for i in range(len(lines) - 1, -1, -1)
                  if lines[i].strip().startswith(")")), len(lines) - 1)
    indent = "    "
    added = []
    for f in sorted(missing, key=lambda x: RANK[x]):
        pres = fields_present("\n".join(l.split("#")[0] for l in lines))
        close = next((i for i in range(len(lines) - 1, -1, -1)
                      if lines[i].strip().startswith(")")), len(lines) - 1)
        anchor = -1
        for g, ln in pres.items():
            if g in RANK and RANK[g] < RANK[f] and ln < close:
                anchor = max(anchor, ln)
        at = (anchor + 1) if anchor >= 0 else close
        # match the anchor line's spacing: aligned `field   = v` or plain `field = v`
        anchor_line = lines[at - 1] if at > 0 else ""
        am = re.match(r"\s*[a-z_]+(\s+)=", anchor_line.split("#")[0])
        if am and len(am.group(1)) > 1:
            pad = len(anchor_line.split("#")[0].split("=")[0].rstrip()) - len(indent)
            lines.insert(at, f"{indent}{f:<{max(pad, len(f))}} = {value(f)},")
        else:
            lines.insert(at, f"{indent}{f} = {value(f)},")
        added.append((f, value(f)))
    return "\n".join(lines), added

def run(paths, write=False):
    tot_cards = tot_lines = 0
    for path in paths:
        txt = open(path).read()
        out = []; last = 0; n_c = n_l = 0
        for m in re.finditer(r"```python\n(.*?)```", txt, re.S):
            blk = m.group(1)
            if "= Card(" not in blk:
                continue
            new, added = scaffold(blk)
            if added:
                n_c += 1; n_l += len(added)
                out.append(txt[last:m.start(1)]); out.append(new); last = m.end(1)
        out.append(txt[last:])
        if write and n_c:
            open(path, "w").write("".join(out))
        print(f"  {os.path.basename(path):48} {n_c:>4} cards  {n_l:>5} lines")
        tot_cards += n_c; tot_lines += n_l
    print(f"  {'TOTAL':48} {tot_cards:>4} cards  {tot_lines:>5} lines")

if __name__ == "__main__":
    write = "--write" in sys.argv
    args  = [a for a in sys.argv[1:] if not a.startswith("--")]
    paths = args or sorted(glob.glob("V1/04___Card_System___Part[1-4]*.md"))
    print(("WRITING" if write else "DRY RUN") + ":")
    run(paths, write)
