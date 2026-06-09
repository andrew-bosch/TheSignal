# THE SIGNAL — Session Brief
**Session 75 (active) | Updated: 2026-06-09**

Lean startup document — replaces unconditional full reads of Save State and PM05.
Read full files only when deep work requires it.

---

## Current Focus
S75 complete. S76 opens here.

**S65 accomplishments:** 04-n25 PS-as-cost ✅ and pre_loss_calc ✅ closed. Art 04 §6.2 cost field redefined (fungible resources only). Art 04 §6.6 added (Expression Parameters — pre_loss_calc). C37 Sacrifice redesigned v1.1 (cost=None; target_faction required; success=ps−2+IntelToken). C34 Golden Parachute redesigned v2.0 (bribe mechanic; variable cost; retained resources). Art 03 v3.1 signed off (L185) — Beat 0 Retained validation; Beat 2 Golden Parachute procedure; Beat 3 partial payment marker source. XA-38 closed (anchor link sweep — 38 links fixed across 11 artifacts). Network PS recovery/negation modifier card added to modifier_card_ideas.md.

**S66 accomplishments:** 04-n25 ✅ closed. Entry/Exit Controls redesigned v2.0 (district target; permanent placement block; `persistence_condition`). Art 03 v3.2 signed off (L186). Art 04 §6.6 removed. `persistence_condition` added to §6.1/§6.2. New PM05: 04-n29 (counter-card design + Art 03 persistence monitoring), 04-n30 (persistence_condition sweep).

**S67 accomplishments:**
- 04-n26 started: Cluster A in progress (SCIF complete; Land Title, Parasitic, Regulatory Downgrade complete)
- SCIF card: spec cleaned — `success = SCIFRecord(target=faction(target))`, tagline fixed (in-fiction), design_note doctrine-only, arbiter_note flagged ⚠ outstanding (04-n27), `target_district/target_object = None`. SR-xx registered in 00b §4 concept (agy task).
- pool_copies sweep: **04-40 ✅** — 42 code-block instances + 7 prose references removed from Art 04; Pool copies row removed from design_reference.md.
- PM05 additions: XA-45 (merge Art 02a + 02b → Art 02), DB-31 (update tmp_component refs → `component` table).
- IS-xx (Intel Delivery Slip): used by C17 Intercept (success) and C28 Open Channel (redirect scope). Art 03 §11 has one covering sentence; detailed steps not yet written (migration pending, overlaps 04-n27).
- Land Title redesigned v2.0 ✅: Territory/Add/StructureBlock; success = Grant Deed delivered to Syndicate case; no board marker; restriction = district.structure_count == 0. Grant Deed = new tripwire React component (SCIF-pattern, ARBITER tableau). Grant Deed sketch in gap_card_sketches_S62.md. Outstanding: Grant Deed component registration (04-n26), tripwire react window in Art 03 (04-n27).
- Parasitic redesigned v2.0 ✅: Positional wager. Beat 2 checks Beat 3 queue; Intel keyed to first card's submitter (resolution order). No component.
- **00-R40 locked (L187):** ARBITER Cognitive Load governing rule. Art 00a (44 rules, pending re-sign-off) + Art 03 §5 P6 + Art 04 §5 P18. design_reference.md + memory updated.
- Regulatory Downgrade redesigned v2.0 ✅: CovertOperation → PublicAct (permanent). Card-as-condition (success=None). persistence_effect = resource gen −1 tier. Clears: target pays 2 native to Reservoir any time after Beat 4. No TierPenaltyMarker.
- Art 04 §6.1/§6.2: `persistence_effect` field added to schema (S67). PM05 04-n31 added (sweep).
- Regulatory Freeze redesigned v2.0 ✅: PublicAct, card-as-condition (no TierFreezeMarker), self-policing enforcement per 00-R40a. Issues Resolved ✓. Pending sign-off.
- Standing Injunction redesigned v2.0 ✅: PublicAct, card-as-condition (no InjunctionMarker), Permanent with dual clearing (trigger OR Phase 21), target_taxonomy field introduced (§6.1/§6.2), Accords excluded, no operational restriction. Dispatch Token consumed on trigger per 00-R35. Issues Resolved ✓. Pending sign-off.
- Art 04 §6.1/§6.2: target_taxonomy field added to schema (S67).
- 00a: R06a added (corollary to R06 — board states committed on resolution; countering requires forward action).
- 00a: R40a added (corollary to R40 — factions police their own permanent effects; ARBITER adjudicates on call). R40 relocated from §9 to §3. Rule count: 44 → 46. Pending re-sign-off.

