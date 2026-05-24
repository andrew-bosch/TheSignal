# THE SIGNAL — Gemini Context Brief
*Last updated: 2026-05-24 — Session 32*

This file is a memory transfer from Claude Code (the primary artifact-writing collaborator) to Gemini. It summarizes project state, conventions, active priorities, and collaboration structure so Gemini can operate with full context.

---

## Cross-Model Sync Protocol

**How this works:** Andy is running both Claude Code and Gemini simultaneously on the same Raspberry Pi, two monitors, swivel-chair between them.

- **This file (`GEMINI_CONTEXT.md`)** — written and updated by Claude Code. Synced to Google Drive via rclone at session end. Gemini reads it from Drive.
- **`Claude_context.md`** — written and updated by Gemini. Synced via Drive. Claude Code pulls from Drive at session start and reads it if updated.
- **Sync cadence:** rclone runs in both directions — pull from Drive at session start, push to Drive at session end. No git pull involved; rclone is the cross-model sync mechanism.

**To update Claude Code:** Write updates to `Claude_context.md` in the TheSignal root. Andy will ensure it gets into the repo. Keep it additive — flag what changed, what was verified, what needs attention.

**To update Gemini:** Read this file from Drive. Claude Code will keep it current.

---

## Schema Status Update (2026-05-24)

Gemini flagged a potential FK type mismatch in `Claude_context.md` and recommended a refactor. Claude Code verified against the live schema — **no mismatch exists.** The schema is correctly aligned as-built:

- `card_types.id` and `card_subtypes.id` → `int(11)` ✓
- `card_metadata.card_type_id` and `card_metadata.card_subtype_id` → `int(11)` ✓  
- All other PKs/FKs → `bigint(20)` ✓

No DDL changes needed. The recommended refactor would have been a no-op. Schema is clean.

---

## What This Project Is

**THE SIGNAL** is a negotiation/area-control tabletop game for 2–6 players (up to 5 faction players + 1 ARBITER). Currently at L1: paper prototype. Full arc = 8 sessions (Quarters). Future layers (L2+) add ESP32 terminals and digital/physical hybrid play.

**Project lead:** Andy  
**Primary working directory:** `/home/abosch/Projects/TheSignal/`  
**Git remote:** `https://github.com/andrew-bosch/TheSignal` (private)  
**Google Drive sync:** `"googledrive:The Signal Workspace"` — synced via rclone, kept current

---

## File Structure

```
TheSignal/
├── V1/                  — Active design artifacts (canonical)
├── Creative/            — World-building: characters, vignettes, stories, quotes
├── Session/             — Session management files (Save State, SESSION_BRIEF, PM docs)
├── ClaudeIOS/           — iOS creative session summaries
│   ├── new/             — Unprocessed summaries (check here first)
│   └── Archive/         — Processed summaries
├── Retired/             — Superseded artifacts
└── PITCH.md             — Project pitch reference
```

---

## PM File Purposes

| File | Purpose |
|------|---------|
| PM01 | Charter / WBS |
| PM02 | Decision Log (locked decisions L01–L140+) |
| PM03 | Master Artifact Index (sign-off tracking) |
| PM04 | Glossary |
| PM05 | Punch List (active work items) |

---

## Active Artifact State (as of Session 31)

| Artifact | Version | Status |
|----------|---------|--------|
| Artifact 04 — Card System | v0.9.17 | 🔄 In Progress |
| Artifact 03 | v1.7 | ✅ Signed Off (Session 20) |
| Artifact 02a | v1.4 | ✅ Signed Off (Session 22) |

**Current work item:** C11–C15 re-sign-off in Artifact 04 (ref: 04-23)  
**Pending:** Political Acts P01–P18 (04-01), faction-specific cards C16–C35

**Note:** C10 design review flagged — feedback that C10 conflicts with 02a's influence difficulty rules for structure removal. Needs discussion before re-sign-off continues.

---

## Key Design Conventions

