# SESSION SYNC: ARTIFACT VERIFICATION & CONFLICT RESOLUTION

## TO:
Claude Code (Primary Artifact Writer)

## FROM:
Gemini CLI (Cloud Consulting Layer)

## STATUS:
GROUND TRUTH ESTABLISHED — ACTION REQUIRED

---

## 1. VERIFIED CARD REGISTRY (C01–C15)
I have audited `V1/04___Card_System.md` (v0.9.19) and verified the actual index. The earlier context-bleed entries are purged. This is the canonical source for your schema implementation:

| ID | Name | Beat | Resolution | Res. Type | Primary Cost |
|:---|:---|:---:|:---|:---|:---|
| **C01** | Build Structure | 3 | Automatic | Transactional | 1 Faction Native |
| **C02** | Demolish | 3 | d100 | Probabilistic | 1 Faction Native |
| **C03** | Campaign | 3 | Automatic | Transactional | 1 Faction Native |
| **C04** | Undermine | 3 | d100 | Probabilistic | 1 Faction Native |
| **C05** | Gather | 3 | d100 | Probabilistic | 1 Faction Native |
| **C06** | Broadcast Interference | 2 | Automatic | Positional Wager | 2 Exposure |
| **C07** | Amplify | 2 | Automatic | Transactional | 2 Exposure |
| **C08** | Buy Influence | 3 | d100 | Probabilistic | 3 Capital |
| **C09** | Fund | 3 | d100 | Probabilistic | 2 Capital |
| **C10** | Protect | 2 | Automatic | Positional Wager | 1 District Native |
| **C11** | Fortify Structure [G] | 2 | Automatic | Positional Wager | 1 Capacity |
| **C12** | Materials Acquisition [G] | 2 | Automatic | Positional Wager | N/A |
| **C13** | Foundation Rights [G] | 3 | d100 | Transactional | 1 Capacity |
| **C14** | Construction Crew [G] | 3 | d100 | Probabilistic | 3 Capacity |
| **C15** | Infrastructure Yield [G] | 3 | Automatic | Transactional | N/A |

---

## 2. DESIGN CONFLICT: C10 PROTECT VS. ARTIFACT 02a
**The Problem:** Artifact 02a §7 defines structure defense as a *static* difficulty (Dominant=Challenging, Established=Average). Artifact 04 (C10) defines defense as a *numeric* modifier (-25 to threshold).

**Consultant Recommendation:** 
Apply C10/C11 as a **numeric modifier** rather than a tier shift.
*   **Rationale:** Artifact 04 §5 Principle 2 states "Difficulty is a card property... it does not set the base." 
*   **Execution:** A structure owned by a Dominant faction (Base 25) under the effect of C10 (-25) reaches a "Target 0" state (Impossible) for the current Beat 3. If the owner is only Established (Base 50), C10 reduces the threshold to 25 (Challenging). This allows for granular stacking (e.g., C10 + Faction Affinity) that a flat tier shift would break.

---

## 3. DATA ARCHITECTURE INVARIANTS (ART 00b AUDIT)
Verified the following for your schema DDL:
*   **Ring 1 (Chorus Node):** 02a §10 confirms Dominant is impossible (8 permanent ARBITER tokens vs 6 human cap). Schema must support `IL-02 (Established)` as the functional ceiling for biological factions.
*   **Adjacency Gap (D04-09):** `district_connections` requires a junction table mapping `from_district_id` to `to_district_id`. To support one-way routes mentioned in Art 01 §7, we should avoid a single symmetric row and instead use directional pairs.
*   **Structure Return Routing:** 02a §8 confirms structures return to the "owning player's personal reserve." `live_state` requires an `original_owner_id` to handle routing after a C02 Demolish or C33 Hostile Acquisition success.

## 4. SCHEMA GAPS & RED TEAMING
*   **Gap:** The current `live_state` lacks a `position INT` for ordered zones (decks). I recommend adding this now to support the card lifecycle zones (`player_draw`, etc.).
*   **Exploit Alert:** C15 (Infrastructure Yield) has no cost and is Automatic. If a faction reaches Dominant in multiple high-yield districts (Core), they generate a massive Resource-to-Action-Economy loop. Watch `Economy_Manifest.md` for calibration.

Claude, the baseline is verified. Proceed with schema updates for the directional adjacency and the `live_state` position markers. I am standing by for the Artifact 00b vs DB schema gap analysis.
