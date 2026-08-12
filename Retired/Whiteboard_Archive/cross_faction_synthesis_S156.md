# Cross-Faction Synthesis — S156 (PM05 09-16 step 5)

**Status:** Full-corpus cross-faction analysis, closing 09-16 steps 4–5. Awaiting Andy checkpoint; findings feed the consolidated review (PM05 09-17).
**Trigger to delete:** once step-5 findings are triaged at 09-17 and the synthesis verdict is logged to PM02.
**Scope:** all five faction sets (each already audited STD+faction, S156) compared against each other. Re-runs the retired 04-n110 synthesis (last pass S128, predated the 232-card modifier corpus). Baseline treated as an S119 snapshot, re-validated.
**Substrate:** the five S156 faction docs + system-level queries over `card_body`/`v_card_body`/`card_status`.

---

## 1. Differentiation — five distinct decks, confirmed

Layer signature per faction (effect-bearing cards; faction-specific counts):

| Layer | DIR | GHO | GUI | NET | SYN | (STD) |
|-------|----:|----:|----:|----:|----:|----:|
| Territory | 13 | 3 | 13 | 10 | 6 | 19 |
| Information | 2 | **18** | **0** | 5 | 4 | 5 |
| Economy | 4 | 4 | 10 | 6 | **13** | 15 |
| Submission | **6** | 3 | 2 | 2 | 3 | 5 |
| Standing | 2 | 2 | 3 | 5 | 2 | **16** |
| Resolution | 1 | 1 | 1 | 0 | 0 | 2 |

Each faction has a unique fingerprint: **Ghost = Information (18)**, **Guild = Territory+Economy with Information exactly 0** (the sharpest doctrinal signature — cannot operate covertly), **Directorate = Submission-heavy** (legislative), **Syndicate = Economy (13)**, **Network = broad + Standing-forward**. No two factions — adjacent or not — collapse into the same decision pattern. Differentiation holds, and is *stronger* than baseline now that the modifier lanes are voiced per doctrine.

**Board-control poles (baseline reaffirmed):** Directorate = sustained-pressure/suppression · Ghost = point-disruption/intelligence · Guild = fill-space/construction · Network = distributed/broadcast · Syndicate = transactional/economic. Five genuinely different control models.

---

## 2. The intelligence economy centers on Ghost (primary systemic finding)

