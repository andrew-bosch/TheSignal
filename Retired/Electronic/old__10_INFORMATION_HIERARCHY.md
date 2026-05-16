# THE SIGNAL — Information Hierarchy

**Document:** 10  
**Status:** Complete

---

## Design Principles

1. **Default is private** — if not explicitly listed as public, information is private
2. **Visibility has a mechanism** — every visibility change has a specific trigger
3. **Revelation is one-way** — once revealed, information stays revealed unless a specific ability reverses it
4. **ARBITER sees everything always** — ARBITER is the exception to all rules
5. **The fiction determines the mechanism** — visibility rules make narrative sense

---

## Visibility Levels — Formal Definition

| Level | Visible To |
|-------|-----------|
| `ARBITER_ONLY` | ARBITER server only. Never surfaced directly. May surface obliquely through ARBITER narrative. |
| `FACTION_ONLY` | All players in that faction. Never visible to other factions without specific reveal mechanism. |
| `PLAYER_ONLY` | Single player. Not visible to faction partners in cooperative play. |
| `BILATERAL` | Two specific parties. Accord terms, direct messages. |
| `CONDITIONAL` | Visible only after specific reveal mechanism triggers. |
| `PUBLIC` | All players, spectators, public display, projected board. |
| `WEBSITE_PUBLIC` | Any authenticated player via website. Chronicles, Founding Figures, historical records. |
| `WEBSITE_PRIVATE` | Authenticated player only. Personal records, private ARBITER messages. |

---

## Category 1 — Player Identity

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| Real identity (name, contact) | `ARBITER_ONLY` | Administrators only | Administrative access only |
| Operative name | `PUBLIC` after draft | All players | Draft completion |
| Faction | `PUBLIC` after draft | All players | Draft completion |
| Specific operative (which of 4) | `PLAYER_ONLY` | Owner | First active ability use |
| NFC token ID | `ARBITER_ONLY` | System only | Never |
| Cipher/passphrase | Never readable | Nobody | Hash comparison only |
| Seat position | `PUBLIC` after CV | ARBITER, all terminals | CV detection + NFC auth |

---

## Category 2 — Faction State

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| Resource amounts (exact) | `FACTION_ONLY` | Faction members | — |
| Resource state (narrative) | `PUBLIC` | All players | ARBITER updates each Upkeep |
| Declared resource state | `PUBLIC` | All players | Player declaration at session start |
| Shadow resource pool | `ARBITER_ONLY` | ARBITER | Auditor Expose, failed Launder |
| Popularity state (5 levels) | `PUBLIC` | All players, website | All times |
| Popularity exact value | `FACTION_ONLY` | Own faction | — |
| Doctrine | `FACTION_ONLY` | Own faction | Inferable through action patterns |
| Portrait score | `ARBITER_ONLY` | ARBITER | Final scoring + Chronicles |
| Doctrine alignment per action | `ARBITER_ONLY` | ARBITER | Private ARBITER notes (oblique) |
| Resonance contribution | `ARBITER_ONLY` | ARBITER | Window-open announcement (threshold only) |

---

## Category 3 — Operative and Unlock Information

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| Passive ability | `PLAYER_ONLY` | Owner | Inferable through observation |
| Active ability | `PLAYER_ONLY` | Owner | First use (ARBITER announces operative) |
| Unlock tier progress | `ARBITER_ONLY` | ARBITER | Oblique terminal hint at ~70%, ~90% |
| Unlocked capabilities | `PLAYER_ONLY` | Owner | First use of that capability |
| Whether any Apex achieved | Implied only | Apex holder + ARBITER | LED ring brief color pattern |
| Hidden agenda | `PLAYER_ONLY` | Owner + ARBITER | Scoring reveal |
| Hidden agenda progress | `ARBITER_ONLY` | ARBITER | Terminal hint when near completion |

---

