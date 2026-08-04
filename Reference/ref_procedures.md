# Reference — Game Procedures (Art 03)
*Load when: quarter loop, resolution grids, procedure gaps, React card design, Debrief rules, Battlefield Strength, dice mechanics, PA resolution.*

---

## Quarter Loop

The repeatable quarterly sequence. Six sections in order — ARBITER announces each.

```
§7 UPKEEP
  World updates. Resources collected. Tokens distributed. Initiative set.

§8 PLACEMENT
  Deployment Markers placed. Entry requirements enforced.

§9 MONTHLY ACTIVITIES  ×3
  §9.0  Start of Month — PA obligations checked.
  §9.1  Covert Dispatch — cases assembled, sealed, transmitted to ARBITER.
  §9.2  Public Declaration — Public Acts declared in initiative order; placed face-up on Overview.
  §9.3  Countermeasures — CM cards submitted; target queued covert ops or placed Public Acts.
  §9.4  Resolution:
    §9.4.0  Beat 0: The Cases Open
    §9.4.1  Beat 1: Read Board State
    §9.4.2  Beats 2–3: Covert Operations Resolve
    §9.4.3  Beat 4: Public Acts Resolve
    §9.4.4  Close Month
  Repeat for Months 2 and 3. Month 3: proceed to §10 instead of repeating.

§10 RESOLVE DISTRICT TENSION
  Contested districts resolve. d10 roll-off per district. Tension Markers cleared.

§11 QUARTERLY DEBRIEF
  Table reflects. ARBITER delivers Summary, Observation. Ready-to-close mechanic.

§12 QUARTER CLOSE
  Seasonal cleanup. Findings decay. Debrief reward. NS-xx returned. Trackers advanced.
```

Sections do not overlap. ARBITER announces the start of each.

---

## Resolution Grids

Two distinct grids operate during Monthly Activities. Never conflate them.

### ARBITER Resolution Grid (covert domain)

Built fresh at Beat 0; cleared at end of Beat 3. Entirely ARBITER-private — factions never see contents; not a valid card-effect target.

**Structure:** One lane per faction (6 lanes). Each lane has rows for Beat 1 (CM cards — DB:52), Beat 2 (op + target pair), Beat 3 (op + target pair). Up to 4 op-target pairs per lane (one per Dispatch Token).

**How it fills — Beat 0:** ARBITER opens each case; verifies Dispatch Token present. Each operation card placed in the Beat 2 or Beat 3 row of its faction lane per the card's `beat` field. Target Profile (DB:48) stacked under the operation card. CM cards (DB:52) from §9.3 placed in the Beat 1 row of the targeted faction's lane.

**Beat 1:** CM cards processed lane by lane. Each CM applies to all operations in the grid targeting its keyed faction.
- **CM-A:** Flip each targeted op face-down; discard Modifier Cards from those stacks. CM card discarded.
- **CM-B:** Place a CM-B Modifier Token (M-11, −15) on each targeted op. CM card discarded.
- CM cards are gone by end of Beat 1 — they are not in the Beat 2 row and cannot be targeted by Beat 2 cards.

**Beats 2–3:** Row-first processing — all Beat 2 pairs resolve before any Beat 3 pair begins. Within each row: round-robin by case receipt order (submission speed sets initiative, not faction standing order).

**Cards exit:** Operation cards discard or persist per duration type. Target Profiles (DB:48) returned to faction. Grid cleared at end of Beat 3.

---

### Faction Resolution Grid (PA domain)

Built at §9.2; processed at Beat 4. Visible to all players.

**How it fills — §9.2:** Declaring faction places PA card face-up with 1 Dispatch Token and Native Resource tokens (DB:8, DB:12). Intel Tokens (DB:9) submitted as cost payment or information modifiers are also placed face-down on the card at this time. Target Profile (DB:48) placed face-down on the card. Once placed: valid target for countermeasures and other Public Acts; cannot be withdrawn.