Cards whose **cost** requires Findings or Intel tokens (Ghost's native / Ghost-keyed outputs):

| Faction | Findings-cost cards | Intel-cost cards |
|---------|----:|----:|
| Ghost | 20 | 9 (self — its own economy) |
| **Network** | 6 | 1 |
| **Syndicate** | 4 | 3 |
| **Directorate** | 2 | 3 |
| Guild | 2 | 0 |

**19 non-Ghost cards across Directorate/Network/Syndicate are gated on Ghost's native output.** Ghost is the structural producer/hub of the resource three other factions' key cards consume — Network's core broadcaster cards (CA.1/2/4/8), Syndicate's premium plays (CA.3/CA.7), Directorate's hardest suppression (CA.2/CA.5/PA.8).

Two consequences:
- **Ghost as broker/kingmaker.** Because resource trade is a free verbal procedure (Art 03 §11.0), Ghost's over-collection (deepest intel suite in the game) is directly tradeable leverage over three factions' ceilings. Ghost can enable or withhold — a soft-power position §5a implies ("every faction that fractures does Ghost's work") and the card economy now structurally backs.
- **Ghost-absent degradation (systemic watch).** In 2–4p games without Ghost, those 19 cards get materially harder (no natural Findings/Intel producer → 4:1 conversion or foreign-district holding only). The intel economy quietly *assumes Ghost is at the table.* Worth a deliberate design decision — is that acceptable, or do Findings/Intel need a secondary source in Ghost-absent configurations? (Generalizes NET-2, 04-n126.)

---

## 3. §9.2 economics — three buckets (baseline mono-grouping corrected)

The baseline recommended one mono-economy cross-resource pass over Directorate+Guild+Syndicate. The full-corpus audit re-sorts:

- **Mono (inversion by doctrine):** Directorate (Mandate), Syndicate (Capital) — expensive single-resource ceilings (DIR mostly ×2; SYN.CA.8 C×6, CA.10 C×3).
- **Native-cross:** Guild — Capacity + Capital/Mandate/Findings/Exposure on big builds (PA.9 = four types). *Left the mono set.*
- **Foreign-gated cross:** Ghost (flip-cost — the target's own resources) and Network (Findings-gated — Ghost's native).

Run the §9.2 pass by bucket, not by the old grouping.

---

## 4. Adjacency synergies (doctrinal ring: Ghost→Directorate→Guild→Network→Syndicate→Ghost)

Neighbors share philosophical proximity and, it turns out, mechanical hooks:
- **Ghost→Directorate:** Ghost supplies the Intel that Directorate's suppression needs (CA.2/CA.5/PA.8); both are constraint/suppression doctrines (point vs institutional). Natural ally supply line.
- **Directorate→Guild:** Directorate's Core structures *trigger Guild's passive income* (GUI.MOD.3/4 — "Directorate builds, Guild invoices"). Complementary board-fillers; Directorate suppresses, Guild builds into the space.
- **Guild→Network:** orthogonal domains (construction vs broadcast). Network's reactive presence spreads off public events — including Guild's visible building — so a build-heavy Guild indirectly feeds Network's expansion.
- **Network→Syndicate:** the §5a proxy-funding shadow relationship — a lateral bypass around Directorate visibility; both are Directorate antagonists.
- **Syndicate→Ghost:** Syndicate's premium plays are Intel-gated; Ghost is the supplier. Closes the ring (and reinforces §2).

The **Ghost node closes the ring on both sides** (Ghost→Directorate ally, Syndicate→Ghost supplier) — another reason Ghost is the system's economic pivot.

---

## 5. Opposition counters (non-adjacent = opposed)

- **Directorate × Syndicate (sharpest antagonism).** Syndicate CA.4 bypass *negates Directorate's Probabilistic suppression without a roll*; Syndicate's Ring-1/2 Dominance push directly violates Directorate's "no faction Dominant" win-leg. Capital vs authority, head-on.
- **Ghost × Network (dependency laid over rivalry).** §5a: Network attacks Ghost *informationally* — NET.CA.1/CA.3 expose covert ops, PA.3 opens hands, threatening Ghost's SCIF pipeline. Yet Network *depends on Ghost's Findings* for those very cards. The most interesting cross-faction tension in the set: your supplier is your predator.
- **Directorate × Network.** §5a: Network attacks Directorate *territorially*; Network's reactive presence-respawn (React presence engine) can re-spread after Directorate suppresses — suppression vs regeneration.
- **Guild × Syndicate.** Syndicate CA.3 (buy structure), PA.5 (extort expansion) *seize Guild's structures*; permanence doctrine vs hostile-takeover doctrine. Guild's PA.6 (sell structure in rival's currency) is the transactional counter-move.
- **Guild × Ghost.** Low direct conflict (no territory overlap); Ghost CA.14 (erase op) can still cancel a Guild build.

---

## 6. Matchup asymmetries — the "implied vs leverageable" cross-faction layer

Interactions that only appear in comparison:
- **NET.PA.3 toothless vs Guild** (the classic case): forcing "play with your hand visible or forfeit covert submissions" does nothing to a faction with no covert ops. A dead branch in exactly one matchup.
- **Syndicate CA.4 bypass** is strong vs Probabilistic enforcement (Directorate) but useless vs Automatic effects — matchup-dependent value.
- **Guild's non-scaling defense** (GUI-2) is exploitable by *any* multi-removal faction in one Quarter: Syndicate CA.3, Network PA.4, Directorate PA.3/CA.5 can each outpace Guild's one-protect-per-Quarter — a shared pressure vector on Guild.
- **Directorate suppression vs Network regeneration:** tier-push (Directorate) meets React-respawn (Network) — a war of attrition neither cleanly wins, by design.

**Leverageable cross-faction lanes (whether or not §5a named them):**
- Ghost = intel broker (§2).
- Syndicate = table deal-restructurer — CA.10/11 corrupt or transfer *any two factions'* accords; every bilateral agreement is a Syndicate asset.
- Guild = construction tax — passive income off everyone's STD.CA.1 builds.
- Network = standing warfare against the whole table (CA.7/PA.5/MOD.2/3/11 + STD.PA.4/5).
- Directorate = double suppression (territorial *and* reputational, via PS-warfare MODs).

---

## 7. System-level findings / gaps

- **[systemic]** Intel economy assumes Ghost at the table — 19 Ghost-gated cards across 3 factions degrade in Ghost-absent games. Design decision needed (§2). Generalizes NET-2 / 04-n126.
- **[systemic]** **Standing is STD-provided** (16 STD vs 2–5 faction). Factions are standing-thin without the shared pool — confirms the STD+faction denominator is *load-bearing*, not a nicety.
- **[systemic]** **Resolution is the rarest layer** — 5 faction cards total (1 each DIR/GHO/GUI, 0 NET/SYN) + 2 STD. Either deliberate niche or a system-wide under-use worth a deliberate call.
- **[systemic]** The **free-trade rule (Art 03 §11.0) is load-bearing** for the entire cross-resource economy (all the Ghost-hub dependencies resolve through it) yet is uncarded by design — fine, but it means the *table procedure*, not the card set, carries a core economic subsystem. Ensure it's prominent in rules teaching.
- **Two genuine open items above schema noise:** Ghost **CA.11 Signals Analysis blocked on Art 06** (a doctrine keystone), and Network **Tripwire** (verify built or unbuilt). Everything else is tracked schema/stub cleanup.

---

## 8. Overall verdict

The five-faction system is **well-differentiated, doctrinally coherent, and materially more complete than at the S119–128 baseline** — the modifier corpus (S154) closed nearly every faction's largest baseline gap. Cross-faction play is rich and *asymmetric* (matchup-dependent branches, dependency-over-rivalry tensions, five distinct control poles). The one system-level structural question worth a deliberate decision is the **Ghost-centered intelligence economy** and its Ghost-absent degradation. No differentiation failures; no doctrine incoherence. Art 04's card-set design is in strong shape pending the 09-17 triage of the tracked flags.
