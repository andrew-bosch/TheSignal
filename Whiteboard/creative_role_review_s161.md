> **Status:** S161 review pass — the ten World Engine agent roles run by hand over the `Creative/` submission set, as a dry run of the WBS 4.04 consistency checker. Findings only; nothing here changes an artifact or promotes anything.
> **Trigger:** Andy asked (S161) for role-perspective recommendations, and specifically whether any proposed canon would be pushed back to the writer for rewrites given the small corpus. Answer: yes — 4 of 6 vignettes.
> **Deletion target:** delete once Andy has run the `Creative/` evaluation pass these findings feed, and any resulting decisions are logged in PM02 / `CANON_CANDIDATES.md`.

# Creative Submission Set — Ten-Role Review

## 1. Scope and method

**Reviewed:** the six vignettes in `Creative/Vignettes/` (four Gemini 2026-05-16, two Claude Sonnet 2026-05-18), their ~12 attached quotes, and every entry in `Creative/CANON_CANDIDATES.md`.

**Not reviewed:** the two M365 Copilot pieces (Rook, Marek). `CANON_CANDIDATES.md` lists them as approved S34, but the files live in `ClaudeIOS/Archive/`, outside `Creative/`, and were not opened this session. Their verdicts below are inherited, not re-derived.

**Checked against primary sources, not memory:** Art 00 v1.9 (full), Art 01 v2.3 (21 districts, ring structure), `PRIVATE___True_State.md` v1.0, `CREATIVE_BRIEF.md`, PM02 (ring-rename decisions L141/L142, FD-01–FD-06), the `card_body` corpus, and git history where chronology was load-bearing.

---

## 2. Headline answer

**Four of the six vignettes get pushed back to the writer.** Three carry hard canon contradictions; one carries an arithmetic error. **Two of the four are pieces the existing manual pass marked "No edits required"** — including the one it called *"strongest single vignette in the full set."*

The corpus being small did not prevent contradictions. It caused a different failure instead: **canon has already absorbed unapproved content twice**, through no review at all, while the formal queue records nothing as incorporated.

---

## 3. Verdicts

| # | Item | Verdict | Blocking finding |
|---|------|---------|------------------|
| A | "The Third Desk" (Gabriel, Elena) | **Hold** | Terminology; invents a Ministry of Commerce |
| B | "The Dry Run" (Aris Thorne, Maya) | **Rewrite** | 412-second recurring dip contradicts "the Chorus does not repeat" |
| C | "The Shack" (Vance, Dr. Lin) | **Rewrite** | Reception as physical/electrical event contradicts True State §1 |
| D | "The Fourth Register" (ARBITER, Kang, Miller) | **Promote**, with the trim already specified | ARBITER's physical form vs FD-03 — flag, not a block |
| E | "The Calibration Problem" (Holt) | **Rewrite** | A Table session in year fourteen; The Table did not exist |
| F | "The Ground Underneath" (Castellan, Okafor) | **Rewrite** | Year seven to now is 24 years, not 18 |
| — | The ~12 standalone quotes | **Promote** after a terminology pass | Three say "Sprawl" |

---

## 4. Findings by role

### Archivist — canon lookup, conservative

**Retired terminology, every piece.** "Sprawl" was renamed **Baryo** and "the Infrastructure" (as a ring) renamed **The Mid** — PM02 **L141/L142**. All six vignettes and several `CANON_CANDIDATES` entries still use the retired names, including quotes marked "No edits needed."

**The writers are not at fault, and this matters for how the gap gets fixed.** `CREATIVE_BRIEF.md` itself said "Sprawl" seven times and "the Infrastructure perimeter" once until commit `4bc49e0` (2026-05-24, "ring renames"). The submissions are dated 05-16 and 05-18. **They correctly followed the brief they were given, and the brief was corrected a week later.** The lesson is about brief-to-canon sync, not writer discipline — and it is the single most mechanical, most automatable check in this review.

**The card corpus is clean.** `card_body` carries Baryo 17 times and Sprawl zero; all 35 "Infrastructure" hits are the common noun or the card title *Infrastructure Bond*. The drift is confined to `Creative/` and the shortlist.

**Institutions with no canon support:** Ministry of Commerce (A), Department of Anomalous Efficiencies (B quotes), Node Sub-Station 04, Signal Lab 09, "Sector 2/3/4", "Block 14 Mandarin Sector", "Eastern Infrastructure". Art 01 §6.4 fixes 21 districts and none of these is among them. Art 00 §6.5 leaves civic administration undescribed, so these are gap-fills rather than contradictions — but promoting them creates a municipal layer, which is a decision, not a detail.