**S68 accomplishments (pre-compact):** 04-n26 Cluster B complete — C19 Deep Cover v1.1 (R40 fix; IntelToken physical target only), C23 Tort Interference v2.0 (Standard; any faction; Accord lock until game end or breach), C26 Leak v1.1 (pre-execution cancellation; highest-cost target; cross-resource cost 1 Exposure + 1 Findings). Cross-resource cost design principle established and locked to PM05 04-n34c. PM05 04-n34 split into 04-n34a/b/c. PM05 01-n01, 02-n01 added (zone/component design review items).

**S68 accomplishments (post-compact):** C18 Dossier Breach v1.1 — redesigned to SIGINT tap / DispatchReport model (Beat 2 submission; ARBITER delivers DispatchReport from Beat 0 grid data at beat3_pre_resolution). C28 Open Channel — retired to L2 (cross-beat ARBITER state required; R40 + cognitive efficiency violations; PM05 04-n40). C24 Surveillance Placement — mechanics invalidated; narrative-first rethink required (PM05 04-n41; gate for all covert intelligence card redesign). **Governing Principle — ARBITER Cognitive Efficiency** added to 00a §1 (parent of R40 and R40a — objective, not just rule; design question: "how can this narrative function be implemented while impacting ARBITER as lightly as possible?"). Resolution grid confirmed entirely covert — factions never see it; return deliveries only valid L1 intercept targets. NS-xx defined in 00b §4. IS-xx reinstated with tighter definition (R40 misdiagnosis corrected). DR-xx (DispatchReport) registered in 00b §4. PM05 04-n38–04-n41 added. C17 redesign flagged (PM05 04-n39).

**S68 accomplishments (S68+):** 04-n41 gap assessment complete — L1 scan confirmed no new execution problems beyond C17/C24/C28/C18; Beat 0 = payment validation only; Beat 1 = SitRep only; Beat 2 = first resolution opportunity. C24 Surveillance Placement redesigned v2.0 (Beat 2 episodic model; IntelDeliverySlip delivery; no board marker — R06 prohibits covert markers; op type only, no faction; 04-n42/43/44/45/46 added). DR-xx (DispatchReport) collapsed into IS-xx (IntelDeliverySlip) — IS-xx expanded to cover Beat 2/3, column reads (C18) and row reads (C24). C18 Dossier Breach updated v1.2 (subject=IntelDeliverySlip; delivery at Beat 2 resolution). PM03: 04b marked pending re-sign-off (S64 material addition missed). Art 04 v0.9.32. Session startup memory added (boot must be proactive + include summary).

**S68 accomplishments (session close):** 04-n27 substantially resolved — Art 03 §19 Debrief Actions step added (DebriefActionCard type; SCIFRecord first subtype); §25 Modifier React Card Rules updated to cross-reference §28; §28 React Card Rules added (interrupt model; fires on visible board state change only; first-to-announce pauses play; ARBITER decides tiebreakers). Art 03 v3.3 signed off (L189). 04-n39 substantially closed — IS-xx reinstatement confirmed; Art 03 migration concern closed; C17 "silent" PS language removed; beat timing correction flagged (04-n49). Art 04 SCIF card spec updated: DebriefActionCard (type) / SCIFRecord (subtype). PM05 04-n47 (no-branching design constraint), 04-n48 (card redesign batch: C31/C40/C41/C42/Signals Analysis), 04-n49 (C17 beat timing correction) added. 04-n27 sub-items all resolved or delegated.

**S69 accomplishments:** 04-n28 substantially complete. Art 06 §5 reworked (Accords-are-public; player-verified compliance; R40a does not apply). Art 06 §9 Accord governance overhauled and signed off (L191): §9.1–§9.10 — Accord form (mad-libs structured contract), terms, formation (Beat 4 submission; Debrief execution window; all Accord blanks as Beat 4 resolution outcomes), compliance monitoring, breach (form → ARBITER area; Portrait −4 breacher only), completion (Portrait +1/Quarter + +2 on completion), dissolution (Debrief only; no Portrait), Portrait scale (L190 — pending playtesting + modeling), manipulation types (Lock/Alter/Transfer). §6/7/8/10/11/12 stub-flagged non-canonical. Art 06 v0.2. C-S3 outstanding issue added (ARBITER record → physical Accord form). Art 04 §11.7 Outcome addition effect type added. Art 04 §11.8 Overture stub: Instant modifier / outcome addition / Beat 4 / delivers blank Accord form / from ARBITER tableau via C09 success / full spec pending §11 redesign. C09 Fund references updated (AccordCard → Overture). L190/L191 locked.

