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
| Conceal | Transform | Component placed or returned face-down or closed |
| Flip | Transform | Physical orientation changed — not an information state change |
| Corrupt | Transform | A physically written or recorded value is altered |

Core sequence: Remove → Transform? → Place. Human hand is implicit intermediary — not modeled.

---

## Layer Vocabulary (§4.2)

| Layer | Visibility | Governs |
|-------|-----------|---------|
| Territory | Public | Presence tokens, structures, control flags, spatial markers |
| Economy | Public | Native resources, token counts, card counts, Accord existence |
| Information | Private → Public | Token content, written records, attribution, reconnaissance |
| Submission | Split (covert=private, PA=public) | What enters resolution queue: costs, eligibility, blocks, scope |
| Resolution | Split by phase | d100 system: threshold, modifier stack, difficulty, outcome scale |
| Standing | Split (PS=public, Portrait=private) | Reputation tracks: Public Standing and Portrait |

*"Cross-Category" is retired — all cards have a primary layer assignment.*

---

## Function Vocabulary (§5.1)

| Function | Definition | Primary Verb(s) |
|----------|-----------|----------------|
| Add | Brings new element into active play from supply | Add |
| Remove | Takes element out of active play | Remove |
| Redirect | Changes ownership, destination, or allegiance | Move |
| Recover | Returns spent/removed/degraded element to active play | Add |
| Modify | Alters cost, value, or attribute without changing fundamental state | — (abstract constraint) |
| Protect | Preserves current state against a named change | — (meta-constraint) |
| Block | Prevents another action from being initiated or resolving | — (meta-constraint) |
| Copy | Duplicates another action's effect chain with new initiating subject | Invoke |
| Reveal | Makes hidden information visible to named audience | Reveal |
| Conceal | Places information or attribution into hidden state | Conceal |
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

Corrupt targets are strictly: Intel tokens · Accord agreements · Target Profile. Only components with physically written values in the paper prototype.

---

## Construction Logic

**A card's taxonomy = Layer — Function — Subject.**

- **Layer** = which game system the card affects (not narrative, not phase)
- **Function** = what the card does to that system
- **Subject** = the specific component or attribute targeted

Key assignment rules:
1. Same physical verb can serve different Layers — assign Layer by design intent, not by verb.
2. **Dual-aspect components:** count = Economy; content = Information. Assign by dominant design intent (e.g., C05 Gather adds an Intel token but intent is intelligence acquisition → Information/Add/IntelToken).
3. **Protect** assigns to the layer of the protected target.
4. React/Instant/interrupt is timing only — the card still carries its own Layer/Function/Subject.
5. Modifier cards and Pass cards are excluded from taxonomy entirely.
6. Corrupt applies only to physically written/recorded values. Invalid targets: printed card text, marker positions, Chronicle.
7. Portrait is ARBITER-sole-mover — player cards affect Public Standing only (Standing/Shift/PublicStanding).
8. No persistent temporary cross-round effects — effects are either immediate (this Quarter) or permanent (rest of session).