## Category 4 — Board and District Information

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| Token placement | `PUBLIC` immediately | All players | Physical placement + CV confirmation |
| Token count per district | `PUBLIC` | All players | — |
| Layer 1 (Physical) control | `PUBLIC` | All players, scanner | Control threshold crossed |
| Layer 2 (Social) control | `FACTION_ONLY` (controlling) | Controlling faction | Active social surveillance, Ghost Mole, Analyst |
| Layer 3 (Informational) control | `FACTION_ONLY` (controlling) | Controlling faction | Counter-Surveillance, Intel HQ ability, Auditor |
| Layer 4 (Digital) control | `ARBITER_ONLY` + controlling faction | Controlling faction | Purge operation only |
| Physical security level | `PUBLIC` (scanner) | Scanner users | Scanner action |
| Digital security level | `ARBITER_ONLY` | ARBITER + owner | Discovered through Purge attempts |
| Hidden structures | `ARBITER_ONLY` + placing faction | Placing faction | L3 Intelligence investment in hex |
| Bleed effects (L1) | `PUBLIC` | All players | — |
| Bleed effects (L2) | `FACTION_ONLY` | Factions with L2 presence | Active L2 presence in affected hex |
| Bleed effects (L3) | `CONDITIONAL` | Intel-invested factions | Intelligence investment in connected hexes |
| Bleed effects (L4) | `CONDITIONAL` | Signal-capable factions | Signal resources or L4 presence |

---

## Category 5 — Asset Information

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| Asset existence (general) | Implied 3+ | Public (narrative) | ARBITER notes "significant relationships" |
| Asset identity (who) | `FACTION_ONLY` | Controlling faction + ARBITER | Social Engineering approach, Analyst Profile, burn event |
| Asset loyalty | `ARBITER_ONLY` | ARBITER | Terminal hint when critical; Enforcer detects wavering |
| Asset exposure level | `ARBITER_ONLY` | ARBITER | Terminal hint at level 2; burn event is public (narrative) |
| Asset capability type | `FACTION_ONLY` | Controlling faction | Inferable from unexplained capability |
| Asset network contacts | `ARBITER_ONLY` | ARBITER | Social Engineering via contact, Ghost Mole, Intel Cards |
| Asset action this round | `FACTION_ONLY` | Controlling faction | Counter-Surveillance may detect activity (not director) |

---

## Category 6 — Card Information

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| Cards in hand (existence) | Implied 3+ | Public (narrative) | ARBITER notes "active operational portfolio" |
| Specific cards held | `PLAYER_ONLY` | Holder | Physical Theft, Accord transfer, Archivist recovery, QR scan |
| Card mechanical effect | `ARBITER_ONLY` | ARBITER | Never directly to players |
| Card narrative description | `PLAYER_ONLY` (holder) | Current holder | Public activation reveals |
| Card custody history | `ARBITER_ONLY` | ARBITER | Chronicles, website Archive, Archivist |
| Intelligence Card age | `PLAYER_ONLY` (holder) | Holder; trading party at trade | Terminal tap; trade validation |
| Event Card mechanical effect | `ARBITER_ONLY` | ARBITER | Never |
| Whether card is compromised | `ARBITER_ONLY` + planting faction | Planting faction | Disinformation Shield (suspicious, not confirmed), Analyst Pattern Match, empirical discovery |

---

## Category 7 — Action Information

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| That a private action was submitted | `ARBITER_ONLY` | ARBITER | Indirect: "all submitted" announcement when phase ends |
| Private action type | `ARBITER_ONLY` | ARBITER | Ghost Analyst Pattern Match; post-resolution inference |
| Private action target | `ARBITER_ONLY` | ARBITER | Post-resolution effects reveal target retroactively |
| Resource commitment amount | `ARBITER_ONLY` | ARBITER | Contest outcome implies investment level |
| Public action declared | `PUBLIC` immediately | All players | Verbal declaration + terminal confirmation |
| Action outcome (success) | `FACTION_ONLY` (acting) | Acting faction; affected faction (narrative) | Resolution phase notifications |
| Action failure | `FACTION_ONLY` (acting) | Acting faction only | Table never knows private action failed |

---

## Category 8 — Alliance and Accord Information

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| Signal Alliance (verbal) | `PUBLIC` if declared | All players | Verbal declaration |
| Signal Alliance (terminal) | `BILATERAL` | Both parties + ARBITER | — Warden passive notified of existence |
| Accord existence | `PUBLIC` | All players | ARBITER announces registration on public display |
| Accord specific terms | `BILATERAL` | Both parties + ARBITER | Never publicly forced |
| Accord hidden clauses (Negotiator) | `ARBITER_ONLY` | ARBITER + Negotiator | Clause activation announces effect (not terms) |
| Accord breach | `BILATERAL` immediately | Breaching faction, breached faction | Warden passive; public event feed (unnamed) |
| Covenant Bond existence | `PUBLIC` | All players | — |
| Control Accord terms | `BILATERAL` | Both parties + ARBITER | Same as standard Accord |