**S70 accomplishments:** Startup fix — dynamic mtime comparison command added to feedback_agy_context_check.md (prevents hardcoded timestamp false positives). C17 Intercept v1.1: beat=3 → beat=2; checklist/issues/code updated; 04-n49 ✅ closed; pending re-sign-off (04-n50). PM05: 04-n50 through 04-n67 added — set-level card milestone tracking for 6 sets (Standard + 5 factions), each with 3 items: design pass complete / issues resolved / sign-off pass; 04-n50 updated to gate on 04-n54 + 04-n55. 04-n48 substantially complete — all five cards written with outstanding issues: Signals Analysis (BLOCKED — Art 06.x Classified Directive procedure required); C31 Leveraged Acquisition v1.1 (timing=Upkeep removed; Immediate at Beat 3); C40 Weaponized Transparency retired/split → Card A Reputational Strike (React stub) + Card B Forced Disclosure (PA stub); C41 Corporate Blackmail v1.1 split → Card A spec (Capital coercion) + Card B stub (Accord Leverage, deferred); C42 Sanctioned Raid (block-bypass Art 03 rule deferred; issues clarified).

**S71 accomplishments:** C31 v1.4 — redesigned (2:1 cost, restriction=None, boost field added, Issues Resolved ✓). C40A (Reputational Strike) stub moved to §11.8. C41A Corporate Blackmail v2.0 — ElectPlayer covert choice redesign; target_district added; comply/resist model. C41B Accord Leverage v1.0 — modifier card spec (Instant; Accord draft restriction; Lock manipulation). C42 Sanctioned Raid v2.0 — block-bypass removed; modifier card clearing on success; variable threshold (75−10n); Beat 0 declared count mechanism flagged (04-n71). Art 04 §5: "Data schema validation" added as 14th checklist row (04-n68 ✅). Art 04 §6.1/§6.2/§6.3: `boost: BoostExpr | None` first-class schema field added; 04-34/04-36 superseded. PM05: 04-n69–04-n72 added; 00a-xx → 00a-72 (UNBLOCKED — Art 03 v3.3 cleared gate S68). PM05 full review and prioritization conducted. Signals Analysis still BLOCKED (Art 06.x). C40B and C42 per-token cost open.

**S72 accomplishments (partial — context limit, pending Andy grip review):** 00a full structural review complete. 00a v0.5 draft written — material restructure. Rule count 46 → 30. New §3 (Design Principles for this Artifact) and §4 (Foundational Design Principles) added. Former §7 card design constraints flagged for Art 04 migration. §8 and §9 dissolved — content moved to Foundational Design, Art 03, or redistributed into remaining sections. Rules reorganized into parent→corollary structure throughout. Appendix B migration map written (old ID → new ID sweep guide). 00a-72 status: draft complete, pending Andy review in grip → sign-off → L193.

**S73 accomplishments:** PM05 additions complete: 00a-73, 00a-74, XA-46, XA-47, XA-48 added. PM02 D02a-03 updated (00a §5 migration note on resolution; stale R05 ref → R40b). 00a §1 "What This Document Is Not" rewritten (three categories: §3 design principles / §4 foundational premises / §5–§10 governing rules). 00a §3 fully reordered (logical argument sequence); principles scoped to this document; "Time Convention" → "Copy Design Principle — In-Game Terms in Narrative Fields." 00a §3.1 created — all canonical definitions migrated from PM04 (temporal, component/system, physical forms, faction resources, influence levels); hardcoded values replaced with source artifact references. Art 03 §4 temporal framing removed, pointer to 00a §3.1 added. PM04 §1 collapsed to pointer; Purpose updated; §2 stale refs cleaned. L192 locked (source of truth migration — 00a §3.1 canonical for game definitions). L150 amended (Month 3 "political act phase" retired; all months carry both modes; "Provisional" flag retired). PM05 PM04-06 added (PM04 §2 review). §4 Foundational Design Pillars restructured — 8 numbered pillars (4.1–4.8) with lettered corollaries; subsections: Core Design Pillars (4.1–4.6b), ARBITER Design Principles (4.7–4.7b), Guaranteed Effects (4.8–4.8d). Art 00 §5 design principles (6 pillars) migrated to 00a 4.1–4.6; Art 00 §5 vacated with pointer. Rule numbering changed to section-prefixed n.n format across §5–§10. §5–§10 headers include "Rules." §8 renamed "Footprint Rules"; §3.1 Footprint definition row added. §8 precision edits: 8.2 Mechanics (Absent sentence removed — 8.2b owns it); 8.3 Rule simplified; 8.3a header/rule/mechanics precision fix (displaced markers are repositioned, not simply removed). §9: "upkeep income" clarification; 9.1b added (card/action resources ≠ income). §10: 10.1 Lock B (Reveal effect = stake not compulsion); 10.1a cross-ref 4.7a/4.7b; 10.3 header/rule/mechanics updated (limits + expiry). PM05: 00a-13 (7.3b revision), 00a-14 (Source/Governs audit). 31 rules. 00a v0.6 signed off — **L193**.

