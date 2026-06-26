# Covert Inter-Faction Messaging — Design Stub
## Eventual home: Art 06

**Created:** S119 (2026-06-25)  
**Status:** Concept — not yet a locked decision; no artifact impact until sign-off  
**Trigger:** Ghost intelligence trading gap; information diplomacy underdeveloped  
**Delete when:** Migrated to Art 06 design pass

---

## Problem Statement

Debrief (§11) already provides a public free-trade window: resources and Intel Tokens can be exchanged between any two factions, visible to all players at the table.

What doesn't exist: a mechanism for **covert inter-faction communication within the Month** — a way for factions to transfer content privately, timed relative to the resolution cycle, without requiring Debrief's public visibility.

This is the gap the message packet system fills. Its unique value is:
- **Timing** — covert delivery within §9.1–§9.4, not just Debrief
- **Content** — IntelDeliverySlip, Modifier Cards, informal Accord terms, written messages; content types Debrief cannot carry
- **Ghost doctrine** — Ghost's intelligence trading capability (currently absent); also enables under-the-table deals for all factions

Narrative framing: **SMS with attachment** — one faction sends a sealed packet to another. The packet may contain anything a faction can physically hand over.

---

## Component — Faction Message Packet

A faction-labeled envelope. Each faction's Dispatch Case contains one envelope per other faction, pre-labeled with that faction's name/symbol. No TO/FROM fields — direction is context-derived from position.

**Reading direction by context:**
- In sender's possession / handed to ARBITER → read as outgoing (TO [faction])
- In receiver's case on return → read as incoming (FROM [faction])

**Routing flow:** Message packet → Dispatch Case → ARBITER

