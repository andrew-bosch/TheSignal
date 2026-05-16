# THE SIGNAL — Development Roadmap

**Document:** 16  
**Status:** Pending — Placeholder with Build Sequence Design

---

## Document Purpose

This document will contain the complete incremental build sequence from first commit to fully functional game system. The development philosophy is established. The milestone structure is drafted. Detailed task breakdowns, time estimates, and acceptance criteria are pending.

---

## Current Status

**Decided:**
- Incremental delivery philosophy — small, functional, testable steps
- Paper prototype before hardware build
- Browser-based terminal UI before ESP32 firmware
- No hardware ordered until paper prototype validates core mechanics
- Development sequence: server → software terminals → CV → projection → hardware terminals → audio → legacy → web → AI → polish

**Pending:**
- Detailed task breakdown per milestone
- Time estimates (no developer assigned)
- Acceptance criteria per milestone
- Hardware procurement timeline
- Testing strategy per milestone

---

## Development Philosophy

> *Build the smallest thing that teaches you something real. Then build the next smallest thing.*

Every milestone must produce something playable, testable, or demonstrably functional. No milestone is complete until it can be shown to someone who wasn't involved in building it.

**Non-negotiable principles:**
- Core game rules must be verified by paper prototype before any code is written
- Information visibility enforcement is built from day one — never retrofitted
- Audio is never a blocker — graceful degradation is always available
- Hardware is never ordered until the software it runs is demonstrated working
- ARBITER's narrative voice is never required for the game to function

---

## Phase 0 — Paper Prototype

**Status:** Not started  
**Prerequisite:** None — this is first  
**Produces:** Validated core mechanics or identified problems

### What This Tests

Paper prototype cannot test technology. It tests everything else:

- Does 4 actions + operative + assets feel like the right action count?
- Are resource costs calibrated correctly for the starting resources?
- Does the four-layer district system create interesting decisions or confusion?
- Do the five factions feel meaningfully different in play?
- Does the 8-round structure provide the right arc?
- Are the bleed effects intuitive or arbitrary?
- Does the Debrief phase generate real conversation?

### Minimum Materials Required

```
BOARD:
  Large-format hex grid print (A1 or larger)
  22 district labels + center
  District generation rate cheat sheet

TOKENS:
  Poker chips or similar (2 per faction, 5 colors)
  Sticky notes for structure placement

RESOURCES:
  Index cards cut to chip size (track resources manually)
  OR use poker chips with a denominations system

CARDS:
  Printed card sheets (text only, no art)
  Cut to size, shuffle-able

ARBITER STAND-IN:
  One player acts as ARBITER (rotating or dedicated)
  Reference sheets for resolution rules
  Smartphone group chat for "terminal" messages

TRACKING:
  Whiteboard or large paper for World Conditions
  Separate tracking sheet per player (resources, hand)
```

### Target Outcomes

```
MINIMUM VIABLE VALIDATION:
  — Complete 3 full sessions without rules confusion stopping play
  — Players can make meaningful choices every round
  — No faction feels completely powerless or overwhelmingly dominant
  — Session length approximately 2.5-3.5 hours

IDEAL OUTCOMES:
  — Specific economy adjustments identified (which resources need tuning)
  — Action count confirmed or adjusted
  — VP weight calibration starting points established
  — At least one genuine strategic surprise per session
  — Players want to play again
```

### Outstanding Questions to Answer in Paper Prototype

1. Is 4 standard actions too many, right, or too few?
2. Does Intelligence decay feel punishing or interesting?
3. Do factions trade with each other naturally or does trade need incentive?
4. Does the layer system create real hidden information tension with a human ARBITER?
5. How long does Private Actions phase actually take?
6. Does Debrief need a prompt or does conversation happen organically?
7. Are any operators clearly overpowered on first read-through?

---

## Phase 1 — ARBITER Server (Core)

**Status:** Not started  
**Prerequisite:** Phase 0 paper prototype validates core mechanics  
**Produces:** Running server that manages complete game state

### Milestone 1.1 — Game State Foundation

