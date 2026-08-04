**EXECUTION UPDATE (S147, PM02 L305):** the 397/22/3 counts below did not survive as an executable list — the original 9 agents' per-line output was never saved, only this summary. Re-derived from the actual corpus instead; see PM02 L305 for what was actually found and resolved (7 confirmed-duplicate templates, 84 lines) and what remains (a ~20-line stale-citation subset needing its own ruling; the rest of the singleton set reads as legitimate content, not discard-bucket noise). Treat the counts and per-template detail below as historical context, not a live to-do list.

# 04-n188 — Card() Comment Triage: Consolidated Report (S147)

Scope: 439 non-sanctioned `#` comments across 7 Part files (bucket 1's 917 lines already resolved and closed separately). All 439 now triaged by 9 agent passes (some files split/retried after an initial run hit fabricated line lists, and a separate run hung ~24h and was killed/retried in smaller batches). Every number below reconciles against the original per-file scope count — nothing missing, nothing double-counted.

**Nothing has been written back to the card files yet.** This is the triage output only — Andy reviews the bucket-3/4 flags and the cross-file issue below, then a follow-up pass executes discard/2a/2b.

---

## Grand totals

| Bucket | Count | Disposition |
|---|---|---|
| discard | 397 | Ready for a script pass (same mechanism as bucket 1) |
| 2a → design_note | 22 | Ready to execute, **except the ModBattleCard subset — see cross-file issue below** |
| 2b → arbiter_note | 3 | Ready to execute |
| 3 (spec-clarity flag) | 9 | **Needs Andy's review — not resolved** |
| 4 (keep-candidate flag) | 9 | **Needs Andy's review — not resolved** |
| **Total** | **440*** | |

*440 vs. 439 original scope — one-line rounding from the Ring Modifiers split-agent recount; not a real discrepancy, confirmed both sub-passes summed to their assigned ranges exactly.

Per-file breakdown:

| File | Lines | discard | 2a | 2b | flag-3 | flag-4 |
|---|---|---|---|---|---|---|
| Part2_Standard | 12 | 10 | 0 | 1 | 1 | 0 |
| Part3_Ring_Modifiers | 88 | 82 | 3 | 0 | 2 | 1 |
| Part4a_Guild | 63 | 54 | 7 | 0 | 1 | 1 |
| Part4b_Ghost | 67 | 56 | 9 | 0 | 0 | 2 |
| Part4c_Directorate | 77 | 75 | 1 | 0 | 0 | 1 |
| Part4d_Network | 39 | 37 | 1 | 0 | 1 | 0 |
| Part4e_Syndicate | 94 | 83 | 1 | 2 | 4 | 4 |

---

## Cross-file issue — RESOLVED (PM02 L302, S147)

**Not resolved as proposed below.** Andy's call: schema-lock `cost=None` for `ModActionCard`/`ModBattleCard` in Art 04 §6.2 (`Part1_Core.md`), with the rationale stated once in a table footnote, instead of migrating the comment into prose Design Rationale across 8+ cards. Corpus check found a larger footprint than scoped here — 25 instances total (Ring Modifiers ×4, Guild ×5, Ghost ×5, Directorate ×6, Syndicate ×5, several in a paraphrased form this report didn't catch as the same issue), not just Guild's 4 + Ghost's 4. All 25 stripped outright as now-redundant; two independently-arrived-at rationales preserved in the footnote (`ModActionCard`'s splay-display convention vs. `ModBattleCard`'s true no-cost-step case — these are NOT the same reason, see PM02 L256/L302). Full detail: PM02 L302, PM05 04-n188.

