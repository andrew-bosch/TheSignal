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

**First action:** Any scored action immediately exits Ambiguous — positive into Observed (+2), negative into Uncertain (−2).

**Game effects:**
- Private (ARBITER's tableau only)
- Factions cannot read their own position; cannot infer from initiative order (D10 step decouples visible order from hidden rankings)
- Drives ARBITER's initiative order each Quarter
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

**Creation:** ARBITER creates a token when a faction successfully gathers intelligence. Each token records: (1) the faction it concerns, (2) the quarter gathered. Players calculate age themselves.

**Age tiers:**
| Tier | Age | Notes |
|------|-----|-------|
| Fresh | 0–1 Quarters | Full effectiveness |
| Stale | 2–3 Quarters | Reduced effectiveness (−25 modifier in Battlefield Strength) |
| Expired | 4+ Quarters | No mechanical use |

**Use:** Tokens apply only to actions involving the named faction. Standard factions hold guideline max of 2; Ghost holds up to 4. Own-faction tokens don't count against the guideline — defensive use only (block opponents from acquiring them).

**Privacy and disclosure:** Private by default. Holder may disclose publicly, privately to one player, verbally, or via trade. Verbal claims about undisclosed tokens cannot be verified without a specific game action.

**Discard:** Any token may be discarded at any time, immediately, permanently — cannot be retrieved or examined afterward. ARBITER observes discards; may be Portrait-relevant.

**IntelToken field structure:** A token records exactly two things: (1) the faction it concerns, (2) the quarter it was gathered. No other fields exist. `content`, `content=false`, `value`, `verified`, and similar are NOT valid IntelToken states or fields — there is no such thing as a false IntelToken or a content-flagged token.

**Privacy and card targeting — 00a §10.1:** IntelTokens in a faction's private pool are privately held information. No card may compel disclosure or removal of privately held tokens — this is categorically prohibited by 00a §10.1. ARBITER reaching into a faction's private domain to retrieve or remove a token is also prohibited (10.1b covers only ARBITER-initiated disclosure of ARBITER-domain content; it does not authorize card-directed retrieval from faction private pools).

**Only valid cross-faction IntelToken target:** An IntelToken submitted by a faction on a PA in the **Faction Resolution Grid** (§9.2 Public Declaration). Once submitted, the token is in ARBITER's procedural domain — no longer privately held — and is a valid target for card effects at Beat 3 (before Beat 4 processes the PA). This is the only location where another faction's IntelToken can be targeted by a card. Tokens held in private pools cannot be targeted by any card effect.

**Two resolution grid domains (never conflate):**
- **Faction Resolution Grid** — where PAs are submitted (§9.2); factions place their PA cards face-up here with resources and IntelTokens; Target Profile placed face-down. IntelTokens here are ARBITER-domain at Beat 3.
- **ARBITER covert grid** — where covert dispatch cases are assembled (§9.1); entirely ARBITER-domain; never a valid card effect target.