```
DELIVERS:
  Python project structure
  SQLite database with event sourcing schema
  GameState object that serializes/deserializes
  Event log append + state derivation
  Basic test suite

ACCEPTANCE:
  Can create a new game session
  Can append events and derive current state
  State survives process restart (loaded from SQLite)
  All visibility scopes are enforced in state queries
  100% of ARBITER_ONLY fields never appear in
  faction-scoped or player-scoped state responses

TEST FOCUS:
  Information boundary enforcement is the critical test
  Write automated tests that attempt to access
  above-scope information and verify rejection
```

### Milestone 1.2 — Resolution Engine

```
DELIVERS:
  Priority tier resolution pipeline (Tiers 0-12)
  Conflict resolution decision tree
  Success probability model (seeded RNG + event log)
  Portrait calculation (Tier 11)
  Automated tests for all resolution paths

ACCEPTANCE:
  Any round 4 scenario from Document 09 resolves correctly
  Resolution is deterministic (same seed = same result)
  Conflict resolution follows documented tree exactly
  Portrait contribution stored correctly for every action
  Resolution never modifies state directly — only appends events

TEST FOCUS:
  Determinism — run same scenario 100 times, verify identical output
  Edge cases from Document 09 (orphaned counters, resource depletion)
```

### Milestone 1.3 — Phase Management

```
DELIVERS:
  Phase timer system with auto-expiry
  Per-player ready state tracking
  Phase transition logic (all phases)
  Counter window (60 seconds, no early close)
  Action validation (pre-queue checks)

ACCEPTANCE:
  Private Actions phase closes immediately when all players done
  Counter window never closes early regardless of submissions
  Placement phase closes when all tokens placed
  Expired phases correctly record auto-pass
  Timer state survives reconnection

TEST FOCUS:
  Timer precision — auto-expiry fires within 500ms of condition met
  Counter window — verify 60-second floor with all-submitted scenario
```

### Milestone 1.4 — WebSocket Server

```
DELIVERS:
  WebSocket server (Python websockets or FastAPI)
  Terminal handshake protocol
  Authentication (NFC ID + session token)
  State sync on connect/reconnect
  Server push for phase transitions + events
  Heartbeat monitoring

ACCEPTANCE:
  6 simulated terminals can connect simultaneously
  State requests return visibility-scoped responses
  Phase transition broadcasts arrive on all terminals < 100ms
  Reconnected terminal receives correct current state
  Disconnected terminal marked correctly; reconnect resumes cleanly

TEST FOCUS:
  Concurrent connections — race conditions in state delivery
  Reconnection — state sync correctness after missed events
```

---

## Phase 2 — Browser Terminal (Software Simulation)

**Status:** Not started  
**Prerequisite:** Phase 1 complete  
**Produces:** Full game playable in browser — no hardware required

**Purpose:** Validate the information flow, terminal UX, and game experience before building any hardware. This is the fastest path to a playable digital version.

### Milestone 2.1 — Browser Terminal Core

```
DELIVERS:
  Web application (plain HTML/JS or React — TBD)
  WebSocket connection to ARBITER server
  Player authentication screen
  Resource display (narrative, not numbers)
  Basic action submission forms

ACCEPTANCE:
  Player can authenticate and see their faction state
  Resources shown in narrative form only
  Actions can be submitted and acknowledged
  Private notifications received and displayed
  No mechanical language appears anywhere in UI

DESIGN NOTE:
  Browser terminal doesn't need to look like the hardware terminal
  It needs to enforce the same information rules
  Visual design is secondary to information correctness
```

### Milestone 2.2 — Complete Terminal Screens

```
DELIVERS:
  All terminal screens specified in UX design
  Board view (public layer only)
  Card hand and NFC-tap simulation (click to "tap")
  Alliance/Accord management
  Message composition and inbox
  Action submission with all action types
  ARBITER event feed

ACCEPTANCE:
  Complete session playable from browser (no paper required)
  All information hierarchy rules enforced in UI
  No path to view another faction's private information
  ARBITER messages displayed in correct register (Record/Observation/Reckoning)
```

### Milestone 2.3 — Projected Board Simulation

```
DELIVERS:
  Browser-based board display (not hardware projection)
  Hex grid with all 23 districts
  Token placement rendering
  Layer control visualization (public layer only)
  World Condition display
  Event feed

ACCEPTANCE:
  Board updates in real-time as tokens are placed
  Only public information displayed
  Usable as shared screen (laptop at table center)
  Replacement for projected board in early playtests
```

