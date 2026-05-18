# 03a — GAME ENGINE SPECIFICATION
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.1  
**Status:** 🔄 Draft — Placeholder  
**Last Updated:** 2026-05-18  
**Companion to:** [Artifact 03 — Round Structure & Gameplay](03___Round_Structure___Gameplay.md)  
**Depends on:** [00b — Data Architecture](00b___Data_Architecture.md)

---

## 1. Overview

Art 03a is the code-lite technical companion to Art 03. Where Art 03 describes the round structure in design language, Art 03a formalizes the same content as a runnable specification: explicit game state variables, structured beat procedures, and exhaustive decision tables.

**Purpose:** Surface edge cases invisible in prose, enable mechanical balance analysis (modifier stack mathematics), and provide the formal specification from which a digital game engine could be built without ambiguity.

**Relationship to Art 03:** Art 03a does not introduce new mechanics. Every branch and decision here is derivable from Art 03 + 00b. Conflicts between this document and Art 03 should be treated as an error in 03a.

**L108 compliance:** All tables in this artifact follow the L108 Database Translatable Data Design standard (single-typed columns, controlled vocabulary, explicit ID primary keys).

---

## 2. Index

1. Overview
2. Index
3. Scope and Layer Structure
4. Layer 1 — State Model
5. Layer 2 — Beat Procedures (Pseudocode)
6. Layer 3 — Decision Tables & Edge Case Registry
7. Modifier Stack Reference
8. Design Notes

---

## 3. Scope and Layer Structure

Art 03a is organized into three layers of increasing specificity:

| Layer | Contents | Status |
|-------|----------|--------|
| 1 | State Model — formal game state at each beat boundary, using 00b entity IDs as variable vocabulary | 🔄 Pending content pass |
| 2 | Beat Procedures — each beat as a structured pseudocode function (Beat_0() through Beat_5()) with explicit IF/THEN/ELSE branches, named inputs/outputs, modifier stack as summation formula, resolution check as formal inequality | 🔄 Pending content pass |
| 3 | Decision Tables — all branching conditions surfaced as tables; edge cases include face-down/face-up, Apex vs. non-Apex, Critical overrides, partial payment, Infrastructure scope (L107), Type B scope | 🔄 Pending content pass |

**Modifier balance analysis** (original XA-27 scope) is a derived output of Layer 2 once the modifier stack is formally expressed. It will be appended here as Layer 4 when Layer 2 is complete.

---

## 4. Layer 1 — State Model

*Pending content pass.*

State variables are declared using 00b entity ID namespaces (e.g., `M-xx` for Markers, `D-xx` for Districts, `RO-xx` for Resources). Beat boundary snapshots capture the full game state as it must exist at the start and end of each beat.

---

## 5. Layer 2 — Beat Procedures (Pseudocode)

*Pending content pass.*

Each beat is expressed as a structured function:

```
Beat_N(inputs) → outputs
  // Preconditions
  // Procedure steps (IF/THEN/ELSE)
  // Modifier stack (summation formula)
  // Resolution check (formal inequality)
  // State mutations
  // Output
```

Beat functions to define: `Beat_0()`, `Beat_1()`, `Beat_2()`, `Beat_3()`, `Beat_4()`, `Beat_5()`.

---

## 6. Layer 3 — Decision Tables & Edge Case Registry

*Pending content pass.*

Decision tables cover all branching points in Beats 0–5. Confirmed scope:

| Table | Branch Condition | Status |
|-------|-----------------|--------|
| DT-01 | Card orientation at Beat 0 (face-down / face-up) | 🔄 Pending |
| DT-02 | Apex card detection at Beat 0 | 🔄 Pending |
| DT-03 | Critical Success (01–05) override path | 🔄 Pending |
| DT-04 | Critical Failure (96–00) override path | 🔄 Pending |
| DT-05 | Partial payment at Beat 4 | 🔄 Pending |
| DT-06 | Infrastructure modifier scope (L107 — all action types) | 🔄 Pending |
| DT-07 | Type B card scope (Faction Player only vs. all) | 🔄 Pending |
| DT-08 | Apex activation threshold check (Step 4) | 🔄 Pending |
| DT-09 | Emergency Response — assist / thwart Apex (Board Strength delta before Step 4) | 🔄 Pending |

---

## 7. Modifier Stack Reference

*Pending content pass.*

Variable modifier rows are stubbed pending Art 04:

| ID | Modifier Name | Type | Value | Dependency |
|----|--------------|------|-------|------------|
| M-01 | Critical Success | Fixed | −25 | Art 03 §14 |
| M-02 | Critical Failure | Fixed | +25 | Art 03 §14 |
| M-03 | Untrained | Fixed | +25 | Art 03 §14 |
| M-04 | Infrastructure | Fixed | −25 | Art 03 §14, L107 |
| M-05 | Partial Payment | Fixed | +50 | Art 03 §14 |
| M-06 | Experienced | Fixed | −15 | Art 03 §14 |
| M-07 | Known Operative | Fixed | +15 | Art 03 §14 |
| M-08 | Modifier Card | Variable | TBD | Blocked — Art 04 |
| M-09 | Protect | Variable | TBD | Blocked — Art 04 |
| M-10 | Situation Report | Variable | TBD | Blocked — Art 04 |
| M-11 | Type A | Fixed | 0 | Art 03 §14 |
| M-12 | Type B | Variable | TBD | Blocked — Art 04 |

---

## 8. Design Notes

**Source of truth:** Art 03 is authoritative for mechanics. This document is a formalization layer — if 03a contradicts 03, 03a is wrong.

**L2 implication:** The Beat Procedures in Layer 2 are intended to be directly translatable to a server-side game engine (L2 architecture). The TypeScript schema in Retired/Electronic/old__08_DATA_MODEL.md is the target L2 data model; 00b entity IDs should align to it.

**Modifier balance analysis:** Once all modifier rows (M-01–M-12) are fully specified, the summation formula in Beat_3() enables a full balance analysis: expected difficulty shift per modifier combination, pathological stack identification, and recommendation for modifier caps if needed.

---

*End of Art 03a — Game Engine Specification v0.1*
