# THE SIGNAL — Session Brief
**Session 157 next | Updated: 2026-08-05**

Lean startup document. Full session history: `Session/THE_SIGNAL___Project_Save_State.md`

---

## Read These First — Every Session

**Before any design, procedure, or card work:** read `Reference/read_first.md` once per session if you haven't already (explains what this directory is and isn't), then:
- `Reference/design_reference.md` — governing principles, card design rules, schema discipline
- `Reference/design_reference_card_system.md` — Art 04 schema, enums, field conventions
- `Reference/ref_*.md` — pick files relevant to the task (procedures, taxonomy, tracking, card types, components, resources, board narrative)

Terminology, methodology, governing rules, and registered decisions live in those files. Do not rely on SESSION_BRIEF for any of that.

**Art 04 file location (S136):** Card content is split across 8 files — `04___Card_System___Part1_Core.md` (§1–6, §8–15), `Part2_Standard.md`, `Part3_Ring_Modifiers.md`, `Part4a_Guild.md`–`Part4e_Syndicate.md`. Edit these directly. `04___Card_System.md` is a generated build artifact (`tools/assemble_card_system.py`) — never edit it, regenerate it after any Part edit.

**Card design content must stand on its own (locked S142, PM02 L276):** Design Rationale/design_note/arbiter_note must never reference or compare against other cards for explanation — cards are self-contained. A separate strategy-guide artifact is the right home for cross-card comparison, if ever wanted. Checklist Notes: ✓ rows get only the pass-justification (no session numbers, no log-item citations); ⚠ rows describe the issue itself; detailed issues go in an Outstanding Issues section below the checklist, not the Note cell.

**Clean-card rule (locked S154):** A finished card carries **zero** inline `#` comments and **no `arbiter_note`** — printed cards ship with neither. Any comment or note still present is a live signal that Art 03 doesn't yet cover that card's mechanic as a general, printable-independent procedure (or the card needs redesigning to fit one) — not documentation to preserve. The old `# scaffolded, not addressed` marker convention is retired (4,685 instances stripped corpus-wide S154, all confirmed pure noise). "Supported by game procedure" checklist row must be ⚠, not ✓, on any card still carrying either — see PM05 04-n221 for the current tracked list (95 cards, genuine Art 03 gaps after redundancy triage).

---

## Startup Delivery

After reading context files, deliver to Andy:
1. **Last session accomplishments** — summarize from "S[N] Accomplishments" below
2. **Current focus** — list open tracks from "Current Focus" below
3. **Pending sign-offs** — list from "Pending Sign-offs" below

Then prompt: *"What's our focus today?"*

---

## S156 Accomplishments (closed)

**DB-queryable Art 04 bodies — the goal's second step delivered (PM02 L356):** new `card_body` (EAV mirror of every `Card()` field, ~16k rows / 384 cards incl. GD-01), `card_restriction_clause` (restriction decomposed to subject/op/value), and `v_card_body` pivot view in `the_signal_db`. `.md` stays SOT; re-syncable via `tools/extract_card_body.py` + `Database/card_body_schema.sql`. This turned the full faction audit from the ~6-session .md-read slog it was into a 1-session SQL-driven pass. Collation gotcha caught & fixed: MariaDB 11.8 defaults new tables to `uca1400_ai_ci` — must pin `utf8mb4_general_ci` to join `card_status`.

**PM05 09-16 steps 4–5 COMPLETE — the primary Art 04 sign-off gate (PM02 L357):** all five faction set re-audits (**STD+faction** denominator) + the cross-faction synthesis, in one session. Docs: `Whiteboard/{directorate,ghost,guild,network,syndicate}_reaudit_S156.md` + `cross_faction_synthesis_S156.md`. Headline: the S154 modifier corpus closed nearly every faction's largest S119–128 baseline gap. Key findings: §9.2 re-sorts into three buckets (**mono {DIR,SYN} / native-cross {GUI} / foreign-gated cross {GHO,NET}** — baseline's mono grouping corrected); **Ghost is the intel-hub** for NET+SYN+DIR (19 gated cards, transacted via free trade → Ghost-absent games degrade); five distinct control poles, no differentiation failure.

