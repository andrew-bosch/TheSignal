# THE SIGNAL — Website Architecture

**Document:** 14  
**Status:** Pending — Placeholder with Design Constraints

---

## Document Purpose

This document will contain the complete specification for the between-session web experience — the Open Network (public-facing), the Secure Archive (authenticated player portal), and the in-world search and discovery layer. The narrative design of the website is substantially complete. The technical architecture requires decisions before implementation.

---

## Current Status

**Decided:**
- Two-tier access: unauthenticated public layer + authenticated player portal
- In-world presentation only — no mechanical language, no game UI
- Content driven by game state (World Conditions, Chronicle, Founding Figures)
- Hosted primarily on ARBITER Pi — sync to cloud between sessions
- Between-session access must work when ARBITER Pi is offline

**Pending:**
- Hosting architecture (Pi-only vs cloud sync vs cloud-primary)
- Frontend framework selection
- Authentication implementation
- Real-time update mechanism
- Offline capability approach

---

## Conceptual Design

### The Fiction

Players don't visit "the game website." They access **The Open Network** — the world's primary information infrastructure for Chorus-related content — and, with credentials, **The Secure Archive** — ARBITER's record of The Table's proceedings.

The website is diegetic. A new player visiting it before their first session should feel like they've stumbled into something real.

### Two Access Tiers

```
THE OPEN NETWORK [unauthenticated]
  Visible to anyone with the URL
  Contains:
    — Public Chorus information (layers revealed so far)
    — World Condition status (narrative, not numbers)
    — New Meridian news feed (driven by game events)
    — Founding Figures registry (public historical record)
    — In-world search engine (curated results)
    — Session schedule (next convening date/time)
    — Faction public positions (what each faction claims)

THE SECURE ARCHIVE [authenticated]
  Requires player NFC token + passphrase to access
  Contains everything above, plus:
    — Personal Session Chronicles (ARBITER's record)
    — Private ARBITER transmissions (inter-session messages)
    — Faction resource state snapshot (narrative, post-session)
    — Operative legacy record (scars, ascensions, history)
    — Accord registry (what was agreed, what was honored)
    — Portrait contribution (oblique, narrative, never numeric)
    — Between-session narrative events
```

---

## Content Architecture

### World Conditions Display

World Conditions are always presented as narrative, never as numbers. The website mirrors ARBITER's oblique communication style.

```
WORLD CONDITION NARRATIVE STATES

Disclosure (6 levels):
  Level 1: "The matter remains classified. Official denial continues."
  Level 2: "Independent verification has complicated official positions."
  Level 3: "The Chorus is an open secret. Governments have stopped denying."
  Level 4: "Public knowledge. The debate is no longer whether, but what."
  Level 5: "The world is watching. The response question dominates discourse."
  Level 6: "Total saturation. The Table's existence has become suspected."

Consensus (6 levels):
  Level 1: "No framework exists. The factions are not speaking."
  Level 2: "Preliminary contact. Nothing has been agreed."
  Level 3: "Working groups have formed. Progress is tentative."
  Level 4: "A framework is emerging. Key factions have aligned."
  Level 5: "Near-consensus. One or two positions remain unresolved."
  Level 6: "Agreement reached. The Table has spoken with one voice."

[Similar templates for Stability, Chorus Activity, ARBITER Trust]
```

### New Meridian News Feed

The website generates in-world news articles based on game events. These are not mechanical descriptions — they are journalism written from within the fiction.

```
NEWS FEED GENERATION RULES:

Trigger events → article templates:
  District changed control →
    "Infrastructure investment in [district] draws attention"
  Asset burned →
    "[District] resident disappears under unclear circumstances"
  Accord registered →
    "Backchannel negotiations reported in [city]"
  Accord breached →
    "Sources report breakdown in negotiations"
  Popularity change (negative) →
    "[Faction public identity] faces renewed criticism"
  Chorus Activity increase →
    "Researchers report anomalous transmission activity"

Articles are:
  — Written in present tense (recent events)
  — Never named which faction is responsible
  — Accurate to the mechanical event but deniable
  — Consistent with each other across sessions
```

### The Founding Figures Registry

Public, permanent, growing. Each Founding Figure entry contains:

```
[OPERATIVE NAME]
[FACTION]
[ROLE: e.g., "The Urban Planner"]
[SESSION AND COVENANT]

[3-4 sentences in ARBITER's voice about what they accomplished]
[What role they played in the larger negotiation]
[One sentence about their legacy]

"Their work at The Table is complete."
```

This page accumulates across the entire campaign. By the end of a long Covenant, it reads like a memorial wall.

### In-World Search Engine

Players can search the website as they would search the real internet. Results are curated in-world content:

```
SEARCH: "chorus transmission"
RESULTS:
  — Wikipedia-style article: "The Chorus (transmission)" [factual, public knowledge]
  — News article: "Scientists divided on Chorus interpretation" [recent]
  — Academic abstract: "Signal analysis of non-natural EM transmission" [technical]
  — Opinion piece: "Who speaks for humanity?" [editorial]

SEARCH: "the table new meridian"
RESULTS:
  — Nothing at first. [The Table is secret]
  — After Disclosure 4+: Speculative article. [Someone is talking]
  — After Disclosure 6: Direct reporting. [The Table is known]

SEARCH: "[founding figure name]"
RESULTS:
  — Founding Figure registry entry
  — Any news articles that reference them
  — ARBITER's public Chronicle excerpt (if notable)
```

### Private ARBITER Transmissions

Between sessions, ARBITER sends transmissions to authenticated players. These are not game notifications — they are narrative communications from ARBITER to the operative.

```
TRANSMISSION TYPES:

POST-SESSION REFLECTION:
  Arrives 24-48 hours after session end.
  ARBITER's private assessment of the player's
  Portrait contribution. Oblique. Honest.
  
  Example:
  "The Analyst. ARBITER has reviewed the record
   of Session 4. The operation in the Financial
   Clearinghouse demonstrated something that
   does not appear in the official log. ARBITER
   notes it here, privately. The question of
   whether information used to protect information
   is still information, or whether it has become
   something else — ARBITER does not have an answer.
   ARBITER found the question worth keeping."

PRE-SESSION BRIEFING:
  Arrives 24 hours before next scheduled session.
  World Condition update. Narrative summary of
  what has changed. A single oblique observation.

INTER-SESSION EVENT:
  Triggered by World Condition changes between sessions.
  New Meridian does not stop when The Table adjourns.
  
  Example:
  "Something has changed in the Residential Zone.
   ARBITER has noted it. Whether it is relevant
   to The Table's work is for The Table to determine.
   ARBITER has updated the record."

FOUNDING FIGURE NOTIFICATION:
  If a Founding Figure's legacy becomes relevant
  to current events, ARBITER notes the connection.
  
  Example:
  "The work completed by [name] in Covenant 1
   has become relevant in a way [name] could not
   have predicted. The record contains what they
   built. What The Table does with it is, as always,
   The Table's determination."
```

---

## Technical Architecture Options

### Option A: Pi-Primary with Static Export

```
PRIMARY HOST:        Raspberry Pi 5 (ARBITER unit)
BETWEEN-SESSION:     Static HTML export synced to cloud
ONLINE ACCESS:       Cloud-hosted static files
IN-SESSION ACCESS:   Pi-served live content

PROS:
  All data stays on Pi (data sovereignty)
  Between-session access works via cloud
  No subscription fees for hosting
  Full-stack on single device

CONS:
  Pi must be online to sync (requires internet connection)
  Static export loses real-time updates
  Cloud sync is one additional failure point

RECOMMENDED STACK:
  Backend:  FastAPI (Python) on Pi
  Frontend: Server-rendered HTML (Jinja2 templates)
  Sync:     rsync or rclone to cloud storage (S3, Cloudflare R2)
  Cloud:    Static site hosting (Cloudflare Pages, Netlify)
```

### Option B: Cloud-Primary with Pi Sync