**Beat 4:** PAs resolve in initiative order:
1. Submit payment — Native Resources (DB:8, DB:12) and/or Intel Tokens (DB:9) transferred to Reservoir; Dispatch Token returned. Partial payment: −50 modifier placed. Zero payment: card flipped face-down, skips to cleanup (no fail outcome fires).
2. Apex Check — Target Profile (DB:48) flipped face-up; ARBITER reads card against profile.
3. Board state validation — conditions required at §9.2 must still hold; if not, ARBITER announces invalidation and returns card.
4. Apply modifier stack, declare threshold, roll publicly, apply outcome.

**Cards exit by duration:**
| Duration | Exits when |
|----------|-----------|
| Immediate | Removed right after Beat 4 resolution |
| Seasonal | Cleared at §12 Quarter Close |
| Permanent | Cleared only by specific trigger or faction action (00a §8.3a) |

Seasonal and Permanent cards remaining on the grid are collectively **Standing effects** — visible to all players; valid targets for countermeasures and Public Acts for as long as they remain.

---

### Primitive Actions — verb legality

To check whether a verb is legal for a given component, query the database. `applicable_verbs` in each Art 02 component entry is the source of truth. Do not read Art 02 for this; run the query.

---

## Dice Roll Procedure (§13)

**d100:** Two d10 in two distinct colors — one designated tens, one units. Both showing 0 = 100. Color assignment established at session start, held constant.

**Success condition:** Roll must land equal to or below the modified threshold. Threshold = probability of success as a percentage.

**Base difficulty:**
| Difficulty | Threshold |
|------------|-----------|
| Easy | 75 |
| Average | 50 |
| Challenging | 25 |

**Critical results (always apply regardless of threshold):**
- 01–05: Critical Success — `successcrit` fires additively with `success`
- 96–00: Critical Fail — `failcrit` fires additively with `fail`

If threshold ≤ 0: only 01–05 succeeds. If threshold ≥ 100: only 96–00 fails.

**Modifier stack (M-01 through M-13, all cumulative):**
| Modifier | Effect |
|----------|--------|
| Public Standing (Celebrated/Respected/Neutral/Suspect/Discredited) | +20/+10/0/−10/−20 |
| Partial payment | −50 |
| Modifier Card | variable |
| Protect token | variable |
| Type B Countermeasure | −15 |
| Ring adjacency penalty (no Core presence for Mid target) | −25 |
| Stale Intel Token | −25 |
| Situation Report | variable |

Worst-case stack: partial payment + ring penalty + Discredited + Type B = −110, leaving only a crit viable.

---

## Monthly Phase Sequence

Each Month: **§9.1 Covert Dispatch** → **§9.2 Public Declaration** → **§9.3 Countermeasures** → **§9.4 Resolution (Beats 0–4)**. These are the canonical Art 03 names — never "Dispatch A/B/C" or "Phase A/B/C."

**§9.1 Covert Dispatch:** Factions assemble Dispatch Cases (operation card + Dispatch Token + cost resources), seal, and transmit to ARBITER. Cases are ARBITER-domain from this point. Factions name their target faction (and any declared parameters) on the Target Profile inside the case.

**§9.2 Public Declaration:** Factions declare PAs in initiative order — card placed face-up in Faction Resolution Grid with Dispatch Token and resource tokens. Target Profile placed **face-down** on the card. IntelTokens may be submitted here as cost payment or as modifiers. Once placed, card is a valid countermeasure target and cannot be withdrawn.

**§9.3 Countermeasures:** Factions deploy or pass in initiative order. CM cards may target queued covert ops or placed PAs.

**Two resolution grid domains — never conflate:**
- **Faction Resolution Grid** — PA domain; created at §9.2; visible to all players (cards face-up, Target Profiles face-down). IntelTokens submitted here are in ARBITER's procedural domain at Beat 3, NOT in the faction's private pool.
- **ARBITER covert grid** — covert op domain; assembled at §9.1 Beat 0; entirely ARBITER-private. Never a valid card-effect target.

---

## Public Act Declaration (§9.2)

