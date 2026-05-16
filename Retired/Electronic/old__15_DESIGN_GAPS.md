# THE SIGNAL — Design Gaps & Remaining Decisions

**Document:** 15  
**Status:** Complete — Pre-Development Checklist

---

## Purpose

This document captures every design decision that remains unresolved before development begins. Items are organized by dependency — blocking items must be resolved before any related code is written. Non-blocking items can be deferred to parallel design work.

This is a living document. As decisions are made, they should be recorded here with rationale and cross-referenced to the document they update.

---

## Category 1 — BLOCKING: Must Resolve Before Any Code

These gaps block the start of development because their resolution affects fundamental architecture decisions.

---

### 1.1 — Network Protocol Selection

**The decision:** WebSocket vs MQTT vs custom TCP for terminal-to-server communication.

**What depends on it:** ESP32 firmware architecture, Pi server architecture, reconnection handling, message delivery guarantees.

**Options:**

**WebSocket (HTTP upgrade)**
- Pros: Well-supported on ESP32 (Arduino WebSocket libraries), easy browser client for website, familiar to most developers, good for request/response patterns
- Cons: Slightly higher overhead, HTTP handshake required, not ideal for high-frequency small messages
- Best for: Terminals that occasionally request state and submit actions (which is our pattern)

**MQTT (publish/subscribe)**
- Pros: Designed for IoT, very low overhead, built-in QoS levels, natural pub/sub for broadcast events, excellent ESP32 support (PubSubClient library)
- Cons: Requires separate MQTT broker on Pi, different mental model from REST/WebSocket, subscription management complexity
- Best for: Systems where server pushes to many clients frequently (which is partially our pattern)

**Hybrid: MQTT for Pi→Terminal push, HTTP for Terminal→Pi actions**
- Pros: Best of both — MQTT for efficient broadcast (board updates, phase changes), HTTP POST for action submission
- Cons: Two protocols to implement and maintain on both sides
- Best for: If performance becomes a concern at 6 terminals

**Recommendation:** WebSocket. The game's communication pattern is primarily request/response (terminal asks for state, submits action) with occasional server-initiated events (phase transitions, Reckoning messages). WebSocket handles both cleanly. MQTT overhead is not justified for 6 terminals on a local network. The ESP32-S3 WebSocket support is mature.

**Decision needed by:** Before any firmware or server code is written.

---

### 1.2 — Database Engine Selection

**The decision:** What database engine runs on the Raspberry Pi 5 for game state persistence.

**What depends on it:** All server-side data access, schema migration strategy, backup approach, query patterns for Chronicles and legacy data.

**Options:**

**SQLite**
- Pros: Zero configuration, file-based (easy backup = copy the file), excellent Python support (built-in), good performance for our scale, runs anywhere
- Cons: Single-writer limitation (fine for our use case — ARBITER is the only writer), no built-in replication
- Best for: Games with one authoritative server and clear write ownership — which is exactly our design

**PostgreSQL**
- Pros: Full-featured, excellent JSON support, better concurrent performance
- Cons: Overkill for 6 players, requires separate process, more complex setup and backup
- Not recommended for this use case

**JSON files + event log**
- Pros: Human-readable, trivially inspectable, no database engine needed
- Cons: No transactions, no indexing, slow for complex queries (Chronicle generation), difficult to query across sessions
- Viable for very early prototype only

**Recommendation:** SQLite with event sourcing pattern. The game state is derived from an event log — SQLite stores events as rows, current state is materialized from events on demand or cached. This gives us time-travel debugging, complete audit trail, and simple backup. The Python `sqlite3` module is built-in, zero configuration.

**Decision needed by:** Before Pi server code is written.

---

### 1.3 — ESP32 Memory Allocation Strategy

**The decision:** How to partition the ESP32-S3's 512KB RAM + PSRAM between display buffer, WiFi stack, local state cache, and application logic.

**What depends on it:** Display resolution choices, local caching decisions, whether PSRAM is required.

**Known memory consumers:**

```
ILI9341 display framebuffer:
  320 × 240 × 2 bytes (16-bit color) = 153,600 bytes = 150KB
  [This alone is 30% of base RAM]

WiFi stack (ESP-IDF):
  ~80KB minimum

Application code + stack:
  ~50-100KB estimated

Local state cache:
  ~20-40KB (faction resources, card hand, active messages)

TOTAL ESTIMATE: 300-370KB of 512KB
```

