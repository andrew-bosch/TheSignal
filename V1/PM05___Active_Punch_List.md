# PM05 — Active Punch List
## THE SIGNAL P1 — Paper Prototype

**Version:** 2.1
**Status:** 🔄 Active
**Last Updated:** 2026-05-19
**Extracted from:** PM02 §2b as of session 10

---

## Purpose

Living action queue of all changes that need to be incorporated into existing artifacts — including signed-off artifacts, in-progress artifacts, and the PM documents themselves. Items are removed when the change has been applied and verified. When this list is empty, the project's working documents are fully consistent with all design decisions made to date.

**How to use this list:**

- Items marked 🔄 are pending incorporation
- Items marked ✅ are complete — kept for audit trail
- Each item references the source decision or discussion that generated it
- "Non-material" items are discussion points and clarifications that don't alter mechanics but should be captured in the relevant artifact

**Blocking hierarchy:** READY NOW items → 00a sign-off → D02a-01 → Artifact 03 re-sign-off → Artifact 04 completion → Artifact 05+ completion.

---

## Section 1 — Pending Changes by Block

### READY NOW

Items with no blocking dependencies. Can be executed in the current working session or the next one, independent of 00a sign-off or D02a-01 resolution.

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 00-01 | No pending changes to Artifact 00 itself — governing rules extracted to Artifact 00a. | — | — | ✅ |
| PM02-01 | No pending changes — all updates applied in v1.3. | — | — | ✅ |
| XA-18 | **Italic commentary convention — scan and revise all artifacts.** Apply L96 copy design convention across all documents: in procedural sections, explanatory/commentary text (why, context, edge case flags) is italicised and separated from action text by a CR. Scope: Artifact 03 (apply during current review), Artifact 07 (apply during 07 review), any artifact with procedural steps or rules text. Non-material — no mechanics change. | Non-material (style) | L96 | ✅ Session 11 — Artifact 03 done (session 9). Signed-off artifacts (00a, 02a, 02b) audited: structure is tabular/rules-field-based, not step-sequence — L96 not applicable. Artifact 07: deferred to 07 active development (placeholder has no stepped procedures). Full scope complete for current artifact set. |
| PM03-02 | Add code block formatting standard to PM03 §1 document formatting standards. Principle: fenced code block (```) is the standard for schematic/overview content — any structured at-a-glance summary that functions as a map or diagram rather than prose. Include: when to use, when not to use, and example reference (Artifact 03 §6 Round Overview). | Non-material | L95 | ✅ Applied session 10 overnight |
| 04b-02 | §3.9 — update "Flag for PM03 — Future Phases" to "Flag for PM04 — Future Phases" (one reference, non-material rename). | Non-material | PM03 rename | ✅ Applied session 10 overnight |
| 07-02 | Beat 2 name update in any ARBITER script references — "Defenses Hold or Fall" → "The Ground Shifts." | Non-material | L49 | ✅ Applied session 10 overnight — Artifact 07 §8 was a placeholder with no prior named Beat 2; new "Beat 2 — The Ground Shifts" subsection added with canonical name and full scope (C06, C07, C10, C11, C21, C25, C28, C34, C35) |
| XA-30 | **Compound effect text — flag as known L108 gap in Artifact 00b §8.** L108 Requirement 1 (no compound cells) is violated by multi-effect prose strings in all Effect on success fields (e.g., C01 places a structure AND generates upkeep resource — two distinct effects in one text string). The taxonomy triple (Category/Function/Subject) is the correct decomposition model — but decomposing effect fields into typed sub-components (effect type, quantity, target, condition) requires content to be locked first. Action: add a flagged entry to 00b §8 (Design Notes & Known Gaps) documenting this as a known L108 violation, deferred until card content is locked. Non-material — no mechanics change. | Non-material (gap flag) | Session 23 research, L108 | ✅ Session 28 — gap note confirmed present in 00b §8 (compound effect text, L108 Req 1 violation, defer until card content locked). |
| XA-29 | **Component Terminology Cleanup — L109.** Scan all V1 artifacts for bare or unqualified component references and replace with canonical in-game terms (L109). Art 03 is already clean (fixed session 20). Remaining scope: 00, 00a, 01, 02a, 02b, 04, 04b, 07, 08, 09, 10, 10a, 11, PM01. Known terms to enforce: presence chip (not "chip" or "token" alone), deployment marker, operational marker, structure block, intel note, dispatch case, Situation Report (not "event card" in player-facing copy), Operation Resolution card, status marker, initiative strip, Findings token / [Faction] resource token. Cross-check each find against PM04 §1 canonical term before replacing. **Queued for unsupervised/overnight execution.** Non-material — no mechanics change. | Non-material (L109 terminology) | L109, Session 20 | 🔄 |
| PM04-04 | **Add Component Terminology Standard to PM04.** (1) PM04 §2 — add L109 Component Terminology Standard: canonical in-game term must be used for every physical component in all artifacts; bare or generic terms (chip, token, card, block, marker without qualifier) are non-compliant. (2) PM04 §1 — add Component Physical Glossary: table mapping each in-game component name to its physical/real-world description (e.g., presence chip → small coloured disc or poker chip; structure block → wooden cube; deployment marker → double-sided cardboard chit; intel note → small slip; dispatch case → sealed envelope or small box). Expand as new components are defined. | Non-material (PM standard) | L109, Session 20 | 🔄 |
| PM04-05 | **Document schema document vs. data table distinction in PM04 §2.** Session 26: Andy clarified that §6 Card Data Schema is a column specification document, not a data table — L108's primary key requirement does not apply to it. This distinction needs to be formally documented so future schema documents are correctly categorised. Add to PM04 §2 alongside L108 standard: definition of "schema document" (describes data structure; L108 PK requirement exempt) vs. "data table" (contains data records; L108 fully applies). Cross-reference: 00b §3 (L108 compliance standard). | Non-material (PM standard) | L108, Session 26 | ✅ Applied PM04 §2 session 27 — "Data Document Types" subsection added. PM04 v0.6. |
| XA-28 | **L108 compliance audit — all existing data tables.** L108 (Database Translatable Data Design) applies retroactively to every data table in the artifact suite. Known tables requiring audit: (1) Artifact 04 §6 card data structure (21 fields — check for compound cells, confirm typed columns, add card ID as explicit primary key reference); (2) Artifact 00a rule table (R01–R38 + sub-rules — confirm ID column is unique primary key, check for compound Governs/Source cells); (3) Artifact 02b Public Standing table and Portrait track tables — check for compound cells; (4) Artifact 01 district records (if structured as a table) — confirm district ID is a primary key; (5) PM01 WBS 2 component table — confirm ID column, check for compound cells; (6) Any table introduced in future artifacts (07, 09, 10a) must satisfy L108 at design time. Priority: address during each artifact's active design session rather than as a separate pass. Flag violations in each artifact's PM05 entry when found. | Non-material (compliance) | L108 | 🔄 |
| PM04-03 | **Add table design standards to PM04 §2 — Category column pattern and L108 (Database Translatable Data Design).** Two principles established session 20: (1) Category column pattern — any reference table with multiple data types in a single column uses a leading Category column (first applied: §14 Difficulty Modifiers); (2) L108 — all data tables must satisfy five database-translatable requirements: single-typed columns, controlled vocabulary, explicit primary key (ID column), ID-based cross-references, explicit null/N/A. Add both to PM04 §2 alongside code block standard (L95) and italic commentary (L96). Non-material. | Non-material (style standard) | Session 20, L108 | 🔄 |
| PM01-01 | Reference convention documented in PM01 §3. Audit all signed-off artifacts (00, 01, 02a, 02b) to confirm existing cross-references use [Artifact].[Section].[Subsection] format. Update any non-conforming references. | Non-material | PM01 §3 | 🔄 Partial — session 10 overnight: 1 fix applied (01 line 306: "Artifact 02" → "Artifact 02a"). Many informal cross-references lack section numbers, most pointing to incomplete artifacts (07, 10a, 06, 11) — section numbers cannot be added until those artifacts are complete. Full pass deferred to post-04 sign-off. |
| XA-01 | Update PM03 §3 Design Artifact Registry to correct version numbers. Artifact 01 listed as v1.0 (actual: v1.2); 02a listed as v1.0 (actual: v1.2); 02b listed as v1.0 (actual: v1.5); 00a listed as v0.1 (actual: v0.2). | Non-material | PM (Audit) PM03-IQ-01 | ✅ Verified session 10 overnight — version numbers were already correct; no edit required |
| XA-02 | Update PM03 §1 Narrative Language table — change "Hex / board space" to "Board space" (or simply "Space"). Artifact 01 §6 explicitly states New Meridian is a non-hexagonal map; the terminology table should not imply a hex grid. | Non-material | PM (Audit) 01-IQ-01, PM03-IQ-02 | ✅ Applied session 10 overnight — "Hex / board space" → "Board space" in §1 terminology table |
| XA-03 | Update Artifact 11 §6 faction colors to match Artifact 00 §7 canonical values: Ghost = Charcoal green; Network = Bright signal green; Syndicate = Metallic gold; Guild = Industrial orange; Directorate = Deep institutional blue. Note Ghost/Network green adjacency as an open question for Artifact 11 design pass. | Non-material | PM (Audit) XA-IQ-02 | ✅ Verified session 10 overnight — colors already correct in Artifact 11 §6; Ghost/Network green adjacency flag note added |
| 00a-06 | Audit all rule Narrative fields in 00a for invented district names not present in Artifact 01's district map. R17 "Warehouse District" corrected to "Industrial Fringe" in session 5. Other rules may reference generic district descriptors that should resolve to actual named district names. | Non-material | 00a §11 A09 | ✅ Audited session 10 overnight — all 38 Narrative fields checked; R17 prior correction confirmed in place; no additional invented district names found |
| 00a-07 | Full narrative grounding audit is complete as of v0.2 — all 45 rules carry Rule / Narrative / Mechanics / Source / Governs structure. Mark 00a §11 A08 as complete. | Administrative | 00a §11 A08 | ✅ Applied session 10 overnight — A08 marked complete in 00a §11 |
| XA-17 | **Subheader spacing style — apply to all artifacts.** Style standard confirmed session 9: a blank line (CR) between every bold or italic subheader and the copy that follows it. Applied to Artifact 03 session 9 (54 bold subheaders corrected + 2 italic subheaders in Beat 5). All other artifacts require the same pass — particularly 00a (rules block), 02a, 02b, and 04 which use the same bold subheader pattern extensively. Scope: non-material style pass on all documents. | Non-material (style) | Session 9 style standard | ✅ Applied session 10 overnight — 24 violations corrected: 1 in 00a, 10 in 02a, 0 in 02b (already compliant), 13 in 04 |
| XA-16 | **Systematic terminology scan** — one-pass audit of all artifacts for stale or non-canonical terms, replacing with the locked narrative language from PM04 §2 and 00a §6. Priority targets: (1) "bank" → "Reservoir" — all artifacts (03 corrected session 8; others unchecked); (2) "round" → "quarter" — any remaining violations outside Artifact 03; (3) "mat" → "The Overview"; (4) "modifier cards" → pending D04-07 in-world name once resolved; (5) any influence level terms not yet updated (Dominant/Established/Present/Contested confirmed; check for legacy "Claim" or "Control" references); (6) "markers" → confirm against PM04 §2 canonical component names. Scope: all artifacts including signed-off documents. Non-material if only replacing with locked canonical terms. Material if any instance requires context-sensitive judgment. | Non-material (scan) | 00a Copy Design Principle, L86, PM04 §2, session 8 bank→Reservoir fix | ✅ Session 11 — (2) "round"→"quarter": applied across 02a, 02b, 07, 08, 09, 10 (mathematical uses preserved: round down/up/toward); session 15 — applied to Artifact 03 (all instances; Round Tracker and Round Structure preserved); (3) "mat"→"The Overview": applied in 10, 11; (5) "Claim"/"Control" scanned — all instances are legitimate uses, no stale legacy terms; (6) markers verified against PM04 §2: Operational/Deployment/Tension/Control flag all in use per current design decisions. Target (4) remains open — blocked by D04-07. |
| PM02-02 | **Collapse PM02 §2b archived snapshot.** PM02 §2b currently contains ~250 lines of archived punch list table below the pointer to PM05. Replace the archived table with a single-line note: *"Archived as of session 10 — see PM05 §1 for the live punch list."* Non-material — no content is lost (all items are in PM05). | Non-material (cleanup) | Session 11 PM suite gap audit | ✅ Applied session 11 — 244 lines collapsed to 1-line archive note. |
| PM04-02 | **Populate PM04 §1 from Save State In-World Glossary.** The Save State glossary contains canonical in-world term → mechanical meaning mappings. Migrate these entries into PM04 §1 (In-World Data Dictionary) and replace the Save State glossary section with a pointer to PM04 §1. Does not require 00a sign-off — this is the unblocked portion of PM04-01. The 00a §1 Time Convention portion remains tracked under PM04-01 (BLOCKED BY: 00a SIGN-OFF). | Non-material (migration) | Session 11 PM suite gap audit, PM04-01 split | ✅ Applied session 11 — PM04 §1 populated with 3 tables: Component & System Terms (17 entries), Faction Resources (5 entries), Influence Levels (4 levels). PM04 updated to v0.3. |
| XA-20 | **"the ARBITER Player" / "the Faction Player" capitalization scan — all artifacts.** "the" is an article, not part of the term — capitalize only when it is the first word of a sentence, bullet item, or clause following a colon. Mid-sentence uses after commas, em-dashes, prepositions, and conjunctions must be lowercase. First applied in Artifact 03 session 15. Scope: all artifacts. Non-material. | Non-material (style) | Session 15 | ✅ Session 17 — 5 corrections in 00a (lines 89×2, 196, 200, 588); 00, 01, 02a, 02b, 04, 04b, 07, 08, 10, 10a confirmed clean. |
| XA-19 | **Reception language scan — apply Reception Language Convention to all artifacts.** The Chorus is described from humanity's vantage point in all Narrator prose. "First received" not "first transmitted." "Humanity has been receiving the Chorus" not "the Chorus has been transmitting for X years." Convention documented in PM04 §2. Artifact 00: three corrections applied session 12 (lines 138, 144, 184). Scope: 00a, 02a, 02b, 03, 07, 08, 09, 10, 10a, PM documents, CREATIVE_BRIEF.md. Non-material — convention correction only. Faction voice summaries may retain transmit-framing where it reflects the faction's own framing, not the Narrator's authorial voice. | Non-material (scan) | PM04 §2 Reception Language Convention, session 12 | ✅ Session 14 — 7 corrections applied: 02b §3 ("Chorus Portrait" description), Artifact 03 §1 (quarter framing bullet), PM04 §1 Temporal Conventions table, Artifact 00 §6 ("when the Chorus was first received"), PM02 FD-05 (station crew description), CREATIVE_BRIEF §3 (Chorus Node description), CREATIVE_BRIEF §10 (character type list). 00a, 02a, 07, 08, 09, 10, 10a: clean. Faction-framed instances in Artifact 00 §6 (Guild/Ghost interpretive framings) and CREATIVE_BRIEF retained per convention. |

---

### BLOCKED BY: 00a SIGN-OFF

Items that require Artifact 00a to be reviewed and signed off before they can be executed.

*00a current state: v0.2 **Signed off session 7** — 41 rules (R01–R38 + R13a, R13b, R29a), §3–§9, Appendix A. Items in this section are now executable — the 00a sign-off gate has cleared. They remain here rather than READY NOW because each requires either re-sign-off of a downstream artifact or a deliberate review pass rather than a simple mechanical edit.*

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 00a-01 | Complete review and sign off Artifact 00a — Governing Rules & Design Policy. | Material (sign-off gate) | L84, all sessions | ✅ Signed off session 7 — 41 rules (R01–R38 + R13a, R13b, R29a), §3–§9, Appendix A added. |
| 00-05 | Migrate narrative anchors from 00a to a new section in Artifact 00. Anchors to migrate: Presence & The Holt Index (00a §5); Structure Blocks (00a §5); What a Card Is (00a §7). The Overview anchor (00a §4) is not yet written — when written, it should go directly into Artifact 00. Decision: narrative anchors are world content and belong in Artifact 00; 00a carries rules and their mechanical justifications only. Content remains in 00a until migration to avoid loss. Requires re-sign-off of Artifact 00 and corresponding 00a cleanup (remove anchor text, add cross-references to Artifact 00 in Narrative: fields). | Material | L85, 00a §1 Rule Structure Principle | ✅ Session 11 — §14 Narrative Anchors added to Artifact 00 (four anchors: Presence & The Holt Index, Structure Blocks, Deployment Markers, What a Card Is). 00a §5/§7 anchor texts replaced with cross-references. **Artifact 00 requires re-sign-off (material change).** |
| 00-02 | Add Narrative and World Consistency as a design pillar to Artifact 00 §5. Currently 5 pillars; this adds a 6th (or amends an existing pillar). Captured in 00a Governing Principle section pending this formal addition. Requires re-sign-off of Artifact 00. | Material | 00a Governing Principle, PM (Audit) 00-IQ-02 | ✅ Session 11 — Design Pillar 6 "Narrative and World Consistency" added to Artifact 00 §5. 00a §1 Governing Principle updated to reference Artifact 00 §5 pillar. **Artifact 00 requires re-sign-off (material change).** |
| 01-02 | Confirm Artifact 01 carries the global convention: "at least 1 presence token" includes claim markers. Add a design note or definition if not already present. | Non-material | L58, F-ART02A-01 | ✅ Session 11 — canonical global definition annotation added to 01 §6 operational markers text. |
| 02a-01 | Add explicit global convention definition: "At least 1 presence token" on any card includes claim markers. This is the canonical definition — not restated on individual cards. | Non-material | L58, F-ART02A-01 | ✅ Session 11 — Global Presence Convention section added to 02a §6. |
| 02a-02 | Update influence level descriptions to reflect presence token narrative anchor — tokens represent the felt weight of faction power in a district, not physical people or assets. Dominant, Established, Present should each be described in terms of what a person walking into the district would experience. | Non-material (narrative) | 00a §5 narrative anchor | ✅ Session 11 — Holt Index narrative descriptions added to Dominant, Established, Present in 02a §6. |
| 00a-02 | Confirm 00a §11 A01: update Artifact 04b §4 and §6.1 to retire Cross-Category — Shift — Chorus Portrait as a valid player-facing taxonomy function (L84, 00-R44). Execute as part of 04b review once 00a is signed off. | Material | 00a §11 A01, L84 | ✅ Session 11 — 04b §4 Shift row updated (Chorus Portrait struck through, retirement note added). §6.1 Chorus Portrait row retired with Ghost doctrine gap noted. P17 in §5 Card Index flagged for redesign. **04b requires re-sign-off (material change).** |
| 00a-03 | Confirm 00a §11 A03: Artifact 02b §3 describes Portrait as something "ARBITER may adjust in response to any action" — add explicit cross-reference to 00-R01. Non-material. | Non-material | 00a §11 A03 | ✅ Session 11 — (per 00a R01) cross-reference added to 02b §6 What Portrait State Produces. |
| 00a-04 | Confirm 00a §11 A04: Artifact 03 §12 (Beat 3 Step 12, Beat 4 Step 9) references "ARBITER privately updates Portrait track" — verify these survive 00a sign-off unchanged and are consistent with 00-R01. | Non-material | 00a §11 A04 | ✅ Session 11 — verified: Artifact 03 §12 Beat 3 Step 12 and Beat 4 Step 9 reference ARBITER-managed Portrait updates, consistent with 00-R01. No edit required. |
| 00a-05 | Confirm 00a §11 A05: the Chorus Node Portrait Multiplier (02a §10) — confirm ARBITER applies the multiplier, not the faction. Update 02a §10 if the current language implies faction-administered application. | Material (if ambiguous) | 00a §11 A05 | ✅ Session 11 — verified: 02a §10 explicit language states ARBITER applies multiplier. No edit required. |
| XA-04 | Add cross-reference in 00a (§3 or §10) and 02b §6: Portrait ranking is used by ARBITER to determine initiative order each round per Artifact 03 §7. Currently this mechanic exists only in Artifact 03 — designers reading only 00a and 02b would not know Portrait determines initiative. | Non-material | PM (Audit) 02b-IQ-01 | ✅ Session 11 — initiative order cross-reference added to 02b §6 What Portrait State Produces. |
| XA-05 | ~~Clarify "The Record register" vs. three narrative registers in Artifact 07 §9.~~ **RESOLVED (L87):** Four registers locked — The Record, The Observation, The Reckoning, The Witness. The Record is NOT the same as "Procedural." Artifact 07 registers (Procedural/Advisory/Reactive) are outdated and require full replacement with the four-register system. Artifact 07 update required before 07 sign-off. | Material | PM (Audit) 03-IQ-01, L87 | ✅ Session 11 — Artifact 07 §9 fully replaced with four-register system. §5 Principle 2, §4, §7.1, §8.1 updated. Artifact 00 §9 updated to four registers. 00a R02 Rule statement corrected. **Artifact 00 requires re-sign-off (material change). Artifact 07 is a Draft Placeholder — was never signed off; no re-sign-off applicable; will sign off when full draft is complete.** |
| 04-05 | Migrate Card Design Principle — Doctrinal Traceability to Artifact 04 early sections (§1 or principles block). Content: every faction-specific card must pass two tests — mechanical (only this faction would do this) and narrative (only this faction would say it this way). If either fails, the card belongs to no one. Doctrinal anchor must be traceable to Artifact 00 §7. Source: Artifact 04 Principle 7, reclassified from 00a R29 during 00a review. Placeholder cross-reference left in 00a §7 pending migration. | Non-material (migration) | Artifact 04 Principle 7, 00a §7 | ✅ Session 11 — Principle 7 expanded to full Doctrinal Traceability two-test framework in 04 §5. Source: 00a R29. |
| PW-04 | Prioritize PM04 population (PM04-01) before continuing artifact review. PM04 is foundational to L86 (Terminology Sequencing) — terms appearing in 00a and subsequent artifacts require narrative grounding established in PM04 before use. PM04 completion also resolves the fragmented terminology state across PM01, PM03, and Save State. Recommended: complete PM04-01 before 00a sign-off or at minimum before Artifact 03 re-sign-off. | Non-material (sequencing) | L86, PM04-01 | ✅ Session 11 — PM04 §1 fully populated (PM04-02 + PM04-01 both complete). PM04 is now the canonical in-world glossary. |
| PM04-01 | Migrate 00a §1 Time Convention into PM04 §1 (In-World Data Dictionary). After migration, replace 00a §1 content with a pointer to PM04 §1. Requires 00a sign-off to confirm the Time Convention is stable before it is designated canonical in PM04. Save State glossary migration is split out as PM04-02 (READY NOW — does not require 00a sign-off). | Non-material (migration) | L86, PM04 v0.1 | ✅ Session 11 — Temporal Conventions table added to PM04 §1. 00a §1 Time Convention updated to point to PM04 §1. |

---

### BLOCKED BY: D02a-01 RESOLUTION (Chorus Node Translation Rates)

Items waiting on D02a-01 (Chorus Node presence discount scale for The Translation). **D02a-01 adopted as L93 — Contested = 5:1, no presence = 4:1, Present = 3:1, Established = 2:1.**

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 02a-08 | ✅ Complete session 8 — 02a §8 rewritten with presence-based rate table; hardcoded "4:1" removed. | Material | PM (Audit) 02a-IQ-02, 00a Copy Design Principle, D02a-01 | ✅ |
| 02a-09 | Update the Network virtual structure block definition in Artifact 02a — state explicitly that the virtual block at University Perimeter counts as a full structure block for all game purposes, not only resource income. | Non-material (clarification) | L94 | ✅ Applied session 10 overnight — Artifact 02a §10 University Perimeter section updated; full equivalence language added |
| 02a-03 | Update Chorus Node section — add ARBITER Dominance Marker (8 tokens, single fused piece). Clarify that Dominant is structurally unreachable at the Node due to permanent ARBITER token count, not by prohibition. Also update §6 Component Names: remove "1 permanent ARBITER flag for Chorus Node," replace with ARBITER Dominance Marker (reference PM01 §2.08a). Remove "ARBITER is always Dominant" language and replace with language reflecting ARBITER's constitutive presence. | Material | 00a R04, D-P-02, PM (Audit) 02a-IQ-01 | ✅ Session 14 — all four changes applied. **Session 22 re-sign-off complete (v1.4):** Control flag corrected (gold, per-district, placed on Dominant stack); Established marker added (silver, L111); 02a signed off. D-P-02 (visual design) still open. PM01 WBS 2 needs new row for Established marker — see 02a-WBS-01. |
| 02a-WBS-01 | **Add Established marker row to PM01 WBS 2.** New component added session 22 (L111): silver marker, one per Established faction per district, quantity TBD pending Art 11 component spec. Add as new WBS 2 row after 2.03 (deployment marker). | Non-material (component list) | L111 | ✅ Session 22 — added as row 2.08b (after ARBITER Dominance Marker 2.08a); quantity TBD pending Art 11. |
| 10-02 | ARBITER Manual conversion rate table (if D02a-01 adopted) — include flavor text for the 5:1 Contested rate. Tone: The Record register, reads as statement of fact, lands like a warning. The rate is ARBITER's response to factions bringing conflict into the Chorus Node. | Non-material (flavor) | D02a-01, 00a R04 | ✅ Session 14 — §7.6 rate table updated: ARBITER Script column added; Contested rate script written in The Record register (*"The Chorus Node is Contested. The rate is five to one. The request was noted."*); None row updated to 4:1 (L93 adopted); design note added (Contested rate is ARBITER's acknowledgment of what the Chorus has observed, not a penalty). TBD note removed. |

---

### BLOCKED BY: 00a SIGN-OFF + D02a-01 (Both Required)

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 07-03 | ARBITER script for The Translation — the script line when ARBITER facilitates a conversion request must carry the unsettling quality of the act. The faction is doing something unnatural; ARBITER is the instrument they're doing it through. Tone: The Record register, flat and precise, but weighted. Template: *"The conversion is granted. The request was noted."* Full script design pending D02a-03 (Portrait consequence decision). | Material (script design) | 00a R05, D02a-03 | 🔄 |
| 07-04 | ARBITER guide structural requirement — role bifurcation of The ARBITER player. Artifact 07 is the canonical location for the full treatment of The ARBITER player's two operational modes. Content to cover: (1) **Engine mode** — neutral mechanical processing: rolling 2d10, applying difficulty and modifiers per Artifact 03 §12, stating outcomes flat. No register, no character. This is what automation replaces in a tech-enhanced version. (2) **Entity mode** — ARBITER as character: Portrait scoring, private notifications to factions, Chronicle entries, narration in The Witness register. (3) The transition between modes at each resolution beat — explicit cues for when The ARBITER player is in each mode. (4) How to deliver unexpected rulings (per 00a R03) cleanly and in character, without justification. (5) How to sustain both modes across a session without breaking the fiction. The nature of ARBITER's omniscience (why it already knows) belongs in the True State document, not in Artifact 07. | Material (guide structure) | 00a §1 ARBITER omniscience principle, 00a R03, L88 | 🔄 |

---

### BLOCKED BY: ARTIFACT 03 RE-SIGN-OFF

Items waiting on explicit sign-off of the three material changes applied in Artifact 03 v1.5 (Beat 2 rename, Step 6 rewrite, Declaration phase update). Decisions D03-R01 through D03-R03 must be confirmed.

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 03-01 | Beat 2 renamed "The Ground Shifts." Beat 2 opening paragraph updated to name all condition-setting card types. Applied in v1.5. Requires sign-off. | Material | L49, D03-R01 | ✅ Session 13 — signed off |
| 03-02 | Step 6 Card Draw fully rewritten — draw 6 covert / 3 political, hand carry-forward rule, modifier draw conditions table, ring modifier eligibility, Burst Play window, cross-reference to Artifact 04 §12. Applied in v1.5. Requires sign-off. Note: ARBITER announcement revised session 13 — "Assemble hands" → "Prepare operations." Step renamed "Operations Preparation." | Material | L50, D03-R02 | ✅ Session 13 — signed off |
| 03-03 | Declaration phase — Phase 4 carries no Accord exception. Free Accord card from C09 classified as Political Act card; card self-governs. D03-R03 resolved session 15 (L100). | Material | L100, D03-R03 | ✅ Session 15 |
| 03-04 | Once signed off: update version to 1.5 ✅ and update status in PM01 WBS table. | Administrative | PM governance | ✅ Session 28 — PM01 dependency table updated to v1.7 ✅ Signed Off Session 20. Playtest Readiness Checklist 1.05 updated to ✅. |
| 03-05 | During 03 review — audit all ARBITER script lines in Artifact 03 for hardcoded resource rates or values that should reference the canonical rate table (02a §8, D02a-01). | Material | 00a Copy Design Principle, D02a-01, L93 | ✅ Complete session 8/9 — all ARBITER rate references updated; §14 ARBITER Conversion section now cross-references 02a §8; Contested handling correct throughout |
| 03-07 | Terminology: "Effect Card" → "Event Card" — propagate to all artifacts. Artifact 03 updated session 9. Signed-off artifacts 01, 02a, 02b may reference "Effect Card" — audit required. PM04 §2 terminology table to be updated. Resolves part of XA-06 naming question. | Non-material (rename) | XA-06, PM04 §2, session 9 | ✅ Audited session 10 overnight — "Effect Card" not found in 01, 02a, 02b, or PM03; all clean. Formal terminology table entry for "Event Card" is XA-06 scope (Broadcast Card / Event Card definition pending that decision). |
| 03-08 | "Expired area of ARBITER tableau" — new component area introduced in Artifact 03 Step 3 action 7. Define in Artifact 07 (ARBITER Toolkit): what the expired area is, how it is organised, and whether expired Event Cards are ever referenced again (e.g. Chronicle, Debrief). Add to PM01 component list. | Material | Artifact 07, PM01 | 🔄 |
| 03-09 | **Apex activation vs. Beat 0 — design conflict (L103).** Resolved: L104 (session 19). Beat 0 silent note; Beat 3 queue trigger; resources non-refundable; Apex success suspends and fails remaining ops. §16 and §17 updated. Affects Artifact 05 (Apex rules cross-reference). | Material (design decision) | L103, L104 | ✅ Session 19 |
| 03-10 | **Beat 4 payment validation — political act underpayment handling.** Resolved: L106 (session 19). Submit Payment section added to Beat 4 before resolution; three-outcome validation identical to Beat 0. Each player resolves at their own tableau — no public grid. Phase 4 Declaration Step 3 updated — resources stay on tableau until Beat 4. | Material (design decision) | L105, L106 | ✅ Session 19 |
| 03-06 | **L91 vs. Artifact 03 difficulty table — resolved (A).** Influence level table removed from Artifact 03 §12. Difficulty is a card property (L91, L97). Influence level may appear as a modifier on specific cards but does not set universal base difficulty. Beat 3 Step 3, Beat 4 Step 2, and 2d10 System table updated. | Material | L91, L97 | ✅ Session 13 — Option A adopted |
| XA-06 | Define "Broadcast Card" and "Effect Card" in Artifact 01 (board layout spec) and Artifact 09 (card specifications). Artifact 03 §7 Phase 1 Step 2 introduces these two named card types but neither term appears in PM04 §2 terminology table and neither is defined in any artifact. | Material | PM (Audit) 03-IQ-02 | 🔄 |
| XA-07 | Define "Status marker" (states: Discussing / Ready + any third state), add to PM01 component list, and add to Artifact 03 §7 Phase 1 Step 1 as a named component reference. | Material | PM (Audit) 03-IQ-06 | 🔄 WBS 2 row 2.33 added — definition in Artifact 03 and 07 still pending |
| XA-08 | Add dispatch timer to PM01 component list (WBS 2) as a component selection item. | Material | PM (Audit) 03-IQ-04, session 9 | ✅ Covered by WBS 2 row 2.28 (Countdown device / Timer) |
| XA-09 | Define "Personal Tiebreaker cards" in Artifact 07 (ARBITER Toolkit) — referenced in Artifact 03 §7 Step 7 D10 table (result 9) but not defined anywhere. Add as a component to PM01 component list. | Material | PM (Audit) 03-IQ-05 | 🔄 WBS 2 row 2.34 added — definition in Artifact 07 still pending |
| XA-10 | During Artifact 03 re-sign-off review: move Ghost's extra dispatch case slot rule to Artifact 04 as the governing location for faction-specific card play constraints. Keep a cross-reference in Artifact 03. Consider whether 00a needs a rule about asymmetric slot sizes. | Material | PM (Audit) 03-IQ-03 | 🔄 |

---

### BLOCKED BY: ARTIFACT 04 COMPLETION (C16–C35 AND POLITICAL ACTS)

Items waiting on Artifact 04 card review to continue and complete. Currently paused at Ghost C16 (paused until 00a signed off). Ghost C16–C20 redesign (D04-02) is the next card review task after 00a sign-off.

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 04-00 | Add Resolution field to §6 data structure definition — 21st required field. Apply standard 2d10 value to all C01–C15 signed-off cards. Also add Beat field to covert operation card data structure (§6 definition) — Beat field already present for political acts (04-01) but not covert operations. Principle: beat assignment is a card property; Artifact 03 Beat 2 does not enumerate which cards belong to which beat (list removed session 15). | Non-material | L76, session 15 | ✅ Session 23 — Resolution field added to §6. Applied to all C01–C15. Beat field was already present. |
| 04-00b | Split Taxonomy field into three fields (Taxonomy — Category, Function, Target) in §6. Apply to all C01–C15. | Non-material | L77 | ✅ Session 23 — §6 table split. All C01–C15 updated. |
| 04-00c | Split Card type into three fields (Card Type, Card Subtype, Card Faction) in §6. Apply to all C01–C15. | Non-material | L80 | ✅ Session 23 — §6 table split. All C01–C15 updated. Faction field removed (replaced by Card faction). |
| 04-00d | Split Portrait into three fields (Portrait Unconditional, Portrait Bonus, Portrait Bonus Condition) in §6. Apply to all C01–C15 using unconditional rule. | Non-material | L81, L82 | ✅ Session 23 — §6 table split. All C01–C15 updated using unconditional rule (all portrait values in Unconditional; Bonus and Bonus Condition set to N/A). |
| 04-00e | All structural field changes (L76–L82) must be applied and confirmed on C01–C15 before Artifact 04 sign-off. Confirm during dedicated structural pass. | Non-material (gate) | L76–L82 | ✅ Session 23 — All structural field changes applied to C01–C15. Gate passed. |
| 04-23 | **C01–C15 re-sign-off pass — CURRENT WORK ITEM.** Multiple session 27–28 changes cascaded to signed-off cards C01–C15: L130 (C01 Guild income redesign), L131 (Flat modifier principle), L132 (Target field split), L133 (C02 Guild portrait Flat → Submitter), L134–L135 (Target object field added), L136 (Taxonomy.Subject rename), session 28 §6 schema cleanup (enum values moved Constraints → Notes column; Crit effect constraints tightened to "N/A if Resolution = Automatic"). Review each C01–C15 card entry to confirm all cascaded changes are correctly applied, content is internally consistent, and portrait logic holds under L131. Sign-off gates: all 15 cards reviewed and confirmed. Does not require new PM02 locks unless content issues found. | Material (re-sign-off) | L130–L136, session 28 | 🔄 |
| 04-02 | Ghost C16–C20 redesign — resolve C18/C19 duplication; add Portrait Shift primary card; add Reveal to named faction; add Copy subset. Pending decision D04-02. | Material | D04-02 | 🔄 |
| 04-03 | Directorate C21–C25 redesign — resolve C21/C25 Block duplication; add Mandate generation card; consider Shift Public Standing. Pending decision D04-03. | Material | D04-03 | 🔄 |
| 04-04 | Network C26–C30 redesign — resolve C26/C28 duplication; replace C27 (doctrinal misalignment); add Exposure generation; add Shift Public Standing primary. Pending decision D04-04. | Material | D04-04 | 🔄 |
| 04-05 | Syndicate C31–C35 redesign — add Corrupt Accord; add Redirect Accord ("small print"); add Reveal Intel tokens held. Pending decision D04-05. | Material | D04-05 | 🔄 |
| 04-01 | Apply full card data structure (§6) to all political acts P01–P18 — Beat, Taxonomy, Faction perspectives, Restriction, crit effects, Portrait, Card version, Pool copies, Trigger condition. Assign Outcome type value (Binary/Elect player/Elect district/Elect faction/Bilateral agreement/Unilateral) per card — this is the key new field for Political Acts. Card-by-card review required. | Material | D04-06, Session 23 | 🔄 |
| 04-11 | P17 Publish Analysis redesign — current effect (Cross-Category — Shift — Chorus Portrait) invalidated by L84. Needs new effect consistent with Ghost doctrine. Cross-Category — Shift — Chorus Portrait retired as a player-facing taxonomy function; update 04b accordingly. | Material | L84 | 🔄 |
| 04-16 | **VS-xx per-field visibility annotation — Portrait field scope pending design decision.** Session 23 applied VS-xx annotations to §6: VS-06 (Conditional) on all four Effect fields; VS-04 (ARBITER-Only) on Design note; VS-01 default stated in preamble. Remaining gap: Portrait base and Modifier value fields carry no explicit VS-xx annotation. The per-card Portrait value (e.g., "+1 Guild") is printed on the card face (VS-01), but the aggregate Public Standing score is ARBITER-managed. Clarify whether Portrait value fields in the schema carry VS-01 (printed on card — confirmed public) or VS-04 (ARBITER-scored — distinguish per-card vs. aggregate). Update §6 Constraints column for all Portrait value rows once confirmed. Non-material if VS-01. | Non-material (annotation) | Session 23 research, §7.6 | ✅ L116 — Portrait Base and Modifier fields = VS-04. Card face carries coded symbol (visible to all; interpreted by ARBITER only). Art 04 §6 updated. |
| 04-15 | **Modifier token set — full component design required.** ARBITER holds and applies all modifier tokens from ARBITER's tableau. Known values currently in use: **−15** (Type B Countermeasure, Beat 2); **+50** (partial payment penalty, Beat 0 L105). Design a unified token set covering all modifier values used in resolution. Requirements: (1) physically distinct tokens per value — size, color, or numeral; (2) stored in a dedicated area of ARBITER's tableau between use; (3) compatible with card-stack cascade display so values remain legible in Beat 3. Confirm whether additional modifier values exist (card effects, Protect operations, Situation Report modifiers) and include all in the set. Design in Artifact 07 (ARBITER Toolkit) §8 or §9; add each token to PM01 component list. | Material (component design) | L102, L105 | 🔄 WBS 2 row 2.32 added — full design in Artifact 07 still pending |
| 04-13 | Audit all operation cards and political act cards for Automatic or Impossible base difficulty values — these are no longer valid base difficulty states (L101). Convert any Automatic instance to explicit card text or the appropriate base difficulty tier. Convert any Impossible instance to explicit card text or remove as card-specific ARBITER ruling. Apply during C01–C15 structural pass and P01–P18 review. | Material | L101 | 🔄 C01–C15 complete (session 23) — all Automatic cards converted: Difficulty set to N/A; Resolution states "No roll required." Effect fields no longer carry "N/A — Automatic" annotation. C14 conditional handled: N/A when uncontested, Average (50%) + ring modifier when contested. P01–P18 pending (political acts pass). |
| 04-14 | Print base difficulty on action cards as both label and percentage value — e.g., "Easy (75%)" not just "Easy." Players and ARBITER read the threshold directly off the card without consulting §14. Apply to all operation cards and political act cards during C01–C15 and P01–P18 design pass. | Material (card layout) | Session 17, L97 | 🔄 C01–C15 complete (session 23) — all roll-based cards updated: Easy (75%), Average (50%), Challenging (25%), with ring modifier notation where applicable. Affinity bonus difficulty values also updated to include percentages. P01–P18 pending (political acts pass). |
| 04-12 | Free Accord card (C09 trigger) — full Political Act card design. Card type: Political Act; cost: 0; return to ARBITER on play (not discarded); ARBITER delivers to acting faction's hand at C09 case resolution. No play-this-round constraint. See L100. | Material (card design) | L100 | 🔄 |
| 04-06 | Apply card data structure to Emergency Response cards — Card ID, Beat, Taxonomy, full effect fields. Pending decision D04-10. | Material | D04-10 | 🔄 |
| 04-07 | Design Countermeasure cards in Artifact 04 (home confirmed — L115). Content to incorporate from Phase 5 (removed session 15): **Type A — District Block** (names a specific district; blocks all offensive operations targeting that district this Quarter); **Type B — Faction Defense** (names playing faction as defender; the target threshold for any operation against that faction's assets is reduced by 15; does not block — makes operations harder); **Rules** (permanently removed after use; 3 per Faction Player per session — flagged for playtesting validation; multiple may be played in Phase 5). D04-12 closed. | Material | L115 | 🔄 |
| 04-08 | Select in-world name for modifier cards — "Modifier cards" is a working designation. Pending decision D04-07. | Non-material (naming) | D04-07 | 🔄 |
| 04-09 | Grid Tap concept — tabled as political act or operative ability. Add to §10 political act design queue and Artifact 05 discussion list when those passes begin. | Non-material (parking) | L74 | 🔄 |
| 04-10 | Rezone concept — tabled as political act. Physical implementation question (overlay component design) must be resolved before card design can finalize. Add to §10 political act design queue. | Material (design prerequisite unresolved) | L73, R17 session 5 notes | 🔄 |
| 04b-01 | Update card taxonomy index (§5) when any card in Artifact 04 is redesigned or added. | Non-material (sync) | Ongoing | 🔄 |
| XA-31 | **Art 04b taxonomy field rename — "Target" → "Subject".** Art 04 §6 renamed Taxonomy.Target to Taxonomy.Subject (L136) and all §1/§6/§13.1 references updated. Art 04b still uses "Target" as the third taxonomy dimension in §4 (Category / Function / Target table) and all card taxonomy assignments. Non-material terminology pass — update 04b §4 table header and any inline references to "Category/Function/Target" notation. Coordinate with 04b-01 (taxonomy index sync) — do both in the same 04b pass. | Non-material (L136 terminology) | L136, Session 27 | ✅ Session 27 — all "Target" → "Subject" in headers (§1, §5, §6.1, §6.2, §7). §4 Board Valid Targets: "Presence (token or claim marker)" → "Presence token, Operational marker". §5 Subject values: 8 Presence → Presence token; C22 → Operational marker; C35 → Named action type. §7 matrix: C22 Operational marker row added; C35 Named action type row added; ~~Chorus Portrait~~ applied. Art 04b v1.2. |
| 02b-01 | Cross-reference audit: verify Intel token mechanics in §8–9 are consistent with current card designs — specifically the Denounce cost structure (L39 vs current P04 design), token age rules, and C05 crit failure notification slip. Resolve any inconsistency. | Material (if inconsistency found) | D04-11, F-ART02B-01 | 🔄 |
| XA-11 | Confirm status of Cross-Category — Shift — Chorus Portrait retirement: identify any cards in Artifact 04 C16–C35 and P01–P18 that use this taxonomy function and confirm they are being redesigned. Update 04b taxonomy table once confirmed. Coordinate with 04-11 (P17 redesign). | Material | PM (Audit) 04-IQ-01, L84 | 🔄 |
| XA-12 | Flag for re-check when Artifact 04 is signed off: "Incursion" is referenced in signed-off Artifacts 01 §5, 02a §6, and 03 (multiple locations) as a known mechanic. If Incursion is renamed, redesigned, or removed in 04, all three signed-off artifacts need updating. | Non-material (flag) | PM (Audit) XA-IQ-04 | 🔄 |
| XA-13 | Flag for re-check when Artifact 04 is signed off: "Burst Play" is referenced in Artifact 03 §7 Phase 1 Step 6 but defined in Artifact 04 §12.6. If Burst Play is removed or renamed in 04, Artifact 03 needs updating. | Non-material (flag) | PM (Audit) 04-IQ-02 | 🔄 |
| D04-14 | **Faction-specific deck physical organization** — decide whether faction-specific covert and political act cards live in separate per-faction decks or a shared pool by type. Does not block current card data design — card content is correct either way. Resolve before Artifact 09 production spec and before Art 04 information architecture is finalized. Open decision logged in PM02 D04-14. | Design decision | D04-14, session 26 | 🔄 |
| 04-17 | **§6 Type vocabulary — reconcile with 00b data architecture.** Session 26 established a Type controlled vocabulary for the Card Data Schema (String, Semver, Integer, Enum, Prose, ±Integer — L121). This vocabulary was created without cross-referencing 00b's entity type system. 00b is the data architecture reference. Review: (1) do these type names conflict with or duplicate any type names in 00b's entity registry or schema reference? (2) should 00b §3 (L108 compliance standard) be updated to reference the §6 type vocabulary as the canonical type set for all schema documents? Resolve before any new schema document is created. | Non-material (data architecture) | L121, Session 26 | ✅ L123 — no conflict found. ID Reference added as implicit FK type. L121 vocabulary promoted to 00b §3 suite-wide standard. |
| 04-18 | **Faction perspectives field — L108 compound cell evaluation.** The "Faction perspectives" field in §6 is typed as String but contains 5 per-faction sub-values (one sentence per faction). This is structurally a compound cell — an L108 Req 1 violation analogous to XA-30 (compound effect text). Evaluate two options: (A) decompose into 5 faction-specific fields (Faction perspectives — Guild / Directorate / Network / Ghost / Syndicate), similar to how Portrait was decomposed in L119; or (B) document as a deliberate exception in 00b §8 (Design Notes & Known Gaps), as with XA-30. Option A has cascade cost (5 new §6 rows, update all 15 card entries). Option B defers decomposition until card content is locked. Confirm direction before P01–P18 data structure pass. | Design decision | L108, L119, Session 26 | ✅ Option B — documented as deliberate exception in 00b §8. Revisit if individual faction perspective querying becomes a use case post-design (open question). |
| 04-19 | **Design note Displayed = No — confirm.** Session 26 assigned Displayed: No to the Design note field (not printed on card). This was my assignment, not explicit direction from Andy. Confirm: should Design notes ever appear on a physical card product — e.g., on a card back, in an ARBITER sleeve insert, or in a separate reference document delivered with the card? If the answer is "no physical component ever," the current assignment is correct. If Design notes should appear in an ARBITER-only reference document (distinct from the card face), the Displayed value and VS-04 annotation may need revisiting. | Clarification needed | Session 26 | ✅ Confirmed correct. VS-04 (who sees it during play) and Displayed: No (never on a physical card component) are orthogonal. Design notes are design-document-only — they inform Art 11 and Art 07 as input, not as printed content. |
| 04-20 | **Portrait modifier magnitude — design principle needed.** The ±Integer type for Portrait Flat, Submitter, and Modifier fields does not constrain the magnitude of the value. No design principle currently governs Portrait modifier size. Establish before C16–C35 and P01–P18 Portrait design: (1) Is ±1 the standard modifier? (2) Can a single card give ±2 or higher? (3) Does magnitude scale with card cost or difficulty? (4) Is there a maximum cumulative Portrait shift per Quarter? Game balance and Chorus narrative implications — the Portrait track IS the Chorus's real-time answer; runaway Portrait shifts from a single card could distort the signal. | Design decision (game balance) | L119, L120, Session 26 | ✅ L125 — ±1 locked as standard per-card Portrait modifier. 4 actions × 8 Quarters = 32 max movements on a 0–20 track. Portrait economy analysis post-spec: PM05 04-21. |
| 04-21 | **Portrait economy analysis — post-spec action item.** Once all C01–C35 and P01–P18 are designed, analyze the full Portrait modifier distribution: (1) ratio of Portrait-neutral cards (N/A) to ±1 cards; (2) cumulative Portrait movement scenarios across a full 8-Quarter session; (3) modifier card interaction with Portrait (unknown at design time — flagged per L125); (4) confirm no faction has structurally skewed Portrait exposure based on card set. Flag any balance concerns before V1 playtest. | Game balance (post-spec) | L125, Session 27 | 🔄 |
| 04-22 | **C02 Demolish — Guild Flat −1 review per L131.** L131 prohibits Flat portrait modifiers on standard (Card faction: All) cards. C02 currently has Guild Flat −1 (fires whenever ANY faction demolishes a structure, regardless of submitter). At 5 factions × 2 copies × 8 quarters this is unbounded in the negative direction. Options: (A) remove Flat, no portrait effect — demolition is narratively neutral for Guild's Chorus alignment; (B) Guild Submitter −1 — portrait penalty only when Guild itself demolishes (against doctrine); (C) redesign the portrait logic entirely for C02. Review during C01–C10 sign-off. | Design decision (game balance) | L131, Session 27 | ✅ L133 — Option (B) selected: Guild Flat −1 → Submitter −1. Narrative anchor: "We build. We do not unmake." Guild's portrait falls only when Guild demolishes — doctrinal self-betrayal, not when others do. |

---

### BLOCKED BY: ARTIFACT 04 COMPLETION → ARTIFACT 01 ADJACENCY TABLE

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 01-01 | Add formal district adjacency table — list which districts are adjacent to which. Required by cards C02, C04, C05, C14, C29, C30. Final card set must be confirmed before adjacency table is authoritative. **Session 22:** Art 04 is critical path; adjacency is a self-contained bounded task (single-pass, no design decisions) to execute at a natural break once the adjacency-dependent card set (C02, C04, C05, C14, C29, C30) is stable enough to confirm — need not wait for full Art 04 sign-off. | Material | D04-09, F-ART01-01 | 🔄 |

---

### BLOCKED BY: ARTIFACT 04 COMPLETION → ARTIFACT 09

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 09-01 | "Delivered in case" — establish as standard phrase for all privately delivered effects. Apply consistently across all card text in Artifact 09. | Non-material (standard) | L59, F-ART09-01 | 🔄 |
| 09-02 | "Return primary cost to dispatch case" — establish as standard resolution phrase for crit success refunds. Apply consistently. | Non-material (standard) | L60, F-ART09-02 | 🔄 |
| 09-03 | Modifier card value rating field (1–3) — every modifier card must carry a value rating for Option C playtest evaluation. Apply to all modifier card designs. | Non-material (field) | L67, F-ART09-03 | 🔄 |
| 09-04 | Free Accord card (C09 Fund) — not drawn from political deck. ARBITER-delivered. Note this in Artifact 09 card production tables. | Non-material (clarification) | L51, F-ART09-04 | 🔄 |
| 09-05 | Pre-written ARBITER notification slip — define as a component category. Design slip text for C05 crit failure (draft: "An unknown party attempted to access sensitive information about your operations in [district]. The attempt was identified and neutralised. Exercise appropriate caution.") and any other cards that trigger private slips. | Material (component design) | A-04-05, F-ART07-01 | 🔄 |
| 09-06 | Modifier card individual content — all faction modifier decks and ring modifier decks need individual card designs. Full design pass required. Pending decision D04-08. | Material | D04-08 | 🔄 |
| 09-07 | Modifier card in-world name — apply final name once D04-07 is resolved. | Non-material (naming) | D04-07 | 🔄 |
| 09-08 | Operator card physical format — postcard size (3×5" or 5×6") to allow visual prominence and richer content than standard card format. Exact dimensions to be confirmed during visual design pass. | Material (component spec) | Artifact 11, Artifact 05, session 8 | 🔄 |
| 09-09 | Operator card information design and narrative — full content design pass for operator cards. Coordinate with Artifact 05 and Artifact 11 (visual design). | Material (content design) | Artifact 05, Artifact 11, 09-08, session 8 | 🔄 |
| 09-10 | Portrait field layout on card face — Artifact 04 §6 now carries 20 per-faction Portrait fields (Portrait — [Faction], Portrait — [Faction] Condition, Portrait — [Faction] Modifier, Portrait — [Faction] Modifier Condition for each of the 5 factions). Card face design must determine how to present per-faction portrait data legibly — e.g., a portrait table, icon strip, or faction-keyed sidebar. Cards with all-N/A factions may suppress the portrait block entirely. Coordinate with Artifact 11 (visual design). | Material (card layout) | Session 23 | 🔄 |
| 09-11 | **§6 Displayed column — complete per-field values.** Artifact 04 §6 has a Displayed column (Face / Back / No / TBD) separate from VS-xx (visibility scope). VS-01 = public knowledge; does not imply printed on card. Currently: Face set for fields required on card face by Principle 6 (name, costs, effects, difficulty, resolution, target, restriction); No set for Pool copies (pool metadata, not printed); TBD for all other fields including Card ID, Card version, Card type/subtype/faction, Beat, Portrait fields, Narrative, Taxonomy. Complete TBD values during Artifact 09 card layout pass. | Design decision | Artifact 04 §6, session 26 | 🔄 |

---

### BLOCKED BY: ARTIFACT 07 (NOTIFICATION SLIP FEASIBILITY + MODIFIER AUDIT)

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 07-05 | **ARBITER Portrait Reference Table** — design a Card-ID-keyed lookup table for ARBITER covering all 20 Portrait fields per card (Base and Condition × 5 factions, Modifier and Modifier Condition × 5 factions). ARBITER uses this table at resolution to determine Public Standing effects without parsing card faces. Design questions: (1) format — single table or per-faction columns; (2) whether to include cards with all-N/A Portrait rows or omit them for brevity; (3) playtest data collection: does lookup vs. card-face parsing affect ARBITER pace? File in Artifact 07. | Material (ARBITER reference design) | L116, L117 | 🔄 |
| 07-01 | Pre-written notification slip — establish as a physical component category in Artifact 07. Confirm feasibility for paper prototype. This gates 09-05 (slip text design) and any other card effects that deliver private slips. | Material (component feasibility) | A-04-05, F-ART07-01 | 🔄 |
| XA-26 | **§14 Modifier table — ARBITER Debrief reward row (pending Art 07).** §15 End of Quarter Step 2 states ARBITER selects a Tier A/B/C Debrief reward effect. If any Tier reward includes a threshold modifier applicable to the subsequent Quarter's operations, §14's Difficulty Modifier table needs a row for it ("ARBITER Debrief reward | As specified in Artifact 07"). During Art 07 Debrief reward design: confirm whether any reward modifies Roll thresholds, and update §14 accordingly. | Non-material (flag) | Session 20 modifier audit | 🔄 |

---

### BLOCKED BY: OPEN DECISIONS (SPECIFIC)

**Blocked by session 20 modifier audit:**

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| XA-24 | **Infrastructure −25 applicability to political acts — design decision needed.** Phase 2 Placement states the −25 threshold penalty applies to "all operations targeting this district" if no adjacent Core district holds Established or Dominant presence. "All operations" is ambiguous — does it include political acts (Beat 4) or only covert operations (Beat 3)? Both beats now call out the Infrastructure penalty in their modifier lists (added session 20). If the intent is covert-only, update Phase 2 language and both beat procedures. If the intent is all actions, no change needed. Confirm and lock. | Material (design decision) | Session 20 modifier audit | ✅ L107 — "operation" is inclusive of all action types (covert, political, operative). Both beats and Phase 2 language confirmed correct as written. |

**Blocked by XA-IQ-01 — Define or remove "Chorus Question" from L1:**

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| XA-14 | Resolve what "Chorus Question access" means in Artifact 01 §5 and Artifact 02a §10. Both signed-off artifacts reference it as a Chorus Node benefit without definition. Decision needed: is it a round-based ARBITER event, a voting privilege, a narrative access mechanic, or a future-layer mechanic that should be removed from L1 until designed? | Material | PM (Audit) 01-IQ-02, XA-IQ-01 | 🔄 |

**Blocked by D-P-02 — ARBITER Dominance Marker visual design:**

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 01-03 | Update board setup procedure — ARBITER places ARBITER Dominance Marker (2.08a) at the Chorus Node during setup introduction. This is part of ARBITER's opening action, not player setup. Also: distribute 3 Countermeasure cards per Faction Player during player setup (referenced in Artifact 03 §7 Step 6 tableau check). | Material | 00a R04, D-P-02 | 🔄 |

**Blocked by D02a-03 — Does The Translation carry a Portrait consequence:**

*(See 07-03 above, which also requires 00a sign-off.)*

---

### BLOCKED BY: ARTIFACT 00 RE-SIGN-OFF (SESSION 4 ADDITIONS)

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 00-04 | Narrative review and enrichment of Artifact 00. **Session 4 additions pending re-sign-off:** §6 now includes "On the Question of Origin," "On the Question of Cause," "On the Question of Completeness" rewrite, station crew founding history, and "What New Meridian Is" continuation. All additions are Narrator voice. Review and re-sign-off required. | Material | FD-01, 00-03, 00-R03, FD-05 | 🔄 |
| 00-06 | Establish the quarter (one round = three months of real-world time) in Artifact 00 as worldbuilding about The Table's deliberation structure. Currently defined mechanically in Artifact 03 §1 only. | Material | PM04 §2 Narrative Language Convention, 00a §1 Time Convention | 🔄 |
| 00-03 | Add the layer structure to Artifact 00 — narratively only. The layers (physical, social, informational, digital, and ARBITER's layer) are real within the world of The Signal; they are not game mechanics introduced by expansion. Language must be narrative — no mechanical labels, no L1–L5 notation. | Material | FD-01, 00a Governing Principle | 🔄 |
| XA-15 | Add to Artifact 00 §8 (The Table) or §9 (ARBITER): language that ARBITER is the sixth party at The Table — a party with a seat, territory (the Chorus Node), resources (Resolution), a hidden objective, and an agenda. May be part of the 00-04 enrichment pass. Requires re-sign-off. | Material | PM (Audit) XA-IQ-03 | 🔄 |

---

### BLOCKED BY: GHOST/NETWORK COLOR DECISION (Artifact 11 Design Pass)

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| XA-16 | Confirm that the Ghost/Network color adjacency (both green — charcoal vs. bright signal) is sufficient for distinguishing presence tokens at arm's length in dim lighting. If not sufficient, revise one faction's color. Artifact 11 design pass must address this regardless, including colorblind accessibility. Any revision requires 00 re-sign-off. | Material | PM (Audit) 00-IQ-01 | 🔄 |

---

### BLOCKED BY: MULTIPLE UPSTREAM ARTIFACTS (Late-Phase Items)

Items that cannot begin until most or all of 04, 05, 06, 07, and 08 are complete.

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| XA-22 | **Resolution Grid — design and produce physical component.** Staging grid built by the ARBITER Player during Beat 0. Structure: 5 lanes (columns) by case receipt order; rows for Beat 2 cards, then paired Beat 3 card/target rows (up to 4 pairs for Ghost). Grid persists through Beats 1 and 2 as invalid/blocked operations are removed; Beat 3 resolves from the cleaned grid. Beat 3 resolves row-first: all card-1 pairs across all lanes before any card-2 pair (round-robin by case receipt order — L102). Beat 4 political acts do not use a grid — each Faction Player resolves their own political act at their tableau in initiative order; ARBITER observes, validates, and provides modifier tokens. Mixed case contents resolved in ARBITER's placement order. **Modifier card cascade:** modifier cards stack under the operation card in each grid cell, peeking out at top/bottom to display values at a glance — card physical design must support this orientation (value printed at both top and bottom edge). Design in Artifact 07 (ARBITER workflow + component spec); physical production in Artifact 11; add to PM01 component list. | Material (component design) | L102, L103, session 16–17 | 🔄 WBS 2 row 2.31 added — design in Artifact 07 and Artifact 11 still pending |
| XA-23 | **Index jump links — convert all artifact Index sections to internal anchor links.** GFM supports internal anchor links using `[Section Title](#section-title)` format. Anchors are auto-generated from headings: lowercase, spaces→hyphens, punctuation stripped. Convert the numbered list in each artifact's §2 Index to linked entries. Scope: all text artifacts with an Index section (00, 00a, 01, 02a, 02b, 03, 04, 04b, 05, 06, 07, 08, 09, 10, 10a, 11). Method: for each artifact, read the Index section and all headings; generate the correct anchor string for each; rewrite the index list as markdown links. Non-material — purely additive formatting, no content change. If an anchor resolves incorrectly it fails silently (no jump) without breaking anything. Safe to run unsupervised. | Non-material (formatting) | Session 20 | ⬜ Queued — run unsupervised |
| XA-21 | **ARBITER visual indicator for active Situation Report targeting restrictions — retired (L110).** ARBITER reads active restrictions aloud at Beat 0/1. No physical indicator component. Faction Player attention is the designed responsibility — inattention is an intended consequence. | Material (component decision) | Session 16–17, L110 | ✅ Session 22 — Option A chosen. No artifact edit required. |
| 02a-04 | Chorus Node — add cross-reference note in the general Established definition (02a §6): "Exception: at the Chorus Node, only one faction may hold Established at a time — see §10." | Non-material | PM (Audit) 02a-IQ-04 | 🔄 |
| 02a-05 | Chorus Node Tension marker — clarify in 02a §10 that the Chorus Node modifies the Contested trigger from 3+ chips to 2+ chips (Established threshold). Either use a different name for the Chorus Node tie condition, or add an explicit callout. Reflect in 00a as a governing exception. | Material | PM (Audit) 02a-IQ-03 | 🔄 |
| 02a-06 | Portrait Amplifier at Chorus Node — move the defining location from 02a §10 to 00a (as a governing rule or exception) and 02b §10 (special conditions). The 02a §10 reference should become a cross-reference only. Confirm ARBITER administers the multiplier per 00a §11 A05. | Material | PM (Audit) 02a-IQ-05 | ✅ Resolved by design — definition stays in 02a §10. Chorus Node benefits (suppression, amplifier, question access, translation rate) are board-position mechanics and belong with the board document. 02b holds Portrait track mechanics. 00a R01 covers ARBITER administration via cross-reference. Moving to 00a would be a category error; moving to 02b would split the Chorus Node benefit set. Session 22. |
| 02a-07 | Resolve "Asset token" terminology conflict: Artifact 02a §8 states there is no abstract "asset token" wrapper; PM04 §2 lists "Resource token → Asset token" as the in-world term. **PM04 §2 row removed.** Faction-specific resource names (Findings, Exposure, Capital, Capacity, Mandate) are the canonical in-world terms. PM04-01 to confirm no "Asset token" bleeds into PM04. | Non-material | PM (Audit) 02a-IQ-07, PM03-IQ-03 | 🔄 PM04 done — PM04-01 pending |
| 10-01 | Place ARBITER flavor text as a sidebar next to the resource conversion/trade mechanic description in the Player Manual and/or ARBITER Manual: *"The conversion is granted. The request was noted."* This is The Record register. | Non-material (flavor) | 00a R05, 00-04 | 🔄 |
| PW-03 | Add narrative description to every physical game component in PM01 WBS 2 — what it is in the world, what it represents, what holding or placing it means. Dice are exempt (resolution abstraction layer). | Non-material (narrative) | 00a §5, D02a-02, Artifacts 10, 11 | 🔄 |

---

### DEFERRED

Items not on the critical path to first playtest.

| # | Change | Type | Source | Status |
|---|--------|------|--------|--------|
| 11-01 | **index.html as informal visual reference for Artifact 11.** A project homepage was designed in a mobile creative session (2026-05-17) and committed to the repo root. It instantiates the Artifact 11 design direction — dark background (#0a0c0f), faction colors as data series, ARBITER as white (#e8e8e8) reading as categorically different, monospaced/future-punk data aesthetic. Animated Chorus sine wave in header. When the Artifact 11 design pass begins, reference this page as a working visual precedent — particularly the faction color rendering and ARBITER card treatment. No binding design decisions; informal reference only. | Non-material (reference) | Creative session 2026-05-17 | 🔄 |
| 11-02 | **Chorus wave as recurring visual motif — open design question.** The animated sine wave used in the index.html header (transmission violet, scrolling, labeled "UNDECODED // RESPONSE WINDOW OPEN") felt tonally correct in testing. Open question: does a version of this motif appear on physical ARBITER materials — the Chorus Node marker, ARBITER's written materials, or the Chronicle cover? Discuss during Artifact 11 §7 (ARBITER Visual Identity) or V10 (ARBITER Tools visual layouts). No decision required before Artifact 11 design pass. | Non-material (design question) | Creative session 2026-05-17 | 🔄 |
| PW-01 | Review /Retired folder — design documents predate current V1 artifact set. Extract any design elements not yet captured in V1. Incorporate into appropriate artifacts. **Folder reorganized 2026-05-16:** /Retired/Electronic (20 files — original electronic brainstorming suite, docs 00–20, old faction names); /Retired/Paper (6 files + files.zip — 1st gen Paper/pre-V1 artifacts); /Retired/backup.zip (full archive of both). See PM03 §6 for file-level index. | Material (review required) | Design direction | 🔄 |
| PW-02 | Design a unified primary key taxonomy for all IDs across the project. Current systems are inconsistent: rule IDs (00-R01), locked decisions (L01, L-NEW-01), open decisions (D04-01), punch list items (00-01, PW-01), card IDs (C01, P01), playtest variables (PT-02-02), validation targets (V01, PC-01), future state (FD-01), 00a audit items (A01). A unified taxonomy should have consistent structure: category prefix, domain/artifact prefix, sequence number. Apply retroactively across all V1 artifacts, PM documents, and reference documents. | Non-material (renaming) | Design direction | 🔄 |
| 00a-08 | Confirm 00a §11 A06: verify whether "Chorus Portrait Multiplier" language in Artifact 01 §8 is consistent with 02a §10. Low priority — likely non-material. | Non-material | 00a §11 A06 | ✅ Resolved — L92 (session 11). 01 rewritten to match 02a canonical mechanic: Established threshold, flat additive, "Amplifier" renamed. |
| 00a-09 | Confirm 00a §11 A07: when Rezone is designed, it will require explicit governance rule in 00a (R17 notes Rezone as a tabled exception). Flag for political act design pass. | Non-material (flag) | 00a §11 A07, L73 | 🔄 |
| 00a-12 | **Established marker — add to 00a board component lists.** Two rules reference board components by name and currently omit the Established marker (added session 22, L111): R (board always honest — line ~269, lists "presence tokens, deployment markers, structure blocks, control flags, and tension markers"); R (immediate update — line ~321, "Control flags and tension markers update immediately when influence conditions change"). Add "Established markers" to both lists. Non-material — new component addition only. | Non-material | L111, session 22 | ✅ Session 22 — "Established markers" added to both 00a Mechanics fields. |
| 00a-10 | Retroactive ARBITER / ARBITER player terminology audit across all 00a Mechanics fields (L88). Rule statements and Narrative fields use "ARBITER" correctly by convention. Mechanics fields must be audited: replace "ARBITER" with "The ARBITER player" wherever the described action is physical execution in the paper prototype. R01 Mechanics corrected as first application. Full pass required before 00a sign-off. Extend audit to Artifacts 03 and 07 at their respective review passes. | Non-material | L88, 00a §1 ARBITER governing principle | 🔄 |
| 00a-11 | Governs field audit across all 00a rules — identify any remaining pending/temporary references incorrectly placed in Governs and move them to the new Pending: field. R13a and R15 corrected as first applications. Full pass required before 00a sign-off. | Non-material | 00a §1 Rule Data Structure principle | 🔄 |
| 07-05 | Add "How to Read Portrait Values on a Card" guide section to Artifact 07. Dependent on D09-05 (Portrait visual coding system). | Material | L90, D09-05, 00a R29a | 🔄 Blocked by D09-05 |
| 07-07 | Add ARBITER continuous observation guidance to Artifact 07 — ARBITER's awareness extends beyond structured phases; trades, negotiations, disclosures, and table behavior during Debrief or between phases are within ARBITER's awareness and may be reflected in the Chronicle. Source quote preserved: *"We thought the conversation between quarters didn't count. ARBITER was there. ARBITER is always there."* — Syndicate counsel, post-session notes. | Material | 00a R43 (retired), Artifact 00 §9 | 🔄 |
| 07-06 | Design the ARBITER player's Intel note tracking mechanism — how does The ARBITER player know, during play, what each faction holds, how many notes, and how current they are? Options include a private tracking sheet, a reference zone on The Overview, or a running log in the Chronicle. | Material | 00a R33, Artifact 02b §8 | 🔄 |
| D09-05 | Portrait visual coding system on card face — design a system ARBITER can parse at Resolution (Portrait values, faction impact) that is opaque in purpose to faction players. Options include color coding, glyph/symbol system, positional encoding, or combination. Locked direction: L90. Dependent: Artifact 07 "How to read Portrait values on a card" guide section (07-05). | Material | L90, Artifact 09 | 🔄 |
| 00-05 | *(Duplicate — tracked under BLOCKED BY: 00a SIGN-OFF above.)* | — | — | ✅ Session 11 |
| 06-01 | **Dispatch case contents — migrate from Artifact 03.** The canonical list of what goes inside a dispatch case (operation cards, modifier cards, resource tokens, target slips, Pass card) was removed from Artifact 03 §9 during session 13 scan. It belongs in Artifact 06 — Messaging System as part of the dispatch case design and physical format spec. Artifact 03 §9 now carries a cross-reference only. | Material (migration) | Session 13, Artifact 06 | 🔄 |
| XA-25 | **§14 Modifier table — Operative ability modifier row (pending Art 05).** Art 05 will define operative abilities. If any operative ability modifies operation or political act thresholds (not just serves as the action card), §14's Difficulty Modifier table needs a row: "Operative ability | As specified on Operative Card." During Art 05 design: confirm whether operative abilities can stack as threshold modifiers, and update §13 accordingly. Coordinate with 04-15 (modifier token set) if operative ability tokens need a physical form. | Non-material (flag) | Session 20 modifier audit | 🔄 |
| XA-27 | **03a — Game Engine Specification.** Scope expanded session 20: from modifier catalog to full code-lite technical companion to Art 03. Three layers: (1) **State Model** — formal game state at each beat boundary using 00b entity IDs (M-xx, D-xx, RO-xx) as variable vocabulary; (2) **Beat Procedures as pseudocode** — each beat as a structured function (Beat_0() through Beat_5()) with explicit IF/THEN/ELSE branches, named inputs/outputs; modifier stack as summation formula; resolution check as formal inequality; (3) **Decision Tables & Edge Case Registry** — all branching conditions surfaced as tables (face-down/face-up, Apex vs. non-Apex, Critical overrides, partial payment, Infrastructure, Type B scope). Variable modifier rows (M-08 Modifier card, M-09 Protect, M-10 Situation Report) stubbed pending Art 04. Fixed modifier math fully specifiable now. Modifier balance analysis (original XA-27 scope) is a derived output once formal stack is expressed. **Placeholder created; structure defined; content pass queued for near-term session.** | Material (new artifact) | Session 20 | ✅ Session 22 — Layers 1–3 draft complete (v0.97). DT-01 through DT-09 and Apex_Activation() drafted in §6. Layer 4 stub added to §9 with known fixed-modifier pathological case noted. Remaining blockers: M-08/M-09/M-10 variable rows (Art 04); Apex threshold values (Art 05); Emergency Response design (Art 04/05). DF-04 (00b entity audit for Case, Packet, GridCell, IP-xx) tracked separately. |
| D-FT-01 | **Faction hidden truths — design question.** Why are these five factions at The Table, and not others? The answer may not be purely philosophical. Working hypothesis: the four non-Network factions have been involved with the Chorus — or with its effects — long before The Table formed, and before The Chorus Papers. The Network is the exception: they genuinely did not know until The Chorus Papers, and arrived because of them. The other four knew more, sooner, through different channels — and their doctrines may be rationalizations of prior involvement rather than independent positions. What does each faction know that it has not disclosed? The Syndicate line in Artifact 00 §6 "The Chorus Papers" — *"The Syndicate was not surprised by this"* — is the first textual marker. Each faction likely has an equivalent: Ghost's classified evidence that the Chorus predates thirty-one years (mentioned in the brief, not yet developed); the Directorate's sanctioned access that predates every other faction; the Guild's physical presence at the Node since construction began. The Network's post-Papers arrival is the design foil — the one faction whose presence at The Table is entirely a consequence of The Chorus Papers, not of prior knowledge. Explore whether these hidden truths belong in a private faction supplement (analogous to PRIVATE___True_State.md). Text anchor: Artifact 00 §6 "The Chorus Papers," paragraph beginning "The Syndicate was not surprised by this." | Design direction | Session 12 | 🔄 |

---

*When all entries in Section 1 show ✅, the punch list is clear. Completed entries are retained for audit trail.*

---

## Section 2 — Validation Target Dashboard

Playtest hypothesis tracking. Updated after each playtest session. Full Validation Tracker with measurement methodology lives in PM02 §3.

**Current status:** Pre-playtest — no sessions completed.

### Player Count Assumptions

| # | Assumption | Target | S1 | S2 | S3 | Status |
|---|-----------|--------|----|----|----|--------|
| PC-01 | Game works with 2 faction players + ARBITER | ≥ 4 contested districts by Quarter 4 | — | — | — | ⬜ Not tested |
| PC-02 | Game works with full table (5 factions + ARBITER) | Resolution < 10 min, < 3 errors/session | — | — | — | ⬜ Not tested |
| PC-03 | ARBITER role is desirable and repeatable | > 50% would ARBITER again | — | — | — | ⬜ Not tested |
| PC-04 | Automated ARBITER fallback is viable | Session completes without breakdown | — | — | — | ⬜ Not tested |

### Core Gameplay Hypotheses

| # | Hypothesis | Target | S1 | S2 | S3 | Status |
|---|-----------|--------|----|----|----|--------|
| V01 | 3 covert operations is right | Beat 3 duration < 8 min by Quarter 3 | — | — | — | ⬜ Not tested |
| V02 | Ghost 4-operation rule is balanced | Ghost ≤ 40% of table activity | — | — | — | ⬜ Not tested |
| V03 | Incursion is used appropriately | 1–3 uses per session | — | — | — | ⬜ Not tested |
| V04 | Accords form naturally | At least 1 Accord per session | — | — | — | ⬜ Not tested |
| V05 | Debrief generates conversation | 2+ min unprompted by Round 3 | — | — | — | ⬜ Not tested |
| V06 | ARBITER completes Resolution in time | < 10 min per quarter | — | — | — | ⬜ Not tested |
| V07 | Public Standing moves meaningfully | 2+ position changes per faction | — | — | — | ⬜ Not tested |
| V08 | Chorus Node is contested | ≥ 2 factions at Present+ by Quarter 6 | — | — | — | ⬜ Not tested |
| V09 | No single faction economically dominant | No faction holds 2× nearest rival at Quarter 4 | — | — | — | ⬜ Not tested |
| V10 | Apex is attempted | ≥ 1 attempt per 3 sessions | — | — | — | ⬜ Not tested |

### Victory System Hypotheses

| # | Hypothesis | Target | S1 | S2 | S3 | Status |
|---|-----------|--------|----|----|----|--------|
| V11 | Public and private VP are both meaningful | Board leader wins < 70% of sessions | — | — | — | ⬜ Not tested |
| V12 | Chorus Portrait can swing the outcome | Portrait changes ranking in > 30% of sessions | — | — | — | ⬜ Not tested |
| V13 | Vote outcome feels meaningful | Players reference the vote post-session | — | — | — | ⬜ Not tested |
| V14 | VP weights produce tension throughout | ≥ 1 visible strategy shift per faction per session | — | — | — | ⬜ Not tested |

### Economy Balance Hypotheses

| # | Hypothesis | Target | S1 | S2 | S3 | Status |
|---|-----------|--------|----|----|----|--------|
| VE-01 | Floor Act is a rarely-needed safety net, not a regular play | ≤ 1 use per faction per session; frequent use (2+) signals economy imbalance | — | — | — | ⬜ Not tested |

*Note on VE-01: If Floor Act is being played often — especially by the same factions repeatedly — investigate resource generation rates and card costs before attributing to player skill.*

### Playtest Variables (design locked, watching for adjustment signals)

| ID | Variable | Watch For |
|----|----------|-----------|
| PT-02-02 | Affinity bonus — uncapped | Income dominance by Ghost or Syndicate by Quarter 4 |
| PT-02-03 | Portrait per-action scoring values (+2/+1/0/−1/−2) | Do Chronicle entries feel proportionate to table behavior? |
| PT-02-04 | Passive generation — 1/quarter | Is 1/quarter sufficient for factions with limited early presence? |
| PT-PC-01 | Playtest session sequence (3P → 5P → 2P) | Does sequence order mask or surface bottlenecks? |
| PT-04-01 | Modifier card play cost — Option A (free) | Do free modifier cards skew late-game balance? |
| PT-04-02 | Deck composition selection (24/30 covert, 12/20 political) | Does pre-session deck building produce meaningfully different postures? |
| PT-04-03 | Ghost 4-operation rule balance with new card system | Does Ghost dominate Beat 3? Does political pass cost feel weighted? |

---

## Section 3 — Playtest Data Collection Protocol

**Purpose:** Define who records what, when, and in what format during an actual playtest session, so data is consistent across sessions and can be compared against validation targets.

**Recorder:** One dedicated observer per session who is not playing a faction or ARBITER. If no dedicated observer is available, assign recording duties to ARBITER for mechanical data and one faction player for qualitative notes.

### Before the Session

| What | Who | Format |
|------|-----|--------|
| Record player count, faction assignments, date, and session number | Recorder | Header on Session Record sheet |
| Record deck compositions selected (covert 24/30, political 12/20 per faction) | Recorder | Deck composition table — one row per faction |
| Note any rule variants or modifications in use | Recorder | Free text |

### During the Session — Mechanical Data (Per Quarter)

| What | Who | Format |
|------|-----|--------|
| Quarter duration (start → end of Resolution) | Recorder | Time log — one row per quarter |
| Beat 3 (covert resolution) duration | Recorder | Subrow of time log |
| Beat-level duration targets (removed from Artifact 03 session 15 — for playtest reference only): Beat 1 ~30s, Beat 2 ~90s, Beat 3 ~3 min, Beat 4 ~90s | — | Compare against time log |
| ARBITER errors or corrections (rule lookup, incorrect resolution, re-adjudication) | Recorder | Tally per quarter |
| Covert operations submitted per faction | Recorder | Count per faction per quarter |
| Political acts submitted per faction | Recorder | Count per faction per quarter |
| Incursion uses (who, target district, outcome) | Recorder | Event log |
| Accord proposals (proposing faction, parties, outcome: agreed / failed / broke) | Recorder | Event log |
| Floor Act uses per faction (VE-01) | Recorder | Tally per faction per round |
| Modifier cards played per faction | Recorder | Tally per quarter |
| Burst Play triggered (yes/no per faction) | Recorder | Flag per faction per quarter |

### During the Session — Board State Snapshots

| When | What | Format |
|------|------|--------|
| End of Quarter 4 | Resource counts per faction (all five resource types) | Snapshot table |
| End of Quarter 4 | District presence counts (Dominant / Established / Present / Contested) | Board snapshot — 22 districts |
| End of Quarter 6 | Chorus Node presence state (who is at Present or Established) | Single-row note |
| End of Quarter 8 | Final VP tallies (public VP, private VP, Portrait VP, total) | Scoring sheet |
| End of Quarter 8 | Final Chorus Portrait track positions per faction | Track photo or manual record |
| End of Quarter 8 | Vote outcome | Result note |

### After the Session — Qualitative Capture

| What | Who | Format |
|------|-----|--------|
| Post-session survey: "Would you want to play Session 2 before leaving?" (yes/no) | All players | Anonymous quick poll |
| Post-session survey: "Would you want to run ARBITER again?" (yes/no) | ARBITER player | Anonymous quick poll |
| Debrief: unprompted conversation time (timer starts after Chronicle is read) | Recorder | Duration in minutes |
| Players' ability to describe opponent strategy unprompted | Recorder | Qualitative note per faction |
| Players' reference to the vote in post-session discussion | Recorder | Yes/no flag |
| ARBITER's assessment: was the Chronicle account accepted? | ARBITER | Qualitative self-report |
| Any mechanic that generated confusion, stalling, or repeated rule lookups | Recorder + ARBITER | Free text |
| Notable emergent behavior (unexpected strategies, surprising Accord formations, Apex attempt) | Recorder | Free text |

### Data Storage and Review

- All session records stored in `~/Projects/TheSignal/Session/` as `Playtest_Session_N_Records.md`
- After each session: update Validation Target Dashboard (Section 2 above) with session data
- After three sessions: review all playtest variables (PT-xx) and flag any warranting design adjustment
- Flag economy issues for PM02 open decisions review before scheduling additional sessions

---

---

## Section 4 — Considerations for Playtest Coordination Phase

*Items to evaluate when transitioning from design to active playtesting. Not blocking current work.*

**Playtest PM methodology** — When we move into active playtesting, coordination will start to look more like traditional project management: scheduling participants, tracking feedback across sessions, managing a version against a test cohort. Standard game PM skills and tabletop playtesting best practices (not generic software/corporate PM frameworks) should be reviewed at that time. Research and incorporate what's relevant into our own system. Flagged session 11.

---

*End of PM05 — Active Punch List v1.4*
