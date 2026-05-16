# PM04 — Glossary & Data Dictionary
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.2
**Status:** 🔄 Updated — Active
**Last Updated:** 2026-05-16
**Supersedes:** PM04 v0.1 Placeholder

---

## Purpose

Single source of truth for all terminology and design conventions used across THE SIGNAL design artifacts. Internal reference document for designers — not player-facing. Player-facing glossary lives in Artifact 10.

Two sections:

1. **In-World Data Dictionary** — what things ARE in the world: component definitions, institutional terms, temporal conventions, named systems. Each entry carries its narrative grounding.

2. **Design Terminology** — conventions governing how design artifacts are written and structured: narrative language table (mechanical → in-world term mapping), voice and typography convention, code block standard, terminology sequencing principle, and cross-artifact reference convention.

---

## §1 — In-World Data Dictionary

*Pending population. Sources to migrate: THE_SIGNAL___Project_Save_State.md (In-World Glossary table), 00a §1 Time Convention (quarter = one round = three months of real-world time). See PM02 PM04-01.*

---

## §2 — Design Terminology

### Narrative Language Convention

All documentation uses in-world narrative terms. Each mechanical term is defined once on first use, then the narrative term is used exclusively throughout all artifacts.

| Mechanical Term | In-World Term | First Defined In |
|----------------|---------------|-----------------|
| Board space | District | 01 §1 |
| Game mat / full shared display | The Overview | 00 §8 |
| Game board / district map (within The Overview) | New Meridian | 01 §1 |
| Influence token | Presence token | 02a §1 |
| Claim marker | Operational marker | 01 §1 |
| Recipe box | Dispatch case | 06 §1 |
| Popularity track | Public Standing track | 02b §1 |
| Portrait score | Chorus Portrait | 02b §1 |
| Proof token | Intelligence token | 02b §1 |
| Modifier card | Working designation — in-world name pending (D04-07) | 04 §11 |
| Counter card | Countermeasure card | 04 §14.2 |
| Private action | Covert operation | 04 §1 |
| Public action | Political act | 04 §1 |
| Hidden objective | Classified directive | 05 §1 |
| Operative card | Field operative dossier | 05 §1 |
| World event card | Situation report | 01 §1 |

| Round (game term) | Quarter (three months of real-world time) | 03 §1 |

*ARBITER and The Table are never renamed — they are already in-world terms.*

**ARBITER typography:** All-caps is unique to ARBITER only. All other terms Title Case.

---

### Voice & Typography Convention

Five distinct voices appear in design artifacts and player-facing materials. Each uses a fixed typographic treatment so voice is identifiable at a glance in both markdown source and rendered output.

| Voice | When Used | Markdown Treatment | Visual Design Intent |
|-------|-----------|--------------------|----------------------|
| **The Narrator** | All "Narrative:" fields in design artifacts. Expository prose that describes the world as it is. Identity deliberately unresolvable — see note below. | Plain prose, no attribution, no special formatting | Precise, observational, neither warm nor cold. The reader cannot determine if this is a human chronicler or ARBITER in an expository mode. Both readings must remain valid. |
| **Character quote** | Flavor in Narrative fields — operative, faction member, citizen, witness. Grounds a rule or world-fact in a specific human moment. | `> *"Quote."*` followed by `> — Role, Faction` on next line | Serif pull quote, attributed |
| **ARBITER vocalized** | Spoken aloud at the table — resolution announcements, Translation script, Apex acknowledgment, Debrief. | `> *"Text."*` (blockquote, italic, no attribution) | ARBITER voice style — the register carries the speaker |
| **ARBITER written** | Delivered on paper — notification slips, Chronicle entries, Accord confirmations, dispatch language. | Fenced code block | Monospace / typewriter / dispatch aesthetic |
| **Faction voice** | Faction-specific documents, opening monologues, internal communications. Each faction has a distinct voice. | Per faction voice guide (Artifact 00 §12) | Differentiated by faction doctrine and emotional register |

