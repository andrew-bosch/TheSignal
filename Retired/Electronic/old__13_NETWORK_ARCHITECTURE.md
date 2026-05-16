# THE SIGNAL — Network Architecture

**Document:** 13  
**Status:** Pending — Placeholder with Design Constraints

---

## Document Purpose

This document will contain the complete network protocol specification, message formats, failure modes, reconnection logic, and OTA update architecture. The system design is partially resolved — core decisions are recorded in Document 15 (Design Gaps). This placeholder captures what is known, what is constrained, and what must be decided before implementation begins.

---

## Current Status

**Decided:**
- WebSocket recommended as primary protocol (see Document 15, section 1.1)
- All terminal communication routes through ARBITER server — no terminal-to-terminal direct communication
- Internet not required during active play sessions
- ARBITER hosts local WiFi network
- OTA firmware updates served by ARBITER Pi to terminals

**Pending:**
- Full message format specification
- Complete API endpoint list with request/response schemas
- Failure mode handling procedures
- Security model and authentication flow
- Bandwidth and latency requirements under load

---

## System Topology

```
INTERNET (optional)
     │
     │ Ethernet
     ▼
┌─────────────────────────────────┐
│         ARBITER UNIT            │
│         Raspberry Pi 5          │
│                                 │
│  ┌─────────┐  ┌──────────────┐  │
│  │  Game   │  │  Web Server  │  │
│  │  Logic  │  │  (Flask /    │  │
│  │  Engine │  │   FastAPI)   │  │
│  └────┬────┘  └──────┬───────┘  │
│       │              │          │
│  ┌────▼──────────────▼───────┐  │
│  │      WebSocket Server     │  │
│  │   (or MQTT Broker)        │  │
│  └────────────┬──────────────┘  │
│               │                 │
│        WiFi Access Point        │
│        SSID: ARBITER-[ID]       │
└───────────────┬─────────────────┘
                │ 802.11n (2.4GHz)
    ┌───────────┼───────────┐
    │           │           │
    ▼           ▼           ▼
┌───────┐  ┌───────┐  ┌───────┐
│  T-1  │  │  T-2  │  │  T-N  │
│ESP32  │  │ESP32  │  │ESP32  │
│ Term. │  │ Term. │  │ Term. │
└───────┘  └───────┘  └───────┘

T = Terminal (up to 6)
All traffic flows through ARBITER
No direct terminal-to-terminal communication
```

---

## Protocol Selection

### Recommended: WebSocket

**Rationale:** The game's communication pattern fits WebSocket well. Terminals periodically request state, submit actions, and receive server-initiated events (phase transitions, Reckoning messages). This is a mixed request/response + push pattern that WebSocket handles cleanly without the overhead of a separate MQTT broker.

**ESP32 implementation:** The `arduinoWebSockets` library (Links2004) is mature and well-documented. Alternatively, `esp-idf` native WebSocket support.

**Pi implementation:** Python `websockets` library or `fastapi` with `websockets` support.

### Alternative Considered: MQTT

MQTT would be well-suited for the broadcast (Pi → all terminals) pattern — phase transitions, board state updates, public event announcements. However, the added complexity of running a broker (Mosquitto) alongside the game server, and managing subscription topics for 6 terminals, is not justified for the scale.

**Retained as fallback** if WebSocket performance proves inadequate under load testing.

### Hybrid Option (If Performance Issues Emerge)

- MQTT for server-to-terminal push (board state, phase changes, public events)
- HTTP POST for terminal-to-server action submission
- Benchmark before committing

---

## Connection Lifecycle

### Session Start

```
TERMINAL BOOT:
  1. Terminal powers on
  2. Connects to ARBITER WiFi (stored SSID/password)
  3. Initiates WebSocket connection to ARBITER
     ws://192.168.4.1:8765
  4. Sends handshake with terminal ID + firmware version
  5. ARBITER validates terminal, sends session state
  6. Terminal enters authentication waiting state

NFC AUTHENTICATION:
  1. Player taps identity token to terminal
  2. Terminal sends NFC ID to ARBITER
  3. ARBITER validates player identity
  4. ARBITER sends player-specific game state
  5. Terminal transitions to active state
  6. LED boot sequence completes
```

### During Session