```
PRIMARY HOST:        Cloud server (VPS or managed)
GAME STATE SYNC:     Pi pushes state to cloud after each session
ONLINE ACCESS:       Always available via cloud
IN-SESSION ACCESS:   Real-time via cloud

PROS:
  Always online regardless of Pi status
  Real-time updates without Pi being accessible
  Professional URL, SSL managed automatically

CONS:
  Monthly hosting cost
  Game state leaves Pi (privacy consideration)
  Requires internet connection during sync
  More complex deployment

RECOMMENDED STACK:
  Backend:  FastAPI on VPS
  Database: PostgreSQL (cloud) + SQLite (Pi, sync)
  Frontend: React or plain HTML/JS
  Hosting:  Railway, Render, or Fly.io
```

### Option C: Pi-Only (Simplest)

```
PRIMARY HOST:        Raspberry Pi 5 only
ACCESS:              Local network only (or Pi exposed via tunnel)
BETWEEN-SESSION:     Players access via local network or
                     Pi exposed via ngrok/Cloudflare Tunnel

PROS:
  Simplest implementation
  No cloud dependency
  All data stays local

CONS:
  Not accessible when Pi is off/not at home
  No "between session" narrative experience
  Requires Pi to be always-on or players to schedule

NOT RECOMMENDED for full experience
Viable for prototype/playtest phase
```

### Recommendation

**Option A for prototype/early play, Option B for production release.**

The between-session experience is narratively important — players should be able to access Chronicles, transmissions, and the news feed without the Pi being present. A hybrid approach where the Pi generates content and syncs to a static cloud host achieves this without ongoing hosting complexity.

---

## Frontend Design Principles

The website must feel like a real information system from 2041, not like a game website.

```
VISUAL DESIGN PRINCIPLES:
  — Dark, functional aesthetic (not dark mode — dark by design)
  — Monospace elements for data, serif for narrative
  — No game UI elements (no HP bars, no resource displays)
  — The ARBITER symbol (◈) as the only recurring visual brand
  — Subtle amber/gold accent color (matches terminal LED)
  — Mobile-first (players will access between sessions on phones)

TYPOGRAPHY:
  Narrative text:    Serif, generous line height, readable at night
  Data/technical:    Monospace, precise, clinical
  ARBITER voice:     Slightly different treatment — more space,
                     more weight, distinct from editorial content
  Headlines:         Sans-serif, restrained

INFORMATION DENSITY:
  Not information-dense
  Each page has one primary thing to read/discover
  Navigation is sparse and deliberate
  The site feels like it's being careful with you

WHAT THE SITE NEVER DOES:
  — Show resource numbers
  — Name game mechanics
  — Break the fiction (no "game" language anywhere)
  — Show real player names (only operative handles)
  — Reveal ARBITER_ONLY information
```

---

## Authentication Implementation

### Player Login Flow

```
1. Player visits Secure Archive URL
2. Presented with minimalist authentication screen
   [No username/password fields — just a prompt]
   "ARBITER SECURE ARCHIVE
    Authentication required.
    Present your credentials."
3. Two authentication paths:
   A. NFC token + passphrase (primary)
      — Token UID transmitted (requires Web NFC API or
        player manually entering token ID shown on terminal)
      — Passphrase entered
      — Server validates against stored hash
   B. Operative handle + passphrase (fallback)
      — For access when NFC token is not available
      — Slightly degraded access (no sensitive legacy records)
4. Session token issued (JWT or server session)
5. Player enters Secure Archive as their operative
```

### Web NFC Consideration

The Web NFC API allows browsers to read NFC chips on supported devices (Android Chrome primarily). This would allow players to tap their identity token to their phone to authenticate.

```
BROWSER SUPPORT (as of 2026):
  Android Chrome:    Supported
  iOS Safari:        Not supported
  Desktop Chrome:    Not supported

IMPLICATION:
  NFC authentication works on Android phones
  iOS users must use operative handle + passphrase fallback
  This is acceptable — fallback should always exist
```

### Session Management

```
Session duration:    7 days (persistent login between sessions)
Token storage:       HttpOnly cookie (prevents XSS theft)
Token refresh:       Sliding expiry on activity
Logout:              Explicit logout or token expiry
Multi-device:        Allowed (player may access from phone and laptop)
Concurrent sessions: Allowed (no conflict)
```

---

## Content Generation Pipeline

### Post-Session Chronicle Publication