**Example:** Ghost sends to Syndicate. Ghost loads content into their SYN-labeled envelope, places it inside their Dispatch Case alongside covert ops, seals, and hands the case to ARBITER at §9.1 — same physical motion as always, no separate submission gesture. At Beat 0, ARBITER opens Ghost's case, finds the SYN envelope, moves its contents into Syndicate's GHO-labeled envelope (already in Syndicate's case). Ghost's empty SYN envelope returns with Ghost's case at Beat 3. Syndicate opens case at Beat 3–4 boundary, sees GHO envelope has content — reads as from Ghost.

**Per-case inventory:** 4 faction-labeled envelopes (one per each other faction — not own faction).

**Total at setup:** 5 factions × 4 packets = **20 packets**. Fixed supply, distributed at game setup alongside Dispatch Cases.

**Legislation note:** The message packet is sufficiently analogous to the action packet that new legislation gaps should be minimal. Key differences to legislate: no Dispatch Token required; no resolution trigger; ARBITER routes rather than resolves; contents are not a board state until delivered. Most existing action packet rules will not apply — it's a transport component, not an action component.

**Contents (any combination):**
- Intel Token(s)
- IntelDeliverySlip(s)
- Modifier Card(s)
- Native Resources
- Written message (informal Accord terms, plain text, offers, threats)
- Nothing (bluff packet)

**Cost to send:** Free. No Dispatch Token required. No resource cost.

**Visibility:** Entirely within ARBITER's domain. The message packet travels inside the sealed Dispatch Case — no observable submission gesture. Other factions see Ghost hand their case to ARBITER as normal; they cannot observe that a message is inside. ARBITER routing (case to case at Beat 0) occurs within ARBITER's physical workspace. The recipient discovers the message only when their case is returned at the Beat 3–4 boundary. No faction other than sender, ARBITER, and recipient has any knowledge a message was sent — unless a Beat 0 intercept card is played.

---

## Delivery — Option A: ARBITER Intermediary ✅ Confirmed S119

Direct faction-to-faction handoff (Option B) was considered and rejected: it produces no interceptable board state and no Ghost design space. ARBITER as intermediary is the confirmed delivery mechanism.

**How it works:**
- Sender seals packet and hands to ARBITER during **§9.1 Covert Dispatch**, alongside case assembly
- ARBITER receives, reads, and routes the packet — **all processing complete by end of Beat 0**
- Packet placed in destination faction's receive slot before Beat 1 begins
- Procedure is generalizable: the same Beat 0 step handles all message packets regardless of content

**Observable properties:**
- Transit is visible: all players see a packet handed to ARBITER and placed at a destination
- Destination faction is visible; contents are not
- Creates a board state (a physical packet exists at a known location = valid target for card effects)
- Interceptable: Ghost can develop Packet Intercept cards that create a compelled-disclosure trigger

---

## ARBITER Visibility — ✅ Confirmed S119

**ARBITER reads all packet contents.** No exceptions. Consistent with ARBITER's supreme-observer doctrine (electronic version precedent: ARBITER knowledge is total).

**ARBITER's obligation: none by default.** Reading does not create a disclosure duty. ARBITER holds the information in its own domain (GR 10.1b applies: discloses from own domain only when a valid trigger is submitted).

**Compelled disclosure via card action:** A faction may play a card (e.g., Ghost Packet Intercept) that submits a valid trigger compelling ARBITER to open and reveal packet contents. This is the only disclosure path. No card = no disclosure.

**Design implication:** Every faction sending a message implicitly accepts that ARBITER knows its contents. This is not a vulnerability — it is the nature of ARBITER's role. Factions choose to send anyway because the alternative (no covert communication) is worse. Written informal accords carry the same weight as spoken ones: ARBITER is aware, but awareness alone creates no enforcement obligation.

---

## Timing — ✅ Confirmed S119

**Messaging occurs in §9.1 / Beat 0 — before resolution.**

**Rationale (order of knowledge):** Messages are composed and submitted in §9.1, before PAs are declared (§9.2) and before any resolution information is available (Beats 1–3). A faction cannot send a message referencing information they do not yet have. The covert queue is sealed before ARBITER routes the packets. Knowledge order is preserved: message content reflects only what was known at §9.1 submission time.

**Sequence within the monthly cycle:**

```
§9.1  Covert Dispatch     ← messages submitted here, alongside Dispatch Cases
§9.2  Public Declaration  ← PAs declared (message not yet delivered)
§9.3  Countermeasures
§9.4  Resolution:
  Beat 0  The Cases Open  ← ARBITER reads packets, routes to destination; 
                             packets fully processed and back in sealed form by end of Beat 0
  Beat 1  Read Board State
  Beat 2–3  Covert Resolution
  Beat 4  Public Acts Resolve
§9.4.4  Close Month
```

**When does the recipient read their message? ✅ Confirmed S119**

All returns — Dispatch Cases AND message packets — stay with ARBITER through Beat 3. Return is simultaneous between Beat 3 complete and Beat 4 begin.

Factions receive covert op outcomes and messages at the same moment. They enter Beat 4 (Public Act resolution) with full information from both. PA declarations are already locked (§9.2) so this information cannot alter the queue — but it informs how factions watch Beat 4 unfold and what they negotiate in future months.

**Ghost Packet Intercept window: ✅ Confirmed S119**

Interception occurs within Beat 0, after the resolution grid is fully built. Message packets are opened AFTER action packets — Ghost's intercept resolution requires the Beat 3 grid to already exist (floor intel fallback references it).

**Beat 0 sub-step order — confirmed S119:**

```
Beat 0:
  1. Open all action packets (Dispatch Cases) → build full resolution grid
       [all CA/PA operations placed; Beat 3 queue established per faction]
  2. Open message packets (AFTER grid is built)
       ARBITER reads all message packet contents
  3. Resolve Ghost Intercept cards
       Ghost submitted Packet Intercept at §9.1, naming a target faction
       IF message exists to/from target:
         → reveal message contents to Ghost (intercept); consume message or re-seal per card text
       IF no message exists for target:
         → produce IS-xx on target faction's first CA in Beat 3 queue (floor intel)
  4. Re-seal remaining message packets → place in destination queue
  5. All packets + cases held by ARBITER until Beat 3–4 boundary
```

**Ghost pre-commitment requirement:** Ghost submits the Packet Intercept card at §9.1 alongside their Dispatch Case. Ghost names the target at submission time — before Beat 0, before knowing whether any message will be sent. Ghost cannot adjust the target after seeing traffic.

**Floor intel fallback:** If the target faction sent no message that Month, the Packet Intercept card produces an IS-xx (IntelDeliverySlip) on the first CA in the target faction's Beat 3 queue — identical in effect to GHO.CA.2 Intercept but generated at Beat 0, not Beat 2. Ghost always receives minimum intelligence value from the intercept card; the card is never wasted.

**Card design implication:** The Ghost Packet Intercept card is a dual-purpose intelligence card:
- **Primary effect** (message present): message content disclosed to Ghost
- **Fallback effect** (no message): IS-xx on target's first Beat 3 CA

This makes the prediction element meaningful but low-risk — Ghost bets on diplomatic communication patterns, and if wrong, defaults to standard covert intelligence. The card's value floor prevents it from being a pure gamble.

**Debrief note:** §11 already provides free Intel Token and resource trades between factions. The message packet system adds value during the Month, not as a Debrief replacement. Content types not covered by Debrief (IntelDeliverySlip, Modifier Cards, informal Accord terms, written messages) are the unique contribution.

---

## Ghost Design Space (Option A)

If Option A is chosen, Ghost gains a natural card design space for interacting with the messaging system:

| Ghost CA concept | Layer | Function | Analogy |
|---|---|---|---|
| Packet Intercept | Information | Reveal | GHO.CA.2 Intercept (covert ops) |
| Packet Corruption | Information | Corrupt | GHO.CA.12 Source Substitution |
| Packet Trace | Information | Reveal | Disclose sender/recipient to named faction |

These would live in Ghost's CA set alongside the existing covert op intercept cards. Ghost becomes not just an intelligence collector but an intelligence broker and communications interceptor.

---

## Open Questions

1. **Can Ghost alter and re-seal an intercepted packet?** If Ghost intercepts, can Ghost re-seal and forward it (modified or unmodified) — or does interception mean the packet is consumed/voided? Extending Ghost's corruption doctrine into messaging vs. keeping interception as pure intelligence gathering.
2. **Physical component design** — faction-labeled envelopes confirmed. Must be physically distinguishable from the Dispatch Case and action packets at the table. Exact form TBD (Art 02 component entry).
3. **Informal Accord validity** — written messages are player-to-player with no mechanical enforcement. ARBITER is aware but has no obligation to flag violations unless a card trigger compels it. Confirm this is the intended position.
4. **Multiple messages per month** — unlimited (free action) or a limit per faction per Month? If free, there is no cost to flooding ARBITER with traffic — may be intended (noise is a Ghost concern) or may need a limit.
5. **Ghost intercept target specificity** — must Ghost name a sender–recipient pair, or can Ghost target all messages from/to a named faction? Blanket targeting is more powerful; pair targeting requires better prediction but is more surgical. Note: floor intel (IS-xx fallback) fires regardless of whether the named target is a sender or recipient — this needs to be defined in the card spec.
6. **IS-xx on floor intel** — if target faction has no CA in Beat 3 queue (they submitted no covert op that Month), does the floor intel fire at all? Possible: no CA in queue = card still not wasted — Ghost gets attribution that the faction submitted no covert action (itself intelligence). Or: card produces nothing if no CA queued (pure gamble). Needs a decision.

---

## Art 03 / Art 06 Integration Notes

**Procedure language rule (confirmed S119):** Beat 0.3 and all covert messaging procedure steps in Art 03 must be written without faction-specific language — even if Ghost is the only faction currently designed with cards that interact with this step. The procedure describes the mechanical step; the card's `beat` field and effect text self-identify the faction. Art 03 language: "any faction holding a Beat 0 intercept card" — never "Ghost."

This system eventually lives in Art 06 (Classified Directives / covert system components). Procedure will require:
- §9.1 amendment: message packet assembly and submission step added to Covert Dispatch
- Beat 0 amendment: message packet sub-steps (§9.4.0.x) — generalised, no faction names
- New component entry: Faction Message Packet (Art 02)
- New procedure entry: Covert Messaging (Art 03 §9.x or Art 06 §x)
- Beat 0 intercept card procedure: generalised trigger, dual-effect (message intercept / IS-xx fallback)
- Faction CA cards targeting this procedure: designed per faction doctrine, not named in the procedure (Art 04)

---

*Last updated: S119 (2026-06-25)*