**Three scope corrections mid-audit (Andy):** (1) denominator is STD+faction (universal STD CA/PA pool + faction set), matching the 09-16 step-4 "(STD+faction)" definition; (2) resource trade incl. Intel is a verbal procedure (Art 03 §11.0, `ref_procedures.md:191–192`), never a card gap; (3) treat the S119–128 baseline as a dated snapshot — re-validate every claim (proven: Guild's "zero-cross" §9.2 claim was stale).

**Two genuine open items resolved/scoped:** Network "Tripwire" = stale pre-ModReact terminology → **§5a Network rewritten** to center the React modifier engine (PM02 L355, monolith regenerated). Ghost **CA.11 Signals Analysis → flagged for full reimagining** (mechanism undefined, depends on undesigned Classified Directive subsystem); does NOT gate Art 04.

**Findings tracking:** `Whiteboard/audit_findings_log_S156.md` — 22 open findings + audit ground rules + triage routing. PM05 **09-17** created as the single consolidated-review item (spins off reactive actions after triage).

**Wiki:** top nav consolidated 11→8 tabs (Game System + Reference & Notes merges) in `tools/build_wiki.py` (survives rebuilds); deployed to pinky.

Full detail: PM02 L355–L357.

---

## Current Focus (S157)

**PRIMARY — PM05 09-17: consolidated triage of the steps 4–5 audit findings.** The full audit is done (S156). 22 findings sit in `Whiteboard/audit_findings_log_S156.md` with a routing summary + audit ground rules. Triage in one pass and spin off reactive actions: schema items → `schema_cleanup_log.md`; Art 03 procedure gaps → 04-n221; design/§9.2/balance questions → Andy + PM02; verify items → confirm against source. This is the gate between the completed audit and Art 04 sign-off. Read the per-faction docs + `cross_faction_synthesis_S156.md` for context; the `card_body`/`v_card_body`/`card_restriction_clause`/`card_checklist` tables in `the_signal_db` are the query substrate.

**Highest-signal items to land first (from the synthesis):** (a) SYS-1 — the Ghost-centered intel economy + Ghost-absent-game degradation (design decision, generalizes 04-n126); (b) the §9.2 pass re-run **by the three buckets**, not the old mono grouping; (c) Guild GUI-1 (baseline §9.2 claim stale → revisit 04-n119) and GUI-2 (defense scaling).

**Then — the other Art 04 sign-off gate:** the pre-existing card-audit backlog (Add-vs-Redirect mis-tag sweep; `target`-field audit SYN.PA.1; 04-n177; `ref_board_narrative.md` sync; 04-n221's 95-card procedure list). Card-level sign-offs stay gated behind both this and 09-17.

**Design item (its own session — do not start cold):** Ghost **CA.11 full reimagining** — tied to what Ghost's "act on hidden objectives / suppress premature consensus" endpoint should mechanically be, plus the undesigned Classified Directive subsystem (content home Art 05-vs-08; deduction/partial-reveal procedure). Explicitly not gating Art 04.

**Opportunistic backlog (full detail in PM05):** schema stragglers 04-n203–04-n212; content/voice gaps 04-n213/214/216–220; 04-n180 (session-commentary sweep); MariaDB HNSW RAG ingestion + cron agent-memory sync; smaller carried items (04-n163/164/166/167/168/148/150/26/27/126/123, XA-54, 06-n01).

---

## Pending Sign-offs

- **Art 04** — Draft. **Gate (1) 09-16 steps 4–5 CLEARED S156** (faction + cross-faction re-audit complete — the milestone that had been the primary sign-off gate). Two gates remain before any set-level sign-off: (a) PM05 **09-17** — consolidated triage of the 22 audit findings + resolution of anything material it surfaces (primary focus above); (b) the pre-existing card-audit-issue backlog (mis-tag sweep, target-field audit, 04-n177, board narrative sync, the 95-card 04-n221 list). Card-level sign-offs stay gated behind both. **CA.11 explicitly does NOT gate** (flagged for reimagining). §5a Network text updated S156 (L355).
- **Art 00a** — v0.13, Signed Off.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.15, Signed Off. (Will need re-opening once 04-n221's procedure-writing starts.)
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
