# STD + GHO Card Set Analysis — S119 Working Document

**Started:** S119 (2026-06-25)  
**Status:** Active — S120 complete; review and economic integration done; findings migrated  
**Source data:** Art 04 v0.9.47 · Art 04b v2.2 · card_status DB  
**Delete when:** All open design decisions resolved and findings migrated to PM05 / Art 04b §8

---

## Design Space Framing (S119)

Coverage gaps should be evaluated across all three card types — CA, PA, and MOD — before assuming a new CA is the answer. MOD subtypes carve up the space differently:

| MOD Subtype | What it does | Gap-fill potential |
|---|---|---|
| **Resolution Modifier** | Alters threshold, cost, or outcome while an action resolves | Boost underpowered STD baseline; let a faction punch above its CA set without adding a slot |
| **React** | Triggers on a publicly observable event | Standing defense, information interception, territory response — without consuming a Beat slot |
| **Battlefield Modifier** | Persistent state change | District locks, sustained economic pressure, structural advantages across beats |

GHO.MOD.1 (Clarify Misinformation) is the model: a React that fires on a PA submission event rather than a CA that consumes a covert slot. Standing gaps for GHO/SYN/GUI may be better served by a React or Resolution Modifier than by a new CA.

**Current MOD inventory (6 cards, none signed off):**

| Faction | MOD cards |
|---|---|
| Standard | STD.MOD.1 Overture |
| Ghost | GHO.MOD.1 Clarify Misinformation |
| Network | NET.MOD.1 Signal Break · NET.MOD.2 Reputational Strike |
| Syndicate | SYN.MOD.1 Accord Leverage |
| Guild | GUI.MOD.1 Return to Site |
| **Directorate** | **None** |

MOD design is largely unexplored — the gap analysis below should be read with this in mind.

---

## Standard Doctrine (confirmed S119)

Standard = the shared toolkit. All factions can use Standard cards regardless of internal doctrine to perform basic functions. Standard does not cover every action — intentional gaps exist. Where Standard and faction cards overlap, Standard is higher cost or less effective. Faction cards either enhance a Standard capability (cheaper/more powerful version of the same function) or fill gaps that Standard does not cover at all.

**Pending:** Art 04b needs a §8.0 Standard section to formalize this doctrine. Estimate: one paragraph. Low word count, high leverage before the 04-n87 audit.

---

## A. STANDARD SET

### Coverage map (from DB)

| Layer | Function | Subject | STD cards | Notes |
|---|---|---|---|---|
| Territory | Add | PresenceToken | CA.3, CA.8, PA.1 | Deep — basic deployment |
| Territory | Add | StructureBlock | CA.1, PA.3 | Basic build |
| Territory | Remove | PresenceToken | CA.4, PA.2 | Basic removal |
| Territory | Remove | StructureBlock | CA.2 | Basic demolition |
| Economy | Redirect | NativeResource | CA.9 | Fund — Art 07 dependency open |
| Economy | Redirect | IntelToken | CA.15 | Blind random — STD floor |
| Economy | Redirect | ModifierCard | CA.16 | Blind random — STD floor |
| Economy | Remove | IntelToken | CA.14 | Blind random — STD floor |
| Economy | Remove | NativeResource | PA.6 | — |
| Economy | Add | AccordAgreement | PA.8 | Table an Accord |
| Information | Add | IntelToken | CA.5 | Basic intel gathering |
| Information | Reveal | ActionAttribution | PA.5 | — |
| Information | Corrupt | Accord | CA.11 | Tort Interference |
| Resolution | Modify | PublicAct | CA.7 | — |
| Resolution | Protect | CovertOperation | CA.10 | — |
| Standing | Shift | PublicStanding | CA.13, PA.4, PA.7 | **Floor only** — see Standing gap below |
| Submission | Block | CovertOperation | CA.12 | Only system-wide CA block |
| Submission | Modify | PublicAct | CA.6 | — |

