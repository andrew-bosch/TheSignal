# THE SIGNAL

A legacy tabletop board game for 5 players + ARBITER. Factions negotiate humanity's response to an extraterrestrial transmission called The Chorus. Set in New Meridian, 2041.

---

## Project Status

**Current phase:** L1 — Paper Prototype (physical-only, no electronics)
**Active design layer:** `/V1`
**Design milestone:** Artifact 03 pending re-sign-off; Artifact 04 in progress

---

## Folder Structure

```
TheSignal/
├── V1/           ← Active design documents — work happens here
├── Session/      ← Session management files (save state, private design axioms)
├── Retired/      ← Superseded document generations, read-only
│   ├── Electronic/   ← Original electronic brainstorming suite (pre-paper prototype)
│   └── Paper/        ← 1st generation paper prototype artifacts (pre-V1 baseline)
└── README.md     ← This file
```

### /V1 — Active Design Layer

The complete L1 paper prototype design suite. All active artifact editing happens here. Start with `/V1/README.md` for a navigation index, or `/V1/PM03___Master_Artifact_Index.md` for the full artifact registry with status.

**Artifact reading order:** 00 → 00a → 01 → 02a → 02b → 03 → 04 → 04b → 05 → 06 → 07 → 08 → 09 → 10 → 10a → 11

**Design governance:** PM01 (charter), PM02 (decision log + punch list), PM03 (artifact index), PM04 (glossary)

The "V1" designation refers to Layer 1 of the design — the paper prototype physical layer. When the electronic version begins, that will be V2 (L2). V1 does not need renaming as the project evolves.

### /Session

Files that govern the working design session but are not part of the artifact set:

- `THE_SIGNAL___Project_Save_State.md` — tracks where each session ended, what's in progress, recommended next steps. Read this to resume after any break.
- `PRIVATE___True_State.md` — design axioms and private worldbuilding known only to the designer. Not for distribution.

### /Retired

Two generations of pre-V1 design documents. Read-only reference — content has been redistributed into the V1 artifact set. See PM03 §6 for a full file-level index.

- `Electronic/` — Original electronic brainstorming suite (20 documents). Uses old faction names (Architect, Warden, Signal). Includes TypeScript schemas, hardware specs, network architecture.
- `Paper/` — 1st generation paper prototype artifacts. Early versions of V1 documents under current naming conventions.
- `backup.zip` — Complete archive of the Retired folder prior to reorganization.

---

## Design Conventions

- **In-world language:** All mechanical terms have canonical in-world equivalents (Districts not Hexes, Presence tokens not Influence tokens, etc.). PM03 §1 is the authority.
- **Terminology sequencing:** No term appears in an artifact before its narrative grounding is established. Artifact 00 is always read first.
- **Change governance:** Material changes require re-sign-off. Non-material changes (style, terminology, clarification) do not. See PM02 §2b punch list for all pending changes.
- **Vocabulary:** ARBITER, Faction, The ARBITER Player, Faction Player — four distinct terms used precisely. See PM02 L88.

---

## Version Control

This repository uses git. Commit at the close of each design session with a message describing what was decided or completed.

Suggested commit convention:
```
session N — [primary decision or milestone]

e.g. "session 10 — L88 four-term convention; 03 phases 2-6 conventions applied"
```

The `/Retired` folder is tracked in git for historical reference but should not be edited. The `/Session` folder is tracked; `PRIVATE___True_State.md` should remain in `.gitignore` if distributed to collaborators.