**S74 accomplishments:** Art 00 v1.6 signed off (L194) — §5 Art 00 design principles added (5 principles: Derivability, Sustained Ambiguity, World over Mechanics, Attributable Perspective, Narrative Frame); all subsections numbered throughout (§1.1–§14.9). 00a v0.7 signed off (L196) — §3 renamed "Design Principles for This Document" + scope routing note; §4 scope line added; §4.6 amended with Narrative Origin Principle: Art 00 as sole canonical narrative source (L195). Art 01 v2.0 signed off (L197) — Component Physical Forms column → "Proposed Form"; 01-10 (table → Art 02a, add Design Requirements column) and 01-11 (scope overhaul: §8→03-init, §11/§12→downstream) flagged. PM05: 00-15 (Art 00 full narrative revision per §5 P1+P5), 01-10, 01-11, 00a-75 added.

**S75 accomplishments:** XA-47 ✅ — Art 04 §5 P19–P25 added (R21–R28 migrated from former 00a §7); P5 updated (authoritative R26 constraint note); P6 cross-ref to P19; checklist rows updated (Effect duration → P6/P19; Portrait validity → +P22); Art 04 v0.9.34. XA-48 ✅ — Art 07 §9 already had four-register content; `00a R02` source ref removed. XA-46 ✅ — ~120 rule ID substitutions across 11 files (Art 03, Art 04, Art 07, 02a, 02b, PM03, design_reference.md, gap_card_sketches, 3 memory files); zero `00-R` strings remain; PM02 + SESSION_BRIEF preserved as historical records; `00-R29` → `Design Pillar [04-n6 pending]` throughout. PM05: 04-n73 (P1–P18 restatement audit) + XA-49 (design_reference.md reset) added.

**S76 entry point:** XA-49 (design_reference.md reset — before card spec work) → 04-n28 (Overture full spec, gates §11 redesign) → 04-n40 (C28 Network replacement).

**Priority order:** XA-49 (design_reference.md reset) → 04-n28 (Overture, gates §11) → 04-n40 (C28 replacement) → C40B narrative → C42 per-token cost resolution.

**Also pending:** 04-n40 (C28 Network replacement); 04-n44/45/46 (IS-xx Art 03/02a/00b updates — gate: C24 sign-off); 04-n71 (Art 03 Beat 0 boost procedure); 04-n72 (Art 03 covert ElectPlayer procedure); 04-n69/70 (schema sweep); Standing Injunction 5 open flags; agy DB-S63-01/02/03 check-in; 00b/04b re-sign-offs; 04-n73 (P1–P18 restatement audit).

---

## 04-n26 Component Analysis — Full Cluster Map
*Captured S67 mid-session. Read this before any n26 work.*

**Governing principle (Andy S67):** Walk each card individually — components are not automatically needed. Ask whether the card can be reworked to avoid a new component before committing to registration. Only SCIF Record (SR-xx) confirmed as new component so far.

### Cluster A — Process-blocked (new game procedures required)

| Component | Card | Status | Direction |
|-----------|------|--------|-----------|
| SCIFRecord (SR-xx) | Ghost SCIF | ✅ Component confirmed — 00b §4 registration (agy). Art 03 Debrief procedure outstanding (04-n27). | ARBITER slip, not board marker |
| GrantDeed | Syndicate Land Title | ✅ Spec written — registration pending | New component (SCIF-pattern). Blank card in ARBITER tableau; filled + dispatched to Syndicate case at Beat 3. Fields: `district \| owner`. Tracks under 04-n26. |
| ParasiticMarker | Syndicate Parasitic | ✅ No component needed | Positional wager redesigned v2.0. Beat 2 checks Beat 3 queue; Intel keyed to first card's submitter. No marker, no deferred effect. Decision S67. |
| TierPenaltyMarker | Directorate Regulatory Downgrade | ✅ No component needed | Redesigned v2.0 as Permanent PublicAct. Card-on-board IS the condition. Clearing: target pays 2 native to Reservoir. S67. |
| TierFreezeMarker | Directorate Regulatory Freeze | ✅ No component needed | Redesigned v2.0 as Permanent PublicAct. Card-on-board IS the condition. S67. |
| InjunctionMarker | Directorate Standing Injunction | ✅ No component needed | Redesigned v2.0 as Seasonal PublicAct. Card-on-board IS the condition. target_taxonomy field introduced. Art 03 void procedure outstanding (04-n27). S67. |

