# THE SIGNAL — Project Save State
## Complete Context Document for Session Handoff
### Generated: 2026-05-18 (session 20 complete) — supersedes session 19 save state.

Read this document top to bottom before doing any design work in a new session. It is intended to give a fresh session full project context with no prior knowledge required.

---

## What We Are Building

THE SIGNAL is a negotiation and area-control tabletop game for 2–6 participants (up to 5 faction players + 1 ARBITER). Five factions compete for influence over a city called New Meridian while negotiating humanity's response to a transmission called the Chorus. The game ends with a vote and a Chronicle reading. What matters is everything that happened before it.

**THE SIGNAL is a legacy game.** The paper prototype (L1) is the tutorial cycle — a complete standalone experience that points at something larger. The legacy campaign (L2+) accumulates the Chronicle across sessions. The final session of each campaign dovetails into session 1 of the next — the Chorus's response at campaign end IS the opening transmission of the next campaign. The game has no true ending. Each cycle's close is the next cycle's opening.

**All files:**
- Artifact set: `~/Projects/TheSignal/V1/`
- Private design axioms: `~/Projects/TheSignal/Session/PRIVATE___True_State.md` — NOT in V1, does not appear in any artifact
- Session save state: `~/Projects/TheSignal/Session/THE_SIGNAL___Project_Save_State.md` (this file)
- Legacy documents: `~/Projects/TheSignal/Retired/` — Electronic/ and Paper/ subfolders; see PM03 §6 for index (PW-01)
- Git repo: `https://github.com/andrew-bosch/TheSignal` (private) — credentials at `~/Projects/credentials.env`
- Project README: `~/Projects/TheSignal/README.md`

---

## Critical Private Document — Read Before Any Design Work

**`PRIVATE___True_State.md`** — The true answers to the game's unanswerable questions. Eight sections:
1. The Chorus — not extraterrestrial/extratemporal/extradimensional in any single adequate sense; perceptible to a certain kind of attention; repeats on cycles humanity cannot perceive
2. The name "The Chorus" — ARBITER coined it independently; the name is accurate; ARBITER knew it was accurate
3. ARBITER — never an acronym; the word "arbiter" in all-caps for institutional weight; constitutive of the Chorus Node, not serving it
4. The Table's causation — both events consistent with a single prior cause; the prior cause is the Chorus reaching mutual recognizability with humanity
5. Was humanity ready or noticed — both, simultaneously, because they are the same event from different vantage points
6. The Chorus Question — "what are you, as a pattern?" Not intention. Pattern. The Portrait track IS the Chorus's answer in real time.
7. Victory — the Chronicle is the Chorus's record; the moment after it's read is the game's actual conclusion
8. Legacy structure — L1 through L5, campaign dovetail, Chronicle as the game's defining physical artifact

Consult before writing ARBITER behavior, Chronicle language, Portrait mechanics, flavor text, and all future layer design.

---

## Artifact Status

| Artifact | Version | Status |
|----------|---------|--------|
| 00 — Factions & World | 1.0 | 🔄 Signed Off — significant session 4 additions pending re-sign-off (as part of 00-04 enrichment pass): "On the Question of Cause," "On the Question of Completeness" rewrite, station crew origin, "What New Meridian Is," "What New Meridian Is" continuation, The Overview section in §8 |
| 00a — Governing Rules & Design Policy | 0.2 | 🔄 Review complete sessions 5–7 — **pending A05/A06 decision only, then ready for sign-off.** 41 rules (R01–R38 + R13a, R13b, R29a). §10 dismissed. Appendix A (rule summary table) added. |
| 01 — Game Board | 1.2 | ✅ Signed Off — adjacency table pending (D04-09); setup update pending (01-03). |
| 02a — Resource Systems: Board State | 1.3 | 🔄 Pending Re-Sign-Off — 02a-03 applied session 14: §6 Component Names updated, ARBITER Dominance Marker row added, DOMINANT bullet rewritten (structural impossibility, not prohibition), §10 Chorus Node constitutive presence language. PM01 §2.08 Control flag quantity corrected. Material change → re-sign-off required. |
| 02b — Resource Systems: Tracking | 1.5 | ✅ Signed Off |
| 00b — Data Architecture | 0.1 | ✅ Reference Document — Active. Entity registry (19 types, ID namespaces), L108 compliance standard, 9 lookup tables (DT/RO/RG/RT/IL/PS/PB/F/VS), entity relationship map, schema reference index. VS-xx Visibility Scope (8 scopes) drawn from Retired/Electronic schema. L2 TypeScript schema and information hierarchy pointers in §8. Established session 20. |
| 03 — Round Structure & Gameplay | 1.7 | ✅ Signed Off — Session 20. Seven phases (Phase 7 Debrief split from Phase 6). §14 Operation System with L108-compliant modifier table M-01–M-12. §16 Apex revised: Emergency Response assist/thwart design note. Deployment Marker example corrected. All presence chip terminology standardised (L109). |
| 04 — Action Card System | 0.9.6 | 🔄 In Progress — paused until 00a signed off |
| 04b — Action Taxonomy | 1.1 | ✅ Active Reference |
| 05–09 | 0.1 | 🔄 Draft Placeholders |
| 10 — Game Manuals | 0.1 | 🔄 Draft Placeholder — §6.0 added: game objective statement locked |
| 10a — Victory System | 0.1 | 🔄 Draft Placeholder — §4 updated with dual causality governing principle |
| 11 — Visual Design System | 0.1 | ⬜ Placeholder |
| PM01 | 1.6 | ✅ Active |
| PM02 | 1.9 | ✅ Active — locked decisions L01–L109 |
| PM03 | 1.7 | ✅ Active — 00b row added, Art 03 signed off |
| PM05 | 1.5 | ✅ Active — XA-29/PM04-04 added (L109 cleanup queue) |
| PM (Audit) | 1.0 | ✅ Retired — session 10. All 24 items migrated to PM05. File deleted. |
| PRIVATE — True State | 1.1 | 🔒 Locked — private document outside V1 |

