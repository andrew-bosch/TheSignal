# Reference — Action Taxonomy (Art 04b)
*Load when: assigning Layer/Function/Subject to new cards, taxonomy disputes, 04b audit work.*

**S97 Architecture:** Physical verb definitions + Component × Verb Matrix → **Art 02 §13** (component source of truth). Primitive Action Model + Legalization Analysis → **Art 03 §22** (legality source of truth). Art 04b §3 is now a pointer only.

---

## 7 Physical Verb Primitives (Art 02 §13.1)

| Verb | DB Primitive | Definition |
|------|-------------|------------|
| Add | Place | Component enters active play from supply or off-board |
| Remove | Remove | Component exits active play to supply or off-board |
| Move | Remove + Place | Component relocates from one on-board location to another |
| Reveal | Transform | Component face/contents become visible to named recipients |
| Conceal | Transform | Component placed or returned face-down or closed *(physical system behavior — dispatch case, faction terminal, ARBITER screen; not a card-triggered function — L224)* |
| Flip | Transform | Physical orientation changed — not an information state change |
| Corrupt | Transform | A physically written or recorded value is altered |

Core sequence: Remove → Transform? → Place. Human hand is implicit intermediary — not modeled.

---

## Layer Vocabulary (§5.1)

| Layer | Visibility | Governs |
|-------|-----------|---------|
| Territory | Public | Presence tokens, structures, Dominant markers, spatial markers |
| Economy | Public | Native resources, token counts, card counts, Accord existence |
| Information | Private → Public | Token content, written records, attribution, reconnaissance |
| Submission | Split (covert=private, PA=public) | What enters the resolution queue: costs, eligibility, blocks, scope. Cards that affect whether and how an action reaches resolution — before the dice roll. |
| Resolution | Split by phase | The d100 system: threshold, difficulty, modifier stack, Battlefield Strength, outcome scale. Cards that alter how the queue resolves — at or during the dice roll, not the submission of the action. |
| Standing | Split (PS=public, Portrait=private) | Reputation tracks: Public Standing and Portrait |

*"Cross-Category" is retired — all cards have a primary layer assignment.*

---

## Function Vocabulary (§5.1)

| Function | Definition | Primary Verb(s) |
|----------|-----------|----------------|
| Add | Brings new element into active play from supply | Add |
| Remove | Takes element out of active play | Remove |
| Redirect | Changes ownership, destination, or allegiance | Move |
| ~~Recover~~ | **Retired S106 (04b-20)** — GR 7.2b: committed board states are final; restoring a prior board state retroactively modifies a committed state. | — |
| Modify | Alters cost, value, or attribute without changing fundamental state | — (abstract constraint) |
| Protect | Preserves current state against a named change | — (meta-constraint) |
| Block | Prevents another action from being initiated or resolving | — (meta-constraint) |
| Copy | Duplicates another action's effect chain with new initiating subject | Invoke |
| Reveal | Makes hidden information visible to named audience | Reveal |
| ~~Conceal~~ | **Retired S107 (L224)** — system behavior, not a card function; 7.2a prohibits hidden board state | — |
| Shift | Moves a track value (Public Standing, Portrait) up or down | Move |
| Corrupt | Alters a physically written or recorded value | Corrupt |

---

## Subject Vocabulary — Most Common (§5.2)

| Subject | Layer(s) typically used with |
|---------|------------------------------|
| Presence token | Territory |
| Structure block | Territory |
| Deployment marker | Territory |
| Native resource | Economy |
| Intel token | Economy / Information |
| Accord agreement | Economy / Information |
| Modifier card | Economy / Submission |
| Covert operation | Submission / Resolution |
| Public act / Political act | Submission / Standing |
| Action attribution | Information |
| Written record | Information |
| Public Standing | Standing |
| DebriefActionCard | Information |
| BroadcastCard (DB:25) | Information / Submission — public narrative half of the Broadcast two-component pair; used as selector when targeting the linked BEC |
| BroadcastEffectCard (DB:98) — ARBITER tableau, private | Information — mechanically applied effects; subject of GR 10.1b-domain Reveal (e.g., GHO.PA.4); linked by ID to its Broadcast Card |

Corrupt targets are strictly: Intel token faction-name field (location constraint applies) · Accord agreement terms · Accord named party (L227) · Target Profile. Only components with physically written values in the paper prototype.