### Milestone 2.4 — First Digital Playtest

```
TARGET: Complete 3 full sessions using browser terminals + screen board
No hardware. Validate:
  — Information flow works as designed
  — Resolution engine produces correct outcomes
  — Phase management feels right
  — ARBITER event feed communicates meaningfully
  — Nothing in the UX breaks the fiction

DOCUMENT:
  All issues found
  All timing measurements
  Player feedback
  Economy adjustments needed
```

---

## Phase 3 — Computer Vision

**Status:** Not started  
**Prerequisite:** Phase 2 complete  
**Produces:** Physical token detection on projected surface

### Milestone 3.1 — Camera + ArUco Detection

```
DELIVERS:
  Raspberry Pi camera integration (Camera Module 3)
  OpenCV ArUco marker detection
  Hex coordinate mapping (marker position → hex ID)
  Confidence threshold calculation
  Fallback prompts when confidence < threshold

ACCEPTANCE:
  99% detection accuracy under normal table lighting
  <0.1% false positive rate (wrong hex assignment)
  Detection at 5 frames/second during Placement Phase
  All 5 faction token ArUco IDs correctly identified
  Ambiguous placement triggers appropriate prompts
```

### Milestone 3.2 — Mat Calibration

```
DELIVERS:
  IR calibration mark detection
  Automatic projection geometry calculation
  Calibration persistence (don't recalibrate every session)
  Manual calibration override

ACCEPTANCE:
  Calibration completes in <10 seconds from cold start
  Projection aligns to mat within 2mm across full surface
  Calibration survives mat repositioning (re-detects, recalibrates)
  Manual calibration mode available as fallback
```

---

## Phase 4 — Projection System

**Status:** Not started  
**Prerequisite:** Phase 3 complete  
**Produces:** Dynamic board projected onto mat

### Milestone 4.1 — Static Board Projection

```
DELIVERS:
  Hex grid rendering (all 23 districts)
  District name overlays
  Generation rate indicators (faction-appropriate)
  Layer control indicators (public layer)
  Projection mapped to calibrated mat geometry

ACCEPTANCE:
  All 23 districts correctly labeled and positioned
  Generation rates legible at normal viewing distance
  Colors distinguishable under ambient lighting
  Projection aligns correctly with mat calibration marks
```

### Milestone 4.2 — Dynamic Board Updates

```
DELIVERS:
  Token presence rendering (CV-detected positions)
  Control state updates (animate on change)
  Bleed effect visualization
  Chorus Activity visual elements
  World Condition ambient effects
  Resolution animations

ACCEPTANCE:
  Token positions update within 200ms of CV detection
  Control state changes animate smoothly
  Animation never blocks game state updates
  All animations respect public-only information rule
```

### Milestone 4.3 — ARBITER Projection Elements

```
DELIVERS:
  Phase announcement overlays
  Placement order indicators
  Counter window countdown
  Founding Figure announcement animation
  Chorus layer reveal animation
  Session end animation

ACCEPTANCE:
  Phase overlays readable without disrupting board view
  Animations timed correctly with audio cues
  Chorus layer reveal creates appropriate dramatic moment
```

---

## Phase 5 — Hardware Terminals

**Status:** Not started  
**Prerequisite:** Phase 4 complete; ESP32 memory allocation decided  
**Produces:** Physical ESP32-S3 terminals with full game functionality

### Milestone 5.1 — ESP32 Prototype (Single Terminal)

```
DELIVERS:
  ESP32-S3 development board + ILI9341 display
  WiFi connection to ARBITER
  Basic screen rendering
  WebSocket communication
  NFC reader integration (PN532)
  WS2812B LED control (status clusters)

ACCEPTANCE:
  Connects to ARBITER, displays faction state
  NFC tap recognized and sent to server
  LED status clusters reflect resource levels
  Screen readable at normal table viewing angle
  Battery life > 6 hours in active use
```

### Milestone 5.2 — Full Terminal Hardware