**The Narrator — design principle (locked, PM02 FD-05):**

The Narrator's identity is deliberately never established. It has access to faction internals, Chorus analysis, ARBITER records, and The Table's proceedings — without explaining how. Its register is precise and observational: it notices the right detail, not the obvious one. It states things directly and lets implications stand without developing them. The test for any Narrator sentence: could this have been written by a human who knows too much, or by ARBITER in an expository mode? If both readings are valid, it is correct. If the sentence resolves the ambiguity in either direction, revise it. The Narrator's unresolvability is not a gap — it is the voice.

**The Character Cast — design principle (locked, PM02 FD-05):**

Character quotes are not generic "faction member" flavor. They build a cast — individuals with implied histories, roles, specific relationships to the events they are describing. Each faction has a differentiated pool of voices: the analyst who has been in the same lab for fifteen years; the field coordinator who grew up in the Sprawl and never left; the trader who learned to read rooms before she learned to read; the structural engineer who thinks in load-bearing walls; the liaison who chose the institution over everything else, and knows what that cost. Unnamed characters carry their world in their attribution line. Named operatives (Artifact 05) carry it in their dossier and their quotes. The reader should be able to hear the difference between a Ghost quote and a Guild quote without reading the attribution — the faction's doctrine should be present in how the person phrases what they saw. The cast is not limited to faction operatives or to New Meridian. Pre-Chorus residents carry knowledge no faction operative has. Voices from outside the city — foreign correspondents, remote academics, officials from other governments, people passing through — imply a world larger than The Table and older than the Chorus. Some characters are trying to win something. Some of them are just people who were there.

**Rules:**

- Narrator fields use no special formatting — plain prose. Never attribute them.
- Character quotes always have attribution (role and faction, not personal name unless the character is a named operative).
- ARBITER vocalized quotes never have attribution — the register identifies the speaker.
- ARBITER written blocks are never italicized — monospace is the signal.
- Faction voice is reserved for faction-authored documents and monologues — it does not appear in design artifact Narrative fields.
- No two character quotes from the same faction should sound interchangeable. If they do, one is wrong.

---

### Code Block Standard

**Code block (fenced ```)** — Standard format for any content that functions as a map, schematic, or at-a-glance structural summary rather than prose. Use when: (1) content is a structured overview meant to be scanned, not read; (2) the visual distinction from surrounding prose is intentional and meaningful; (3) the content would become a designed diagram or infographic element in final layout. Do not use for prose explanations, rules text, or examples. Applied: Artifact 03 §6 Round Overview.

*Locked as L95 in PM02.*

---

### Information Design Principle — Terminology Sequencing

No term, in-world concept, or named component may appear in an artifact without its narrative grounding having been established first — in a prior artifact or earlier in the same artifact. A reader moving through the artifact set in order should never encounter a term before the world has given it meaning. The mechanics that use a term are downstream of the fiction that defines it.

This applies to: in-world component names, faction concepts, institutional terms, temporal conventions, and named game elements. Violations are not copy problems — they indicate missing narrative foundation.

*Example: "quarter" as the deliberation period must be established in Artifact 00 before it appears in 00a or Artifact 03. The Narrative Language table above is the audit instrument — if a term appears there, verify its narrative grounding in Artifact 00 precedes its first mechanical use.*

*Locked as L86 in PM02.*

---

### Cross-Artifact Reference Convention

Standard reference format: **[Artifact ID].[Section].[Subsection]**

Examples:
- `Artifact 04 §8` — Section 8 of Artifact 04
- `Artifact 03 §12.3` — Section 12, Subsection 3 of Artifact 03
- `Artifact 02b §8–9` — Sections 8 through 9 of Artifact 02b
- `PM02 §2b` — Section 2b of PM02

Applies to all in-document references, cross-artifact design notes, PM02 blocking decisions, and punch list source citations. Section number changes are a non-material change — references should be audited and updated when an artifact is restructured. Full definition in PM01 §3.

---

*End of PM04 — Glossary & Data Dictionary v0.2*