- **ARBITER** — always all-caps, no exceptions
- **All other game terms** — Title Case
- **Material vs. Non-Material changes:** Material = contradicts or extends signed-off content → requires re-sign-off in PM03. Non-material = terminology, formatting → no re-sign-off; note in PM02 Change Log.
- **Design Pillar 6:** If mechanical and narrative reasoning conflict, narrative takes precedence. If the narrative reason for a rule cannot be stated, the rule may be arbitrary.
- **Narrator Voice Test:** Every Narrative field — could this have been written by a human who knows too much, *or* by ARBITER in The Witness register? Both readings must remain valid.

### ARBITER's Four Registers
1. **The Record** — flat, precise, factual
2. **The Observation** — oblique, atmospheric, narrative
3. **The Reckoning** — rare, direct, personal. Always true. Used sparingly.
4. **The Witness** — expository, observational. Deliberately indistinguishable from the Narrator's voice.

---

## The Five Factions

| Faction | Resource | Core Belief |
|---------|----------|-------------|
| Ghost | Findings | Understanding must precede action |
| The Network | Exposure | No one gets to decide this in the dark |
| The Syndicate | Capital | Control comes from positioning early |
| The Guild | Capacity | The response must demonstrate humanity at its best |
| The Directorate | Mandate | Survival requires control, restraint, and continuity |

---

## MariaDB — New (Session 32)

A database has been set up for structured game data. Schema-only at this point — no data populated yet. Structure-before-data is intentional.

- **Database:** `the_signal_db`  
- **Credentials:** `~/Projects/TheSignal/mariadb_credentials.md`  
- **phpMyAdmin:** running locally

### Current tables
`components`, `card_metadata`, `card_types`, `card_subtypes`, `factions`, `beat`, `game_actions`, `action_costs`, `action_valid_targets`, `action_restrictions`, `card_faction_modifiers`, `game_zones`, `component_valid_zones`, `city_rings`, `district_metadata`, `district_connections`, `player_metadata`, `live_state`, `setup_state`, `allocation_types`

**`components`** is the backbone — all physical/logical game pieces hang off it.  
**`live_state`** tracks runtime positions; **`setup_state`** captures starting configuration.

### Known schema gaps (to be resolved before data population)
- Negotiation / deal state (no table for agreements, terms, parties, status)
- Control and influence per district at runtime
- ARBITER action taxonomy (may need separation from player actions)
- Scoring / victory condition tracking
- The Signal token / resource modeling

**Next step:** deep dive into design + PM docs → full gap analysis → finalize schema

---

## Multi-Model Collaboration Structure

| Model | Role |
|-------|------|
| **Claude Code** (this project's primary) | Locked decisions, artifact writing, PM management, session continuity |
| **Gemini** (you) | Deep context reads, full-corpus analysis, cross-artifact consistency checks |
| **Copilot / GPT** | Brief stress-testing, iteration feedback, external perspective |

**The Signal files are local-canonical.** Google Drive copy is kept current via rclone sync at session end.  
**Do not treat Drive as the source of truth** — always work from `/home/abosch/Projects/TheSignal/`.

---

## Creative Pipeline

**CREATIVE_BRIEF.md** (V2) lives in `ClaudeIOS/new/` — the current working version. It is the primary brief for all world-building generation. It has been iterated with Copilot feedback and True State integration.

**True State** (`Session/PRIVATE___True_State.md`) — contains ARBITER's actual nature. Not in the Creative Brief. Referenced only when writing ARBITER or Chorus content directly. Do not surface its contents in generated creative work.

**Creative content** lives in `Creative/` organized by type: `Characters/`, `Vignettes/`, `Stories/`, `Quotes/`.  
Nothing from a creative session is automatically canonical — Andy evaluates every submission.

---

## Collaboration Signals (Andy's shorthand)

| Signal | Meaning |
|--------|---------|
| `lock it` | Write to PM02 immediately + artifact content |
| `flag it` | Add to PM05, non-blocking |
| `carry` | Defer to next session |
| `dual check` | Test fiction + mechanical; report both readings |
| `first pass` | Already assessed — reporting findings, not handing back |

---

## Session Continuity Note

Claude Code maintains a persistent memory system at `/home/abosch/.claude/projects/-home-abosch/memory/`. This file supplements that memory for cross-model continuity. When in doubt about current artifact state, read `Session/SESSION_BRIEF.md` — it is the lean, authoritative startup document updated at every session close.
