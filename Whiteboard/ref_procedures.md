# Reference — Game Procedures (Art 03)
*Load when: procedure gaps, React card design, Debrief rules, Battlefield Strength, dice mechanics, PA resolution.*

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
| Modifier card | variable |
| Protect token | variable |
| Type B Countermeasure | −15 |
| Ring adjacency penalty (no Core presence for Mid target) | −25 |
| Stale Intel Token | −25 |
| Situation Report | variable |

Worst-case stack: partial payment + ring penalty + Discredited + Type B = −110, leaving only a crit viable.

---

## Monthly Phase Sequence

Each Month: **§9.1 Covert Dispatch** → **§9.2 Public Declaration** → **§9.3 Countermeasures** → **§9.4 Resolution (Beats 0–5)**. These are the canonical Art 03 names — never "Dispatch A/B/C" or "Phase A/B/C."

**§9.1 Covert Dispatch:** Factions assemble dispatch cases (operation card + Dispatch Token + cost resources), seal, and transmit to ARBITER. Cases are ARBITER-domain from this point. Factions name their target faction (and any declared parameters) on the Target Profile inside the case.

**§9.2 Public Declaration:** Factions declare PAs in initiative order — card placed face-up in Faction Resolution Grid with Dispatch Token and resource tokens. Target Profile placed **face-down** on the card. IntelTokens may be submitted here as cost payment or as modifiers. Once placed, card is a valid countermeasure target and cannot be withdrawn.

**§9.3 Countermeasures:** Factions deploy or pass in initiative order. CM cards may target queued covert ops or placed PAs.

**Two resolution grid domains — never conflate:**
- **Faction Resolution Grid** — PA domain; created at §9.2; visible to all players (cards face-up, Target Profiles face-down). IntelTokens submitted here are in ARBITER's procedural domain at Beat 3, NOT in the faction's private pool.
- **ARBITER covert grid** — covert op domain; assembled at §9.1 Beat 0; entirely ARBITER-private. Never a valid card-effect target.

---

## Public Act Declaration (§9.2)

1. Declarations in initiative order. Factions may pass verbally.
2. To declare: announce the public act; place card face-up in unresolved PA zone of Faction Resolution Grid with 1 Dispatch Token and resource tokens. Place Target Profile **face-down** on the card. Resource tokens remain with the card (not committed until Beat 4).
3. Modifier cards placed face-up alongside in Faction Resolution Grid.
4. Once placed: valid target for Countermeasures and other public acts. Cannot be withdrawn or modified.
5. Resolve in initiative order at Beat 4.

---

## Public Act Resolution — Beat 4 Key Steps

1. **Submit Payment:** Initiative order — resource tokens transferred to Reservoir; Dispatch Token returned. Full payment acknowledged; partial payment gets −50 threshold marker; zero payment = invalid (card flipped face-down, auto-fails).
2. **Apex Check (§9.4.3.1.1):** Acting Faction Player flips Target Profile face-up; reads public act card and Target Profile. Face-down PA cards auto-fail (do not flip — they remain face-down and go directly to fail outcome).
3. **Validate board state conditions:** If conditions required at Phase B declaration no longer met (altered by Beat 3 outcomes) — ARBITER announces invalidation, card returned.
4–8. Acting faction reads base difficulty, applies all modifiers, declares threshold aloud, rolls publicly, compares to threshold.
9. **Apply outcome:** Acting faction makes all board changes.
10. **Clean up:** Modifier cards discarded. Card remains per its duration type — Immediate cards only are removed immediately.

---

## React Card Rules (§18)

React cards fire in response to **publicly visible board state changes only** — cannot fire on ARBITER-internal changes such as the Resolution Grid.

**Timing window (§18.0.1):** Opens when a publicly visible board state change occurs. Closes at the next board state change or procedure advance — whichever comes first. Not instantaneous; a brief window is valid.

**Trigger and interrupt:**
- When trigger condition is met, holding faction announces "React," presents card, states trigger condition. ARBITER confirms validity and **pauses the quarter procedure**.
- Only one React resolves at a time. A second React may only fire in response to the new board state produced after the first resolves.

**Tiebreaker:** First to announce pauses play. ARBITER decides tiebreakers.

**Resume:** Once React resolves, original procedure resumes from the point it was paused.

**Modifier React cards:** If a modifier react card creates a persistent board state, it remains with its duration type per the Duration Taxonomy (§15).

---

## Debrief Procedure (§11)

No initiative order, no phase timer. ARBITER announces: "The Table is in Debrief."

**Free actions (§11.0 — any order, any terms):**
- Trade resources between any two factions
- Trade Intel Tokens between any two factions (examination permitted)
- Accept/decline/counter-propose Accord terms

**Debrief Action cards (§11.1):** Any faction holding a Debrief Action card resolves in initiative order — announce → execute → ARBITER confirms → card removed from game or returned to supply per card text. Runs before Chorus Question Window.

**Chorus Question window (§11.2):** If Chorus Activity track has reached Question threshold AND Chorus Node is not Contested — any faction with at least Present at the Node may propose a question. Simple majority passes. ARBITER answers in The Observation register. If Node is Contested, window does not open.

**Ready to Close (§11.3):** Faction Players flip Status marker to Ready when done. When 3 of 5 show Ready: ARBITER starts 60-second courtesy timer. Debrief closes when timer expires or all 5 show Ready → proceed to §11.4 ARBITER Debrief.

**ARBITER Debrief (§11.4 — in order):**
1. **Summary (§11.4.0)** — factual account of Quarter outcomes (The Record register). Q4 only: Annual Report follows Summary.
2. **Observation (§11.4.1)** — one observation (The Observation register). Form A: names a Portrait State without identifying faction. Form B: names the faction with a vague adjective. Never combined. Debrief closes; proceed to §12 Quarter Close.

**Debrief Reward:** §12.2 (Quarter Close, not part of Debrief proper).

---

## Battlefield Strength (§10 — Contested District Resolution)

**Triggers:** After Beat 5, ARBITER scans for Tension markers. Resolves Ring 3 inward to Ring 0.

**Calculation:** Each contesting faction simultaneously counts:
- All presence chips + structure blocks in contested district AND each adjacent district (deployment markers = 1 presence chip)
- Plus Battlefield Modifier Cards played face-up (+n per card; discarded immediately)
- Plus +2 per Fresh Intel Token (age 0–2) targeting opposing faction (tokens spent on use)

Each faction rolls a d10, adds to declared total. Highest total wins.

**Outcome:** Winner removes 1 presence chip belonging to any contesting faction from contested district; removes Tension marker. Loser may **press** (spend 1 chip from adjacent district to re-run from Step 3 with updated counts).

**Tie:** Each tied faction removes 1 chip. If one drops below Dominant and other holds — that faction wins. If both drop below Dominant — no winner, Tension marker removed. No continuation after a tie.

Board update: all control flags, Established markers, and Tension markers updated in contested district and any adjacent districts from which chips were removed.