**Intel token location constraint (L222):** Tokens are valid Corrupt targets ONLY when publicly placed (on a Public Act as payment, Beat 0–4). Tokens in faction terminal or ARBITER terminal are not reachable. Round-number field is additionally prohibited by 7.2b.

---

## Construction Logic

**A card's taxonomy = Layer — Function — Subject.**

- **Layer** = which game system the card affects (not narrative, not phase)
- **Function** = what the card does to that system
- **Subject** = the specific component or attribute targeted

Key assignment rules:
1. Same physical verb can serve different Layers — assign Layer by design intent, not by verb.
2. **Dual-aspect components:** count = Economy; content = Information. Assign by dominant design intent (e.g., STD.CA.5 Gather adds an Intel token but intent is intelligence acquisition → Information/Add/IntelToken).
3. **Protect** assigns to the layer of the protected target.
4. React/Instant/interrupt is timing only — the card still carries its own Layer/Function/Subject.
5. Modifier cards and Pass cards are excluded from taxonomy entirely.
6. Corrupt applies only to physically written/recorded values. Invalid targets: printed card text, marker positions, Chronicle, Intel token round-number field (7.2b). Intel tokens must be in public-placement window to be reachable (L222).
6b. InfluenceTier is not a targetable component — it is derived from token counts. Only board state changes (add/remove tokens) affect tier (L223).
7. Portrait is ARBITER-sole-mover — player cards affect Public Standing only (Standing/Shift/PublicStanding).
8. Card effects use exactly one of four valid duration types: **Immediate** (resolved at beat; no lingering marker) · **Transient** (removed at end of current Month) · **Seasonal** (removed at end of current Quarter / Phase 21) · **Permanent** (persists until a named action or condition removes it). No card creates a state that expires after a defined number of Quarters. *(Art 04b §4.7)*

---

## Key Governing Rules for Card Design

**§4.8 — ARBITER is the information authority (corollary to GR 10.1).** ARBITER is the only entity that can surface hidden information while preserving the covert structure. ARBITER-reveal is outside GR 10.1 because ARBITER holds nothing strategically — its disclosure is the game's information system functioning, not a faction act. Faction Reveal = creates a stake (§4.15 below); ARBITER Reveal = game function. **Portrait is the sole carveout:** never disclosed as a product of any card, script, or ARBITER procedure. *(Art 00a GR 10.1b)*

**§4.15 — Reveal creates a stake, not a compulsion (GR 10.1).** The Reveal function does not force a player to disclose. It creates a consequence for the holder's choice — reveal and gain the benefit (or avoid the penalty), withhold and accept the alternative. The decision belongs to the holder; the card sets the stakes. Any card where the Reveal effect fires without the holder's choice is a GR 10.1 violation regardless of framing.

**§4.16 — Income generation is untouchable (GR 9.1).** No card may directly modify a faction's income generation — neither suppress it nor amplify it beyond board state. InfluenceTier is not a targetable component; it is derived from token counts. A card can affect income only by changing the underlying board state (add/remove tokens), which changes the tier, which changes income naturally. Distinguishes Economy|Remove|NativeResource (permissible — removes current holdings) from income suppression at Upkeep (prohibited). DIR.PA.4 Regulatory Downgrade and DIR.PA.5 Regulatory Freeze are BLOCKED on this basis.

---

## Layer × Function Validity Matrix (Art 04b §5.1)

`✓` = valid design space. `—` = prohibited by governing rule or physical constraint.

| Layer | Add | Remove | Redirect | Modify | Protect | Block | Copy | Reveal | Shift | Corrupt |
|-------|-----|--------|---------|--------|---------|-------|------|--------|-------|---------|
| Territory | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Economy | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ |
| Information | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Submission | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Resolution | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Standing | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — |

*Invalid cells (—):*
- Territory and Economy | Reveal: layer is fully public — no hidden state to surface
- Territory | Corrupt: component positions tracked by physical placement, not written values
- Resolution | Corrupt: no physically written or recorded values in the resolution system
- Standing | Add / Remove: subsumed by Shift
- Standing | Reveal: PS is public; Portrait is the sole prohibited reveal target — never surfaced by card effect (GR 10.1b)
- Standing | Corrupt: track positions are physical markers, not written values
- All non-Standing | Shift: Shift applies only to Standing track values

*Three Corrupt exclusions (Territory, Resolution, Standing) governed by §4.6 (Corrupt scope definition).*