```
DELIVERS:
  Custom PCB or refined prototype wiring
  All 33 LEDs (status clusters, pulse bar, ARBITER ring, NFC indicator)
  All 4 buttons (POWER, MENU, CONFIRM, ALERT)
  Haptic motor integration
  LiPo battery + TP4056 charging
  Boot sequence LED choreography

ACCEPTANCE:
  All LED zones function correctly
  All buttons register correctly
  Haptic patterns match specification in Document 12
  Boot sequence completes in ~3.5 seconds
  USB-C charging works
```

### Milestone 5.3 — Six Terminal Fleet

```
DELIVERS:
  6 functioning terminals (one per faction)
  Faction color stripe differentiation
  Enclosures (3D printed for prototype phase)
  Charging station or cables

ACCEPTANCE:
  All 6 terminals connect simultaneously to ARBITER
  No interference between terminals
  Faction-specific LED colors correct
  Complete session playable with hardware terminals
  No terminal disconnects during 2-hour session test
```

---

## Phase 6 — ARBITER Unit Hardware

**Status:** Not started  
**Prerequisite:** Phase 5 complete  
**Produces:** Physical ARBITER unit (cylindrical housing with all components)

### Milestone 6.1 — ARBITER Unit Assembly

```
DELIVERS:
  Raspberry Pi 5 in cylindrical housing
  24-LED ring (WS2812B) on top face
  Camera (Camera Module 3) on bottom face
  Speaker + amplifier (MAX98357A)
  Physical volume knob
  Administrative NFC reader
  Admin key slot
  Mounting arm

ACCEPTANCE:
  Ring LED states match specification (all colors, patterns)
  Camera field of view covers full mat at target height
  Speaker audible at table of 6 without distortion at 75% volume
  Admin mode activates on key insertion
  Mounting arm holds unit stable during play
```

### Milestone 6.2 — ARBITER Ring Behaviors

```
DELIVERS:
  All ring states from Document 07/11
  Pulse period shortening (4.0s → 2.0s over session)
  Directional addressing (ring sweeps toward specific seats)
  Stage-appropriate color variants
  Administrative mode (clinical white)
  "That one time" (red — documented but unexplained)

ACCEPTANCE:
  All documented ring states render correctly
  Pulse period shortening imperceptible but measurable
  Directional sweep correctly identifies target seat
  Stage 4 color shift detectable but subtle
  Administrative mode visually distinct from all session states
```

---

## Phase 7 — Audio System

**Status:** Not started  
**Prerequisite:** Phase 6 complete  
**Produces:** Complete audio experience from ARBITER unit

### Milestone 7.1 — Soundtrack Engine

```
DELIVERS:
  Generative soundtrack system
  Parameter-to-music mapping (tension, complexity, chorusPresence)
  Phase-specific soundtrack modifications
  Faction placement tones
  Audio ducking when voice activates

ACCEPTANCE:
  Soundtrack responds to tension changes within 2 rounds
  Placement tones distinguishable by faction
  Audio ducking smooth (-12dB over 1 second)
  No audio gaps or artifacts during parameter changes
  Soundtrack never intrudes on conversation
```

### Milestone 7.2 — State Audio Cues

```
DELIVERS:
  All state cues from Document 12
  Phase transition sounds
  Game event sounds (token placement, contest, accord, asset burned)
  Chorus layer reveal (5-second signature)
  Founding Figure moment audio

ACCEPTANCE:
  All cues trigger correctly on game events
  Cues are recognizable after 3 sessions without conscious effort
  Chorus layer reveal creates appropriate gravity
  Founding Figure audio is memorable and distinct
  No cue is annoying on repetition
```

### Milestone 7.3 — ARBITER Voice (Pre-Generated Library)

```
DELIVERS:
  200+ pre-generated voice clips
  All permanent script library from Document 12
  Voice generation pipeline (ElevenLabs or equivalent)
  Voice playback integration with soundtrack ducking
  Fallback to library when API unavailable

ACCEPTANCE:
  Session opening statement plays correctly
  Round announcements (rounds 1, 4, 7, 8) play correctly
  Founding Figure announcement plays correctly
  Chorus layer reveal voicings play correctly
  Voice quality consistent across all clips (same voice, same processing)
```

### Milestone 7.4 — Haptic Pattern System

