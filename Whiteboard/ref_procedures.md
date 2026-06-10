# Reference — Game Procedures (Art 03)
*Load when: procedure gaps, React card design, Debrief rules, Battlefield Strength, dice mechanics, PA resolution.*

---

## Dice Roll Procedure (§21)

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

## Phase B — Public Declaration Rules

1. Declarations in initiative order. Factions may pass verbally.
2. To declare: announce the public act; place card face-up on Overview in target district; stack target slip and 1 Dispatch Token on top. Resource tokens remain with the card (not committed until Beat 4).
3. Modifier cards modifying the act placed face-up alongside card on Overview.
4. Once placed: valid target for Countermeasures and other public acts. Cannot be withdrawn or modified.
5. Resolve in initiative order at Beat 4.

---

## Public Act Resolution — Beat 4 Key Steps

1. **Submit Payment:** Initiative order — resource tokens transferred to Reservoir; Dispatch Token returned. Full payment acknowledged; partial payment gets −50 threshold marker; zero payment = invalid (card flipped face-down, auto-fails).
2. **Apex check / face-down check:** Face-down cards auto-fail.
3. **Validate board state conditions:** If conditions required at Phase B declaration no longer met (altered by Beat 3 outcomes) — ARBITER announces invalidation, card returned.
4–8. Acting faction reads base difficulty, applies all modifiers, declares threshold aloud, rolls publicly, compares to threshold.
9. **Apply outcome:** Acting faction makes all board changes.
10. **Clean up:** Modifier cards discarded. Card remains per its duration type — Immediate cards only are removed immediately.

---

## React Card Rules (§28)

React cards fire in response to **publicly visible board state changes only** — cannot fire on ARBITER-internal changes such as the Resolution Grid.

**Trigger and interrupt:**
- When trigger condition is met, holding faction announces "React," presents card, states trigger condition. ARBITER confirms validity and **pauses the quarter procedure**.
- Trigger window is immediate — must be announced at the moment the triggering board state change occurs. Retroactive declaration is invalid; the window closes.
- Only one React resolves at a time. A second React may only fire in response to the new board state produced after the first resolves.

**Tiebreaker:** First to announce pauses play. ARBITER decides tiebreakers.

**Resume:** Once React resolves, original procedure resumes from the point it was paused.

**Modifier React cards:** If a modifier react card creates a persistent board state, it remains with its duration type per the Duration Taxonomy (§23).

---

## Debrief Procedure (§19)

No initiative order, no phase timer. ARBITER announces: "The Table is in Debrief."

**Free actions (any order, any terms):**
- Trade resources between any two factions
- Trade Intel Tokens between any two factions (examination permitted)
- Accept/decline/counter-propose Accord terms

**ARBITER conversion:** Available during Debrief and between phases. Not during active Resolution beats.

**Chorus Question window:** If Chorus Activity track has reached Question threshold AND Chorus Node is not Contested — any faction with at least Present at the Node may propose a question. Simple majority passes. ARBITER answers in The Observation register. If Node is Contested, window does not open.

**Debrief Action cards:** After Chorus Question window (or immediately if no window): any faction holding a Debrief Action card resolves in initiative order — announce → execute → ARBITER confirms → card removed.

**ARBITER's structured address (in order):**
1. **Summary** — factual account of Quarter outcomes (The Record register)
2. **Observation** — one or two pattern observations (The Observation register). Form A: names a Portrait State without identifying faction. Form B: names the faction with a vague adjective about Portrait contribution. Never combined.
3. **Distribution** — Quarter-end rewards (§20)

**Closing:** Faction Players flip Status marker to Ready (green) when done. When 3 of 5 show green, ARBITER starts a 60-second courtesy timer. Debrief closes when timer expires or all 5 show green.

---

## Battlefield Strength (§17 — Contested District Resolution)

**Triggers:** After Beat 5, ARBITER scans for Tension markers. Resolves Ring 3 inward to Ring 0.

**Calculation:** Each contesting faction simultaneously counts:
- All presence chips + structure blocks in contested district AND each adjacent district (deployment markers = 1 presence chip)
- Plus Battlefield Modifier Cards played face-up (+n per card; discarded immediately)
- Plus +2 per Fresh Intel Token (age 0–2) targeting opposing faction (tokens spent on use)

Each faction rolls a d10, adds to declared total. Highest total wins.

**Outcome:** Winner removes 1 presence chip belonging to any contesting faction from contested district; removes Tension marker. Loser may **press** (spend 1 chip from adjacent district to re-run from Step 3 with updated counts).

**Tie:** Each tied faction removes 1 chip. If one drops below Dominant and other holds — that faction wins. If both drop below Dominant — no winner, Tension marker removed. No continuation after a tie.

Board update: all control flags, Established markers, and Tension markers updated in contested district and any adjacent districts from which chips were removed.