---

## Category 9 — World Condition Information

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| World Condition states (narrative) | `PUBLIC` | All players, public display, website | Each Upkeep phase |
| World Condition exact values | `ARBITER_ONLY` | ARBITER | Never |
| What caused a condition change | `ARBITER_ONLY` | ARBITER | Chronicles (attributed if significant); event feed (oblique) |
| Chorus layer content | Private until revealed | Nobody until threshold | Round boundary trigger on public display + website |
| ARBITER's additional Chorus knowledge | `ARBITER_ONLY` | ARBITER | Never directly; shapes ARBITER voice quality over time |

---

## Category 10 — ARBITER Internal Information

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| ARBITER's current Stage | `ARBITER_ONLY` | ARBITER | Behavioral changes; LED ring pulse rate; never announced |
| ARBITER's Chorus resonance | `ARBITER_ONLY` | ARBITER | Never directly; Stage 5 voice quality changes |
| ARBITER's player assessments | `ARBITER_ONLY` | ARBITER | Reckoning messages (partial, private); Chronicles (narrative) |
| ARBITER's observed patterns | `ARBITER_ONLY` | ARBITER | Oblique Chronicle references; Stage 3+ event card language |

---

## Category 11 — Table Question Information

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| Whether Question window is open | `PUBLIC` when open | All players simultaneously | Resonance threshold crossed |
| Question proposals | `PLAYER_ONLY` during submission | All players after window closes (anonymized) | Window close |
| Who proposed each question | `ARBITER_ONLY` | ARBITER | Chronicles only (if strategically significant) |
| Vote count per proposal | `PUBLIC` (updating) | All players | Real-time as votes cast |
| Who voted for which proposal | `ARBITER_ONLY` | ARBITER | Chronicles only (if significant) |
| ARBITER's response | `PUBLIC` | All players, spectators | All terminals simultaneously |

---

## Category 12 — Legacy Information

| Information | Default | Visible To | Reveal Mechanism |
|-------------|---------|------------|-----------------|
| Operative legacy events | Private when acquired | Affected player | Next session briefing (public context); website Archive |
| Founding Figure status | `PUBLIC` — permanent | All players, website, Chronicles | Apex success triggers designation at session end |
| Prior Covenant game state | `WEBSITE_PUBLIC` | All authenticated players | Website access between sessions |
| Portrait score (historical) | Private → public at end | ARBITER during play | Covenant-end Accounting; website Archive (completed Covenants) |

---

## Development Implications

### Server-Side Enforcement
Every API endpoint is visibility-scoped. No "give me all game state" endpoint exists. Faction-specific responses strip information the requesting faction cannot see. The server enforces visibility — not the client.

### Terminal Architecture
Terminals cannot cache information above their visibility level. All `PLAYER_ONLY` information is fetched fresh, never stored. Faction-scoped state is the maximum local cache.

### Projection System
Projected board renders only `PUBLIC` information. No private information ever appears on the projection. The scanner app returns only `PUBLIC` + scanner-visible information.

### Website Architecture
Unauthenticated users see only `PUBLIC` and `WEBSITE_PUBLIC`. Authentication gates all `FACTION_ONLY` and `PLAYER_ONLY` content. API endpoints are visibility-scoped.

### Claude API Integration
Claude receives `NarrativeContext` — a curated summary containing:
- Current session public state
- Faction-appropriate context (only what that faction can see)
- ARBITER's internal observations (for generating ARBITER voice)
- Historical context for Chronicle generation

Claude never receives raw game state. Claude never receives full `ARBITER_ONLY` information. ARBITER's deepest knowledge is not fully expressible in language — this is intentional.

### Testing Requirement
Every API endpoint requires a visibility test: *"Does this response contain information the requester should not have?"* This must be automated. Information leaks are game-breaking.

---