### Cluster B — Information-state objects (private reveal + visibility)

*Andy S67: Many of these may be taxonomy labels, not physical components. Walk each card before committing to registration.*

| Component | Card | Key Question |
|-----------|------|-------------|
| CardHandContents | C18 Dossier Breach | Is this a physical component or a taxonomy subject label? Ghost reads hand — no physical object changes hands. |
| ActionAttribution | C19 Deep Cover, C26 Leak | Concept of "who did the action" — is this a component or a record in ARBITER's ledger? |
| ClassifiedDirective | Ghost Signals Analysis | IS a physical component — the faction's secret objective card. Likely already registered or easily registered. |
| WrittenRecord | C23 Evidence Preservation | Locks an existing record (Intel token, Accord). May not need separate registration — acts on existing components. |
| PrivateCommunications | C28 Open Channel | Scope undefined: which ARBITER-to-faction comms qualify? Intel Delivery Slips and Notification Slips confirmed in scope. |

### Cluster C — Taxonomy mismatch

| Component | Card | Fix |
|-----------|------|-----|
| SurveillanceDevice | C24 Surveillance Placement | `subject = IntelToken` is wrong — primary effect is surveillance infrastructure. Needs `subject = SurveillanceDevice` once a SurveillanceDevice component is defined. Design SurveillanceDevice before fixing subject field. |

### Standing Injunction open flags (under 04-n26)
1. Restriction wording: "Directorate Established+ in any district where target also has Established+" — confirm intent vs. original "same ring as primary operations"
2. InjunctionMarker: component registration
3. PA type declaration: by card name or by taxonomy (e.g., Territory/Add)?
4. Art 03 gap: Phase B procedure for voiding a declared PA not specified
5. Accord overlap: does PA block apply to Accord-type PAs (P08/P10)?

**ALWAYS read `TheSignal/Whiteboard/design_reference.md` before any Art 04+ design work.**
**ALSO read `TheSignal/Whiteboard/gap_card_sketches_S62.md` before any Art 04 gap card work.

## In-Progress Artifacts

| Artifact | Version | Open Item |
|----------|---------|-----------|
| 00 — Factions, World & Narrative | 1.6 | ✅ Signed Off — S74 (L194). §5 Art 00 design principles added (5 principles). Subsections numbered §1.1–§14.9. Open: 00-09 (World Conditions panel); 00-15 (full narrative revision per §5 P1+P5). |
| 00a — Governing Rules & Design Policy | 0.7 | ✅ Signed Off — S74 (L196). §3 renamed + scope routing note; §4 scope line; §4.6 Narrative Origin Principle (L195). 31 rules. Open: 00a-73 (7.3b revision), 00a-74 (Source/Governs audit), 00a-75 (Derivability principle documentation). |
| 01 — Game Board: New Meridian | 2.0 | ✅ Signed Off — S74 (L197). §6 Component Physical Forms column → "Proposed Form". Open: 01-10 (table → Art 02a); 01-11 (scope overhaul §8/§11/§12). |
| 02a — Resource Systems: Board State | 1.6 | ✅ Signed Off — S42. |
| 03 — Quarter Structure & Gameplay | 3.3 | ✅ Signed Off — S68 (L189). §19 Debrief Actions step (DebriefActionCard type); §25 updated (cross-refs §28); §28 React Card Rules added (interrupt model). |
| 04b — Action Taxonomy | 1.6 | ✅ Signed Off — S48. S64: §5.2 +5 rows (Disinformation Campaign, Standing Injunction, Disprove, Intel Extraction, Modifier Raid). 04-63 flagged (stale C27 §4.6 entry). |
| 04 — Action Card System | 0.9.34 | S75: §5 P19–P25 added (card design constraints migrated from 00a §7 — effect duration types, partial payment, crit cost, portrait card property, ring modifier scope, corrupt scope, standard language). P5 updated (authoritative R26 constraint). P6 cross-ref P19. Checklist rows updated. XA-46 rule ID sweep applied. S71: C31 v1.4. C41A v2.0. C41B v1.0. C42 v2.0. §6 boost field. Signals Analysis BLOCKED (Art 06.x). C17 ⚠ re-sign-off pending (04-n50). |
| 00c — Economy Manifest | 0.4 | §8, §9 stubs only. |
| 03a — Game Engine Specification | 0.98 | Tier 4 stub remaining. XA-37 pending (strip "Layer N —" prefixes from section headings). |
| 07 — ARBITER Toolkit | 0.1 | Initiative procedure (03-11) + initial draft pending. |