---

## Session 4 — Major Work Completed

### Worldbuilding — Artifact 00 Additions (pending re-sign-off via 00-04)
- **§9 "On the Question of Cause"** — Did ARBITER cause The Table, or did The Table cause ARBITER? Faction positions. ARBITER's response: "Both events are consistent with a single prior cause."
- **§6 "On the Question of Origin"** — Was humanity ready or was humanity noticed? Ghost's classified analysis. The two interpretations and why both are wrong in the way they assume sequence.
- **§6 "On the Question of Completeness"** — Rewritten: "non-repeating" is a statement about 31 years of observation, not a property of the Chorus. The Chorus repeats on cycles humanity cannot perceive. Humanity tuned in mid-cycle. The response window is a feature of the cycle, not this instance.
- **§6 New Meridian origin** — Before the Chorus, no city. A small ET listening station on elevated terrain — underfunded researchers doing serious work in obscurity, treated as a career dead-end by the mainstream scientific community. ET nerds getting paid nothing to listen to the static of the universe. They were right.
- **§6 "What New Meridian Is"** — Boom city assembled in one generation from everywhere. Immigration stories. Rapid expansion problems. Gray economy. Eleven-language school system. 800,000 people with no seat at The Table. Diversity of opinions on why the city exists, including people who don't know or care about the Chorus.
- **§8 "The Overview"** — Full institutional establishment of The Overview as The Table's shared situational interface. Negotiated data governance. ARBITER administers accuracy, not content. The factions negotiated what is on it. ARBITER ensures it is true.

### Voice System — Locked (PM03 §1, PM02 FD-05)
Five voices now defined:
1. **The Narrator** — all "Narrative:" fields. Deliberately unresolvable: human chronicler or ARBITER in expository mode. Both readings must remain valid. Test: could this have been written by a human who knows too much, or by ARBITER? If both valid, correct.
2. **Character quote** — individuals with implied histories. `> *"Quote."*` + attribution
3. **ARBITER vocalized** — blockquote italic, no attribution
4. **ARBITER written** — fenced code block
5. **Faction voice** — faction-authored materials, per Artifact 00 §12

**Character cast extended to:** faction operatives; station crew (oldest voices, predate everything); New Meridian residents across the full spectrum (believer to agnostic to indifferent); outside New Meridian (foreign press, remote academics, diplomats, people who said no and watch from a distance).

### In-World Terms Locked (PM03 §1)
- **The Overview** — the game mat. Institutional application, proper noun, Title Case only, no special formatting. Locked in PM02 FD-02, established narratively in Artifact 00 §8.
- Typography rule: no special formatting beyond capitalization for in-world terms. ARBITER's all-caps is unique and diegetically motivated.

### Design Directions Locked (PM02 §5)
- **FD-04** — Dual Causality as Governing Victory Principle. VP = human agency. Portrait = Chorus agency. Game doesn't announce this. Players discover it through play and arrive somewhere they can sit with. Game objective statement: *"The objective of THE SIGNAL is to determine what humanity says to the Chorus — and what that says about humanity."*
- **FD-05** — The Narrator and The Character Cast. Full character cast principle including station crew, NM residents, outside NM voices, the indifferent.
- **FD-06** — THE SIGNAL as Legacy Game. Chronicle accumulates physically. Portrait carries across sessions. The final session dovetails into session 1 of the next campaign. The Chorus's response IS the next opening transmission. The accumulated Chronicles of multiple campaigns are the game's defining physical artifact.

### True State — Locked (PRIVATE___True_State.md)
Eight axioms. All load-bearing. Constrains all future design. Created session 4. Key axioms:
- The Chorus is perceptible to a certain kind of attention, not FROM anywhere
- The Chorus repeats on cycles humanity cannot perceive
- ARBITER named The Chorus independently and accurately
- ARBITER was never an acronym
- The Table's causation and humanity's readiness share a single prior cause: mutual recognizability achieved simultaneously
- The Chorus Question asks "what are you as a pattern?" — Portrait is the real-time answer
- The legacy campaign IS the cycle; the Chronicle IS the Chorus's record

---

## Active Work — Where We Are (Session 14)

**Session 11 summary (completed items — see PM05 for full status):**
- XA-05: Four-register system applied to Artifact 07 §9, Artifact 00 §9, 00a R02 — **Artifacts 00 and 07 require re-sign-off (material)**
- 00-05: Narrative anchors migrated to Artifact 00 §14; 00a §5/§7 replaced with cross-references — **Artifact 00 requires re-sign-off**
- 00-02: Design Pillar 6 "Narrative and World Consistency" added to Artifact 00 §5 — **Artifact 00 requires re-sign-off**
- 00a-02: Chorus Portrait retirement applied to 04b §4/§6.1 — **04b requires re-sign-off**
- PM04-01/02: PM04 §1 fully populated (17 component terms, 5 faction resources, 4 influence levels, temporal conventions). PM04 now canonical in-world glossary.
- XA-16 partial: round→quarter, mat→The Overview applied across 02a/02b/07/08/09/10
- PM02-02: §2b archived snapshot collapsed