```
SESSION ENDS:
  1. ARBITER generates Session Chronicle (Claude API)
  2. Chronicle stored in SQLite on Pi
  3. Chronicle formatted for web (markdown → HTML)
  4. Faction-specific sections split by visibility scope
  5. Public portion published to Open Network immediately
  6. Full Chronicle (with private sections) available in
     Secure Archive to relevant players

SYNC TO CLOUD:
  After each session, Pi syncs:
    — New Chronicle entries
    — Updated World Conditions
    — New Founding Figure entries (if any)
    — Updated news feed articles
    — New ARBITER transmissions
  Sync triggered manually (admin key) or automatically
  after session end if internet is available
```

### Between-Session Content

```
ARBITER generates between-session content:
  — Post-session reflections (per player, 24-48h delay)
  — Pre-session briefings (24h before next session)
  — World Condition narrative updates (if tracks changed)
  — Inter-session events (triggered by World Condition thresholds)

GENERATION METHOD:
  Claude API with session Chronicle as context
  Pre-generated templates as fallback
  All content stored in SQLite before delivery
  Delivery via email or website (player preference)
```

---

## Page Map (Planned)

### Open Network Pages

```
/                     — Landing: The Chorus situation, current date
/chorus               — The transmission: public layers revealed so far
/new-meridian         — City overview, current conditions, news feed
/new-meridian/news    — Full news feed, filterable by district/faction type
/factions             — Public positions of the five factions
/founding-figures     — Registry of all Founding Figures, all Covenants
/search               — In-world search engine
/archive              — Gate to Secure Archive (authentication)
```

### Secure Archive Pages

```
/archive/dashboard    — Personal overview: current session status
/archive/chronicle    — Session Chronicles (all sessions, own visibility)
/archive/operative    — Operative legacy record: scars, ascensions, history
/archive/transmissions — ARBITER's private messages to this player
/archive/accords      — Accord registry: active, honored, breached
/archive/portrait     — Portrait contribution (oblique ARBITER narrative)
/archive/factions     — Faction-level detail (own faction only)
/archive/new-meridian — Enhanced map view with faction-visible layer data
```

---

## Outstanding Decisions Required

Before this document can be finalized:

1. **Hosting architecture** — Option A (Pi + static cloud) vs Option B (cloud-primary) vs Option C (Pi-only for now)
2. **Frontend framework** — Plain HTML/JS/Jinja2 (simplest) vs React (richer but more complex)
3. **Authentication approach** — JWT vs server sessions; Web NFC integration yes/no
4. **Email delivery** — For between-session transmissions: SendGrid vs Mailgun vs player-configured SMTP vs no email (website-only)
5. **Cloud sync mechanism** — rsync vs rclone vs API push vs none
6. **URL/domain** — Permanent URL for the game or local IP only
7. **Mobile PWA** — Whether to implement Progressive Web App for offline access and home screen install
8. **Content calendar** — Who writes/approves the in-world news articles and search results (ARBITER-generated vs human-authored templates)
9. **Search implementation** — Static curated results (simple) vs actual search index (complex)
10. **ARBITER transmission delivery** — When Pi is offline between sessions, how are transmissions stored and delivered

---

## Important Considerations

### The Diegetic Requirement

Everything on the website must be defensible within the fiction. A first-time visitor who has never heard of the game should be able to read the Open Network and believe it is a real information site about a real event.

This constraint affects every content decision:
- No game jargon anywhere
- News articles must be written as real journalism
- The Founding Figures registry must read like a real memorial
- ARBITER's transmissions must sound like ARBITER

If any page breaks immersion, the design has failed.

### Data Privacy

Players' game behavior is recorded in ARBITER's database. The website makes some of this visible. Before launch:
- Clear privacy policy for what is stored and who can see it
- Player ability to delete their account and associated data
- No real names stored — only operative handles and NFC hashes
- Covenant histories are shared among players of that Covenant — not globally public

### Scalability Non-Requirement

This website does not need to scale. It serves one gaming group (2-6 players) per ARBITER instance. Design for simplicity, not traffic. A single Pi can serve this workload indefinitely.

The only exception: if cloud-hosted, the static Open Network pages may be seen by prospective players. These should load quickly and look good — but the backend will never see significant load.

---