**Name collisions: none.** Verified by word-boundary search across all artifacts and the card DB. Vance, Lin, Castellan, Okafor, Rook, Marek, Kang, Miller, Gabriel, Elena, Maya appear nowhere. **Holt appears only as "the Holt Index"** (Art 00 §14.2) and **has no first name anywhere in canon** — E gives him a face while preserving that, which is the right instinct, but promoting him still closes a gap Art 00 deliberately left open.

### Historian — timeline and causality

**E, hard contradiction — and it is one error, not two.** *"Year fourteen. A Table session Holt had not been invited to attend…"* The Chorus Papers were published 18 months ago; **The Table formed sixty days later** (Art 00 §6.6, §8) — roughly year 30. There were no Table sessions in year fourteen. **The venue is the whole error.** The Holt Index itself is fine in year fourteen: Art 00 §14.2 has *Ghost field operatives* naming it after the analyst first, with The Table adopting it as a shared reference only later — so the term is in circulation well before The Table exists. What cannot exist in year fourteen is a Table session, its monitoring room, and a room of observers treating the number as common currency.
*Fix, one clause:* keep year fourteen and make the venue a Directorate or Ghost internal briefing — Art 00 §6.6 supports it, the factions "had been operating independently for years." Moving the flashback to ~year 30 also works but costs the scene its point, which is that the Index became infrastructure long before Holt could stop it.
*Softer, same scene:* a **Directorate** liaison quoting a Ghost coinage in year fourteen implies cross-faction currency pre-Table. Plausible, not contradicted, worth a glance.

**F, arithmetic.** Castellan: *"We filed in the second quarter of year seven,"* and the site has been held *"Eighteen"* years. Year seven to the present (year 31) is **24 years**. Year seven is the right anchor and should stay — Art 00 §7.4 and §7.7 both date Syndicate ground acquisition to "as early as year seven" — so the duration is what changes.
*Minor, same piece:* Renata is "a development VP for eleven years" (from ~year 20) but built towers "during the year-nineteen housing surge," before that tenure begins.

**Verified consistent, for the record:** year-four temporary housing, year-seven second construction wave, year-nine reorganization, year-eleven noodle cart, year-twelve concrete pours, and C's *"The Directorate wasn't here until month two"* — which reads as a contradiction of "They were here first" (Art 00 §7.6) but is not: the Directorate's primacy is among **factions**, and the original station crew predates all of them. Half of an apparent-contradiction list dissolves on inspection, which is itself a design requirement for the checker: it must cite the passage that clears a flag, not only the one that raises it.

### Editor — validation and voice

**B, the load-bearing one.** A dip *"exactly three-point-eight percent below the expected galactic background — occurring every four hundred and twelve seconds"* is a repeating, reproducible, human-observable period. Art 00 §6.1 states flatly that **the Chorus does not repeat**; §6.2 makes non-repetition a claim about the limits of observation; True State §1 confirms cycles exist but on geological or non-human-temporal scales. A 412-second cycle sits inside the observation window and contradicts the one fact that, in the corpus's own words, "has held without revision for thirty-one years."
*Fix, preserving the piece:* make the interval fail to reproduce on the second run. The scene's power is the absence, not its regularity.

**C, physics.** *"It ran down the chassis. It cooked the worms right out of the dirt around the shack."* True State §1 holds that the Chorus does not occupy a position, is not a directed transmission, and is perceptible under conditions of focused observation. Induction that kills soil fauna makes it an energy flux with a direction and a power budget.
*Fix:* keep the groaning bolts and the ridge (perceptual, ambiguous, excellent); cut the chassis and the worms.

**Format.** All four Gemini files lack the header block the brief calls mandatory ("Do not omit, reorder, or reformat"). Both Claude files have it. Trivial, and exactly the kind of check that should never reach a human.

**Already caught by the manual pass, credited:** faction colors used as sensory detail (charcoal-green pin, signal-green pencil) in three pieces, and the plumbing/vibration motif saturating four. The existing human review caught all of these. It caught none of the timeline or physics contradictions above.

### Canon Diff — existing canon vs. candidate

**Canon has already absorbed unapproved content, twice, with no promotion step.**