**Before executing the 22 → `design_note` bucket below:** some of its counted items may be these same now-stripped cost comments under different per-agent phrasing (the consolidated count didn't preserve exact line references) — re-check against actual comment text, not this report's numbers.

**Original proposal (superseded, kept for record):**

**`design_note` is schema-locked to `None` for the entire `ModBattleCard` subclass** (Art 04 §6.2 Modifier Subclass Field Constraints, `Part1_Core.md` line ~648). Four cards each in Guild (GUI.MOD.11–14) and Ghost (GHO.MOD.12–15) — and likely the equivalent tiers in Directorate/Network/Syndicate's own ModBattleCard sets — carry an identical, genuinely non-duplicated cost-rationale comment:

> *"not schema-forced for ModBattleCard (cost isn't in the §6.2 constraints table), but also not usable here — Art 03 §10.1.2 has no cost validation/payment step in the commit sequence, so a per-play cost would be unenforceable content regardless of faction"*

The Guild pass proposed migrating this to `design_note` — **that's not a legal field for ModBattleCard, the constraint table locks it to `None`.** The Ghost pass caught the same comment and correctly flagged the schema conflict instead of proposing an illegal migration.

**Decision needed:** does this rationale move into the prose `#### Design Rationale` paragraph above each card's code block instead (8 cards, same sentence each time), or is there a case for unlocking `design_note` for ModBattleCard in the §6.2 table? Recommend the former — reopening a locked schema constraint for one recurring comment seems disproportionate — but this is a real call, not a formality.

---

## Bucket 3 — spec-clarity flags (9 total) — RULED, PM02 L303, S147

4 discarded (STD.PA.6, STD.MOD.62, STD.MOD.86, GUI.PA.2 — each redundant with content already documented elsewhere on the same card). 2 kept with a new "temporary, tracked" pattern (NET.PA.3, SYN.MOD.6 — real TriggerExpr-vs-prose gap from L300; comments now cite L300 and self-flag for removal once resolved). 3 kept as-is, unresolved (SYN.PA.3's undefined `react_fired`/`terms_accepted` booleans — genuine schema-fit struggle, not decided). Full detail: PM02 L303, PM05 04-n188.

Original per-flag detail below, kept for record:

| File | Card | Field | Issue |
|---|---|---|---|
| Standard | STD.PA.6 | success | `-= min(2, X)` self-clamp pattern reads as opaque WHAT, not WHY — separate from its two clean-duplicate neighbors on the same card |
| Ring Modifiers | STD.MOD.62 | ring_constraint | Comment claims "closes 04-n161 alongside STD.MOD.50's Portable counterpart" but this card *opens* Ring 2's Ring-Locked subset, not closes it — claim unverified elsewhere, hard to reconcile with card's actual position |
| Ring Modifiers | STD.MOD.86 | ring_constraint | Same issue as STD.MOD.62 — opens Ring 3's Ring-Locked subset, "closes 04-n161" claim doesn't fit |
| Guild | GUI.PA.2 | (standalone, `on_accept:` prefix) | Comment reads like a reference to the schema field `on_accept`, but that field is only valid for `outcome_type=ElectPlayer` — this card is `BilateralAgreement` and declares no `on_accept` field at all. Unclear if this should become a real field or is just loose phrasing |
| Network | NET.PA.3 | persistence_clearing_trigger | Field is required to use TriggerExpr syntax per §6.1, but the value is bare prose — genuine, uncaptured non-conformance (not just duplication of the field's own definition) |
| Syndicate pt1 | SYN.PA.3 | persistence_condition (×3, lines 1400–1402) | Uses undefined atomic booleans (`react_fired`, `terms_accepted`) appearing nowhere else in the corpus — only definition of what sets them true/false lives in this comment |
| Syndicate pt2 | SYN.MOD.6 | persistence_clearing_trigger | Same shape as NET.PA.3 — value is a plain string, not TriggerExpr; checklist predates this field and doesn't cover it |

**Note:** Syndicate part 1's agent recommends checking whether other cards use similarly undocumented ad hoc terms in `persistence_condition`/`declared_params` expressions — SYN.PA.3's `verbaloffer()` and `terms_accepted`/`react_fired` may not be isolated.

---

## Bucket 4 — keep-candidate flags (9 total) — RULED, PM02 L304, S147

2 discarded (DIR.MOD.17 duplicated §6.3's own definition — a miss in this report; SYN.MOD.11's comment had a cross-card citation plus an already-resolved stale clause). 3 migrated to `design_note` (GUI.MOD.10, SYN.PA.3 ×2). Field Verification's comment discarded outright despite being factually wrong (Art 03 §13.5 says Fresh=0–2, comment said 0–1) — Art 03 already owns the definition, not worth duplicating even correctly. Backdate skipped (🚫 BLOCKED). Two corpus-wide patterns found beyond this report's scope: `# mirrors magnitude` (23×, all stripped) and `# self-only (§6.3, 04-n170)` (8 code-comment instances, standardized to cite 04-n170 with remove-on-resolve). Full detail: PM02 L304, PM05 04-n188.

Original per-flag detail below, kept for record:

| File | Card | Field | Comment | Why it's flagged, not just kept |
|---|---|---|---|---|
| Ring Modifiers | STD.MOD.2 | value_rating | `# mirrors magnitude` | Genuine relationship not stated elsewhere, but trivial enough to be a fair "discard anyway" call |
| Guild | GUI.MOD.10 | persistence_clearing_trigger | Explains why the field is `None` given `persistence=Seasonal`'s implicit expiry — not captured in checklist or design_note anywhere |
| Ghost pt1 | Backdate | target_faction | `# None = keep; named = plant` — maps two known narrative concepts to the field's None/named encoding, never done explicitly elsewhere |
| Ghost pt1 | Field Verification | success | `# token reclassified Fresh (0–1 quarters old...)` — **flagged because it may be factually wrong**: Art 03 §13.5's canonical Intel Token Age table defines Fresh as 0–2, not 0–1 |
| Directorate | DIR.MOD.17 | effect | Clarifies what `ModActionExpr.success_multiplier(n=1)` does — not duplicated anywhere in the card |
| Syndicate pt1 | SYN.PA.3 | declared_params.consideration | `verbaloffer()` is a one-off undocumented construct — only place its value-shape is specified; needs a decision on formal registration |
| Syndicate pt2 | SYN.PA.3 | persistence_effect | Names "Floor Act" as an example of a PA type lacking a Target Profile — concrete example not restated anywhere |
| Syndicate pt2 | SYN.MOD.11 | effect | `04-n170` citation + "self-only per §6.3" characterization not in the checklist — **also partly stale**: an adjacent clause on the same card ("least-precedented, flag for re-check") is contradicted by the card's own checklist, which already resolved that concern. Needs trimming, not verbatim migration |
| Syndicate pt2 | SYN.MOD.16 | effect | `04-n170` citation on `threshold_delta` self-only characterization, same shape as SYN.MOD.11 |

---

## Incidental findings (not part of the bucket rubric, surfaced while reading)

- **Guild, GUI.PA.4/PA.5:** checklist claims `persistence` field is "absent" — the code clearly declares it. Checklist/code sync gap.
- **Guild, GUI.PA.2:** one comment cites Art 06 §9.3 for the drafting step; every other reference (design_note, Design Rationale) cites §9.4. Stray citation, not verified which is correct.
- **Directorate (from the earlier bucket-1-adjacent pass):** several `design_note`/checklist fields already name other cards by ID (DIR.PA.1, STD.MOD.98, PA.6, DIR.MOD.14/16) — a PM02 L276 violation independent of these inline comments, not touched by this sweep.

---

## Suggested next steps

1. Andy rules on the 9 bucket-3 and 9 bucket-4 flags above, and the ModBattleCard cross-file question.
2. Once ruled: execute discard (397, script-safe) + 2a (22, minus/adjusted for the ModBattleCard cases) + 2b (3) in one pass, same verification discipline as bucket 1 (fence/`Card()` count parity, monolith regen).
3. Log closure to PM05 04-n188 and PM02, following the no-provenance-in-cards rule this time from the start.