Signed-off artifacts: 00b (v0.2), 01 (v1.9), 02b (v1.5), 03 (v2.0), 04b (v1.2 — 04b-03 audit pending). Authoritative: PM03.

---

## Active PM05 — Top Items

| ID | Item | Status |
|----|------|--------|
| **00-07** | Art 00 multicultural texture pass | ✅ S40 |
| **00a-08** | 00a v0.3 re-sign-off | ✅ S40 |
| **01-05** | Art 01 overhaul — physical zone hierarchy, all Overview children | ✅ S40 |
| **04-54** | Art 04 §5 P1–P15 signed off + C17 signed off | ✅ S49 |
| **XA-37** | Haiku sweep: rename Ln/Layer N expansion tier refs → Tier N across 00b, 00c, 03a, Art 07–11; strip "Layer N —" from 03a section headings | ✅ S49 |
| **DB-22–26** | agy S48+S50 DB fixes — upkeep primitives, Status marker, Portrait marker, SitRep/Target Profile, Move mismatch | ✅ S50 (agy) |
| **DB-27** | agy: register Emergency Response card id=97 in tmp_component + seed role/beat primitives | ✅ S50 (agy) |
| **DB-09** | Create district_adjacency table — ✅ S50 (agy). 21 districts, 104 adjacency rows seeded. | ✅ S50 |
| **DB-11** | agy ALTER TABLE component_positions — rename anchored_to_component_id → on_component_id + add on_game_zone_id | ✅ S46 (agy) |
| **03-14** | Art 03 v2.1 sign-off — Beat 3/4 outcome steps restructured (7a/7b/7b.i); L170 locked | ✅ S52 |
| **01-07** | Art 01 §4 Narrative Function — remove (content in §3 + Physical Table Layout) | ✅ S41 |
| **01-08** | Art 01 narrative anchor pass — staged in Whiteboard/Art01_Narrative_Anchors_S41.md | Open — after 02a sign-off |
| **08-00** | Art 08 — define scope + create stub (Faction Player Tableau + ARBITER Tableau) | Open |
| **03-12** | Battlefield Strength trigger model | ✅ S43 — L160 |
| **04-48** | Art 03 v2.0 sign-off | ✅ S43 |
| **01-06** | Claude Design visual wireframe — table layout + mat layout | Open |
| **04b-03** | Action taxonomy audit | ✅ S46 — §4 redesigned, pending sign-off |
| **04b-04** | Art 04b §3 cleanup — update stale verb refs (Block→Flip, Redirect→Move, React reclassification); prerequisite to v1.3 sign-off | Open — S46 |
| **DB-11** | agy ALTER TABLE live_state rename | ✅ Confirmed executed agy S46 |
| **DB-14** | Decision — promote tmp_ taxonomy tables to permanent the_signal_db schema | Deferred — after 04b sign-off |
| **XA-32** | Art 07 — ARBITER ring modifier calculation guide | Open |
| **GEM-01** | Cross-reference integrity audit — assigned to Gem | Active — deploy via 3-file upload |
| **PM06-01** | Create PM06 — Lessons Learned | Deferred — next session |
| **00-09** | World Conditions panel — content undefined | Open |
| **00-10** | Faction Representative as named component — design question | Open |
| **FS-01-WBS** | Add faction screen to PM01 WBS 2 | Open |
| **04-n10** | Pentagram gap — Ghost↔Guild opposed pair has no card-level expression | Open — P-series pass |
| **04-n11** | Pentagram gap — Guild↔Network neighbor pair has no cooperative mechanic | Open — P-series pass |
| **04-n12** | Faction Terminal unique zone design direction (L183) — define per-faction named zones in Art 08 | Open — Art 08 |
| **04-n13** | Network modifier card — auto-trigger off C42 Sanctioned Raid sweep | Open — modifier card pass |
| **04-n14** | C32 Short the Market — mechanical redesign required ("applied silently" doesn't survive paper prototype; tagline/code conflict on generation vs stockpile) | Open — redesign pass |
| **04-n15** | Standard equivalents for Source Substitution, Backdate, Field Verification — hired data specialist / PI versions; higher cost or lower threshold (Principle 17) | Open — S62 |
| **04-n16** | Apply Principle 17 systematically — audit full card set for faction-native capabilities lacking outsourced standard counterparts | Open — S62 |
| **04-n17** | Gap card specs: Disinformation Campaign ✓, Standing Injunction ✓, Disprove ✓, Intel Extraction ✓, Modifier Raid ✓. Standing Injunction 5 open flags → tracks under 04-n26. | ✅ S64 |
| **04-n18** | Art 04b §5.2 refresh complete (artifact side). agy DB cascade outstanding (DB-S63-01/02/03 queued). | ✅ S63 (agy pending) |
| **04-n19** | Accord procedure design pass (Art 06) required before Group A gap cards. After 04-n27 (Art 03 gaps). | Blocked — after 04-n27 |
| **04-n20** | Directorate covert reclassification — review C21 Invoke Jurisdiction, C22 Detain, C23 Evidence Preservation, C25 Tactical Redirection, C42 Sanctioned Raid for PA reclassification | Open |
| **04-n23** | P09–P18 Voice fit gap — 20 perspectives written. Gates Issues Resolved ✓ for all P09–P18. | ✅ S63 |
| **04-n25** | CRITICAL — Art 04 §6 schema field gaps: `target_ring`, `pre_loss_calc`, PS-as-cost | Critical — S65 |
| **04-n26** | HIGH — Component interaction design pass: 12+ components needing lifecycle design before Art 02 registration | High — S65+ |
| **04-n27** | HIGH (before accord) — Art 03 procedure gaps: 6 holes blocking Issues Resolved on multiple cards | High — S65+ |
| **04-n28** | Art 06 Accord design — §9 signed off (L191). Overture stub in §11.8. Remainder: Overture full spec (gates §11 redesign). | 🟡 Substantially complete — S69 |
| **XA-46** | 00a rule ID sweep — all 11 files. | ✅ S75 |
| **XA-47** | Art 04 §5 P19–P25 added (card design constraints from 00a §7). | ✅ S75 |
| **XA-48** | Art 07 §9 ARBITER Registers already had content. Source ref cleaned. | ✅ S75 |
| **XA-49** | design_reference.md reset — review before Art 04 card spec work resumes. Gate: before 04-card-spec. | Open — S76 |
| **04-n73** | Art 04 §5 P1–P18 restatement audit — identify and replace upstream duplicates. | Open — S75+ |

→ Full list: `V1/PM05___Active_Punch_List.md`

---

## Last 3 Locked Decisions

- **L197** (S74): Art 01 v2.0 signed off. §6 Component Physical Forms column → "Proposed Form" (non-binding, not material spec). Open: 01-10 (table → Art 02a + Design Requirements column); 01-11 (scope overhaul — §8→03-init, §11/§12→downstream).
- **L196** (S74): Art 00a v0.7 signed off. §3 renamed "Design Principles for This Document" + scope routing note. §4 scope line added. §4.6 amended: Art 00 as origin of all canonical narrative (L195).
- **L195** (S74): Art 00 as sole canonical narrative origin. No canonical narrative may originate in a downstream artifact. Art 00 amended first; downstream artifacts reference it. Written to 00a §4.6. Governs all V1 artifacts.
- **L194** (S74): Art 00 v1.6 signed off. §5 Art 00 design principles added (5 principles). §11 term table → 00a §3.1 pointer. Subsections numbered §1.1–§14.9.
- **L185** (S65): Art 03 v3.1 signed off. Golden Parachute bribe mechanic written to Beat 0/2/3. Art 04 §6.2 cost field (fungible only). §6.6 added (pre_loss_calc). C37 Sacrifice + C34 Golden Parachute redesigned.
- **L184** (S63): L108 amended — 3NF requirements (6 + 7) added; component.transformable → virtual generated; action.prereq_beat_id dropped.
- **L183** (S61): C22 Detain — detention zone on Directorate public tableau; faction Terminals may be unique per faction doctrine.
- **L182** (S61): Art 00a v0.4 signed off. 00-R21 (4-type duration taxonomy), 00-R22 (partial payment model), 00-R29b (Missing Author Vacuum renamed from duplicate 00-R30), 00-R39 (covers covert ops + public acts). 43 rules.
- **L181** (S61): Art 03 v3.0 signed off. Beat 3 Step 12 cleaned; Beat 4 Submit Payment → Step 1, steps renumbered 1–13; section breaks added; duration taxonomy 5→4 types.

*S62 design decisions (not locked — draft pass only): PA persistence policy; Territory/Recover removed from valid taxonomy; Copy/PA no narrative value; Principle 17 (outsourced equivalents); Accord procedure prerequisite for Group A gap cards.*

→ Full log: `V1/PM02___Decision_Log___Validation_Tracker.md` (L01–L175)

---

## Pending Sign-Offs

- **Art 00 v1.6** — ✅ Signed Off S74 (L194)
- **00a v0.7** — ✅ Signed Off S74 (L196)
- **Art 01 v2.0** — ✅ Signed Off S74 (L197)
- **02a v1.6** — ✅ Signed Off S42
- **Art 03 v3.3** — ✅ Signed Off S68 (L189)
- **C17** — ⚠ v1.1 pending re-sign-off (beat=2 correction S70 — tracked 04-n50)

---

## Key Concepts Established S39–S40 (Not Yet in All Artifacts)

- **MIRROR** = Meridian Interface for Real-time Reporting, Observation, and Recording. Holographic projection device at Chorus Node. Predates The Table and possibly ARBITER. Origin of "New Meridian" name. Written to Art 00 §8.
- **Zone vs. Component distinction** = Zones are named physical locations (infrastructure); components are portable objects placed within zones. Central Area is a zone; The Overview is the component that fills it. Established S40 — in Art 01 §6 Physical Environment.
- **district_adjacency** = bidirectional adjacency table for all 21 districts. In Art 01 §[City]. DB table needed (agy). Feeds Entry Rule A/B and Battlefield Strength (03-12).
- **component_positions** = renamed from live_state (S45). Spec in 00b §8. DB-11 queued for agy: RENAME TABLE, RENAME COLUMN anchored_to_component_id → on_component_id (nullable), ADD COLUMN on_game_zone_id.
- **Art 08** = new planned artifact for Faction Player Tableau and ARBITER Tableau physical component placement. Referenced in Art 01 §8–§9 stubs. Not yet defined.
- **Force-reveal action class** = actions compelling faction to expose Terminal contents. L154. Design direction for Art 04 card design.
- **Faction Terminal unique zones** = L183. Terminals may have named zones per faction doctrine. Directorate: public Detention zone (C22). Others TBD — develop in Art 08.

---

## Key Files

| File | Purpose |
|------|---------|
| `Session/THE_SIGNAL___Project_Save_State.md` | Full session history, complete artifact table |
| `Session/PRIVATE___True_State.md` | Read before writing ARBITER or Chorus content |
| `Whiteboard/Art01_Scope_S39.md` | Physical layout decisions from S39 — migrate to Art 01 during overhaul |
| `V1/PM02___Decision_Log___Validation_Tracker.md` | All locked decisions |
| `V1/PM03___Master_Artifact_Index.md` | Authoritative sign-off status, dependency map |
| `V1/PM05___Active_Punch_List.md` | Full punch list |
| `gem_task.md` | Active Gem task — edit this to assign new work; script copies to Desktop |

---

## Terminology

| Use | Not |
|-----|-----|
| Quarter | Round |
| The Overview | Game mat / board |
| MIRROR | (device name — use in narrative context) |
| Terminal | Faction tableau / personal board |
| Presence token | Influence token |
| Deployment marker / Operational marker | Claim marker |
| Public Standing track | Popularity track |
| Covert operation | Private action |
| Public act | Political act / Public action |
| Situation report | World event card |
| The Mid | Infrastructure ring |
| Baryo | Sprawl |
| The Backlog | Reservoir (for Dispatch Tokens) |
| Session Timeline | Round Tracker / Quarter Tracker |

ARBITER: always all-caps. All other game terms: Title Case.

**Four Registers** (Art 00 §9, Art 07 §9): The Record · The Observation · The Reckoning · The Witness

---

## Standing Methodology (Established S39)

**Foundational-first:** Foundational artifacts must be complete and signed off before downstream work proceeds. Gaps in upstream documentation propagate as inconsistencies throughout the artifact tree. Dependency order is the work order: 00 → 00a → 01 → 02a → 03 → 04.

---

---


*Updated S39 Phase 1 close. Sources of truth: PM03 (artifacts), PM02 (decisions), PM05 (punch list).*
