# 03-init — Game Initialization
## THE SIGNAL P1 — Paper Prototype

**Version:** 0.1 — Stub  
**Status:** ⬜ Stub — pending content migration and design  
**Last Updated:** 2026-05-29  
**Depends on:** 00c — Economy Manifest; 01 — Zones; 02a — Components: Board State; 02b — Components: Tracking  
**Called by:** 03 — while session(true): Round Structure (at session start, before loop begins)

---

## Purpose

This artifact owns the game initialization procedure — everything that happens before the first Quarter begins. It is the `init()` function in the program architecture: reads immutable setup_state, seeds all runtime tables, and returns a valid game state for the main loop.

Content currently distributed across 00c §[economy setup], 02a §[board setup], and 02b §[component distribution] migrates here as those artifacts mature.

---

## Scope

03-init covers:

1. **Load game objects** — confirm zones (Art 01) and components (Art 02a/02b) are available
2. **Seed positions** — place all components at starting locations per setup_state
3. **Seed resources** — set faction resource pools to starting values (from 00c)
4. **Seed standing** — set faction standing to baseline (neutral or per faction doctrine)
5. **Distribute decks** — shuffle and assign card pools per faction; set aside ARBITER deck
6. **Distribute classified directives** — one sealed directive per faction
7. **Seat and orient** — ARBITER screen, faction Terminals, dispatch cases, session timeline marker
8. **Return initialized state** — all runtime tables ready for Quarter 1, Beat 0

---

## setup_state

`setup_state` is the immutable T=0 snapshot. It defines what the board looks like at game start before any player action occurs. The running game may not modify it — it is the reference configuration.

Corresponding DB structure: a set of `init_*` tables (or a `setup_state` snapshot table) that runtime tables (`component_positions`, `faction_resources`, `faction_standing`, `district_control`) are seeded from at game start.

*[TBD — full setup_state specification pending 00c, 02a, 02b content maturity.]*

---

## Sections (stub)

1. Overview
2. setup_state Definition
3. Load Procedure
4. Faction Setup (per faction)
5. ARBITER Setup
6. First Quarter Entry Conditions
7. Setup Variants (player count, scenario)

---

*End of Artifact 03-init v0.1 Stub*