**The PSRAM question:** ESP32-S3 supports external PSRAM (up to 8MB via QSPI). The display framebuffer is the primary candidate for PSRAM — moving it there frees 150KB of internal RAM for application use.

**Options:**
A) Use PSRAM for display framebuffer — requires PSRAM-equipped ESP32-S3 variant (N8R8 or similar, ~$2 more per unit)
B) Use smaller display buffer (partial refresh) — reduces RAM but complicates display driver
C) Reduce color depth to 8-bit (256 colors) — halves buffer to 75KB, acceptable color range

**Recommendation:** Option A — specify PSRAM variant in BOM. The $2 premium per terminal is worth the architectural simplicity. Specify ESP32-S3-WROOM-1-N8R8 (8MB flash, 8MB PSRAM).

**Decision needed by:** Before ordering hardware for prototypes.

---

### 1.4 — Claude API Integration Architecture

**The decision:** How the Claude API integrates with ARBITER's server — request patterns, context management, rate limiting, cost control.

**What depends on it:** Server architecture, narrative generation pipeline, fallback behavior, cost projections.

**Key questions:**

**Q: Synchronous or asynchronous?**
ARBITER generates narrative during Resolution and Debrief phases. Players are waiting. A 2-3 second API call delay during resolution is acceptable — Chronicle generation at session end can take longer (10-15 seconds is fine).
Recommendation: Async — queue narrative generation requests, deliver when ready, never block game resolution.

**Q: Context window management?**
Each API call needs NarrativeContext — the curated game state summary. Context size must stay reasonable.
Target: ~2000 tokens per NarrativeContext. At 8 rounds × 2 calls/round = 16 calls/session + Chronicle generation = ~17 calls. Total context tokens per session: ~34,000 tokens input.

**Q: Caching?**
Standard ARBITER phrases (session opening, round announcements, Chorus layer reveals) should be pre-generated and cached — not API calls. API is reserved for dynamic, contextual content.

**Q: Fallback?**
When API is unavailable: use pre-generated library (200+ clips). ARBITER acknowledges disruption in character. Resolution is never blocked by API unavailability.

**Q: Cost model?**
Using Claude Sonnet 4 pricing as reference:
- ~17 API calls per session × 2000 tokens input + 500 tokens output = ~42,500 tokens/session
- Plus Chronicle: ~1 call × 4000 tokens input + 2000 tokens output = ~6,000 tokens
- Total per session: ~48,500 tokens
- At current pricing: estimate $0.50-2.00 per session depending on model and tier
- Acceptable for a premium game experience

**Decision needed by:** Before ARBITER server narrative layer is built.

---

### 1.5 — Computer Vision Pipeline Specification

**The decision:** Exact CV pipeline implementation — library choice, processing frequency, accuracy requirements, fallback behavior.

**What depends on it:** Pi server architecture, token design, camera hardware selection, calibration system.

**Minimum acceptable accuracy:** 99% token identification confidence on valid placements. Below 99%: manual confirmation prompt.

**False positive rate target:** <0.1% — ARBITER should almost never incorrectly identify a token as being in a hex it isn't in.

**Processing frequency:** 5 frames/second during Placement Phase (sufficient for real-time feel without overloading Pi). 1 frame/second during other phases (detecting if tokens were moved between turns).

**Library:** OpenCV via Python on Pi 5. ArUco marker detection is built into OpenCV's `cv2.aruco` module. Well-documented, well-tested, adequate performance on Pi 5.

**Fallback when CV fails:**
- Token position uncertain (confidence < threshold): ARBITER projects a highlighting arrow at the ambiguous token and requests player confirmation via terminal
- Full CV failure: Self-declaration mode — ARBITER projects numbered zones, players tap terminals in sequence
- CV failure is not a session-stopper; it degrades to manual input gracefully

**Decision needed by:** Before camera/CV code is written.

---

## Category 2 — HIGH PRIORITY: Resolve Before Building Related Systems

---

### 2.1 — Complete Action Cost Table

**Status:** Partially specified in Document 05 and Document 09. Gaps remain.

**Missing costs:**
- Surveillance Install exact cost
- Intercept (passive) setup cost vs ongoing cost
- Plant False Data tiered costs (basic/sophisticated/deep)
- All Propaganda type costs unified in one place
- Asset active action costs by capability type
- Operator unlock ability costs (all 60 unlock abilities need verified costs)

**Resolution approach:** Create a complete action cost reference table as an appendix to Document 05. Every action type, every modifier, no gaps.