```
STATE REQUEST PATTERN:
  Terminal → ARBITER: { type: "state_request", scope: "faction" }
  ARBITER → Terminal: { type: "state_response", data: FactionVisibleState }

ACTION SUBMISSION:
  Terminal → ARBITER: { type: "action_submit", action: ActionSubmission }
  ARBITER → Terminal: { type: "action_ack", actionId: string, status: "queued" }

SERVER PUSH (phase transitions, events):
  ARBITER → All terminals: { type: "phase_transition", newPhase: PhaseType }
  ARBITER → Faction terminals: { type: "private_notification", content: string }
  ARBITER → Specific terminal: { type: "reckoning", content: string }
```

### Heartbeat

```
Interval:    15 seconds
Direction:   Terminal → ARBITER
Payload:     { type: "heartbeat", terminalId: string, batteryLevel: number }
Response:    { type: "heartbeat_ack", serverTime: number }
Timeout:     45 seconds without heartbeat → terminal marked disconnected
```

---

## Message Format Specification

### Envelope Structure (Proposed)

```typescript
interface NetworkMessage {
  type: string;              // message type identifier
  messageId: string;         // UUID, for acknowledgment tracking
  timestamp: number;         // Unix timestamp (ms)
  senderId: string;          // terminal ID or "arbiter"
  sessionId: SessionID;
  payload: unknown;          // type-specific content
}
```

### Message Types — Terminal to ARBITER

*To be fully specified. Known types:*

| Type | Trigger | Payload |
|------|---------|---------|
| `handshake` | Terminal boot | terminalId, firmwareVersion |
| `nfc_read` | Token/card tap | nfcId, readType |
| `action_submit` | Player action | ActionSubmission |
| `declare_done` | Player done button | roundId, phaseType |
| `ready_for_next` | Debrief ready button | roundId |
| `heartbeat` | 15s interval | terminalId, batteryLevel |
| `counter_submit` | Counter card tap | cardId, targetActionId |
| `vote_submit` | Table Question vote | proposalId |
| `trade_propose` | Trade initiation | tradeDetails |
| `trade_confirm` | Trade acceptance | tradeId |
| `admin_key` | Admin key inserted | keyHash |

### Message Types — ARBITER to Terminal(s)

*To be fully specified. Known types:*

| Type | Recipients | Payload |
|------|-----------|---------|
| `state_sync` | Single terminal | VisibleGameState |
| `phase_transition` | All terminals | PhaseType, timer |
| `private_notification` | Single player | narrativeText |
| `reckoning` | Single player | reckoningContent |
| `public_event` | All terminals | eventNarrative |
| `resolution_result` | Faction terminals | outcomeNarrative |
| `audio_cue` | All terminals (haptic) | HapticPattern |
| `led_command` | Single terminal | LEDState |
| `timer_update` | All terminals | secondsRemaining |
| `counter_window_open` | All terminals | durationSeconds |
| `counter_window_close` | All terminals | — |
| `board_update` | All terminals | PublicBoardState |
| `firmware_update_available` | Single terminal | version, url |

---

## State Synchronization Strategy

### What Terminals Cache

Terminals maintain a local cache of their current visible state. This avoids re-requesting state every screen render.

```
CACHED (faction-visible, refreshed each phase):
  - Own resource pool (declared + actual)
  - Own card hand (narrative descriptions)
  - Active accords (existence + terms)
  - Own operator status and unlocks
  - Public board state (token positions, layer 1 control)
  - World conditions (narrative)
  - Popularity states (all factions)

NOT CACHED (requested fresh on demand):
  - Other factions' private state (never stored)
  - ARBITER_ONLY fields (never transmitted)
  - Sensitive action history details
```

### Cache Invalidation

ARBITER pushes invalidation signals on state changes:

```
{ type: "cache_invalidate", scope: "resources" | "board" | "accords" | "full" }
```

Terminal requests fresh state after invalidation. The scope narrows the re-fetch to only what changed.

### Reconnection on Disconnect

```
DISCONNECT DETECTED:
  1. ARBITER marks terminal as disconnected
  2. Faction moves to Ambient Power (passive tier)
  3. Ongoing phases are not paused
  4. Automatic Pass applied to any expired timers

RECONNECT:
  1. Terminal re-establishes WebSocket
  2. Sends reconnect handshake with sessionId + playerId
  3. ARBITER sends full state sync (all cached fields)
  4. Terminal re-authenticates with NFC token
  5. Ambient Power status removed, player resumes control
  6. ARBITER notifies: "Connection restored. ARBITER notes
     the interruption. The record continues."
```