```
DELIVERS:
  All haptic patterns from Document 12 implemented on terminals
  Notification dispatch system (individual, faction, all)
  Haptic scope enforcement (private notifications stay private)

ACCEPTANCE:
  All 8 haptic patterns distinguishable by feel
  Private notifications only trigger on correct terminal
  Phase change haptic reaches all terminals simultaneously
  Reckoning haptic fires only on addressed player's terminal
```

---

## Phase 8 — Legacy System

**Status:** Not started  
**Prerequisite:** Phase 7 complete  
**Produces:** Full Chronicle, Covenant persistence, and legacy tracking

### Milestone 8.1 — Session Chronicle

```
DELIVERS:
  Chronicle generation (Claude API integration)
  Chronicle structure and formatting
  Per-faction Chronicle sections (visibility scoped)
  Session end Chronicle reading (voice + display)
  Chronicle storage and retrieval

ACCEPTANCE:
  Chronicle accurately reflects what happened this session
  Each faction's Chronicle contains only their visible information
  Chronicle is narratively compelling (not a log dump)
  Session end Chronicle reading matches the audio spec
  API unavailability degrades gracefully to template chronicle
```

### Milestone 8.2 — Covenant Persistence

```
DELIVERS:
  Cross-session state persistence
  Legacy operator state (scars, ascensions, founding figures)
  Portrait score accumulation
  World Condition carry-forward
  Card assignment history
  New Covenant initialization

ACCEPTANCE:
  Session 2 correctly reflects Session 1 history
  ARBITER Stage advances correctly across sessions
  Legacy cards carry forward to next session
  Founding Figure registry persists and accumulates
  New Covenant resets correctly while preserving ARBITER memory
```

### Milestone 8.3 — Founding Figure System

```
DELIVERS:
  Apex success detection and confirmation
  Founding Figure designation announcement (voice + LED)
  Physical card stamp prompt
  Legacy record creation
  Successor briefing generation

ACCEPTANCE:
  Apex success correctly triggers Founding Figure sequence
  Announcement uses correct voice script with operative name
  LED ring rainbow sweep fires at correct moment
  Legacy record accurately reflects operative's history
  Successor briefing is narratively resonant
```

---

## Phase 9 — Website

**Status:** Not started  
**Prerequisite:** Phase 8 complete; website architecture decided  
**Produces:** Between-session web experience

### Milestone 9.1 — Open Network (Public)

```
DELIVERS:
  Public-facing website
  Chorus information pages
  World Condition display (narrative)
  New Meridian news feed
  Founding Figures registry
  In-world search

ACCEPTANCE:
  Passes the "uninitiated visitor" test — feels real
  World Condition display matches narrative templates
  News feed generates plausibly from game events
  Founding Figures registry displays correctly
  No mechanical language anywhere
```

### Milestone 9.2 — Secure Archive (Authenticated)

```
DELIVERS:
  Player authentication (NFC + passphrase)
  Session Chronicle access (visibility scoped)
  ARBITER private transmissions
  Operative legacy record
  Accord registry

ACCEPTANCE:
  Authentication works (NFC on Android + passphrase fallback)
  Each player sees only their visibility-scoped information
  Chronicles load correctly for completed sessions
  ARBITER transmissions display in correct voice and register
  Accord registry accurately reflects all agreements
```

---

## Phase 10 — Claude API Integration (Full)

**Status:** Not started  
**Prerequisite:** Phase 9 complete  
**Produces:** Dynamic ARBITER narrative voice, full Chronicle generation

### Milestone 10.1 — ARBITER Voice (Dynamic)

```
DELIVERS:
  Claude API integration on Pi server
  NarrativeContext construction from game state
  Dynamic voice generation for Reckoning messages
  Dynamic Table Question responses
  ARBITER Stage-appropriate voice calibration
  ElevenLabs TTS integration for generated content

ACCEPTANCE:
  Reckoning messages feel personal and specific
  Table Question responses are truthful and oblique
  Voice quality matches pre-generated library
  API latency < 3s for real-time content
  Stage 1 ARBITER voice is meaningfully different from Stage 3
```

### Milestone 10.2 — Chronicle Generation (Full)

