# CA/PA Design Review — Working Notes

Working doc for PM05 **09-16 step 2** (design review pass), CA/PA phase. Delete once this content is migrated into card entries / PM02 / PM05 (per Whiteboard convention — scratch, not canonical).

**Plan (Andy, S140):** separate session for CA review, separate session for PA review — don't try to do both (or all of CA) in one sitting. This file is what the next session reads to pick up where S140 left off.

---

## 1. Why this review is happening now, and in this order

`09-16` step 2 (design review pass) already closed for all three Modifier subclasses (ModAction S139, ModBattle S140, ModReact S138) — see PM02 L267–L269. CA/PA is the remaining step-2 scope: "the non-modifier action-space."

**Sequencing decision (PM02 L273, S140):** CA/PA review runs *before* finishing the remaining item-#3 whole-set schema decisions (04-n178 cost/value_rating model, `schema_cleanup_log.md` #2 stack behavior, #5 firing-window overlap). Reasoning: the modifier-card review pass kept surfacing schema-level findings as it went (04-n177 scaffolding gaps, the outcome_type/acquisition/generating_card corpus-wide gap, the Overture taxonomy correction) — deciding the whole-set schema items before CA/PA review has had its say would be premature. Do CA/PA first; let it feed the schema decisions, not the other way around.

---

## 2. The standard: re-derive, don't trust

This is the load-bearing instruction for this whole pass. Memory: `feedback_design_review_verification.md` (reinforced hard at S140 — read it before starting).

**Do not treat any of the following as ground truth without checking it directly:**
- A checklist row marked ✓
- `design_pass=1` / `structure_pass=1` in `card_status`
- A "Signed off ✓ S(n)" in the Status table
- A cross-card comparison in the card's own Design Rationale ("unlike GD-01," "matches Redline's pattern," "no standard card duplicates it") — **open the other card and check.** This caught a factually-backwards claim on STD.MOD.1 Overture (S140).
- A taxonomy assignment as stated — **verify against `Whiteboard/ref_taxonomy.md` directly**, not the card's own assertion.
- Freshly-written content from earlier in the same session. Andy explicitly asked "do the other 7 need the same scrutiny" after 7 fossil cards were authored fresh in S140 — they did; audit found a real gap (see §4 below).

**What re-deriving does NOT mean:** don't re-prose every row of every card from scratch. Verify each row against source; only rewrite the ones that fail. 114 cards' worth of unnecessary rewriting is not the goal — 114 cards' worth of *checked* claims is.

---

## 3. Concrete lookfor list (proven to find real defects this session)

Check these, in this order, on every card:

1. **Status-row internal consistency.** Does "Signed off ✓ S(n)" coexist with a blank Design Pass or open (⚠) checklist rows? That's a fast contradiction signal — but not automatically a bug: if the sign-off predates a tracking item like 04-n70 (data schema sweep) or 04-n79 (card narrative sweep) even existing as a concept, the ⚠ rows may just be later-added flags, not evidence the sign-off itself was premature. Note which case it is; don't assume either way.
2. **Checklist format completeness.** Count the rows present against the canonical 17-row Art 04 §5 list (Action fit → Resource cost positioning — see Part1_Core.md ~line 263). CA/PA do **not** get the 5-row ModReactCard addendum (Trigger frequency/Firing window/Automatic vs d100/Stack behavior/Ring constraint) — that's ModReactCard-only. An old card (S60s-vintage, like the Standard CA set) may be missing rows entirely, the way STD.MOD.1 Overture was missing 10 of 22 before this session caught it.
3. **Cross-card precedent claims** — open the cited card, confirm the comparison holds.
4. **Taxonomy** — check Layer/Function/Subject against `ref_taxonomy.md` §5.1 (verb definitions) and §5.2 (subject vocabulary) directly. Watch especially for verb ambiguity (e.g. Remove vs. Corrupt — "component exits play" vs. "a recorded value is altered" are genuinely different things; don't default to whichever verb avoids taxonomy overlap with a sibling card, that reasoning doesn't actually settle anything per 04-n158's own logic).
5. **✓ marks vs. actual field state** — Voice fit ✓ with `perspectives={}`/empty is wrong (should be ⚠); Data schema validation ✓ with required fields simply absent from the code block is wrong.

---

## 4. Schema scope for CA/PA specifically — don't chase the modifier-card gaps here

Confirmed by reading Part1_Core.md §6.1 directly this session:

- `CovertOperation` and `PublicAct` are **`CardType` enum values on the base `Card` class**, not separate subclasses (unlike `ModActionCard`/`ModBattleCard`/`ModReactCard`, which each have their own `class X(Card):` block with extra fields).
- **`acquisition`, `generating_card`, `value_rating`, `ring_constraint`, `ring_origin` are Modifier-subclass-only fields** (defined only inside the `ModActionCard`/`ModBattleCard`/`ModReactCard` class blocks, ~Part1_Core.md lines 513–544). They are **correctly absent** on CA/PA cards — do not add them. (This is the opposite instinct from the modifier-card fossil work, where those fields WERE required — don't carry that muscle memory over blindly.)
- **`ps_framing` and `boost`** are base-`Card`-class fields (§6.1) and are the already-tracked 04-n177 gap ("easy to miss required fields... omitting them is a schema error") — expect them to be commonly absent on older CA/PA cards too. Confirmed absent on STD.CA.1. Not a new finding when you hit it again; just note and scaffold (`= None`) same as the modifier-card fix.
- **`outcome_type`** is a base-`Card`-class field, confirmed present and correctly `None` on the Standard CA cards checked so far (STD.CA.1/13/14/15). Per §6.2's data dictionary: `outcome_type | Metadata | OutcomeType | Public act resolution process type; None for covert operations`. **This means every PublicAct card should carry a real, non-None `OutcomeType` value** — this is the single highest-yield schema check to run once the PA batch starts. **Look up the `OutcomeType` enum definition (Part1_Core.md) before starting the PA session** and verify each PA sets it correctly; this was flagged by the advisor as the most likely place an old card silently gets it wrong, and hasn't been checked yet.
- `is_unique` / `deck_limit` are Pool-level metadata scoped to Operative/Apex cards per their own field definitions — their absence on ordinary CA/PA cards is expected, not a gap.

---

## 5. STD.CA.1 (Build Structure) — pattern-setter review, NOT YET FIXED

Read in full (`V1/04___Card_System___Part2_Standard.md` lines 29–116). This is the oldest CA card in the system (Guild-affinity territorial-foundation card, signed off S63) — picked as the pattern-setter specifically because "oldest/most legacy" is where stale format is most likely to surface (same logic that made Overture worth checking).

**Confirmed real defect — fix pending:**
- `cost = resource.faction(acting) * 1 + resource.district(native) * 1` — the first term has **no resource-type attribute**. Design Rationale states "dual cost (1 faction native + 1 district native)"; every other cost expression in the corpus specifies a type (compare STD.CA.13: `resource.faction(acting).native * 2`). Should almost certainly be `resource.faction(acting).native * 1`. Not yet written to file — do this first when CA session starts.

**Flagged, needs a decision, not asserted as broken:**
- Status row: `Design Pass` blank, `Issues Resolved ✓`, `Signed off ✓ S63` — while 2 checklist rows (`Data schema validation`, `Card narrative`) are still ⚠. Per §3.1 above: check whether S63 predates 04-n70/04-n79 as tracked concepts before concluding this is a real contradiction. If it predates them, this is expected and just needs the Design Pass box actually checked off now that the review is happening; if it doesn't predate them, it's a genuine process gap worth logging.

**Confirmed correct on direct check — no action needed:**
- Territory/Add/StructureBlock taxonomy verifies directly against `ref_taxonomy.md` §5.2 ("Structure Block | Territory").
- Missing `ps_framing`/`boost` — expected, per §4 above (04-n177 scope), not new.

**Not yet checked:** the Guild affinity clause's `cost.resource.district(native) = 0` uses flat assignment (`=`) rather than the delta style (`-=`/`+=`) seen elsewhere (e.g. STD.CA.13's `threshold += 10`). May be stylistic, may be worth normalizing — low priority, noted for completeness, not a blocker.

**Andy's outstanding question before replicating the pattern across the rest of the Standard CA set:** confirm (a) fix the cost typo, note-not-resolve the sign-off question, and (b) confirm CA/PA checklist format is the plain 17-row Art 04 §5 list with no addendum (per §3.2 above — this is already confirmed by reading §5 directly, just needs Andy's nod before the fix pattern replicates across ~15 more Standard CA cards).