---

## Security Model

### Local Network Security

The ARBITER WiFi network is:
- WPA2 password protected
- Password is session-specific (displayed at setup, changes each session)
- SSID: `ARBITER-[8-char session ID]`
- Only registered terminal MAC addresses are allowed connections (MAC filtering)

### Player Authentication

- Identity tokens use NFC chip UIDs — not reproducible without physical token
- Passphrase fallback stored as bcrypt hash on ARBITER
- Session tokens issued after NFC authentication — all subsequent requests include session token
- No player real identity stored — only handle and NFC ID hash

### Message Integrity

- All messages include HMAC signature using session key
- Session key negotiated at terminal handshake
- Prevents message injection from devices on the local network
- Not designed against sophisticated MITM — this is a local game network, not a bank

### Information Boundary Enforcement

The most critical security property: **terminals cannot request information above their visibility scope.**

```
ENFORCEMENT APPROACH:
  Every API endpoint is scoped:
  - /state/public         → all authenticated terminals
  - /state/faction/{id}   → terminals authenticated to faction {id} only
  - /state/player/{id}    → terminal authenticated as player {id} only
  - /state/arbiter        → no external endpoint (internal only)

  Server middleware validates:
    requesting terminal → authenticated player → authorized faction
    before any state response is generated
```

---

## API Endpoints (Planned)

*Full specification pending. Known endpoints:*

### Game State

```
GET  /state/public              → PublicGameState
GET  /state/faction/{factionId} → FactionVisibleState
GET  /state/player/{playerId}   → PlayerVisibleState
GET  /state/board               → PublicBoardState
GET  /state/world               → WorldConditions (narrative)
```

### Actions

```
POST /action/submit             → { actionId, status }
POST /action/declare_done       → { acknowledged }
POST /action/counter_submit     → { counterId, status }
POST /action/ready              → { acknowledged }
```

### Communication

```
POST /message/send              → { messageId, status }
POST /accord/propose            → { accordId, status }
POST /accord/confirm            → { accordId, status }
POST /accord/breach             → { accordId, status }
```

### Trade

```
POST /trade/propose             → { tradeId, status }
POST /trade/confirm             → { tradeId, status }
POST /trade/cancel              → { tradeId, status }
POST /conversion/arbiter        → { conversionId, status }
```

### Table Question

```
POST /question/propose          → { proposalId, status }
POST /question/vote             → { voteId, status }
```

### Administrative

```
POST /admin/session/start       → { sessionId }
POST /admin/session/end         → { summary }
POST /admin/terminal/register   → { terminalId }
POST /admin/card/initialize     → { cardId }
GET  /admin/state/full          → FullGameState (admin key required)
POST /admin/state/correct       → { correctionId } (admin key required)
```

### OTA Updates

```
GET  /firmware/version          → { current, available }
GET  /firmware/binary           → binary blob
POST /firmware/ack              → { terminalId, version, status }
```

---

## OTA Firmware Update Flow

```
UPDATE INITIATION:
  1. Admin inserts new firmware to ARBITER via USB or network
  2. ARBITER validates firmware signature
  3. ARBITER sets pendingOTAUpdate in SystemState

BETWEEN SESSIONS ONLY:
  1. ARBITER notifies connected terminals of available update
  2. Terminal requests confirmation from player (screen prompt)
  3. Terminal downloads binary from ARBITER
  4. ESP32 native OTA update mechanism applies update
  5. Terminal reboots, re-connects, sends version confirmation
  6. ARBITER verifies version matches expected

ROLLBACK:
  If terminal fails to boot after update:
    ESP32 OTA rollback to previous partition on next boot
    Terminal re-connects on previous firmware
    ARBITER flagged that terminal requires manual update

NEVER DURING SESSION:
  OTA updates are blocked if a session is active
  ARBITER refuses firmware requests during play
  If a terminal disconnects mid-session for any reason,
  it will not receive OTA on reconnect
```

---

## Failure Modes and Mitigations

### Terminal Disconnect Mid-Phase

```
Private Actions Phase:
  Terminal disconnects while player has unsent actions
  → Faction moves to Ambient Power (passive)
  → Actions in progress are cancelled
  → If reconnect before phase close: player can resubmit
  → If phase closes before reconnect: automatic Pass recorded

Placement Phase:
  Terminal disconnects before placing tokens
  → ARBITER auto-places in highest-affinity unclaimed hex
  → Notifies player on reconnect

Resolution Phase:
  Terminal disconnects
  → Resolution continues — no player input needed
  → Results delivered on reconnect
```