1. **The noodle cart.** E (committed 2026-05-18, session 18) introduces the depot cart, the construction-contract mother, the daughter who runs it on alternate days, and her reaction to the Chorus Papers — *"waiting for a specific word in a sentence and had finally heard it."* Art 00 §6.7 now contains the same woman, the same daughter, since year eleven, saying *"I wasn't surprised. I was waiting for a word I already had."* That text entered Art 00 on **2026-07-03 (session 134)**, seven weeks later. **The district changed in transit:** the vignette puts the cart at a transit depot on the Infrastructure perimeter; Art 00 puts it on the Commercial Strip, in Baryo.
**This resolves in Art 00's favour and is not an open question.** Art 00 is v1.9 Signed Off and the vignette is still pending, so canon wins by default — and E's location is wrong twice over, since "Infrastructure perimeter" is retired terminology regardless. **E moves to the Commercial Strip.** Editing Art 00 to match the vignette is the expensive branch, not a co-equal one: it is a material change to a signed-off artifact requiring a proposed draft and re-sign-off, and it should only be raised if Andy actively wants the depot setting.
2. **Aris Thorne — a process gap, stated precisely, because the precise version is smaller than it first looks.** True State §11 cites *"Dr. Aris Thorne — Atacama radio astronomer, ~4,000 miles from NM per vignette"* as a downstream consideration for the undefined question of New Meridian's location. That line entered on **2026-05-27 (session 44)**, under a header reading **"🔒 Locked — Session 4."**
**What this is not:** True State being corrupted. The document's closing line anticipates revision — "Revisions require the same deliberation as any locked decision — but the bar is higher" — so editing it is permitted, and §11 is the *open questions* section, the least load-bearing part of the file. Nothing in §1–§10 was touched.
**What it is:** an unapproved character cited inside designer truth with **no PM02 entry recording the decision**, at a bar the document itself sets higher than normal. The vignette that produced him is also one of the four needing rewrites.
*Fix, either way:* log it in PM02 and legitimize the citation, or drop it to a role descriptor ("an Atacama radio astronomer") so §11's constraint survives without depending on a pending character.

**Therefore `Creative/README.md`'s "Canon That Has Been Incorporated: *Nothing yet*" is false.** Two things were incorporated; neither went through the queue.

**The shortlist is stale about its own placements.** `CANON_CANDIDATES.md` says Jae-won Seo is "Named in Art 01 §4." Art 01 §4 was migrated to Art 02 at S90 and contains no character names; Seo survives only in PM05 and PM05 Archive. Placement claims in the shortlist cannot be taken at face value.

### Curator — value against complexity cost

Nothing here should be rejected. The set's hit rate is high and the two Claude pieces plus D are the strongest material the project has produced.

The governing consideration is not quality, it is **commitment**. Promoting E names the person behind the game's own measurement vocabulary. Promoting C seats Vance as *the* original-crew figure — and **three characters now compete for that seat** (Vance, Rook, Marek), which True State §11 explicitly lists as an open question. Promoting A creates a municipal government layer. Each is cheap as prose and expensive as canon.

**Recommended order:** the quotes first (low commitment, high reuse), then D, then E and F once corrected, then decide the original-crew seat as one decision covering all three characters rather than three separate ones.

### Political Analyst — faction realism

D's Kang/Miller exchange is doctrinally accurate on both sides: procedural stonewalling against exposure, neither caricatured. C's Dr. Lin behaves correctly as Ghost — pursuing primary sources the Directorate says were scrubbed.

**One flag:** Miller claims *"The Network has the telemetry from the year-four water mains."* The Network arrived after the Chorus Papers, eighteen months ago (Art 00 §7.3). Twenty-seven-year-old municipal telemetry implies a source — a Guild leak, a sympathetic Mid technician — and the piece does not supply one. Art 00 §7.3 says they have "more relationships than anyone is comfortable admitting," so this is answerable in one clause.

**FD-03 flag, not a block:** D renders ARBITER as *"a matte-black housing no larger than a terminal relay, bolted directly into the oak floorboards."* PM02 **FD-03** describes ARBITER's canonical physical form as an object at the **center** of the table. The vignette's ARBITER sits between the participants but is bolted to the floor, and the session is in a conference room rather than the chamber at the Chorus Node (Art 01 §3). Worth settling before this becomes the reference image for ARBITER's form — it is otherwise the best ARBITER writing produced.

### Cultural Anthropologist — societal texture

**The Mid is missing entirely.** All six pieces are set in the Core, Baryo, or outside New Meridian. Art 00 §6.7 gives the Mid the richest unused texture in the document — shift work, crossing permits, company-adjacent housing, the ozone-and-relay-hum crossing, and a specific bitterness about the Papers ("the people who maintain a city's machinery had assumed, without ever saying so, that they knew what the machinery was for"). Nothing has been written into it.