**Blocking:** Terminal dispatch screen UI cannot be finalized without complete costs.

---

### 2.2 — Victory Point Weight Calibration

**Status:** Victory conditions defined, VP weights not specified.

**What needs numbers:**

```
PUBLIC VP SOURCES:
  Layer 1 control at round end:        [X VP per district]
  Layer 2 control at round end:        [X VP per district]
  Layer 3 control at round end:        [X VP per district]
  Layer 4 control at round end:        [X VP per district]
  Chord Node control at round end:     [X VP — special]
  Honored Accord at session end:       [X VP per Accord]
  Completed public faction objective:  [X VP — varies]

HIDDEN VP SOURCES:
  Hidden agenda completion:            [5-10 VP per agenda]
  Successful unlock used this session: [1 VP per tier]
  Undetected private operations:       [1 VP each? Cap?]
  
PORTRAIT VP (session contribution):
  Added to total at scoring reveal
  Range: how many VP can Portrait contribute?
  
VICTORY CONDITION THRESHOLDS:
  What VP total wins Domination?
  What VP total wins Shadow Victory?
  How do these relate to each other?
```

**Design target:** Public VP leader at Round 8 end should be identifiable but not inevitable. Hidden VP should be able to swing the outcome but not trivially. Portrait VP should matter but not override everything.

**Blocking:** Cannot test scoring without numbers. Playtest calibration will adjust these significantly.

---

### 2.3 — Starter Covenant Design

**Status:** Not designed. No Session 1 starting configuration exists.

**What needs designing:**

**The Opening Narrative**
What does ARBITER say at the very first session of Covenant 1? The first words this game ever speaks should be considered carefully. They establish everything.

**Session 1 Board Configuration**
- Starting control matrix (Document 04 has this — needs to be locked as Session 1 canon)
- Any Session 1-specific rules or simplifications for new players
- Tutorial round concept vs full game from Round 1

**First Session Pacing**
- Should Round 1 have reduced complexity? (e.g., no asset actions until Round 2)
- Or full game from the start with ARBITER providing more guidance?
- Recommendation: Full game, ARBITER provides Initiate-level guidance on terminals

**Recommended Starting Operators**
- Some operators are more accessible for first-time play
- Should Session 1 have a recommended operator set?
- Or trust players to draft freely?

---

### 2.4 — Playtest Strategy

**Status:** Not designed.

**The fundamental question:** Can the core game loop be tested before the technology exists?

**Paper Prototype Plan:**
The mechanics can be tested with:
- Printed hex board (large format print)
- Colored tokens (poker chips or similar)
- Index cards for resources
- One player acting as ARBITER with reference sheets
- Smartphones for "terminal" communication (group chat)

**What a paper prototype tests:**
- Action economy (4 actions + operative + assets — is it too many? too few?)
- Resource costs (can players afford meaningful things? are they ever stuck?)
- Layer control (does the four-layer system create interesting decisions?)
- Bleed effects (do they feel connected to the city or arbitrary?)
- Victory conditions (do they emerge naturally or feel forced?)

