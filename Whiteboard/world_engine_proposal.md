> **Status:** Source capture — Andy's World Engine proposal (Copilot conversation, pasted S161, 2026-09-11). Verbatim content; markdown structure restored from a flattened paste, wording unchanged.
> **Trigger:** Chartered S161 as PM01 WBS 4 ("charter now, build later"). First-pass assessment and scoping live in PM05 WE-xx, not here.
> **Deletion target:** Delete once a World Engine design doc exists (WBS 4.01 kickoff) and this proposal's content has been migrated or explicitly set aside there.

---

# Project Proposal: THE SIGNAL World Engine

**AI-Assisted Canon Governance, World Expansion, and Story Generation Platform**

- **Project Status:** Concept Proposal
- **Audience:** CLI Agent / Engineering Implementation Agent
- **Author:** Andrew Bosch + AI Architectural Proposal
- **Purpose:** Create a scalable local-first knowledge-management and creative-generation system capable of expanding, validating, governing, and utilizing THE SIGNAL canon while preserving coherence across stories, lore, timelines, factions, institutions, and future campaign evolution.

## Executive Summary

THE SIGNAL is no longer best understood as a collection of markdown documents.

It is a growing knowledge ecosystem consisting of:

- Public canon
- Institutional truth
- Designer truth
- Historical records
- Character histories
- Faction doctrines
- Narrative artifacts
- Story outputs
- Future possibilities

The goal is not simply to enable a local LLM to write stories.

The goal is to create a persistent world simulation and canon governance system that continuously:

1. Analyzes existing lore.
2. Identifies gaps.
3. Generates candidate expansions.
4. Creates stories and creative artifacts.
5. Validates consistency.
6. Surfaces proposed additions for human approval.
7. Updates canon repositories after approval.

The human remains Creative Director and final authority on canon.

The AI ecosystem functions as a staff of researchers, historians, analysts, writers, editors, archivists, and worldbuilders.

## Problem Statement

The current lore repository consists primarily of markdown documents.

Markdown is excellent for:

- Authoring
- Reading
- Revision
- Version control

Markdown is increasingly poor for:

- Relationship discovery
- Canon validation
- Cross-reference management
- Historical analysis
- Character tracking
- Timeline consistency
- Retrieval quality

As the world expands, several risks emerge:

- **Canon Drift** — Established facts become contradicted.
- **Knowledge Fragmentation** — Related information exists across multiple files without explicit relationships.
- **Story-Induced Contradictions** — Generated content introduces elements that conflict with established world rules.
- **Worldbuilding Bloat** — Interesting ideas accumulate without governance, causing canon complexity to grow faster than narrative usefulness.
- **Retrieval Degradation** — Increasingly large markdown collections produce less effective prompt retrieval.

## Guiding Principles

### Principle 1: Canon Is a Managed Asset

Canon should not be treated as documents.

Canon should be treated as:

- Entities
- Relationships
- Events
- Doctrines
- Perspectives
- Truth States

Documents become representations of knowledge.

Knowledge becomes the actual source of truth.

### Principle 2: Stories Do Not Update Canon

Approved stories produce canon changes.

The workflow becomes:

```
Story → Review → Canon Extraction → Approval → Canon Repository
```

not:

```
Story → Lore File Edit
```

### Principle 3: Human Approval Required

AI never directly updates canon.

AI proposes.

Human approves.

Canon evolves intentionally.

### Principle 4: Multiple Truth Layers

THE SIGNAL explicitly contains multiple reality layers.

These must be maintained separately.

## Canon Architecture

- **Layer A — Public Canon.** Knowledge available to ordinary observers. Examples: New Meridian; Factions; The Chorus Papers; Public faction doctrines.
- **Layer B — Institutional Truth.** Knowledge available to privileged actors. Examples: Ghost hypotheses; Directorate archives; Restricted research.
- **Layer C — Designer Truth.** True State repository. Examples: Nature of the Chorus; Nature of ARBITER; Hidden causal structures.
- **Layer D — Story State.** Current unpublished development state. Examples: Draft chapters; Planned arcs; Current campaign developments.
- **Layer E — Idea Pool.** Unapproved concepts. Examples: Candidate factions; Candidate events; Potential future stories.

## Recommended Technical Architecture

```
Obsidian Vault or other repository
        │
        ▼
Markdown Source Files
        ▼
Knowledge Extraction Layer
        ▼
SQL based Database (Structured Canon)
        ▼
Vector Store (Semantic Retrieval)
        ▼
Knowledge Graph (Relationship Layer)
        ▼
Agent Ecosystem
        ▼
Review Queue
        ▼
Canon Promotion Pipeline
```

## Storage Architecture

### Markdown

Purpose: Human authoring; Long-form documentation; Version control.

Repository: `/docs` `/lore` `/stories` `/chronicles` `/notes`

### SQL Database

Purpose: Structured facts. Examples: Characters; Locations; Factions; Organizations; Events; Artifacts; Concepts.

SQLite or MariaDB is proposed because: Lightweight; Locally hosted; Easily queryable; Sufficient for MVP.

### Vector Store

Purpose: Semantic retrieval.

Proposed: Qdrant. Reasons: Local; Strong metadata support; Open source; Excellent retrieval quality.

### Knowledge Graph

Optional Phase 2. Purpose: Relationship reasoning.

Example:

```
ARBITER —intersects— Chorus
Ghost —suspects— Hypothesis X
```