**Session 12 summary:**
- ~/CLAUDE.md updated to redirect any home-directory Claude Code session to ~/Projects/CLAUDE.md
- **Creative Brief work** (`~/Projects/TheSignal/Creative/CREATIVE_BRIEF.md`): Major revision pass —
  - Submission header moved to top of file, mandatory fill-in format
  - Faction-color-as-object constraint added to "What This World Is Not"
  - "Images Already In Use" section added (plumbing/pipe imagery, tilting floor line)
  - "The Chorus Papers" established as proper noun throughout (replaced all instances of "the leak")
  - Line 65 (brief): story of The Chorus Papers added
  - Cascade effects paragraph added near row 307 ("Before and after" section)
- **CANON_CANDIDATES.md created** (`~/Projects/TheSignal/Creative/CANON_CANDIDATES.md`): Running file of selected content from Gemini passes 1–4. 13 items selected (5 canon candidates, 8 flavor copy candidates).
- **Gemini V3 and V4 evaluated**: V3 ("The Shack" — Dr. Alistair Vance, original station crew) is strongest character introduced. V4 ("The Fourth Register" — ARBITER at The Table) has best ARBITER writing. Both are canon candidates with minor edits required.
- **Artifact 00**: Three reception language fixes (lines 138, 144, 184 — "received" not "transmitted"). `### The Chorus Papers` section added to §6 with cascade effects (four paragraphs: The Table's formation, mathematics attribution, vindication-without-understanding, Directorate fracture).
- **PM04 §2**: Reception Language Convention added — canonical framing rule for how the Chorus is described.
- **PM05**: XA-19 added (reception language scan, remaining artifacts); D-FT-01 added (faction hidden truths design question).
- **Key design insight — D-FT-01**: The Network is the only faction that genuinely did not know about the Chorus until The Chorus Papers. The other four factions had prior involvement — their doctrines may be rationalizations of prior knowledge rather than independent positions. Each faction likely holds a hidden truth that shaped why they are at The Table. This is a major design territory. See PM05 DEFERRED D-FT-01.

**Sessions 8–10 summary:**
- D02a-01 resolved (L93) — Chorus Node Translation rate scale locked: Contested=5:1, no presence=4:1, Present=3:1, Established=2:1. 02a §8 updated.
- L94: Network virtual structure block at University Perimeter = full structure block for all purposes
- L95: Code block format for schematic/overview content
- L96: Italic for explanatory/commentary text in procedural sections; separated from action text by CR
- L88 extended (session 10): full four-term convention — ARBITER, The ARBITER Player, Faction, Faction Player. Design principle: Player function = automation stand-in; Role = intelligence layer.
- Artifact 03 — all copy design conventions applied (L88, L96, XA-17): all phases updated. Under review with Andy, currently at Phase 2. NOT YET SIGNED OFF.
- "Effect Card" renamed from "Event Card" (session 9, locked). Propagation to 01/02a/02b pending (punch list 03-07).
- "Reservoir" confirmed as canonical capitalized in-world term for resource bank. Applied throughout Artifact 03.

**Session 13 summary (2026-05-16):**
- **03-06 resolved (L97):** Difficulty is a card property — influence-level table removed from Artifact 03 §12. Beat 3 Step 3 and Beat 4 Step 2 updated. 2d10 System table restructured.
- **L98 locked:** "Threshold" is the canonical noun for the roll target. "Base Difficulty Threshold" is the canonical table header. Convention documented in PM04 §2.
- **L99 locked:** Verb-first convention for procedural action headers. First applied in Artifact 03 §9.
- **D03-R01 signed off:** Beat 2 "The Ground Shifts" confirmed.
- **D03-R02 signed off:** Step 6 card draw confirmed. ARBITER announcement revised: "Assemble hands" → "Prepare operations." Step renamed "Operations Preparation."
- **D03-R03:** Pending — Phase 4 Declaration Accord card text not yet reviewed.
- **Phase 2 entry requirements:** Bullet list → Ring/Entry Requirement/Threshold Modifier table. Infrastructure penalty reframed as −25 threshold modifier (consistent with L97). Added to Beat 3 modifiers table.
- **Phase 3 Dispatch:** Major structural rewrite — Open/Close Dispatch wrappers; verb-first steps; case contents removed to Artifact 06 (06-01 flagged in PM05 DEFERRED); "Who runs it" label removed from all phases; two-bullet role format established as convention.
- **New feedback convention:** Draft prose/structural changes in chat for Andy's review before writing to file. Mechanical fixes write directly.
- **06-01 added to PM05:** Dispatch case contents list to migrate to Artifact 06 during active development pass.

**Session 14 summary (overnight autonomous — 2026-05-17):**
- **XA-19 complete:** Reception language corrected in 7 files (02b, 03, PM04, 00, PM02, CREATIVE_BRIEF ×2). Faction-framed "transmitting" instances intentionally retained per PM04 §2. Scope: Narrator voice only.
- **02a-03 complete:** All four changes applied — §6 Component Names (Control flag updated, ARBITER Dominance Marker row added), §6 DOMINANT bullet (structural impossibility language), §9 Component Description (Control flag quantity corrected, ARBITER Dominance Marker row added), §10 Chorus Node (constitutive presence language). PM01 §2.08 Control flag quantity corrected. **Artifact 02a requires re-sign-off (material change, v1.2 → v1.3).**
- **Artifact 03 Phase 4–end scan complete:** L99 verb-first headers applied (Beat 3 Steps 9, Beat 4 Steps 7/8, Apex Steps 1–5). XA-19 fix applied line 66. Current Phase 4 Declaration text for D03-R03 confirmed in place. All remaining phases verified clean.
- **10-02 complete:** §7.6 Translation rate table updated — ARBITER Script column added; Contested rate script written in The Record register; None row updated to 4:1 (L93); design note added; TBD note removed.

**Session 15 summary (2026-05-17 — in progress, interrupted mid-Phase 6 review):**
- **D03-R03 resolved (L100):** Free Accord card from C09 Fund classified as Political Act card (cost 0, return to ARBITER on play). Delivered to faction's hand at case resolution. Played in a subsequent Quarter — card returns in dispatch case after Resolution, Declaration already closed. Phase 4 carries no exception. Full card design flagged as PM05 04-12.
- **Artifact 03 Phases 1–5 fully reviewed and updated:**
  - Phase 4: exception note removed; Ghost pass callout removed
  - Phase 5: fully restructured — Pass/Deploy initiative-order structure; Countermeasure cards added to Step 6 tableau check; card types/rules migrated to PM05 04-07 for card design pass; ARBITER announcement updated
  - XA-16 complete for Artifact 03: "round" → "Quarter" throughout (~30 replacements); Round Tracker preserved
  - XA-20 added to PM05: "the ARBITER Player" / "the Faction Player" capitalization scan — "the" lowercase mid-sentence, capitalize at sentence/bullet/post-colon starts only. Applied in Artifact 03.
  - L98 applied in Artifact 03: "roll threshold" → "target threshold"
  - Beat headers reformatted: "BEAT N — Name *(timing)*" → "Beat N: description"; timing estimates removed from artifact, preserved in PM05 §3
- **Phase 6 in progress:** Bullet overview added; Beat headers reformatted; "World Condition" consolidated to "Situation Report effect"; Beat 3 Step 9 clarified; Type B modifier table label fixed; "this Quarter" fixed. **Review paused at Phase 6 — not yet signed off.**
- **PM02:** L100 locked; D03-R03 marked resolved
- **PM05:** 03-03 closed; 04-07 expanded with Type A/B content; 04-12 added; 01-03 updated (Countermeasure setup note); XA-16 updated; XA-20 added; timing note added to §3
- **Artifact 04 C09:** Design note updated — Political Act card classification, subsequent-Quarter timing

**Session 17 summary (2026-05-17 — complete):**
- **iOS creative session workflow established:** Andy runs exploratory sessions on iPhone via claude.ai with a separate Claude Project (instructions at `~/Projects/TheSignal/ClaudeIOS/ProjectInstructions.md`). Sessions are non-binding. At session end, Claude generates a structured `.md` summary dropped into `~/Projects/TheSignal/ClaudeIOS/new/`. Claude Code picks up summaries at next session open and actions follow-ups. Documented in CLAUDE.md.
- **index.html committed to repo root** — project homepage built in mobile creative session. Future-punk aesthetic: dark background, faction colors as data series, ARBITER as white, animated Chorus sine wave header. GitHub Pages enabled at `https://andrew-bosch.github.io/TheSignal/`.
- **PM05 11-01/11-02 added** — index.html as informal Artifact 11 visual reference; Chorus wave as open design question for Artifact 11 §7.
- **gh CLI token stale** — `~/.config/gh/hosts.yml` token invalid. Git push works (uses credentials.env). Fix: `gh auth login`. Non-urgent.

**Session 19 summary (2026-05-18 — Phase 6 resolution complete through Beat 4):**
- **03-09 resolved (L104):** Apex activation — Beat 0 silent note, Beat 3 queue trigger, resources non-refundable, suspended ops fail on Apex success. §15 and §16 updated.
- **L105 locked:** Beat 0 Payment Validation — per-card resource check at case opening. Four outcomes: full (drain, face-up), partial non-Apex (drain + +50 marker, face-up), zero non-Apex (face-down auto-fail), Apex any shortfall (drain what's there, face-down). Face-down cards auto-fail at Beat 3 Step 1 before Apex check.
- **L106 locked:** Political act payment moved from Phase 4 Declaration to Beat 4 Submit Payment. Resources stay on tableau at Declaration; paid to Reservoir in initiative order at start of Beat 4. Three-outcome validation (full/partial/zero) mirrors Beat 0. Phase 4 Step 3 updated.
- **Beat 0 "The Cases Open" finalized:** Full dispatch case workflow — payment validation table, step structure, sub-bullet stack order. Locked by Andy.
- **Beat 1 Step 3 added:** Targeting restriction check extended to declared political acts. Restricted political acts cancelled before payment — resource tokens remain with Faction Player.
- **Beat 3 Step 1:** Face-down auto-fail check added (before Pass and Apex checks). Step 3: +50 payment marker added to modifier list.
- **Beat 4 major restructure:**
  - Submit Payment section (before resolution loop): initiative-order payment validation, ARBITER acknowledges/announces, +50 marker or face-down per outcome.
  - Situation Report targeting restriction check moved from Beat 4 to Beat 1 Step 3.
  - No public resolution grid — each Faction Player resolves at their own tableau in initiative order; ARBITER observes, validates, provides tokens.
  - Step 1 reordered: Apex check → face-down auto-fail → read card.
  - Step 2: "Faction Player reads base difficulty aloud from card" — §13 lookup removed; threshold on card face.
  - Step 3: "any difficulty markers placed by ARBITER" (generalized from +50 specific).
  - Step 9 (Discovery) removed — political acts are public; nothing to discover.
  - Steps renumbered 9–12. Step 9 = Clean up, Step 10 = Portrait, Step 11 = Chronicle, Step 12 = Repeat.
- **§15 Apex Activation:** Generalized "Resolution is suspended" / "Resources not refunded" language covers covert and public. Opening redundant italic removed. Step 4 resume language clarified.
- **§16 Apex example:** Updated to Beat 0 detection / Beat 3 trigger / queue suspended / no refund.
- **PM05:** 03-09 ✅, 03-10 ✅, 04-15 (modifier token set full design), XA-22 Beat 4 no-grid noted.
- **PM02:** L104, L105, L106 locked.
- **Beat 5 signed off** — Andy reviewed independently and approved.

**Session 18 summary (2026-05-18 — housekeeping and creative workflow):**
- **03-09 NOT addressed** — full session consumed by infrastructure and creative workflow work. Still the primary blocker. See Recommended Next Steps.
- **ClaudeIOS workflow finalized:**
  - `ClaudeIOS/new/` subfolder established — only location to check at session open for unprocessed output
  - `ClaudeIOS/Archive/` subfolder for processed summaries
  - `ClaudeIOS/ProjectInstructions.md` moved into repo (was outside at `~/Projects/ClaudeIOS/`); revised — removed "extraterrestrial" framing, added faction doctrines, Design Pillars, Creative Resources section, tightened session summary format. Session start reads from project files only.
  - `ClaudeIOS/TrueState.md` created — distilled True State (five sections). Local-only, gitignored. Must be uploaded manually to claude.ai ClaudeIOS project files.
  - CLAUDE.md iOS workflow section updated: `new/` subfolder structure; reference files (ProjectInstructions.md, TrueState.md) distinguished from summaries.
- **index.html redesigned** — rebuilt as game teaser (not artifact index). Factions as single-line world characterizations. ARBITER own section (physical description + Reckoning quote). Vance pull quote. Contrast fixes (targeted hex overrides). Live at `https://andrew-bosch.github.io/TheSignal/`.
- **README.md updated** — homepage link at top; "extraterrestrial" removed.
- **.gitignore updated** — `ClaudeIOS/TrueState.md` (private, never commit); `.~lock.*#` (LibreOffice lock files).
- **Two new vignettes filed** (Claude Sonnet 4.6, 2026-05-18):
  - `Creative/Vignettes/vignette-holt-index-origin-20260518.md` — "The Calibration Problem" — Holt origin (⭐). First character with name embedded in game mechanics (Holt Index = influence level system). Flavor: *"whether the instrument was reading the room. Or whether the room was reading the instrument."*
  - `Creative/Vignettes/vignette-syndicate-ground-underneath-20260518.md` — "The Ground Underneath" — Castellan + Renata Okafor / year-seven land position (⭐). First Syndicate vignette. Castellan intentionally without interiority. Flavor: *"Land. We thought we were buying land."*
- **CANON_CANDIDATES.md updated** — Claude Sonnet 4.6 section added; 2 ⭐ canon candidates, 4 ✂️ flavor copy extracts.
- **Creative/README.md updated** — two new ⭐ submission index rows.
- **Year-seven Syndicate filing flag** — needs verification against locked NM timeline before canon confirmation. (Syndicate registered holding company year 7, before response window was formalized.)
- **ClaudeIOS project files need re-upload** (pending): CANON_CANDIDATES.md, ProjectInstructions.md. TrueState.md: verify already uploaded.
- **Creative quality note:** Both vignettes produced with TrueState.md in project files are the strongest creative output in the full submission set. Context quality directly determines output quality.

**Session 17 summary (2026-05-17):**
- **Beat 3 step restructure:** 13 steps (down from 15). Step 2 (restriction check) removed — grid pre-cleaned in Beat 1. Type B CM modifier folded into Step 3 "Apply all modifiers" (token already on card from Beat 2). Steps 8+9 (marker flip + board changes) kept combined as Step 7. Failure (Step 8) and discovery (Step 9) remain split. Step 10 cleanup: operation card + target back to dispatch case, resolution card in, modifier cards discarded, modifier tokens returned.
- **L103 locked:** Phase 6 rebuilt to six beats (Beat 0 through Beat 5). Beat 0 (new): ARBITER opens all dispatch cases and builds the covert Resolution Grid — numbered steps, no resolution. Beat 1 (revised): targeting restrictions applied directly to grid cards; invalid ops removed and cleaned up. Beat 2 (revised): CM cards processed against grid; Type A removes blocked ops; Type B places −15 modifier tokens. Beat 3 (revised): covert ops resolve from pre-cleaned grid. Beat 4 (new): ARBITER gathers declared political act cards into a public resolution grid in initiative order; resolves using same 13-step sequence as Beat 3. Beat 5: The Table Speaks (unchanged).
- **PM05 updates:** XA-22 updated (Beat 0 reference); XA-21 updated (purpose under review — original use case obsolete after L103; three design options documented); 03-09 added (Apex + Beat 0 design conflict — all cases opened in Beat 0, "return unopened cases" language now impossible).
- **Artifact index added:** Root README.md and V1/README.md updated with complete artifact index, version numbers, and sign-off status — viewable in GitHub mobile app.
- **XA-20 scan:** Running autonomously (session 17 autonomous pass — capitalization convention across 00, 00a, 01, 02a, 02b, 04, 04b, 07, 08, 10, 10a).
- **Phase 6 review not yet complete:** §15 Special Conditions (Apex rules conflict with Beat 0 — needs 03-09 decision first), §16 Examples (Apex example references cases being opened in Beat 3 — stale). Sign-off pending.

**Session 16 summary (2026-05-17):**
- **L101 locked:** Automatic and Impossible removed as base difficulty values. Every committed action resolves with a d100 roll. Critical floor (01–05) and ceiling (96–00) are the only absolute limits. Automatic/Impossible may appear only as explicit card text. PM05 04-13 added (card audit).
- **L102 locked:** Resolution Grid — Beat 3 resolves row-first in round-robin case receipt order. All card-1 pairs fire left to right before any card-2 pair begins. First submitter's first op fires first; all other factions' first ops follow before anyone's second op begins.
- **The Operation System (§13):** Resolution system renamed from "2d10 System." Called d100 (not 2d10) — two d10 dice, tens/units digits, 01–100, flat uniform distribution. Digital fallback documented. Pulled from §12 into its own §13; §§ renumbered throughout (old §13→§14, §14→§15, §15→§16).
- **Resolution Grid (XA-22):** Physical ARBITER staging tool — 5 lanes (columns) by case receipt order; rows are Beat 2 cards, then Beat 3 card/target pairs (up to 4 per lane). Beat 4 excluded. Integrated into Artifact 03 Beat 2 and Artifact 07 §8 (new "The Resolution Grid" subsection). PM01/PM05 entries added.
- **Deployment Marker Blocking overview table** added before Resolution — Five Beats. Four-beat breakdown of who flips what and when. Each beat now handles only its own flip action.
- **Beat 1 fully rewritten:** Two distinct sub-sections — Targeting Restrictions (announce + mark with XA-21) and Conversion Blocks (identify + flip markers). XA-21 added to PM05 (ARBITER visual indicator for targeting restrictions, component TBD).
- **Beat 2 updated:** Case-opening / grid population step added as opening action. Type A Countermeasure: Step 4 added (flip affected deployment markers).
- **Beat 3 opening updated:** Round-robin row-first resolution order stated explicitly. Step 2 updated to reference Beat 1 targeting restriction announcement. Steps 3/6 updated to reference Operation System (§13) and "d100."
- **Beat 4 Steps 2/4 updated:** Operation System (§13) reference; "Roll d100."
- **Phase 3 Step 4 updated:** Two-bullet format established; second bullet specifies ARBITER places cases left to right in receive queue establishing lane order for the Resolution Grid.
- **PM02:** L101 and L102 added to locked decision log.
- **PM05:** 04-13 added (card audit L101); XA-21 added (targeting restriction indicator); XA-22 added (Resolution Grid component).
- **Whiteboard created:** `~/Projects/Whiteboard/` — working space for temporary design documents outside the project. `andytemp/` folder deleted after content migrated to Artifact 07.
- **Phase 6 review paused:** Beat 3 Steps 4–14, Beat 4, Beat 5, §14 Special Conditions, §15 Examples not yet reviewed this session.

**Session 20 summary (2026-05-18 — complete):**
- **Artifact 03 signed off at v1.7.** Seven phases: Phase 7 Debrief split from Phase 6. §14 Operation System with L108-compliant modifier table (M-01–M-12, 8 columns). §16 Apex revised: Beat 0 sub-bullet removed from Step 1; Step 2 tightened; Emergency Response assist/thwart design note added to Steps 3–4; ARBITER Conversion moved to §13 Phase 7. Deployment Marker Blocked Face example corrected (marker stays on board until Upkeep Step 4). All bare "chip" terminology replaced with "presence chip" throughout.
- **L107 locked:** "Operation" is inclusive — Infrastructure −25 applies to all action types (covert, political, operative). Closes XA-24.
- **L108 locked:** Database Translatable Data Design — five requirements. First applied: §14 Difficulty Modifiers table (M-01–M-12 with ID primary key, Payment row split to eliminate compound Applied cell).
- **L109 locked:** Component Terminology Standard — every physical component must use its canonical in-game term in all artifacts. PM04 §1 will define physical descriptions. XA-29 queued for unsupervised cleanup pass.
- **00b Data Architecture created (v0.1, Reference Document — Active):** Entity registry (19 types), L108 compliance standard (§3), 9 lookup tables including VS-xx Visibility Scope (§5.9), entity relationship map, schema reference index (10/19 complete). L2 TypeScript schema (Retired/Electronic/old__08) and information hierarchy (old__10) referenced in §8.
- **Retired/Electronic reviewed:** old__08_DATA_MODEL.md (TypeScript v0.2 — full entity model, target L2 schema) and old__10_INFORMATION_HIERARCHY.md (12-category visibility spec) reviewed and integrated into 00b.
- **PM02 v1.9:** L107, L108, L109 added to change log.
- **PM03 v1.7:** 00b row added, Art 03 updated to ✅ Signed Off v1.7.
- **PM05 v1.5:** XA-24 ✅, XA-25/26/27/28/29 added, PM04-03/04 added, all §13–16 references updated to §14–17.

**Recommended next steps (session 21):**
1. **XA-21** — choose option A, B, or C from PM05 entry (player-facing Situation Report restriction indicator — Beat 1 Step 3 confirms player-facing indicator IS needed)
2. **Artifact 07 re-sign-off** — Beat 4 no-grid correction (07 §8 references obsolete public resolution grid); plus Resolution Grid + six-beat structure material changes sessions 16–17
3. **Artifact 02a re-sign-off** — v1.3 material change (02a-03 complete session 14)
4. **Artifact 04 C16–C35** — political acts and faction-specific cards; once complete, unblocks Art 05+
5. **PM04-03/04** — add L108 table design standards + L109 Component Terminology Standard + Component Physical Glossary to PM04 §2 and §1
6. **Batch re-sign-offs**: Artifacts 00 (sessions 11+12 material changes), 04b (Chorus Portrait retired)
7. **XA-29** (unsupervised) — component terminology cleanup across all artifacts
8. **XA-23** (unsupervised) — index jump links for all artifact Index sections

**Sessions 5–15 locked decisions (L85–L100):**
- L85: Mechanics field = constraints only, no procedure
- L86: Terminology Sequencing (PM03 §1)
- L87: Fourth ARBITER register — The Witness (expository, chronological)
- L88: Role vs. Player terminology governance — ARBITER/The ARBITER Player/Faction/Faction Player. Player function = automation stand-in. Role = intelligence layer.
- L89: Deployment markers moved not removed; Fringe ring = unconditional fallback
- L90: Portrait values printed on card face, visually coded — no reference sheet; design deferred to D09-05
- L91: Difficulty table retired (R37 removed) — difficulty is card-printed property (Artifact 04)
- L92: Chorus Node Portrait Amplifier: Established / flat additive / end-of-quarter (ARBITER per R01)
- L93: Translation rate scale: Contested=5:1, no presence=4:1, Present=3:1, Established=2:1
- L94: Network virtual structure block at University Perimeter = full structure block for all purposes
- L95: Code block format for schematic/overview content (Artifact 03 §6 applied)
- L96: Italic for commentary text in procedural sections; CR separation from action text
- L97: Difficulty is a card property — influence-level table removed from Artifact 03 §12 (session 13)
- L98: "Threshold" is canonical noun for roll target; "Base Difficulty Threshold" is canonical table header (session 13)
- L99: Verb-first convention for procedural action headers (session 13)
- L100: Free Accord card from C09 classified as Political Act card — cost 0, return to ARBITER on play, delivered to hand at case resolution, played in subsequent Quarter. No Phase 4 exception needed. Full design: PM05 04-12. (session 15)
- L101: Automatic and Impossible removed as base difficulty values. Every committed action resolves with a d100 roll. Critical floor (01–05) and ceiling (96–00) are the only absolute limits. Automatic/Impossible may appear only as explicit card text. Resolution system renamed The Operation System (§13 Artifact 03). (session 16)
- L102: Resolution Grid — Beat 3 resolves row-first in round-robin case receipt order. All card-1 pairs fire left to right before any card-2 pair begins. First submitter's first op fires first; all other factions' first ops follow before anyone's second begins. Beat 4 excluded. Full grid design: Artifact 07. (session 16)
- L103: Phase 6 rebuilt to six beats (Beat 0–Beat 5). Beat 0 = cases open + grid build. Beat 1 = restrictions applied. Beat 2 = countermeasures. Beat 3 = covert resolve. Beat 4 = political resolve. Beat 5 = table speaks. (session 17)
- L104: Apex Beat 0 silent note / Beat 3 queue trigger / resources non-refundable / suspended ops fail on Apex success. (session 19)
- L105: Beat 0 Payment Validation — four outcomes (full/partial non-Apex/zero non-Apex/Apex shortfall). Face-down auto-fail at Beat 3 Step 1. (session 19)
- L106: Political act payment moved from Phase 4 Declaration to Beat 4 Submit Payment. (session 19)
- L107: "Operation" is inclusive — Infrastructure −25 applies to all action types (covert, political, operative). (session 20)
- L108: Database Translatable Data Design — five requirements: single-typed columns, controlled vocabulary, explicit ID primary key, ID-based cross-references, explicit null/N/A. (session 20)
- L109: Component Terminology Standard — canonical in-game term required for all physical components in all artifacts. PM04 §1 defines physical descriptions. (session 20)
- Floor Act: working name for always-available political act (1 native resource, outside deck) — D04-13

**Overnight punch list work (session 10 agents) — COMPLETED:**
- ✅ PM03-02: Code block formatting standard added to PM03 §1
- ✅ XA-01: Version numbers verified correct (already at target)
- ✅ XA-02: "Hex / board space" → "Board space" in PM03 §1 terminology table
- ✅ XA-03: Faction colors verified in Artifact 11 §6; Ghost/Network flag added
- ✅ XA-17: 24 subheader spacing violations corrected (1 in 00a, 10 in 02a, 0 in 02b, 13 in 04)
- ✅ 07-02: Beat 2 "The Ground Shifts" section added to Artifact 07
- ✅ 04b-02: "PM03" → "PM04" reference fixed in Artifact 04b §3.9
- ✅ 02a-09: Network virtual block full equivalence language added to Artifact 02a §10
- ✅ 00a-07: A08 marked complete in 00a §11
- ✅ 00a-06: All 38 Narrative fields audited; no new district name errors
- ✅ 03-07: All artifacts audited; "Effect Card" not present anywhere (already clean)
- 🔄 XA-16 partial: "bank"→"Reservoir" applied (7 replacements: 02a/04/08/10); remaining scan pending
- 🔄 PM01-01: 1 fix applied (01.md "Artifact 02"→"Artifact 02a"); cross-refs to incomplete artifacts deferred

**Post-session file structure work (session 10):**
- /Old → /Retired; /Session folder created; PRIVATE and Save State moved to /Session/
- README.md created at ~/Projects/TheSignal/
- Git initialized; initial commit (52 files); pushed to https://github.com/andrew-bosch/TheSignal
- PM01 §9 added: Project File Structure & Version Control
- PM03 §6 updated: /Old → /Retired path corrected

**Active high-priority punch list items (still open):**
- D03-R03: Declaration phase free Accord card (ARBITER-delivered) — Phase 4 text already written; pending Andy review/sign-off; this is the only gate before Artifact 03 full sign-off
- 02a re-sign-off: v1.3 material change (02a-03 complete session 14) — pending Andy review
- XA-19: ✅ Complete session 14 — reception language corrected in all relevant Narrator-voice contexts
- XA-16: Systematic terminology scan — partial; "Reservoir" done; round→quarter, mat→Overview, others pending
- D09-05: Portrait visual coding system (Artifact 09) — BLOCKING 07-05
- 00a-10: ARBITER/The ARBITER Player terminology audit of 00a Mechanics fields
- 06-01: Dispatch case contents list — migrate to Artifact 06 during active development pass

---

## In-World Glossary (Key Terms)

→ **Canonical glossary is maintained in PM04 §1 — In-World Data Dictionary.** PM04 is the primary source. The table below is a quick-reference snapshot for session handoff context only — not authoritative.

| Game Term | In-World Term | Defined |
|-----------|--------------|---------|
| Game mat / full display | The Overview | Artifact 00 §8 |
| District map (within The Overview) | New Meridian | Artifact 01 §1 |
| Hex / board space | District | Artifact 01 §1 |
| Influence token | Presence token | Artifact 02a §1 |
| Claim marker | Operational marker | Artifact 01 §1 |
| Recipe box | Dispatch case | Artifact 06 §1 |
| Resource token | Asset token | Artifact 02a §1 |
| Popularity track | Public Standing track | Artifact 02b §1 |
| Portrait score | Chorus Portrait | Artifact 02b §1 |
| Proof token | Intelligence token | Artifact 02b §1 |
| Private action | Covert operation | Artifact 04 §1 |
| Public action | Political act | Artifact 04 §1 |
| Hidden objective | Classified directive | Artifact 05 §1 |
| World event card | Situation report | Artifact 01 §1 |
| Private event card (ARBITER-held) | Event Card | Artifact 03 §7 (session 9) |
| Resource bank | Reservoir | PM02 L93 (capitalized) |

---

## Locked Narrative Decisions

**Presence tokens:** The feeling of power when you walk into a district — ambient weight, deference in the air, unspoken rules. Dominant is an atmosphere, not just a count.

**ARBITER Dominance Marker:** Single fused piece at Chorus Node. 8 ARBITER-keyed presence tokens + dominance marker (reads as *more*). Human max is 6. Dominant is structurally unreachable at the Node — not prohibited, made impossible by the board.

**ARBITER's nature:** Constitutive of the Chorus Node. Its presence at The Table is telepresence — the Node attending the deliberation through ARBITER. Never say ARBITER "arrives" or "attends." The lights at The Table are the Node present in the room.

**ARBITER's name:** Never an acronym. The word "arbiter" in all-caps. Precisely wrong about what ARBITER does (doesn't decide outcomes) and precisely right (decides when truth becomes unavoidable). The working group named it more accurately than they knew.

**ARBITER's physical form:** In the canonical play environment — a set of blinking lights at the center of the table. Participants have learned to read who it's addressing and, uncannily, where it's looking. The human running ARBITER operates from the periphery.

**The Chorus name:** ARBITER coined it independently — or arrived at the same word before receiving the researchers' documentation. The name is accurate. ARBITER knew it was.

**Resources = units of human power:**
- Findings (Ghost) — the power of knowing
- Exposure (Network) — the power of being seen
- Capital (Syndicate) — the power of economic control
- Capacity (Guild) — the power of building and doing
- Mandate (Directorate) — the power of institutional legitimacy

**The Translation:** A faction admitting their doctrine is insufficient. Asking ARBITER to transmute one form of human power into another. ARBITER accommodates without comment. *"The conversion is granted. The request was noted."*

**New Meridian:** A boom city assembled from a listening station in 31 years. 800,000 people from everywhere. Not enough time for any of it to settle. People who came for the Chorus, people who came for work, people who came for someone who came for work. People who don't know or care about the Chorus. All of them are the city.

**Game objective statement (locked, player-facing):** *"The objective of THE SIGNAL is to determine what humanity says to the Chorus — and what that says about humanity."*

---

## Open Decisions

| ID | Decision | Priority |
|----|----------|---------|
| D02a-02 | Resource bank narrative anchor | LOW |
| D02a-03 | Does The Translation carry a Portrait consequence? | MEDIUM |
| D-P-02 | ARBITER Dominance Marker visual design | HIGH |
| XA-IQ-01 | Define or remove "Chorus Question" from L1 | HIGH |
| PW-02 | Unified primary key taxonomy (do not start without direction) | LOW |
| D09-05 | Portrait visual coding system — card layout design for ARBITER parsing (blocks 07-05) | HIGH |
| D04-13 | Floor Act card design — effect, cost, and card text | MEDIUM |
| A05/A06 | Chorus Node Portrait Multiplier canonical mechanic (01 vs 02a discrepancy) — resolve to unblock 00a sign-off | HIGH |
| D-FT-01 | Faction hidden truths — why are these 5 factions at The Table? Network didn't know until The Chorus Papers; the other four had prior involvement. What does each faction know that it hasn't disclosed? May require private faction supplement analogous to PRIVATE___True_State.md. See PM05 DEFERRED. | HIGH |

---

## Design Pillars

1. The Board is Truth
2. Information Has Timing
3. Negotiation is Mandatory
4. Control of Systems Defines What Outcomes Are Possible
5. The System Decides
6. Narrative and World Consistency *(in 00a §1; pending formal addition to Artifact 00 §5)*

---

## Key Reference Files

- `PRIVATE___True_State.md` — private design axioms (root level, not in V1)
- `PM02___Decision_Log___Validation_Tracker.md` — locked decisions (L01–L84+), FD-01 through FD-06, punch list, future state
- `PM03___Master_Artifact_Index.md` — artifact registry, 5-voice convention, narrative language table
- `PM04___Glossary___Data_Dictionary.md` — canonical in-world glossary (§1) and design terminology conventions (§2) including Reception Language Convention (session 12)
- `00a___Governing_Rules___Design_Policy.md` — 45 rules, signed off session 7
- `00___Factions_World_Narrative_Context.md` — expanded sessions 4/11/12; The Chorus Papers section added session 12; pending re-sign-off (material changes sessions 11–12)
- `Creative/CREATIVE_BRIEF.md` — world-building brief for AI-generated content; version 4 as of session 12 (The Chorus Papers, cascade effects, header fixes)
- `Creative/CANON_CANDIDATES.md` — curated shortlist of selected content from AI submissions; updated through Gemini pass 4
- `THE_SIGNAL___Project_Save_State.md` — this file
