# Reference — Tracking Systems: Portrait, Public Standing, Intel (Art 02 §12)
*Load when: Portrait or PS design, scoring questions, Intel Token mechanics, initiative order.*

---

## Portrait System

**Narrative meaning:** Not a score — a record. The Chorus observes every action and extrapolates trajectory. It does not forget, does not revise, is indifferent to performance or appearance. Portrait captures what a faction actually *is*, not what it claims.

**Scale:** −20 to +20. All factions start at 0 (upper boundary of Ambiguous). Bands are bell-curve distributed — center band is narrow by design; the Chorus forms a trajectory quickly.

| State | Range | Chorus Stance |
|-------|-------|---------------|
| Resonant | +18 to +20 | This faction has become something the Chorus recognizes |
| Aligned | +13 to +17 | Behavior and doctrine have converged |
| Coherent | +8 to +12 | A consistent pattern is emerging |
| Legible | +4 to +7 | The Chorus can begin to read this faction |
| Observed | +2 to +3 | Initial signals noted. Trajectory forming |
| Ambiguous | −1 to 0 | No determination. Observation continues |
| Uncertain | −2 to −3 | Early contradictions detected |
| Dissonant | −4 to −7 | Stated doctrine and observed behavior diverge |
| Fractured | −8 to −12 | The pattern of contradiction is consistent |
| Collapsed | −13 to −17 | This faction no longer produces readable signal |
| Void | −18 to −20 | Silence. The Chorus has nothing to interpret here |

*Band boundary values are design targets — pending Art 07 Portrait design sign-off (PM05 07-13). Treat as provisional.*

**Starting position and Ambiguous:** All factions start at 0, the upper boundary of Ambiguous. Any Portrait movement — positive or negative — exits Ambiguous into the next band (Observed at +2 or Uncertain at −2). Ambiguous is a temporary origin, not a stable state.

**What moves Portrait:** Three sources, all applied by ARBITER as sole physical mover:
1. **Card Portrait fields** — the card's printed Portrait instruction; ARBITER evaluates and applies at resolution.
2. **ARBITER discretion** — ARBITER may move Portrait for any observed behavior not covered by card fields: Debrief negotiations, table conduct, unprompted choices.
3. **Roleplay observations** — ARBITER observes and may act on: faction player conversations, in-doctrine or out-of-doctrine roleplay, stated faction reasoning. Staying in character, arguing doctrine, or contradicting it are all Portrait-relevant. No faction knows their Portrait state; no faction sees ARBITER apply it.

**Game effects:**
- Private (ARBITER's tableau only)
- Factions cannot read their own position; cannot infer from initiative order (D10 step decouples visible order from hidden rankings)
- Initiative: ARBITER reads Portrait scores to rank factions 1–5, then rolls a d10 to select an ordering method from a table of permutations and social triggers (e.g., rank order, reverse rank, "middle-out down," seating order L→R from ARBITER, narrative triggers). Final initiative order is deliberately hard to reverse-engineer into Portrait rank. Q1 exception: clockwise from ARBITER's left regardless of d10. *(Full d10 table pending Art 07 documentation — PM05 03-11)*
- Determines tone of each faction's Chronicle entry
- Contributes to final scoring (Art 10a)
- ARBITER may adjust Portrait for any behavior including Debrief negotiations and table conduct

**Strategic note:** Portrait is invisible to opponents and permanently recorded. Cannot be faked, gamed, or socially managed.

---

## Public Standing System

**Narrative meaning:** What New Meridian thinks. Volatile, reactive, forgetful — driven by opinion, art, graffiti, collective impression. Public memory is short; standing drifts toward neutral when nothing dramatic is happening.

**Scale:** 0–20. All factions start at 10 (Neutral). Fully public — visible to all players.

| State | Range | Threshold Modifier |
|-------|-------|--------------------|
| Celebrated | 18–20 | +20 (easier) |
| Respected | 14–17 | +10 |
| Neutral | 7–13 | 0 |
| Suspect | 3–6 | −10 |
| Discredited | 0–2 | −20 |

**Threshold mechanics:** Modifier shifts the difficulty target before the roll. Example: Challenging base = 01–25. Celebrated (+20) makes it 01–45; Discredited (−20) makes it 01–05. Applies to all d100 rolls the faction makes — covert operations, public acts, Incursion, everything. Not location-specific.

**Natural drift:** Applied at Quarter end after all other changes:
- Above 13 → −1 per Quarter
- Below 7 → +1 per Quarter
- 7–13 → no drift

**Beyond roll thresholds:** PS also affects weight in the session's final vote (Art 10a).

---

## Intel Token System

**States:** Four states across the token lifecycle: Blank (unfilled — in ARBITER supply before use) → Fresh → Stale → Expired.

**Creation:** ARBITER takes a Blank token from supply and fills in (1) the faction it concerns and (2) the quarter gathered when a faction successfully gathers intelligence. Players calculate age themselves.

**Age tiers:**
| Tier | Age | Notes |
|------|-----|-------|
| Fresh | 0–1 Quarters | Full effectiveness |
| Stale | 2–3 Quarters | Reduced effectiveness (−25 modifier in Battlefield Strength) |
| Expired | 4+ Quarters | No mechanical use; partial payment only |

**Use:** Tokens apply only to actions involving the named faction. Standard factions hold guideline max of 2; Ghost holds up to 4 *(balance/playtest values — not mechanically enforced; ARBITER adjudicates called violations per Art 07)*. Own-faction tokens don't count against the guideline — defensive use only (block opponents from acquiring them).

**Privacy and disclosure:** Private by default. Holder may disclose publicly, privately to one player, verbally, or via trade. Verbal claims about undisclosed tokens cannot be verified without a Reveal effect (00a §10.1a).

**Discard:** Any token may be discarded at any time, immediately, permanently — cannot be retrieved or examined afterward. Tokens spent as cost payment or modifiers via action resolution are also consumed on use (not returned). ARBITER observes discards; may be Portrait-relevant.

**IntelToken field structure:** A token records exactly two things: (1) the faction it concerns, (2) the quarter it was gathered. No other fields exist. `content`, `content=false`, `value`, `verified`, and similar are NOT valid IntelToken states or fields — there is no such thing as a false IntelToken or a content-flagged token.

**Privacy and card targeting — 00a §10.1:** Applies to ALL private components (hand cards, modifier cards, directives, IntelTokens, etc.) — not IntelTokens only. No card may compel disclosure or removal of any privately held component. ARBITER reaching into a faction's private domain is also prohibited (10.1b covers only ARBITER-initiated disclosure of ARBITER-domain content; it does not authorize card-directed retrieval from faction private pools).

**IntelToken targeting — design observation:** An IntelToken submitted by a faction on a PA in the Faction Resolution Grid (DB:88) at §9.2 is no longer privately held — it is in ARBITER's procedural domain and is a valid card effect target at Beat 3 (before Beat 4 processes the PA). This is the only location where an opposing faction's IntelToken can be reached. This is a structural consequence of the §9.2 submission model, not a named governing rule in Art 00a.

**Two resolution grid domains (never conflate):**
- **Faction Resolution Grid** — where PAs are submitted (§9.2); factions place their PA cards face-up here with resources and IntelTokens; Target Profile placed face-down. IntelTokens here are ARBITER-domain at Beat 3.
- **ARBITER covert grid** — where covert dispatch cases are assembled (§9.1); entirely ARBITER-domain; never a valid card effect target.