Recommended later if query complexity demands it.

## Agent Ecosystem

### Agent 1: Archivist
- **Role:** Canonical knowledge steward.
- **Responsibilities:** Lore retrieval; Canon lookup; Relationship resolution; Timeline lookup.
- **Temperament:** Conservative. If no evidence exists: "No canon support found."

### Agent 2: Historian
- **Role:** Manages historical continuity.
- **Responsibilities:** Timeline construction; Event dependency tracking; Historical causality.
- **Example:** Given "Economic collapse", Historian identifies: Political fallout; Migration patterns; Faction effects.

### Agent 3: Writer
- **Role:** Creative generator.
- **Responsibilities:** Vignettes; Stories; Interviews; Reports; Quotes; Songs; Poetry.
- **Input:** Prompt + Relevant Lore + Story State. **Output:** Narrative Artifact.

### Agent 4: Editor
- **Role:** Quality control.
- **Responsibilities:** Lore validation; Timeline validation; Voice validation; Consistency review.
- **Output:** Issues; Warnings; Approval Recommendation.

### Agent 5: Curator
- **Role:** Canon governance.
- **Responsibilities:** Evaluate: Utility; Narrative value; Redundancy; Complexity cost.
- **Recommendation:** Promote; Reject; Archive.

### Agent 6: Lore Miner
- **Role:** Gap discovery.
- **Responsibilities:** Analyze corpus for: Missing systems; Unexplored areas; Weakly-defined institutions; Incomplete histories.
- **Example:** Education system undefined; Healthcare largely undefined; Religious schisms underdeveloped.

### Agent 7: Political Analyst
- **Role:** Faction realism.
- **Responsibilities:** Evaluate: Incentives; Coalitions; Political outcomes.

### Agent 8: Cultural Anthropologist
- **Role:** Societal realism.
- **Responsibilities:** Develop: Customs; Rituals; Festivals; Vernacular; Social norms.

### Agent 9: Economist
- **Role:** Resource realism.
- **Responsibilities:** Evaluate: Trade systems; Economic incentives; Supply chains; Market shocks.

### Agent 10: Canon Diff Agent
- **Role:** Change analysis.
- **Responsibilities:** Compare Existing Canon vs Candidate Addition.
- **Output:** Additions; Modifications; Potential Conflicts.

## Continuous Worldbuilding Loop

1. **Phase 1 — Analyze Canon:** Coverage; Relationships; Gaps; Weak Areas.
2. **Phase 2 — Generate Proposals:** Historical Event; Character; Institution; Myth; Cultural Practice.
3. **Phase 3 — Stress Test:** Evaluate proposal against History; Politics; Economics; Doctrine.
4. **Phase 4 — Create Narrative Artifacts:** Stories; Broadcasts; Interviews; Situational Reports; Poetry; Research Notes.
5. **Phase 5 — Extract Candidate Knowledge:** New Characters; New Events; New Locations; New Concepts.
6. **Phase 6 — Run Editor:** Validate against canon.
7. **Phase 7 — Run Curator:** Score value.
8. **Phase 8 — Human Approval Packet:** Summary; Reasoning; Canon Impact; Recommendation.
9. **Phase 9 — Promote Approved Content:** Update Markdown; SQLite; Vector Store; Knowledge Graph.

## Scoring Framework

Every proposed canon addition receives:

- **Consistency Score** — Does it fit?
- **Novelty Score** — Does it add something?
- **Story Value Score** — Will it produce stories?
- **Reusability Score** — Will it appear again?
- **Complexity Cost** — Does it make the world harder to manage?
- **Canon Recommendation** — Promote / Hold / Reject

## Story Production System

The system should generate:

- **In-Universe:** Stories; Vignettes; Field reports; Interviews; Broadcasts; Chronicle fragments.
- **Cultural Works:** Songs; Poetry; Speeches; Religious texts; Folktales.
- **Institutional Artifacts:** Directorate memos; Ghost reports; Guild planning documents; Network broadcasts; Syndicate analyses.

## Resource Strategy

Current Hardware Assumption: 16GB VRAM; 14B Model; 4-bit Quantization.

Recommended runtime model: Qwen 14B or Gemma 12B variants.

Focus on many small focused generations rather than a single giant generation.

The real leverage comes from iterative reasoning among agents.

## Human Role

The human operator is not a writer.

The human operator is: **Creative Director**.

Responsibilities: Strategic direction; Canon approvals; Priority setting; Gap selection; Narrative guidance.

AI should produce options.

Human chooses truth.

## Success Criteria

The system is successful when:

- Canon remains internally coherent.
- Contradictions are detected automatically.
- New lore emerges continuously.
- Stories enrich the world.
- Approved stories become structured canon.
- Historical traceability exists.
- The world grows deliberately rather than randomly.
- AI output quality improves as canon expands.
- The human remains final arbiter of world truth.

## Long-Term Vision

The end-state is not a chatbot with lore files.

The end-state is: **Persistent World Engine**

```
Knowledge Repository
      + Canon Governance
      + Creative Generation
      + Historical Memory
      + Human Creative Direction
```

THE SIGNAL becomes a living universe whose history, institutions, narratives, and future development are continuously explored by specialized agents while remaining grounded in a coherent, governed canon. The AI does not replace the creator. It functions as a permanent worldbuilding studio, continuously generating, testing, and refining possibilities for human approval.