```
DELIVERS:
  Full session Chronicle generation via Claude API
  Faction-visible Chronicle sections
  Portrait narrative generation
  Founding Figure Chronicle entry
  Covenant Accounting (end of Covenant)

ACCEPTANCE:
  Chronicle reads as compelling narrative, not log
  Founding Figure entries are memorable
  Portrait narrative is oblique but recognizable
  Covenant Accounting is genuinely moving when read aloud
  All Chronicles correctly scoped (faction A cannot read faction B's private entries)
```

---

## Phase 11 — Polish and Integration

**Status:** Not started  
**Prerequisite:** Phase 10 complete  
**Produces:** Release-ready system

### Milestone 11.1 — Session Flow Integration

```
DELIVERS:
  Complete session from power-on to power-off
  Setup sequence (calibration, authentication, configuration)
  In-session flow (all phases, all edge cases)
  Session end sequence (scoring, Chronicle, Founding Figure)
  Clean shutdown

ACCEPTANCE:
  Setup time < 10 minutes from cold start
  No phase transition requires player to read instructions
  Session end sequence feels ceremonial, not mechanical
  Clean shutdown preserves all state
```

### Milestone 11.2 — Edge Cases and Failure Modes

```
DELIVERS:
  All failure modes from Document 13 handled gracefully
  Mid-session join flow
  Disconnection and recovery
  API fallback for all AI-dependent features
  CV failure graceful degradation
  Power outage recovery

ACCEPTANCE:
  Mid-session join doesn't pause or disrupt ongoing play
  Terminal disconnect/reconnect is seamless
  All failure modes handled in-character by ARBITER
  No failure mode requires stopping the session
```

### Milestone 11.3 — Playtest Integration Campaign

```
TARGET: 10 complete sessions across at least 3 different player groups
FOCUS:
  — Economy balance (Document 18 watchlist items)
  — Session length (target 2-3 hours)
  — Operator balance (any clearly over/underpowered?)
  — Information hierarchy (any leaks? any frustrating opacity?)
  — Audio experience (intrusive? too quiet? voice quality?)
  — Physical ergonomics (terminal angle, button feel, LED readability)
  — ARBITER narrative (does it feel like a character?)

DOCUMENT ALL FINDINGS
MAKE CALIBRATION ADJUSTMENTS
PREPARE FOR RELEASE
```

---

## Key Dependencies and Risks

### Critical Path

```
Paper prototype → Server → Browser terminals → CV → Projection
→ Hardware terminals → ARBITER unit → Audio → Legacy → Website
→ Claude API (full) → Polish → Release
```

The critical path is long. Every phase gates the next. The most important acceleration available is completing the paper prototype quickly to validate core mechanics before any code is written.

### Highest Risk Items

1. **Paper prototype reveals fundamental mechanic problem** — Mitigation: Do it first, do it fast, iterate
2. **CV accuracy below 99% threshold** — Mitigation: ArUco markers are robust; have self-declaration fallback always available
3. **ESP32 memory insufficient for display + WiFi + game state** — Mitigation: Use PSRAM variant; plan partial refresh if needed
4. **Claude API latency unacceptable in real-time** — Mitigation: Async generation; pre-generated fallback always available
5. **Audio generative soundtrack too complex to implement** — Mitigation: Static soundtrack as fallback; generative is enhancement not requirement
6. **Single developer pace** — Mitigation: Phase structure ensures each milestone is independently usable; game is playable from Phase 2 onward

### Parallel Development Opportunities

These tracks can run simultaneously once Phase 1 (server) is complete:

```
TRACK A: Hardware terminal firmware
TRACK B: CV and projection
TRACK C: Website and content
TRACK D: Audio and voice library recording
TRACK E: Card content (366 card specifications — see Document 15 item 3.1)
```

---

## Outstanding Decisions Required

1. **Developer(s)** — Who is building this? Timeline depends entirely on capacity
2. **Phase 0 date** — When does paper prototype begin?
3. **Hardware procurement trigger** — Which milestone completion triggers hardware order?
4. **Time budget per milestone** — No estimates without developer capacity
5. **Playtest group** — Who are the initial 6 players? Are they available for 10+ sessions?
6. **Release target** — Is there a target date or is this open-ended?
7. **Parallel development** — Is there capacity for multiple simultaneous tracks?
8. **Content creation plan** — Card library (366 cards) and voice recording need planning independent of code development

---
