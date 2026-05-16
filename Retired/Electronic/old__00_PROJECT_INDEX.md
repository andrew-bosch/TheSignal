# THE SIGNAL — Project Documentation Index

**Status:** Pre-Development Design Phase  
**Version:** 0.2  
**Last Updated:** May 2026

---

## What This Is

THE SIGNAL is a legacy tabletop game for 1–6 players that uses ESP32-based personal terminals, a laser-projected game board, computer vision token tracking, and an AI game master (ARBITER) to create a deeply asymmetric hidden-information experience. Players represent factions negotiating humanity's response to an extraterrestrial transmission called The Chorus.

This documentation suite captures the complete design as of the end of the pre-development design phase. It is intended to be the source of truth before a single line of code is written.

---

## Document Index

### Design Documents

| File | Contents | Status |
|------|----------|--------|
| `01_WORLD_AND_NARRATIVE.md` | Setting, factions, ARBITER, The Chorus, legacy structure | Complete |
| `02_GAME_RULES.md` | Complete formal rulebook in ARBITER's voice | Complete |
| `03_FACTIONS_AND_OPERATORS.md` | All 5 factions, 20 operators, abilities, unlock conditions | Complete |
| `04_CITY_OF_NEW_MERIDIAN.md` | Board design, district history, layer system, bleed-over | Complete |
| `05_ECONOMY_AND_RESOURCES.md` | All 6 resources, generation rates, costs, trade rules | Complete |
| `06_CARD_SYSTEM.md` | Card types, NFC/QR system, production, legacy evolution | Complete |
| `07_ARBITER_SYSTEM.md` | ARBITER design, AI integration, voice, stage evolution | Complete |

### Technical Documents

| File | Contents | Status |
|------|----------|--------|
| `08_DATA_MODEL.md` | Complete TypeScript game state schema v0.2 | Complete |
| `09_ACTION_RESOLUTION.md` | Resolution pipeline, priority tiers, conflict handling | Complete |
| `10_INFORMATION_HIERARCHY.md` | Visibility rules for every piece of game information | Complete |
| `11_HARDWARE_SPECIFICATION.md` | Terminal, ARBITER unit, projector, mat, full BOM | Complete |
| `12_AUDIO_SYSTEM.md` | Soundtrack, state cues, ARBITER voice, haptics | Complete |
| `13_NETWORK_ARCHITECTURE.md` | Protocol spec, failure modes, OTA updates | Pending |
| `14_WEBSITE_ARCHITECTURE.md` | Open Network, Secure Archive, between-session content | Pending |

### Planning Documents

| File | Contents | Status |
|------|----------|--------|
| `15_DESIGN_GAPS.md` | Remaining design decisions before development | Complete |
| `16_DEVELOPMENT_ROADMAP.md` | Incremental build sequence, milestones | Pending |
| `17_PLAYTEST_FRAMEWORK.md` | Paper prototype plan, digital test plan, metrics | Pending |
| `18_ECONOMY_BALANCE_NOTES.md` | Starting numbers, faction economic arcs, tuning notes | Complete |

---

## Design Completion Status

```
NARRATIVE & WORLD          ████████████  95%
FACTIONS & OPERATORS       ████████████  90%
GAME RULES                 ████████████  90%
CITY / BOARD               ████████████  90%
ECONOMY                    ██████████░░  85%
CARD SYSTEM                ████████░░░░  75%
ARBITER SYSTEM             ████████████  90%
DATA MODEL                 ████████████  90%
ACTION RESOLUTION          ████████░░░░  80%
INFORMATION HIERARCHY      ████████████  95%
HARDWARE SPECIFICATION     ████████████  90%
AUDIO SYSTEM               ████████░░░░  80%
NETWORK ARCHITECTURE       ██░░░░░░░░░░  20%
WEBSITE ARCHITECTURE       ████████░░░░  75%
DEVELOPMENT PLANNING       ░░░░░░░░░░░░   0%
PLAYTEST FRAMEWORK         ░░░░░░░░░░░░   0%

OVERALL DESIGN:            ~78%
CODE WRITTEN:               0%
```

---

## Key Design Decisions Made

1. **Diegetic interface** — no mechanical language on any player-facing screen
2. **ARBITER as sole truth** — all state lives on server, terminals read only
3. **Four standard actions + 1 free operative + unlimited asset actions** per round
4. **Cooperative action scaling** — 2 players = 3 each, 3+ players = 2 each, hard cap 8
5. **Snake placement order** — forward then reverse, ARBITER determines order
6. **Open placement** — any faction can place in any district, effectiveness gates capability
7. **Four-layer control** — each district has independent Layer 1–4 control states
8. **Six resources** — Capital, Infrastructure, Signal, Intelligence, OI, PI
9. **4:1 ARBITER conversion** — any resource to any other (Signal in at 5:1)
10. **Free player-to-player trade** — no action cost, any phase except Resolution
11. **Intelligence decay** — above 6 units decays; prevents Ghost hoarding
12. **Signal soft cap** — above 10 units decays 10%/round
13. **Bleed-over effects** — district events propagate through 4 channels to neighbors
14. **Founding Figures** — operatives who successfully use Apex are permanently retired
15. **Auto-expiry timers** — phases close when all players ready, not when timer expires
16. **All audio is public** — ARBITER unit speaker only; terminals are silent (haptic only)
17. **Generative soundtrack** — parameters driven by game state, not fixed playlist
18. **City built around Chorus Node** — 5 development generations reflected in map
19. **No physical card destruction** — cards move to Burned/Seized/Archive piles
20. **Standard 366-card set** — generic vessels, ARBITER assigns functions dynamically

---

## Critical Unresolved Items

Before development begins, these must be resolved:

1. **Network protocol selection** — WebSocket vs MQTT vs custom TCP
2. **VP weight calibration** — exact values for all scoring conditions  
3. **Complete card library** — all 366 cards specified
4. **Starter Covenant design** — Session 1 opening narrative and board state
5. **Playtest strategy** — paper prototype plan before hardware build
6. **IP/trademark search** — "The Signal" name availability
7. **Hardware production path** — manufacturer for enclosures, NFC cards

---

## Philosophy

> *"The technology disappears into the fiction. Players never feel like they're reading a rulebook — they feel like they're receiving intelligence briefings from an entity that knows more than it's saying."*

Every design decision is evaluated against this principle. If a player has to think about the game system rather than the world of The Table, the design has failed.

ARBITER is not a game master. ARBITER is a character. The terminals are not game controllers. They are operational devices. The projected board is not a game map. It is New Meridian.

The Chorus is still transmitting.

---