**Register saturation:** the plumbing/hum motif is the city's sensory signature in four of six pieces. The brief's banned-motifs list already logs it. Untouched: the eleven-language officially-monolingual school system, the 28-year-old festivals, the Broadcast Tower busker economy of being watched, the commissary-and-dining-room social order of the Core.

### Economist — resource and incentive realism

A's premise is canon-solid — Art 00 §6.6 establishes thirty years of Chorus-derived mathematics moving into commercial patents, and the Syndicate "was not surprised by this."

**Plausibility flag, A:** a cooling array that drops ambient temperature "by precisely four percent" because *"these don't move it. They invite it to leave"* reaches past the brief's ban on technology exceeding plausible physics. The patent-fraud framing carries the scene without it.

**F is the most mechanically useful economic content produced.** A ninety-nine-year ground lease, a revenue-participation clause on Chorus-derived IP, and a non-voting observer seat is Syndicate doctrine rendered as instrument, and it maps directly onto Art 00 §7.4 and the Structure Block anchor (§14.3), where what the mark *represents* varies by faction and is never surfaced. Once the arithmetic is fixed this is card- and Accord-adjacent material.

### Lore Miner — gaps this pass exposed

- **No municipal government layer.** Three pieces independently invented ministries. Canon has districts and factions and no city administration.
- **No Mid-ring protagonist**, against the richest unused texture in Art 00.
- **No below-leadership Directorate or Network protagonist** — both appear only as principals at The Table.
- **Holt has no first name**, and Art 00 §14.2 keeps him deliberately faceless.
- **The original-crew seat is contested three ways** and is a logged open question (True State §11).
- **Undefined and repeatedly brushed against:** schooling, healthcare, religious practice, and what the ~800,000 residents who are not faction operatives actually do about any of it.

### Writer — what goes back

Four pieces, four small fixes. None is a rewrite from scratch:
- **B:** break the 412-second regularity — one sentence.
- **C:** cut the chassis and the worms; keep the bolts and the ridge.
- **E:** move the flashback to ~year 30, or reframe the audience as a faction-internal briefing.
- **F:** eighteen years → twenty-four; reconcile Renata's tenure with the year-nineteen surge.

---

## 5. What this says about the World Engine build

**Every hard finding came from three roles:** Archivist (terminology, unregistered institutions, name collisions), Historian (date arithmetic against fixed anchors), and Canon Diff (what canon already absorbed). All three are lookup-and-compare work against a structured store — the cheapest thing to automate, and the thing a 12–14B local model can do reliably because each finding is checkable against a citation.

**Editor needed judgment** — B and C required reading a claim against True State §1 and deciding whether it resolved ambiguity. That is a real reasoning task and the one place a local model's output would need verification every time.

**Curator, Political Analyst, Anthropologist and Economist produced no detections at all** — they produced opinion, ranking, and gap-spotting. Valuable, but that is the work that stays with Andy, Gem, or me. As standing agents they would generate volume against the queue that is already the bottleneck.

**The empirical case for the checker:** three hard contradictions survived a manual review pass that examined these same pieces closely enough to catch faction-color violations and a fourth-instance plumbing motif — and that marked two of the three contradicting pieces "No edits required." The failure was not attention. It was that catching them required holding six timeline anchors, a 21-district list, two retired ring names, and True State §1 in mind simultaneously while reading prose. That is precisely the task a structured canon store makes trivial and unaided reading makes unreliable.

---

## 6. Recommended actions

1. **Decide the four rewrites** — or overrule any of them. All four fixes are one or two sentences.
2. **Terminology pass over `Creative/` and `CANON_CANDIDATES.md`** — Sprawl → Baryo, the Infrastructure → The Mid. Mechanical, and the card corpus is already clean.
3. **Resolve the two informal absorptions, in the cheap direction.** The noodle cart: move **E** to the Commercial Strip to match signed-off Art 00 §6.7, and record the absorption so the shortlist reflects it. Thorne: either a PM02 entry legitimizing the True State §11 citation, or drop it to a role descriptor. Neither requires touching a signed-off artifact; raise the Art 00 route only if the depot setting is wanted on its merits.
4. **Correct `Creative/README.md`** — "Nothing yet" is inaccurate. **Check the two Copilot pieces while you are in there:** `CANON_CANDIDATES.md` records Rook and Marek as "approved S34," which either makes them a third incorporation the README contradicts, or is itself a stale claim like the Seo placement. Not resolved here — those files were not audited this pass.
5. **Settle the original-crew seat** (Vance / Rook / Marek) as one decision, against True State §11.
6. **Carry findings 1–5 into WBS 4.01** as the checker's first test set — a checker that cannot reproduce these findings is not finished.