1. Declarations in initiative order. Factions may pass verbally.
2. To declare: announce the Public Act; place card face-up in unresolved PA zone of Faction Resolution Grid with 1 Dispatch Token and resource tokens. Place Target Profile **face-down** on the card. Resource tokens remain with the card (not committed until Beat 4).
3. Modifier Cards placed face-up alongside in Faction Resolution Grid.
4. Once placed: valid target for Countermeasures and other Public Acts. Cannot be withdrawn or modified.
5. Resolve in initiative order at Beat 4.

---

## Public Act Resolution — Beat 4 Key Steps

1. **Submit Payment:** Initiative order — resource tokens transferred to Reservoir; Dispatch Token returned. Full payment acknowledged; partial payment gets −50 threshold marker; zero payment = invalid (card flipped face-down — skips directly to cleanup; no fail outcome fires; Acting Faction takes Public Standing −1, "failed commitment" — Art 03 §9.4.3.1.0.3, added S146 PM02 L292).
2. **Apex Check (§9.4.3.1.1):** Acting Faction Player flips Target Profile face-up; reads Public Act Card and Target Profile. Face-down PA cards auto-fail (do not flip — they remain face-down and go directly to fail outcome).
3. **Validate board state conditions:** If conditions required at §9.2 Public Declaration no longer met (altered by Beat 3 outcomes) — ARBITER announces invalidation, card returned.
4–8. Acting faction reads base difficulty, applies all modifiers, declares threshold aloud, rolls publicly, compares to threshold.
9. **Apply outcome:** Acting faction makes all board changes.
10. **Clean up:** Modifier Cards discarded. Card remains per its duration type — Immediate cards only are removed immediately.

---

## React Card Rules (§18)

React cards fire in response to **publicly visible board state changes only** — cannot fire on ARBITER-internal changes such as the Resolution Grid.

**Timing window (§18.0.1):** Opens when a publicly visible board state change occurs. Closes at the next board state change or procedure advance — whichever comes first. Not instantaneous; a brief window is valid.

**Trigger and interrupt:**
- When trigger condition is met, holding faction announces "React," presents card, states trigger condition. ARBITER confirms validity and **pauses the quarter procedure**.
- Only one React resolves at a time. A second React may only fire in response to the new board state produced after the first resolves.

**Tiebreaker:** First to announce pauses play. ARBITER decides tiebreakers.

**Resume:** Once React resolves, original procedure resumes from the point it was paused.

**ModReactCard:** Default behavior is permanently removed from the game once resolved (§18.2.2, added S149) — not returned to a discard pile, not held for reuse — unless the card's own text states otherwise. Not tied to `cost=None`; that was an incomplete prior reading. FRG standing condition variant: some React cards (e.g., DIR.MOD.6 State of Emergency, SYN.MOD.6 Bounty Contract) place themselves face-up on the acting faction's FRG as a Quarter-long standing condition after firing — no custom marker needed. Schema model for this variant pending 04-n145. Confirmed trigger vocabulary: design_reference_card_system.md. Accord trigger semantics: `accord.corrupted` = textual alteration via Covert Op (Accord stays active); `accord.removed` = breach or expiry (Accord card leaves board) — S128 ruling.

---

## Debrief Procedure (§11)

No initiative order, no phase timer. ARBITER announces: "The Table is in Debrief."

**Free actions (§11.0 — any order, any terms):**
- Trade resources between any two factions
- Trade Intel Tokens between any two factions (examination permitted)
- Accept/decline/counter-propose Accord terms

**Debrief Action cards (Art 04 §12a):** Any faction holding a Debrief Action card resolves in initiative order — announce → execute → ARBITER confirms → card removed from game or returned to supply per card text. Runs before Chorus Question Window. Fires as a scheduled procedural checkpoint, not a `TriggerExpr` event (PM05 04-n162).

**Chorus Question window (§11.2):** If Chorus Activity track has reached Question threshold AND Chorus Node is not Contested — any faction with at least Present at the Node may propose a question. Simple majority passes. ARBITER answers in The Observation register. If Node is Contested, window does not open.

