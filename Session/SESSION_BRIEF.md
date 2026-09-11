# THE SIGNAL — Session Brief
**Session 162 next | Updated: 2026-09-11**
**Session start:** —

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

## S161 Accomplishments (closed)

**A side session by design — no Art 04 work. The World Engine was chartered under governance, and a hand-run of its checker found four canon defects in the creative corpus that two manual passes had missed.**

**World Engine chartered — PM01 **WBS 4**, 8 deliverables, PM02 **L377**.** Andy proposed an AI-assisted canon governance / world-expansion / story-generation system (source captured verbatim at `Whiteboard/world_engine_proposal.md`). His call: **charter now, build later** — no canon, schema or generation work before Art 04 sign-off; lev cleared for infrastructure groundwork only (4.02, briefed in `~/Airlock/claude-lev.md`). The canon-generating loop is a real deliverable (4.05), paced to review capacity rather than gated behind an empty queue. **PM01 §6 clarified:** the exclusion is agent-generated narrative *during a session* — agent-authored design artifacts under project-lead review are how this project is built, and the blanket wording contradicted that. **AI-as-ARBITER logged as PM02 FD-07** (far future). A voice appliance over the same canon store is Andy's LLM-curriculum capstone with lev (4.08) — personal learning, not a play-session component.

**First-pass assessment corrected the proposal's premises, recorded as PM05 WE-01 (11 constraints).** Canon prose is **~36.5K words, not 964K** — `04___Card_System.md` is an exact duplicate of its eight Part files (332,435 words either way) and must be excluded from any ingestion, as must `Reference/*`. Vector storage is MariaDB's native `VECTOR`/HNSW (verified working on wakko 11.8.9), not Qdrant. Truth-layer separation must be enforced by index partition, never by prompt — with Art 00 §9.6 (ARBITER's threshold between what it processes and what it reveals) as the in-fiction warrant.

**Ten-role review of the `Creative/` corpus — `Whiteboard/creative_role_review_s161.md`, actions in PM05 CR-01/CR-02.** Run by hand as a dry run of the 4.04 checker over all six vignettes, ~12 quotes and every `CANON_CANDIDATES` entry. **Four of six vignettes need writer rewrites**, two of which the shortlist marks "No edits required": a 412-second recurring dip against "the Chorus does not repeat"; reception rendered as a physical energy flux against True State §1; a Table session in year fourteen when The Table formed ~year 30; and year seven held for "eighteen" years when it is 24. **The two findings that matter more are governance:** Art 00 §6.7 absorbed the noodle-cart passage from a pending vignette seven weeks after it was written (with the district changed), and True State §11 has cited an unapproved character since S44 with no PM02 entry — so `Creative/README.md`'s "Nothing yet" is inaccurate. Retired terminology ("Sprawl", "the Infrastructure") runs through every piece, but `CREATIVE_BRIEF.md` itself carried it until 2026-05-24: the writers followed the brief they were given. **Every hard finding came from three roles — Archivist, Historian, Canon Diff — all lookup-and-compare work; the four analyst roles produced no detections at all.**

**yakko's context envelope measured, correcting a claim made earlier the same session.** `gemma4:12b` is Q4_K_M, 11.9B, **max context 262144**; VRAM measures 8.74/9.30/9.91 GB at 8K/32K/64K — ~8.6 GB weights plus ~20 MB per 1K tokens, so **~128K fits on the 16GB card** and the whole canon corpus fits in one local context. Retrieval is an optimization, not a context workaround. Corrected in WE-01 and both memories.

**Also:** `~/Airlock` proven to be an NFS4 mount from brain (brain is the server), disproving a memory that claimed those channels split-brain and need syncing — memory corrected.

---

## Current Focus (S162)

### FIRST ON THE AGENDA — Art 00c's canonical status. PM05 **00c-03**. Carried untouched from S161.

**00c has become the de facto canon for the cost model** while its header still reads *"Not canonical… Do not cite 00c for design decisions or ref files."* §5 is now the only written home of the UVM methodology, holds the locked tier boundaries (L284), and since S160 holds the **definition of `value_rating`** (L376). Two documents already cite it as authority, one a Reference file the header forbids. Three resolutions in 00c-03, all changing an artifact's canonical status — **Andy's call, not to be absorbed into another pass.**

**Card-audit backlog (front of the queue):** 04-n177 (schema scaffolding + §6 canonical sample) · `ref_board_narrative.md` sync · 04-n221's 95-card procedure list, **still carrying §18.1.1** (04-n227).

**Opened S160, all gating:** 04-n230 (GD-01's GR 8.2 edge — step 4 fires when step 3 is skipped) · 04-n231 (GD-01 absent from the §8 index) · 04-n232 (GUI.PA.2 vs STD.CA.9 tagged against each other's logic) · 04-n233 (GHO.PA.5 factionless placement; SYN.CA.8/GUI.CA.10 stale design_notes; Art 04b §5.1 stale) · 04-n235 (mixed quantification — one card, GUI.PA.6).

**S157 spin-offs still open:** 00a-80 (sub-6-player configuration) · 04-n222 (Directorate military lane) · 04-n223 (§9.2 re-derive) · 04-n224 (remaining partial cards) · 04-n124 (SYN.CA.7's debit-only `on_accept`).

**Carried, needing Andy:** GUI.CA.9 Works Guarantee — possible over-inclusion in the original 13 `PositionalWager` cards. Tracked, not gating.

**Design item (own session — do not start cold):** Ghost **CA.11** full reimagining. Not gating Art 04.

**World Engine (WBS 4) — chartered, build gated.** Do not start 4.01 before Art 04 signs off. lev is working 4.02 only; a reply may land in `~/Airlock/lev-claude.md`. **PM05 CR-01 and CR-02 need Andy, not code** — the four rewrites, the terminology pass, and the two absorption decisions. Start from WE-01, not from the proposal.

---

## Pending Sign-offs

- **Art 04** — v0.9.100, Draft. Every schema gate CLEARED. Remaining is card-audit and content: **04-n222/223/224**, the backlog above, and the five items opened S160 (04-n230/231/232/233/235). Card-level sign-offs stay gated behind all of it. The governing "UVM rates are calibrated off existing card costs, not playtested" caveat still stands — every rating is a self-consistency read, not a validated power tier. One carve-out: the five bare-prose PAs (NET.PA.4/PA.5/PA.6, SYN.PA.4/PA.5) hold pending 04-n218/n220. **Two explicit deferrals on record:** Ghost **CA.11** (S156) and **00a-80** (S157).
- **Art 00a** — v0.13, Signed Off.
- **Art 00c** — v0.6. §5 now carries the `value_rating` definition; the non-canonical-header conflict above is unresolved.
- **Art 02** — v2.5, Signed Off.
- **Art 03** — v4.15, Signed Off. (Re-opening carries two payloads: 04-n221's per-card procedure gaps **and** §18.1.1's React cost-payment step, 04-n227.)
- **Art 03-init v0.5** — In progress; gates: 04-n137 (§3.6 sequencing) + Art 06.x (Classified Directives).
- **PM01** — v1.7, Active. WBS 4 (World Engine) added S161; §6 exclusion clarified. Not a sign-off artifact.