**Note on CA.14-16 (blind random):** Classified as Economy layer, not Information layer. Standard treats Intel Tokens and Modifier Cards as economic resources (blind disposal/transfer). Ghost operates on them at the Information layer (content-aware). The taxonomy encodes the doctrine distinction — intentional.

**Portrait:** Absent from all Standing cards — correct per Art 00a §5. Not a gap.

### Standing gap (confirmed S119)

Standard is the floor for Standing shifts — all 3 STD Standing cards are PublicStanding|Shift. Faction cards should exist that are more efficient (lower cost or more powerful). Current state:

| Faction | Standing cards | Status |
|---|---|---|
| Standard | CA.13, PA.4, PA.7 | Floor — correctly positioned |
| Directorate | DIR.CA.7 Institutional Brief | Calibration check needed — should be more efficient than CA.13 |
| Network | NET.CA.7 Ground Signal | Calibration check needed — should be more efficient than CA.13 |
| **Ghost** | **None** | Design gap |
| **Syndicate** | **None** | Design gap |
| **Guild** | **None** | Design gap |

**Design gate:** STD costs/thresholds must be set as the ceiling before faction versions can be calibrated. PM05 flag needed: *Faction Standing cards needed for GHO, SYN, GUI; calibrate DIR.CA.7 and NET.CA.7 against STD floor.*

### STD outstanding issues (issues_resolved=0)

**STD.CA.9 Fund** — `issues_resolved=0`
- Outstanding: Overture delivery procedure (ARBITER tableau → faction hand at Beat 3) pending Art 07 subroutine pass; anonymous transfer case-return procedure pending Art 03/Art 07
- Type: Art 07 infrastructure gap — not a design question

**STD.CA.12 Absolute Compromise** — `issues_resolved=0` (DB; design decisions cleared S120)
- All design questions resolved: scope CA-inclusive (S119), Type A only not Type B (S119), no refund confirmed (S120 — GR 7.2b). DB and spec updated.
- Remaining gate: 04-n70 (schema validation) + 04-n79 (narrative). Ready for design_pass + issues_resolved in consolidated sign-off pass.
- Art 03 item needed: formally define Type A vs Type B Countermeasure distinction in Art 03 procedure (not a design question — implementation work).

**STD.PA.8 Table an Accord** — `issues_resolved=1` ✓ (marked S120; DB note "Art 06 gate" was stale — card design complete, Art 06 §9.4 is downstream infrastructure)

**STD.MOD.1 Overture** — `issues_resolved=0` (legitimate — outstanding: Perspectives TBD (D-04-08 voice pass), Card ID TBD (04-n1), Value rating TBD (D-04-08), STD.CA.9 balance reassessment post-§11 redesign, Art 07 delivery formalization)

### Art 04b §8.0 and §6.4

**§8.0 Standard doctrine:** Written S119. ✓  
**§6.4 STD+GHO economic integration audit:** Complete S120. ✓ (Art 04b v2.2)

---

## B. GHOST SET

### Coverage map (from DB — non-blocked cards only)