**Ready to Close (§11.3):** Faction Players flip Status Marker to Ready when done. When 3 of 5 show Ready: ARBITER starts 60-second courtesy timer. Debrief closes when timer expires or all 5 show Ready → proceed to §11.4 ARBITER Debrief.

**ARBITER Debrief (§11.4 — in order):**
1. **Summary (§11.4.0)** — factual account of Quarter outcomes (The Record register). Q4 only: Annual Report follows Summary.
2. **Observation (§11.4.1)** — one observation (The Observation register). Form A: names a Portrait State without identifying faction. Form B: names the faction with a vague adjective. Never combined. Debrief closes; proceed to §12 Quarter Close.

**Debrief Reward:** §12.2 (Quarter Close, not part of Debrief proper).

---

## Battlefield Strength (§10.1 — Resolve Contested District) — S132 redesign

**Triggers:** After Month 3 §9.4.4 Close Month, ARBITER scans for Tension Markers (§10.0). Resolves Ring 3 inward to Ring 0.

**§10.1.1 Identify Contesting Factions:** all factions at Dominant influence in the district (more than 2 may contest).

**§10.1.2 Calculate and Declare Totals** — face-down commit, then simultaneous reveal:
- **1.2.1 Count:** each contesting faction counts Presence Tokens + Structure Blocks in the contested district and each adjacent district (Deployment Markers = 1 Presence Token).
- **1.2.2 Commit** (face-down, simultaneous, before anything is revealed): any faction — contesting or not — may play Battlefield Modifier Cards face-down in front of a named contesting faction (target stated verbally at commit, content hidden until reveal); and/or commit fresh Intel Tokens face-down to a central location (target *and* content both hidden until reveal, unlike mod cards).
- **1.2.3 Reveal & Validate:** each contesting faction flips whatever mod cards sit in front of them — **Boost (+n)** adds to the named faction's total, **Hinder (−n)** subtracts (a faction's own Boost cards default to benefiting themselves unless placed in front of someone else). ARBITER flips the central Intel Token pile, validates age (0–2, Fresh) and named target (must be a contesting faction per §10.1.1); valid tokens are placed face-up in front of their target — always **Hinder −2**, regardless of who committed it; invalid tokens (stale, or naming a non-contestant) are set aside, no effect. Everything stays on the table, revealed, until cleanup (§10.1.4.0/§10.1.4.1 — not here).
- **1.2.4 Announce:** each contesting faction sums their 1.2.1 count plus everything Boost/Hinder sitting in front of them, announces the total aloud.

**§10.1.3 Roll d10:** each contesting faction rolls, announces the sum of their 1.2.4 total + roll.

**§10.1.4 Resolve Outcome:** ARBITER compares totals; highest wins; tied → §10.1.4.1.
- **Winner (§10.1.4.0):** ARBITER announces holder. Winner removes 1 Presence Token from any contesting faction in the district; chip + Tension Marker return to ARBITER. Faction that lost the token moves winner's PS marker −1. **Cleanup:** Battlefield Modifier Cards played this round discarded (may not replay this contest or Quarter); Intel Tokens played this round handed to ARBITER, reset/returned to Dossier or discarded if single-use. Then **Will You Press? (§10.1.4.0.1):** if yes → **Press (§10.1.4.0.2)**: loser moves 1 chip from an adjacent district into the contested district, winner moves loser's PS −1, return to §10.1.2 for a fresh round (fresh mod cards/tokens may be committed again from hand — not previously-discarded ones). If no → proceed to §10.1.5.
- **Tie (§10.1.4.1):** no press. Each tied faction removes 1 chip (contested district or adjacent, their choice) to ARBITER for pool return. **Cleanup:** same as Winner, above. Then ARBITER checks the Dominant condition: exactly one or zero Dominant remaining → settled/no contest, Tension Marker removed, proceed to §10.1.5; multiple Dominant remain with no non-tied factions → return to §10.1.2; multiple Dominant remain with non-tied factions present → tied factions step out, remainder return to §10.1.2.

**§10.1.5 Update Board:** Dominant/Established/Tension Markers updated in the contested district and any adjacent districts chips moved from/to.