**What a paper prototype cannot test:**
- Information asymmetry (all players can see each other's "screens")
- ARBITER's narrative generation
- Timer pressure
- The physical device experience

**Recommendation:** Run at least 3 paper prototype sessions before building any hardware. Focus specifically on the economy and action count. These are the highest-risk mechanical elements.

**Minimum viable technology test:**
- Pi server running basic game state
- Browser-based terminal UI (not ESP32)
- No projection (use printed board)
- No CV (manual token logging)
This tests the information flow and network architecture before hardware is built.

---

### 2.5 — IP and Trademark Search

**Status:** Not conducted.

**"The Signal" as a game name:**
- This is a common phrase with multiple existing uses
- Needs trademark search in relevant categories (tabletop games, entertainment)
- May need alternative name consideration

**ARBITER as a character name:**
- Used in other media — needs clearance check

**Chorus as the transmission name:**
- Common word — likely clear but should be verified

**Action required:** Legal/trademark search before any public announcement, Kickstarter, or product development commitment.

---

### 2.6 — Hardware Production Path

**Status:** Component selection complete. Manufacturing path not defined.

**Decisions needed:**

**Enclosure manufacturing:**
- Option A: CNC milled aluminum — highest quality, $60-100/unit, minimum order quantity 1
- Option B: Die cast aluminum — lower per-unit cost at scale, high tooling cost ($5,000-15,000 upfront)
- Option C: 3D printed PETG — lowest cost for prototype, $5-15/unit, lower quality feel
- Recommendation: Option C for first 6 prototype units, evaluate Option A for production

**PCB design:**
- Option A: Custom PCB integrating all components — cleanest result, requires PCB design work
- Option B: Prototype wire assembly on perfboard — fastest to first prototype
- Recommendation: Option B for first build, Option A for production

**NFC card stock:**
- Pre-embedded NFC cards are available from multiple suppliers in minimum quantities of 50-100
- Or: Buy blank cards + NFC stickers separately
- Decision: Who suppliers are and what the lead time is

**Card printing:**
- Can be home-printed on card stock for prototype
- Commercial printing needed for production quality
- Decision: Production print partner

---

## Category 3 — STANDARD PRIORITY: Design Before Related Build

---

### 3.1 — Complete Card Library

**Status:** Card system designed, individual cards not specified.

**What's needed:**
- All 366 cards enumerated with type, narrative description, mechanical effect
- Event Card deck (75 cards) — public narrative face + private mechanical effect for each
- Faction-specific Operation Card pool (5 cards per faction = 25)
- Generic Operation Card pool (~50 cards)
- Counter Card specifications (complete — partially done in Document 09)
- Contact Card role pool by district type (~100 roles)
- Equipment Card specifications (~50 cards)
- Intelligence Card types by district (~40 types)
- Legacy Card templates (20 Ascension, 20 Scar, 10 Turn, 10 Covenant)

**This is substantial content work.** Estimated effort: 40-60 hours to specify all cards.

---

### 3.2 — Operative Hidden Agenda Complete Specification

**Status:** Agenda pool concept defined, individual agendas not specified.

**What's needed:**
- 3-5 agenda options per operative (20 operatives × 4 = 80 agendas minimum)
- Each with: Simple/Moderate/Complex tier, VP value, exact completion condition
- ARBITER assignment logic (which tier to assign based on player experience)
- Agenda progress check functions (machine-readable)

---

### 3.3 — World Event Content Library

**Status:** System designed, content not created.

**What's needed:**
- Event Card narrative text (75 unique cards)
- World Condition narrative templates (6 tracks × 10 states = 60 templates)
- Chorus Layer reveal narratives (5 unique scripts)
- Between-session ARBITER transmissions (20+ templates)
- Website news article templates by World Condition state (40+ articles)
- Search result templates for common queries (30+ in-world articles)

---

### 3.4 — Website Technical Architecture

**Status:** Design complete (Document 14 pending). Technical implementation not specified.

**Key decisions needed:**
- Hosting: Pi-only (no external hosting) vs Pi + cloud sync vs cloud-primary
- Framework: Flask/FastAPI for Pi server API, plain HTML/JS for simplicity vs React for richness
- Authentication: Session-based vs JWT vs custom token system
- Real-time updates: WebSocket to website or polling?
- Offline capability: Service Worker for between-session access when Pi is offline?

---

### 3.5 — Unlock Condition Formal Specification

**Status:** Unlock names and themes defined. Exact machine-readable conditions not specified.

**What's needed:**
Every unlock condition needs a formal specification that can be implemented as a server-side check function:

```
EXAMPLE — ANALYST AWAKENING: "Behavioral Profile"
Unlock condition: "Correctly predict 2 hidden actions"

Formal specification:
  track: pattern_match_successes
  scope: cumulative this session
  threshold: 2
  definition of "correct prediction":
    Player submits Pattern Match targeting FactionX
    with ActionType prediction of Y
    Resolution confirms FactionX submitted ActionType Y
    this round
  reset: yes — resets at session start
  cumulative across sessions: no
```

All 60 unlock conditions need this level of specification.

---

### 3.6 — Table Communication Norms

**Status:** Not defined. Creates UI design ambiguity.

**Questions to resolve:**

- Are players allowed to show other players their terminal screen? (If yes: certain screens need privacy modes. If no: social enforcement only.)
- Are players allowed to lie about what they see on their terminal? (Presumably yes — this is a deception game. But needs to be explicit.)
- Is anything said during Debrief "protected" from being called a lie? Or can players gaslight each other freely?
- Can players communicate in ways ARBITER can't see? (Whispering, notes, hand signals.) Presumably yes — this is a social game.
- Can players physically show each other cards? (The cards have narrative text but no mechanical info — probably yes.)

These are social contract questions but the answers affect:
- Whether the Board View screen needs a privacy mode (showing only what you'd declare)
- Whether terminal screens face away from other players by design
- Debrief UI design

---

### 3.7 — Accessibility Requirements

**Status:** Not addressed in any document.

**Minimum requirements to specify:**

**Color blind support:**
- Faction colors cannot rely solely on hue
- Each faction needs a shape or pattern in addition to color
- LED colors need to be distinguishable in deuteranopia, protanopia, tritanopia
- Recommendation: Test all faction color combinations with a color blindness simulator

**Low vision:**
- Minimum text size on ILI9341: recommend 14pt minimum for readability at arm's length
- Minimum contrast ratio: WCAG AA standard (4.5:1)
- Night mode / high contrast mode for bright environments

**Motor accessibility:**
- Physical buttons should have adequate spacing (minimum 8mm between centers)
- Touch targets on screen: minimum 10mm × 10mm
- Alternative to NFC tap for players who cannot easily tap small objects

**Cognitive accessibility:**
- Complexity tier system (Initiate/Operative/Veteran) already addresses this
- Initiate mode should reduce simultaneous information to minimum viable

---

## Category 4 — PARALLEL: Can Be Developed Concurrently

---

### 4.1 — Development Roadmap

**Status:** Not created.

**What's needed:**
A detailed incremental build sequence following the delivery philosophy:
- Small, functional, testable increments
- Each increment builds on the last
- Hardware and software developed in parallel where possible
- Milestone definitions with acceptance criteria

**Suggested milestone structure:**
1. ARBITER server: basic game state + WebSocket
2. Terminal: WiFi connection + basic screen + ARBITER communication
3. CV: camera + ArUco detection + hex mapping
4. Projection: board rendering + calibration
5. Full round: placement → private → public → resolution
6. Audio: soundtrack + state cues
7. Legacy: Chronicle + Covenant persistence
8. Website: Open Network + Secure Archive
9. AI integration: Claude API + voice generation
10. Polish: LED choreography + haptic patterns + session flow

---

### 4.2 — Playtest Metrics Framework

**Status:** Not designed.

**What to measure during playtesting:**

**Action economy:**
- Do players regularly run out of actions? Or have too many?
- What percentage of rounds does each player use all 4 actions?
- Which action types are most commonly taken? Least?

**Resource economy:**
- Which resources feel scarce vs abundant?
- How often is ARBITER 4:1 conversion used?
- Do factions ever feel unable to act due to wrong resource type?

**Information asymmetry:**
- Do players feel they know too much? Too little?
- How often are players surprised by resolution outcomes?
- Do hidden layer controls get discovered at an interesting rate?

**Session length:**
- How long do sessions actually run? (Target 2-3 hours)
- Which phases take longest? (Target: Private Actions under 4 min, Debrief under 5 min)

**Engagement:**
- Do players feel engaged during other players' turns?
- Is the Debrief phase generating real conversation?
- Do players read the ARBITER event feed?

---

### 4.3 — Physical Aesthetics Specification

**Status:** Partially specified in Document 11. Needs completion.

**Missing:**
- Exact enclosure dimensions with tolerances
- PCB layout specification
- LED diffuser material and specifications
- Button feel specifications (actuation force, travel distance)
- Mat stitching and edge detail
- Token material and weight specification
- Case/box design for storage
- Administrative key form factor

---

## Decision Log

*Record resolved decisions here with date and rationale.*

| Decision | Resolution | Date | Rationale |
|----------|-----------|------|-----------|
| Action count | 4 standard + 1 operative + unlimited assets | Design phase | Creates meaningful choices without paralysis |
| Cooperative scaling | 2 players: 3 each, 3+ players: 2 each | Design phase | Coordination advantage without exponential scaling |
| ARBITER conversion rate | 4:1 (Signal in: 5:1) | Design phase | Meaningful cost without total lockout |
| Free trade | No action cost, any phase except Resolution | Design phase | Enables real-time negotiation |
| Auto-expiry timers | All phases close when all players ready | Design phase | Respects player time, reduces artificial waiting |
| All audio public | Speaker on ARBITER unit only | Design phase | ARBITER speaks to The Table, not individuals |
| No card destruction | Cards move to piles, never removed | Design phase | Legacy persistence, physical objects permanent |
| Snake placement | Forward + reverse pass | Design phase | First mover advantage balanced by late second token |
| City historical map | 5 development generations from Node outward | Design phase | Narrative coherence, map tells a story |
| Founding Figures | Apex success required (not just unlock) | Design phase | Completion requires expression, not preparation |

---