| Layer | Function | Subject | GHO cards | Notes |
|---|---|---|---|---|
| Information | Add | IntelToken | CA.7, CA.8 | Station, Full Take — deep collection |
| Information | Add | DebriefActionCard | CA.9 | SCIF |
| Information | Corrupt | IntelToken | CA.5, CA.12 | Misdirection (FRG-placed tokens, offensive — S119) · Source Substitution (Ghost's own held tokens, self-supply) |
| Information | Remove | IntelToken | CA.4, PA.3, MOD.1 | Deep Cover, Declassified Records, Clarify Misinformation |
| Information | Reveal | CovertOperation | CA.2 | Intercept |
| Information | Reveal | IntelDeliverySlip | CA.3 | Dossier Breach |
| Information | Reveal | BroadcastEffectCard | PA.4 | Public Threat Assessment |
| Information | Reveal | ActionAttribution | PA.1 | — |
| Economy | Add | IntelToken | CA.6 | Synthesize — output token carries consumed token's faction key (S119) |
| Economy | Add | FactionNativeResource | CA.10 | Flip |
| Resolution | Modify | CovertOperation | PA.2 | Signal Review Request |
| Standing | Shift | PublicStanding | — | **None** — design gap |
| Submission | Redirect | CovertOperation | CA.1 | Pattern Match — steal model (S119): Beat 2 intercept moves op from target lane to Ghost lane; Ghost resolves as actor; original faction loses op + cost. Art 04b §5.1 L×F validity check pending. |
| Territory | Add | PresenceToken | PA.5 | Agency Recruitment Fair — restricted to Findings districts |

**Blocked (permanent or gated):**
- GHO.CA.11 Signals Analysis — gated on Art 06 Classified Directive
- GHO.CA.13 Backdate — permanent (L222 + GR 7.2b)
- GHO.CA.14 Field Verification — permanent (GR 7.2b)

### Doctrinal coverage assessment

Ghost's intelligence suite is the deepest in the game — collection, interception, corruption, targeted removal all represented. The structural gap is diplomatic: Ghost cannot privately deliver intelligence to a named faction. All Ghost PA effects are public. Ghost has no way to sell or trade intelligence — significant for coalition-building in 4-5 player games.

**Open gaps per Art 04b §8.1 (updated S119):**
- ~~Information|Reveal|Named faction~~ — **retired S119.** Delivery reading covered by covert messaging system. Surveillance reading already covered by IS-xx (Named faction = IS-xx target, not a new Subject). Target-scope/filter system dependency dissolved.
- Submission|Copy|Subset (Medium) — partial copy — blocked on partial-copy mechanism

**IS-xx information disclosure space (S119 — design seeds, added to Art 04b §6.1):**
ARBITER holds covert case contents between Beat 0 and Beat 3. Four new Information|Reveal Subjects — all gated on a shared ARBITER-domain access procedure (Art 03, not yet written):
- **SubmissionStatus** — whether a named faction submitted a case at all (non-submission is intelligence)
- **DispatchTokenCount** — operation count per case (faction's operational tempo this Month)
- **ResourceCommitment** — resources committed per operation (scale/cost signals)
- **ModifierStackComposition** — Modifier Cards submitted alongside an op (tactical intelligence)

**Debrief Action Card as information space — closed S119:**
- Intel Token validation: no truth value attached to tokens — nothing to validate
- Accord reveals: Accords are public knowledge — no information gap
- ARBITER observation/portrait: protected per 00a §5, ARBITER player's discretion — forced disclosure prohibited
- SCIF clarification: Information|Add|DebriefActionCard = the card produces a Debrief Action Card that captures a snapshot of historical board state (structure counts by ring at generation time). The recipient draws Modifier Cards at Debrief as if at upkeep based on that count. Effect is mechanical, not a live intelligence reveal — snapshot may be months stale by Debrief. **Current Debrief Action Card type: board state snapshot / mechanical bonus only.** If a new Debrief Action Card type is designed, information space may expand — this closure is specific to current card types, not permanent.

### GHO outstanding issues (issues_resolved=0, non-blocked)

**GHO.CA.1 Pattern Match** — `issues_resolved=0`
- Outstanding: copied op cost decision (Options A/B/C — see §C); portrait modifier AND/OR semantics; Prediction resolution undefined in Art 03 §9.4
- Type: 1 design decision + 1 Art 03 gap

**GHO.CA.3 Dossier Breach** — `issues_resolved=0`
- Outstanding: IntelDeliverySlip component entry missing in Art 02 (04-n45); Beat 2 delivery procedure missing in Art 03 (04-n44)
- Type: Art 02/03 infrastructure — not design questions

**GHO.CA.4 Deep Cover** — `issues_resolved=0`, `design_pass=1`
- Outstanding: Issues Resolved pending sign-off review
- Type: Andy's call — design is solid

**GHO.CA.5 Misdirection** — `issues_resolved=0`
- Outstanding: `content=false` not a defined IntelToken field in Art 02; Add vs. Corrupt taxonomy decision (see §C)
- Type: 1 design decision

**GHO.CA.6 Synthesize** — `issues_resolved=0`
- Outstanding: generated token faction-keying unresolved — affects SCIF/Flip gate eligibility (see §C)
- Type: 1 design decision

**GHO.PA.3 Declassified Records** — `issues_resolved=1` ✓ (marked S120)  
**GHO.PA.4 Public Threat Assessment** — `issues_resolved=1` ✓ (marked S120)  
**GHO.PA.5 Agency Recruitment Fair** — `issues_resolved=1` ✓ (marked S120)

**GHO.MOD.1 Clarify Misinformation** — `issues_resolved=0`
- Outstanding: Prediction resolution undefined in Art 03 §9.4 (same blocker as CA.1)
- Type: Art 03 gap

---

## C. Open Design Decisions

**All design decisions resolved (S119/S120).**

| Decision | Outcome | Applied |
|---|---|---|
| GHO.CA.5 Misdirection — Add or Corrupt? | **Corrupt** — alters faction_name on FRG-placed token; L222 compliant; no new fields | Art 04 v2.0 ✓ |
| GHO.CA.6 Synthesize — token keying | **Consumed token's key** — output inherits source faction; enables Gather→Synthesize→Flip pipeline | Art 04 v1.1 ✓ |
| GHO.CA.1 Pattern Match — copied op cost | **Option C fizzle** — wrong resource type or insufficient funds → slot wasted, no copy | Art 04 checklist ✓ |
| STD.CA.12 Absolute Compromise — scope | **CA-inclusive** — ARBITER sweeps both covert grid and FRG at Beat 2; GR 7.2a prohibits hidden state creation but not targeting private grid contents | Art 04 design note ✓ |
| STD+GHO economic integration audit | **✓ No gaps** — all 5 native types have STD spending paths; Flip→Deep Cover pipeline clean; calibration playtest flag added (04-n109) | Art 04b §6.4 v2.2 ✓ |

---

## D. Systemic Blockers — Art 02/03/07 Infrastructure Gaps

Ghost's issues_resolved count reflects infrastructure debt more than card design gaps.

**Prediction resolution procedure (Art 03 §9.4 — not written)**
- Affects: GHO.CA.1 Pattern Match, GHO.MOD.1 Clarify Misinformation
- Both cards functionally complete in spec; unresolvable at table without §9.4
- Prediction = ARBITER evaluates stated outcome against actual result; distinct from Automatic and d100

**IntelDeliverySlip — Art 02 + Art 03 gaps**
- Art 02: no component entry (04-n45)
- Art 03: no Beat 2 delivery step defined (04-n44)
- Affects: GHO.CA.2 Intercept (issues_resolved=1 but IS-xx procedure not written), GHO.CA.3 Dossier Breach

**Information|Reveal|Named faction — target-scope/filter system**
- No framework in Art 03/04
- Gates Ghost's intelligence diplomacy — the most important missing Ghost capability
- §8.1 high priority; no design work started

**Art 07 Overture subroutines**
- STD.CA.9 Fund: Overture delivery (ARBITER tableau → faction hand at Beat 3) not written
- Art 07 beat subroutines not yet designed

---

## E. Audit Bucket (04-n87/n88 — Non-Blocking Hygiene)

**Card ID schema (L219 — [FAC].[TYPE].n):**
- STD.CA.12: `id=39` (old numeric) → needs `card_id="STD.CA.12"`
- STD.CA.13-16: `id="—"` — all four missing L219 card_ids
- GHO.CA.1-3, CA.5-6: old numeric `id=` values (16, 17, 18, 20, 36)
- GHO.CA.13-14: `id="Ghost-ext-TBD"` (BLOCKED — lower priority)

**Heading format drift** (standard: `### [FAC].[TYPE].N — CARD NAME`):
- STD.CA.13-16: `### STANDARD — CARD NAME`
- GHO.CA.7-14: `### Ghost — CARD NAME`

**Misplaced card:**
- STD.CA.11 Tort Interference: appears at line 5377, after all GHO cards. Belongs in STD section.

**GHO.CA.2 sign-off status:**
- `issues_resolved=1` but notes "pending re-sign-off (v1.1 — beat timing correction)"
- If v1.1 change was non-material, prior sign-off holds; if material, re-sign-off needed

---

## F. Ghost §5a Flavor Assessment (S120)

*Reference: Art 04 §5a Faction Playstyle Reference — Ghost entry.*

### What's landing

The intelligence pipeline core is mechanically present: Gather/Station/Full Take generates tokens → Synthesize amplifies → SCIF converts to modifier cards that fund next Quarter's hand. The "build early, compound late" arc §5a describes has support. Collection (Station, Full Take, Gather), corruption (Misdirection, Source Substitution), interception (Intercept, Deep Cover, Dossier Breach) — the intelligence suite is deep and distinct from every other faction. Deck feel — precise, patient, deliberately small — is accurate: 14 non-blocked cards, every play feeding a sequence.

### Where it's thin or misaligned

**"Higher-tier cards" using Flip-acquired resources (plural) — only one exists.** §5a says "higher-tier cards carry a secondary cost drawn from Flip acquisitions." The card set delivers one spending destination for Flip output: GHO.CA.4 Deep Cover. The pipeline (Gather → Synthesize → Flip → Deep Cover) is complete but has a single endpoint. The §5a promise — "arrive at Q8 with a hand assembled from other factions' capabilities" — is not mechanically supported by one Flip endpoint. This is the most significant gap between §5a description and actual card set.

**Passive Intel token generation — unimplemented.** §5a describes "passive generation: Intel tokens from game events occurring near Ghost presence." No current card delivers this. May be a design intent that was never built, or a placeholder for a mechanic yet to be designed.

**§5a win path description is stale post-S113.** §5a calls Deep Cover a "burst card" — that was the pre-S113 design (when Deep Cover targeted private Intel Tokens held by rivals). After S113 redesign, Deep Cover is intelligence interdiction (removes a submitted FRG token before Beat 4). Full Take is the burst card. §5a needs updating to reflect current card design.

**Signals Analysis blocked.** Ghost's highest-value "suppress premature consensus" tool (GHO.CA.11, deduces Classified Directive) is gated on Art 06. Win path has a known missing component at L1.

### Sustained-pressure question (open)

Ghost can disrupt specific plays — void a PA token (Deep Cover), copy an op (Pattern Match), remove a submitted token. These are point-disruption plays. The question is whether point-disruption can actually delay premature consensus across 8 Quarters, or whether Ghost needs at least one standing threat that shapes how opponents plan. SCIF funds Ghost's own hand; it doesn't create opponent pressure. Ghost currently reacts to what opponents do rather than forcing opponents to react to Ghost. Whether this is doctrine-correct ("understanding must precede action") or a design gap is a judgment call — answered by comparing against how DIR/NET sustained-pressure tools feel in their audits.

### Items for 04-n110 cross-faction review

- Ghost's single Flip endpoint vs. §5a's implied tier structure — does Ghost need 1–2 more Flip-fed CA/PA cards, or can Modifier cards carry this?
- Passive Intel generation: design intent or unbuilt? Candidate for a React Modifier.
- Point-disruption vs. sustained pressure: compare against Directorate's suppression toolkit
- §5a text update needed: carry to §5a update pass after all faction audits done

### Design space note — Modifier decks

CA and PA sets are the core doctrinal action set. Faction Modifier decks (largely undesigned at L1) are the secondary design space that can address flavor gaps and play style nuance without expanding the CA/PA slot economy. Before treating a CA/PA gap as a card design problem, ask whether it's a Modifier problem instead. Ghost's passive Intel generation, sustained-pressure gaps, and additional Flip-fed plays are all candidates for the Modifier deck rather than new CAs. This applies across all faction audits — read §5a gaps with Modifier design space in mind before concluding a new CA or PA is needed.

---

*Last updated: S120 (2026-06-25)*
