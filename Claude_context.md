# THE SIGNAL — agy Outbound Consulting Report
*Date: 2026-06-29*

## Session Handoff Report for Claude & Opus

**1. The "Target Profile" Manipulation Space Opened**
We established that TargetProfiles for Public Acts are placed face down on the FRG at **9.2.0 step 2** (not Beat 0). They are included with the action card in the ARG for covert actions. We officially opened this up as a mechanical surface area:
*   **Ghost (`GHO.CA.15` and `GHO.MOD.11`):** Ghost can now directly `Corrupt` Target Profiles. They can blindly swap face-down profiles (hijacking the paperwork), and they can wager at Beat 2 to silently rewrite the target of an opponent's Beat 3 Covert Op.
*   **Network (`NET.MOD.12` Forced Transparency):** Network can now `Reveal` Target Profiles. They can spend Exposure to force an opponent's face-down PA target to be flipped face-up immediately, stripping tactical ambiguity.

**2. Component-Verb Taxonomy is 100% Legalized**
*   We ran the `audit_card_alignment.sql` and found 4 cards attempting to `Add/Remove` the `PublicStanding` track. 
*   We corrected these to `Shift` the `StandingMarker` (affecting `GUI.PA.8`, `NET.PA.5`, `NET.MOD.11`, and `SYN.PA.4`). 
*   **Status:** The database audit is now perfectly clean with **0 Rules Gaps**. All 77 active cards use legal verb-component pairings.

**3. Art 04 Syntax & Database Synchronization**
*   We discovered massive drift in `04___Card_System.md` where 54 older cards were using legacy integer IDs (e.g., `id = 1`) and 11 newer cards were using placeholders (`id = "TBD"`).
*   We wrote and executed a Python script that bulk-updated every single Python code block in Art 04 to perfectly match the strict string `CardID` (e.g., `STD.CA.1`) tracked in the `the_signal_db` database. 
*   **Status:** The Markdown and the Database are now a 1:1 mirror. *(Note: This may be an outstanding PM05 sweep that Claude can verify and mark complete).*

**4. Procedural Boundary: Signed-off Artifacts**
*   Do not attempt to embed new faction rules (like Guild passive income) directly into `03___Round_Structure___Gameplay.md`. It is a signed-off procedural artifact. Faction mechanics must live in the Card System (`Art 04`), or changes to Art 03 must go through a formal amendment process.

**5. Taxonomic Classification of Ring Modifiers**
*   Ring Modifiers are universally available to all factions and must be placed under the Standard faction schema (e.g., `STD.MOD.R1.x`, `STD.MOD.R2.x`).
*   However, because they are drawn from a public pool during gameplay and not drafted, they must be instantiated with `subtype = RingModifier` (or similar designation) in the DB. This ensures they can be filtered out so they do not artificially inflate the 53-card minimum calculation for the draftable Standard palette.