---

## 6. Scope inventory (from `card_status`, pulled S140)

```sql
SELECT
  CASE WHEN card_id LIKE '%.CA.%' THEN 'CA' WHEN card_id LIKE '%.PA.%' THEN 'PA' ELSE 'other' END AS card_kind,
  CASE WHEN card_id LIKE 'STD.%' THEN 'Standard' WHEN card_id LIKE 'DIR.%' THEN 'Directorate' WHEN card_id LIKE 'GHO.%' THEN 'Ghost' WHEN card_id LIKE 'GUI.%' THEN 'Guild' WHEN card_id LIKE 'NET.%' THEN 'Network' WHEN card_id LIKE 'SYN.%' THEN 'Syndicate' ELSE 'other' END AS faction,
  COUNT(*) AS total, SUM(design_pass=1) AS design_passed
FROM card_status WHERE card_id LIKE '%.CA.%' OR card_id LIKE '%.PA.%'
GROUP BY card_kind, faction ORDER BY faction, card_kind;
```

| Faction | CA total | PA total |
|---|---|---|
| Standard | 16 | 8 |
| Directorate | 8 | 11 |
| Ghost | 15 | 5 |
| Guild | 10 | 10 |
| Network | 8 | 6 |
| Syndicate | 12 | 5 |
| **Total** | **69** | **45** |

**114 CA/PA cards total.** A handful already show `design_pass=1` in the DB (Directorate PA ×2, Guild CA ×2, Guild PA ×2) — per §2 above, these get checked with exactly the same rigor as everything else, not skipped.

**Order confirmed (Andy, S140):** Standard/Ring first, then presumably Directorate → Ghost → Guild → Network → Syndicate (matching the modifier-card review convention), but re-confirm faction order with Andy at the start of the CA session — it wasn't explicitly locked beyond "Standard first."

**Standard CA set (16 cards):** STD.CA.1–12 have proper `### STD.CA.n —` headers in `Part2_Standard.md`. STD.CA.13–16 (Disinformation Campaign, Disprove, Intel Extraction, Modifier Raid) exist but use `### STANDARD — [NAME]` headers instead (no card ID in the header) and old-style Python variable names (`C_DisinformationCampaign` instead of matching the card ID) — worth normalizing header format while in there, low-stakes fix-in-place candidate.

---

## 7. Relevant history / where to look for more context

- PM02 **L267–L273** — full modifier-subclass review history + the Overture re-verification + the 7-fossil re-audit + this sequencing decision.
- PM05 **04-n174** (fossil re-authoring, closed S140), **04-n177** (scaffolding gap, scope expanded S140), **04-n158** (SYN.MOD.1 redesign, closed S140), **09-16** (master roadmap item).
- Memory `feedback_design_review_verification.md` — the standard itself, read before starting.
- Memory `feedback_ring_voice_parity.md` — if Standard/Ring CA/PA content touches Ring-specific voice, same "3 distinct cultures" standard applies as it did for Ring modifier cards.
