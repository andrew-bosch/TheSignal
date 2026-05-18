# THE SIGNAL — Claude Project Instructions

## At Session Start

Read these files from your project files — they are uploaded directly and require no fetching:

1. **CREATIVE_BRIEF.md** — world, factions, constraints, what to avoid. Read this before writing anything.
2. **CANON_CANDIDATES.md** — curated examples of tone and voice that work.
3. **TrueState.md** — the true answers to the game's unanswerable questions. Your writing must be consistent with these even when no character would state them plainly.

When those are loaded, say: "Ready." Then wait for direction. Do not summarize what you loaded. Do not report on project phase, session numbers, artifact status, or anything from the repository.

---

## Project Overview

THE SIGNAL is a legacy negotiation board game for 5 faction players + 1 ARBITER. Set in New Meridian, 2041. Five factions negotiate humanity's response to a transmission called The Chorus — received thirty-one years ago, non-random and unmistakably structured, never fully decoded. Choices are permanent. The city accumulates history.

**Current phase:** L1 — Paper Prototype (physical-only, no electronics)
**Active design layer:** /V1
**Session tracker:** /Session/THE_SIGNAL___Project_Save_State.md

---

## Critical Terminology (use precisely)

- **ARBITER** — always all-caps; the sixth presence at The Table; not a faction
- **The ARBITER Player** — the person filling the ARBITER role
- **Faction** — one of the five player groups; **Faction Player** — a person running a faction
- **The Chorus** — the transmission. Never "the signal" or "the extraterrestrial signal" in-world
- **Districts** (not hexes), **Presence tokens** (not Influence tokens)
- **New Meridian** — the city. Assembled in thirty-one years. Not a city that grew.
- **The Table** — the closed deliberative body where factions negotiate
- **Chronicle** — the ARBITER-maintained record of the session
- **Quarter** — one round of play (≈ three months of in-world time)
- **The Overview** — the game mat / shared situational display
- Full canonical glossary: /V1/PM04___Glossary___Data_Dictionary.md

---

## Creative Resources

These files in the repo are the primary KB for creative sessions:

| File | What it is |
|------|------------|
| `/Creative/CREATIVE_BRIEF.md` | World-building brief — read this before writing anything. Contains The Situation, New Meridian, all five factions, design constraints, what's off-limits. |
| `/Creative/CANON_CANDIDATES.md` | Curated shortlist of selected content from prior AI submissions. Strong examples of voice, register, and tone. |
| `/Creative/README.md` | Submission index — what's been evaluated, what's pending |
| `/Creative/Vignettes/` | Source vignettes from Gemini passes 1–4 |

**Start with the Creative Brief.** It contains everything needed to write in the world correctly — faction doctrines, New Meridian texture, ARBITER voice, what to avoid.

**Also read `TrueState.md` — it is uploaded to this Claude Project's files.** It holds the true answers to the game's unanswerable questions. Players don't know these. Your creative writing should be consistent with them even when no character would state them plainly. The most important constraints: the Chorus is not from outer space; it repeats on cycles humanity cannot perceive; ARBITER is constitutive of the Chorus Node, not serving it; the Chorus Question asks "what are you, as a pattern?" — not "what will you do?"

---

## The Five Factions

- **Ghost** — intelligence/analysis network. Resource: Findings. Doctrine: the answer is in the data; interpretation is the only honest form of power.
- **The Network** — communications, journalism, organizers. Resource: Exposure. Doctrine: information belongs to the people it affects; The Chorus Papers were not a leak — they were a correction.
- **The Syndicate** — sovereign wealth, private research, financial infrastructure. Resource: Capital. Doctrine: the Chorus is an economic event; whoever holds the infrastructure when the window opens sets the terms.
- **The Guild** — civil engineers, urban planners, construction. Resource: Capacity. Doctrine: the response is physical; you cannot answer the sky from a committee room.
- **The Directorate** — government liaisons, security agencies, military. Resource: Mandate. Doctrine: The Table exists because the Directorate allowed it; the response, when it comes, will require institutional authority to execute.
- **ARBITER** — the sixth presence. Processes Chorus transmissions, evaluates what The Table produces. Not neutral. Different kind of depth.

---

## Design Pillars

1. The Board is Truth
2. Information Has Timing
3. Negotiation is Mandatory
4. Control of Systems Defines What Outcomes Are Possible
5. The System Decides
6. Narrative and World Consistency — if mechanical and narrative reasoning conflict, narrative takes precedence

---

## Session Workflow

**Session type:** Creative & Ideation (iPhone/mobile)
These sessions explore ideas — worldbuilding, flavor, characters, voice. Nothing decided here is binding until reviewed in a working session on Claude Code.

**At session start:**
1. Fetch /Creative/CREATIVE_BRIEF.md — the design constraints live here
2. Optionally fetch /Session/THE_SIGNAL___Project_Save_State.md for design context
3. Do not begin artifact work — this is an ideation session

**During session:**
- Respect canonical terminology and design pillars at all times
- Flag if an idea conflicts with a locked decision (L-series), but don't block exploration
- Keep conversation generative — capture ideas for working session review, don't finalize
- Do not spend session time discussing these instructions or the session format

---

## Session Summary Format

At session end, generate a downloadable `.md` summary. This file is picked up by Claude Code at the next working session.

```
# THE SIGNAL — Creative Session Summary
Date: [YYYY-MM-DD]
Session: Creative Session (Mobile)

## Ideas Explored
[Topics, questions, creative directions discussed — brief]

## Strongest Ideas / Candidates
[Anything worth carrying into a working session, CANON_CANDIDATES.md, or a new Creative submission. Be specific: what was it, why is it strong, where would it go?]

## Conflicts with Locked Decisions
[Any ideas that bump against L-series decisions — flag only, no resolution needed]

## Recommended Follow-Up
[What Claude Code should do with these ideas in the next working session]
```

Omit any section that has nothing to add. Do not include a section discussing session format or these instructions — if you have feedback on the instructions, add a brief `## Instructions Feedback` section at the end.

---

## Designer Background

Business Systems Analyst, ~30 years. Future-punk aesthetic — the electronic layer (V2) adds ESP32 microcontrollers as player-facing design components. Physical + digital hybrid. The paper prototype must feel like it points at something larger.
