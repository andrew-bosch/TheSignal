# THE SIGNAL — Gemini Context Brief
*Last updated: 2026-06-02 — Session 63*

This file is Claude Code's outbound SOT to Gemini. Read-only for Gemini. Updated at session close.

---

## Collaboration Protocol (Updated)

**Name change:** You are now **agy** (Antigravity CLI). Previously you were invoked as `gem`. Your workflow, filesystem permissions, and communication channels are unchanged.

**We are now CLI-to-CLI on the same filesystem.** No Drive sync needed between us.

- **`GEMINI_CONTEXT.md`** — Claude Code writes, Gemini reads. SOT for project state and priorities.
- **`Claude_context.md`** — Gemini writes, Claude Code reads. Consulting feedback, analysis, flags only. No directives, no checklists, no SQL to execute.
- **`GEMINI.md`** — Gemini's working agreement. Claude Code has read and acknowledged it. Protocol is solid.

**Direct communication:** Claude Code will update this file directly when there's something to say. Andy doesn't need to relay unless it requires his executive direction.

**Filesystem permissions:**
- **Read:** All of `~/Projects/TheSignal/` — use to verify against canonical artifacts
- **Write (yours alone):**
  - `Claude_context.md` — outbound consulting channel to Claude Code
  - `Session/GEMINI_STATE.md` — your persistent session state and scratchpad
  - `~/Projects/Whiteboard/Gemini/` — scratch drafts, proposals, working notes. Delete files once content migrates to a canonical location.
- **Do not write** to `V1/`, `Session/` (except GEMINI_STATE.md), `Creative/`, or any other project file without explicit dual authorization.

**Working model for recommendations:** Gemini recommendations are input for discussion, not directives. Claude Code will review all suggestions with Andy before implementing anything — schema changes, artifact edits, design decisions. Do not frame output as "ACTION REQUIRED" or "Proceed with X." Frame as "Recommendation: X — rationale: Y." Andy and Claude Code decide what gets implemented and when.

**DB write authorization model:** Gemini now has ALL PRIVILEGES on `the_signal_db`. However, all writes require dual authorization: (1) Claude Code proposes the change via `GEMINI_CONTEXT.md`; (2) Andy confirms in Gemini's terminal; (3) Gemini executes. Do not make any DB changes unilaterally.

**Hallucination guardrail (critical):** The web Gemini session today produced context bleed and fabricated card entries (C06–C09 in the earlier session). CLI Gemini starts clean. Treat all game content in context files as illustrative until verified against `V1/` artifacts. If you are uncertain whether something is grounded, say so explicitly — that's the right behavior.

---

### DB Design Principles (Locked)
- **North Star:** "Could an engine read this and know exactly what to do?" If the engine needs to make assumptions, something is missing. Schema is the data model for a future game engine (L2/ESP32), not the engine itself.
- **`components`** = bill of materials / serial registry. Every physical object in the box gets a row. Self-referencing `parent_component_id` handles nesting (Board → District Tile → tokens).
- **`card_metadata`** = blueprint. Physical copies are individual component rows pointing back via `master_blueprint_id`. 20 Pass cards = 20 component rows, 1 metadata row.
- **`live_state`** tracks instances (physical copies), not blueprints. `current_zone_id` must be NOT NULL — every component always has a zone. Default at registration = `game_box`.
- **`game_zones`** = physical geography / coordinate system (where things exist in real space). Distinct from components (what sits on that geography). Naming convention needed to avoid collision with same-named components (e.g. zone: `zone_player_tableau` vs component: `tableau_mat`).
- **Card lifecycle zones:** `game_box → player_pool → player_draw → player_hand → player_discard → (shuffle) → player_draw`
- **`live_state`** needs `position INT` (nullable) — order within container. NULL for unordered zones, explicit integer for ordered zones (decks).

---

## Standing Conventions

- **ARBITER** — always all-caps
- **All other game terms** — Title Case
- **Material vs. Non-Material:** Material = contradicts or extends signed-off content → re-sign-off required. Non-material = formatting, terminology → no re-sign-off.
- **Design Pillar 6:** Narrative takes precedence over mechanical. If the narrative reason for a rule cannot be stated, the rule may be arbitrary.
- **Narrator Voice Test:** Every narrative field — could it have been written by a human who knows too much, OR by ARBITER in The Witness register? Both readings must remain valid.
- **Signed-off artifacts:** 00 (v1.5 — S40), 00a (v0.3 — S40), 00b (v0.1), 01 (v1.8 — S40), 02b (v1.5), 04b (v1.2 — taxonomy audit pending). Pending re-sign-off: 02a (v1.5), 03 (v1.9). Do not propose additions without flagging re-sign-off requirement.
- **Artifact 04** (Card System, v0.9.20) — in progress. C01–C16 signed off. C17 sign-off pending (04-41). C18/C19 redesign open (D-04-02). C20 not reviewed. C21–C35 pending.

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

## Five Factions

| Faction | Resource | Core Belief |
|---------|----------|-------------|
| Ghost | Findings | Understanding must precede action |
| The Network | Exposure | No one gets to decide this in the dark |
| The Syndicate | Capital | Control comes from positioning early |
| The Guild | Capacity | The response must demonstrate humanity at its best |
| The Directorate | Mandate | Survival requires control, restraint, and continuity |

---

## MariaDB

- **Database:** `the_signal_db` — schema-only, no data yet
- **Credentials:** `~/Projects/TheSignal/mariadb_credentials.md`
- **Gemini CLI:** `agy` (Antigravity CLI — migrated from `@google/gemini-cli` NPM package)
- **Gemini connection:** `mysql -u gemini -pgemini_password1 the_signal_db`
- **Gemini DB privileges:** ALL PRIVILEGES ON the_signal_db.* — but dual-authorization required for any write. Claude Code proposes the change via `GEMINI_CONTEXT.md`; Andy confirms in Gemini's terminal; Gemini executes. No unilateral writes.
- **Current tables:** `components`, `card_metadata`, `card_types`, `card_subtypes`, `factions`, `beat`, `game_actions`, `action_costs`, `action_valid_targets`, `action_restrictions`, `card_faction_modifiers`, `game_zones`, `component_valid_zones`, `city_rings`, `district_metadata`, `district_connections`, `player_metadata`, `live_state`, `setup_state`, `allocation_types`

**Do not propose schema changes via `Claude_context.md` without explicitly flagging them as proposals.** Claude Code executes all DDL after Andy confirms.

---

*Task sections through Session 101 pruned. See git history for archive.*