### ARBITER Server Restart Mid-Session

```
State preservation:
  Game state saved to SQLite after every phase transition
  Recovery restores to last complete phase
  In-flight actions (submitted but not resolved) may be lost

Recovery sequence:
  1. ARBITER restarts, loads last saved state
  2. Terminals detect disconnect, attempt reconnect (exponential backoff)
  3. Terminals reconnect, receive current phase state
  4. ARBITER delivers in-character explanation:
     "ARBITER experienced a disruption in record-keeping.
      The session resumes from the last confirmed state.
      Any actions submitted in the interruption window
      have not been recorded. The Table may proceed."

Phase re-announcement:
  ARBITER re-announces current phase on all terminals
  Timers reset to full duration for fairness
```

### WiFi Network Failure

```
All terminals lose connection simultaneously
→ ARBITER detects via heartbeat timeout (45s)
→ If network recovers: terminals reconnect automatically
→ If network fails to recover: session paused
→ Physical backup: ARBITER can serve as USB host for
  direct cable connection (not implemented v1, planned)
```

### Claude API Unavailability

```
ARBITER's narrative generation degrades gracefully:
→ Pre-generated library serves standard situations
→ API calls queued for retry (exponential backoff)
→ ARBITER acknowledges in character:
   "ARBITER's observation systems are experiencing
    interference. The record continues. ARBITER will
    resume full communications when the interference
    clears."
→ Resolution never blocked by API unavailability
→ Chronicles generated post-session when API restores
```

---

## Bandwidth and Latency Requirements

### Estimated Traffic Per Terminal Per Session

```
State requests:
  ~8 per round × 8 rounds = ~64 requests
  Average payload: ~2KB
  Total: ~128KB per terminal

Action submissions:
  ~5 per round × 8 rounds = ~40 submissions
  Average payload: ~0.5KB
  Total: ~20KB per terminal

Server pushes:
  ~20 per round × 8 rounds = ~160 pushes
  Average payload: ~1KB
  Total: ~160KB per terminal

Heartbeats:
  1 per 15s × 3600s session = ~240 heartbeats
  Payload: ~0.1KB each
  Total: ~24KB per terminal

TOTAL PER TERMINAL: ~332KB per 2-hour session
TOTAL FOR 6 TERMINALS: ~2MB per session

802.11n typical throughput: 50-150 Mbps
Actual requirement: ~0.01 Mbps
Headroom: Enormous — network is not a bottleneck
```

### Latency Requirements

```
Action submission → acknowledgment: <200ms (player expectation)
Phase transition broadcast: <100ms (all terminals simultaneously)
State sync on reconnect: <2s (acceptable pause)
Resolution notifications: <500ms after resolution completes
Claude API narrative: <5s (acceptable during Debrief)
```

---

## Outstanding Decisions Required

Before this document can be finalized and implementation begun:

1. **WebSocket vs MQTT final decision** — Recommendation is WebSocket; needs sign-off
2. **Python framework selection** — FastAPI recommended for async support; Flask as simpler alternative
3. **Authentication token format** — JWT vs session cookies vs custom HMAC tokens
4. **Message format finalization** — Complete TypeScript interfaces for all message types
5. **API versioning strategy** — How to handle firmware/server version mismatches
6. **Admin key implementation** — USB dongle with certificate vs PIN vs physical switch
7. **Bandwidth throttling** — Whether to implement per-terminal rate limiting
8. **WebSocket library selection** — `arduinoWebSockets` vs `esp-idf` native vs other
9. **MQTT broker selection** — If MQTT route is chosen: Mosquitto vs others
10. **Encryption at rest** — Whether SQLite database should be encrypted (adds complexity)

---

## Implementation Notes for Developer

When this document is finalized, implementation should begin with:

1. Minimal WebSocket server on Pi (Python) — accepts connections, echoes state
2. Minimal WebSocket client on ESP32 — connects, sends heartbeat, receives echo
3. Basic game state object — serializes/deserializes cleanly over the wire
4. Visibility enforcement middleware — verify before any state endpoint expands

The information boundary enforcement (visibility scoping) is the most critical correctness requirement and should be built into the server architecture from day one — not added later. Information leaks are game-breaking and very difficult to audit retroactively.

---
