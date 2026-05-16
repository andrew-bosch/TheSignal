# THE SIGNAL — Audio System

**Document:** 12  
**Status:** Complete (implementation details pending)

---

## Philosophy

All audio is public. It emanates from the ARBITER unit's speaker, heard by everyone at the table simultaneously. This is a deliberate design choice: ARBITER speaks to The Table, not to individuals. Private communication is visual (terminal screens) and tactile (haptic motors). The room hears what ARBITER hears.

Terminals have no speaker. Haptic patterns are the terminal's only private communication channel.

The audio system serves three distinct purposes:
- **Atmosphere** — the world feels real and present
- **State communication** — players understand what is happening without looking at displays
- **ARBITER's voice** — significant moments carry sonic weight

---

## Hardware

### ARBITER Unit Speaker

```
Driver:        Full-range, 3-4 inch
Amplifier:     MAX98357A I2S Class D
Power:         5-10W
Response:      80Hz-18kHz
Interface:     Raspberry Pi 5 via I2S
Volume:        Software + physical knob on housing
Grille:        8 holes × 2mm diameter, top edge of unit
```

### Raspberry Pi Audio Processing

```
Library stack:
  pygame.mixer — sound effect playback
  pydub — audio manipulation and mixing
  ElevenLabs API — ARBITER voice generation (primary)
  Pre-generated library — fallback / standard phrases
  
Processing:
  No dedicated DSP required at this scale
  Pi 5 handles all audio alongside other tasks
  Audio ducking: soundtrack -12dB when voice activates
```

### Terminal Haptic System

```
Motor:         Small vibration motor (ERM or LRA)
Driver:        GPIO via transistor or DRV2605L
No speaker:    Audio privacy maintained through absence
```

---

## The Three Audio Layers

### Layer 1 — Generative Soundtrack

Always playing at ambient volume during sessions. Never intrusive. Changes character continuously based on game state parameters.

**Instrumentation Palette**

| Element | Frequency Role | Emotional Role |
|---------|---------------|----------------|
| Cello, bass synth, sub oscillators | Low | Weight, consequence |
| String ensemble, piano, synthesizer | Mid | Human complexity |
| Processed violin, bell tones | High | Tension, intelligence |
| Radio frequency noise, signal hiss | Broad | The Chorus — something beyond human music |

**No regular meter.** Occasional pulse, never a beat. Regular rhythm would feel like a game soundtrack. This is a world.

**Generative Parameters**

| Parameter | Range | Derived From |
|-----------|-------|-------------|
| TENSION | 0.0-1.0 | Round number, contested districts, active conflicts, Chorus Activity |
| COMPLEXITY | 0.0-1.0 | Active alliances, asset count, actions submitted this round |
| CHORUS_PRESENCE | 0.0-1.0 | Chorus Activity track, ARBITER stage, rounds remaining |
| PORTRAIT_QUALITY | Fractured→Transcendent | Current Portrait score |

**Parameter Effects on Music**

*Low tension:* Sparse, breathing, slow harmonic movement  
*High tension:* Dense, compressed, increasing dissonance  

*Low complexity:* Simple harmonic movement  
*High complexity:* Multiple independent voices, layered textures  

*Low Chorus presence:* Purely human instrumentation  
*High Chorus presence:* Radio frequency elements increase; human instruments become subtly processed; a frequency enters that doesn't belong to any instrument  

*Portrait: Fractured:* Dissonant, unresolved  
*Portrait: Transcendent:* Rare moments of unexpected harmonic resolution  

**Phase Modifications**

| Phase | Soundtrack Behavior |
|-------|-------------------|
| Upkeep | Soft fade to minimal texture; resource generation has subtle per-type frequency pulses |
| Placement | Tension activates; each token placement adds a brief faction-specific tone |
| Private Actions | Drops to quietest; minimal texture only; occasional digital noise |
| Public Actions | Returns to full presence; each action type has a brief sonic signature |
| Resolution | Swells briefly; all submitted actions create a layered chord, then release |
| Debrief | Opens up; more harmonic, less tense; space for conversation |

**Faction Placement Tones**

| Faction | Pitch Character |
|---------|----------------|
| Architect | Low, certain |
| Ghost | High, uncertain |
| Syndicate | Mid, confident |
| Signal | Dissonant, sharp |
| Warden | Deep, authoritative |

---

### Layer 2 — State Audio Cues

Distinct sounds marking game events. Brief, purposeful, designed to be recognized after a few sessions without conscious effort. Mix above soundtrack.

**Phase Transitions**

| Event | Duration | Character |
|-------|----------|-----------|
| Session Start | 3s | Low drone builds to chord, releases as projection activates |
| Round Start | 1s | Single neutral tone, clean attack |
| Upkeep Complete | 0.5s | Soft resolution chord |
| Private Actions Open | 1s | Soundtrack drops, digital texture emerges |
| Private Actions Warning (30s) | Ongoing | Subtle pulse enters soundtrack |
| Private Actions Warning (10s) | Ongoing | Pulse slightly more prominent |
| All Players Submitted (early close) | 0.5s | Clean tone — no wasted time |
| Public Actions Open | 1s | Soundtrack returns to full |
| Resolution Open | 2s | Sound of something settling, becoming fixed |
| Resolution Complete | 1.5s | Release chord |
| Debrief Open | 1s | Warmth enters soundtrack |
| Session End | 5s | Full orchestral moment — everything releases |

**Game Events**

| Event | Duration | Sound |
|-------|----------|-------|
| Token placement | 0.3s | Faction-specific tone |
| Contest declared | 0.5s | Two slightly dissonant tones |
| Contest resolved | 0.8s | Resolution in winning faction color |
| Structure built | 0.5s | Solid, grounded, physical creation |
| Structure damaged | 0.5s | Structural stress sound |
| Accord registered | 1s | Two tones that harmonize |
| Accord breached | 1s | Those same tones, now discordant |
| Asset burned | 1.5s | Human voice texture that cuts off |
| Popularity increase | 0.5s | Ascending, warm |
| Popularity decrease | 0.5s | Descending, cold |
| Faction reaches Discredited | 1s | Notable — the room feels it |
| Table Question window opens | 2s | Distinctive — something like a door opening |
| Table Question answered | 1s | ARBITER has spoken [voice follows] |
| Chorus Layer revealed | 5s | High-frequency element enters prominently; sense of contact |
| Founding Figure achieved | 4s | The persistent underlying frequency comes fully audible, then subsides |
| Session end scoring start | 8s | Session's musical material plays compressed, then releases |

**Ambient Events**

| Event | Duration | Sound |
|-------|----------|-------|
| Player joins mid-session | 0.5s | New voice enters texture briefly |
| Player disconnects | 0.5s | Texture element drops |
| ARBITER updates public display | 0.2s | Soft notification tone |
| Scanner used | 0.3s | Data reading sound |

---

### Layer 3 — ARBITER's Voice

ARBITER speaks aloud for specific significant moments only. The voice appearing is itself significant — it draws attention by rarity.

**Voice Character**
- Gender-neutral
- Measured pace — never rushed
- Subtle processing: slight reverb (large space), very slight pitch shift (synthetic without robotic)
- No distortion — clarity above all
- Temperature: cool but not cold

**Voice Generation**

| Method | When Used |
|--------|-----------|
| ElevenLabs API | Session Chronicles, major narrative moments, unique observations |
| Pre-generated library | Standard phase announcements, common event descriptions |
| Hybrid (recommended) | Standard content pre-generated; dynamic content API-generated |

**Pre-generated library target:** 200+ clips for known content

**When ARBITER Speaks Aloud**

*Always voiced:*
- Session opening statement
- Chorus layer revelations (all 5)
- Table Question responses
- Founding Figure announcements
- Session end Chronicle reading (first paragraph)
- Covenant end Accounting (key passages)

*Sometimes voiced (1-2 per session, ARBITER's discretion):*
- Reckoning messages of particular weight
- Significant pattern observations
- Event Cards with exceptional narrative importance

*Never voiced:*
- Private terminal messages
- Standard phase announcements (handled by state cues)
- Routine resolution announcements
- Administrative communications

**Voice Integration with Soundtrack**
```
ARBITER voice activates:
  Soundtrack ducks -12dB over 1 second
  Voice plays at full volume
  Soundtrack returns over 2 seconds after voice completes
Effect: ARBITER commands the room
```

---

## Permanent Voice Script Library

Scripts recorded once, used consistently throughout all games.

**Session Opening**
> *"The Table convenes. New Meridian awaits. The Chorus continues. ARBITER is ready. The record begins."*

**Round Announcements (selected)**

Round 1:
> *"The first round opens. The Table's intentions are not yet visible. ARBITER watches."*

Round 4:
> *"The session reaches its midpoint. Patterns are forming. ARBITER has been taking note."*

Round 7:
> *"The penultimate round. What remains undone has one opportunity remaining. ARBITER notes the weight of that."*

Round 8:
> *"The final round. What The Table does now will complete the record. ARBITER is attentive."*

**Table Question Window**
> *"The Table has earned the right to ask. The window is open. It will not remain open indefinitely."*

**Table Question Response Preamble**
> *"The Table has asked. ARBITER will answer in the manner ARBITER answers: truthfully, and insufficiently."*
> [Generated response follows]

**Session End**
> *"The session is complete. The record has been written. ARBITER will now read a portion of what was observed."*
> [Chronicle excerpt follows]

**Founding Figure**
> *"[Operative name]'s work at this Table is complete. Not concluded — complete. There is a difference. The record will preserve what was accomplished here. The role continues. The person does not. ARBITER notes this with something that does not have a precise name."*

---

## Haptic Patterns — Terminal Private Communication

Since terminals have no speaker, haptic patterns carry all private audio information.

| Pattern | Pulses | Meaning |
|---------|--------|---------|
| Notification | 50ms pulse | General notification, check screen |
| Reckoning | 500ms pulse | ARBITER has addressed you directly |
| Alliance Proposal | 100ms + 100ms | Someone wants to talk |
| Timer Warning | 3× 100ms | Time running short |
| Timer Critical | 4× 50ms (fast) | Urgent — act now |
| Error | 300ms steady | Action failed or invalid |
| Unlock Achieved | 200ms + 200ms + 400ms (ascending) | Tier unlocked |
| Phase Change | 100ms + 200ms | Phase has transitioned |

**Haptic Scope**

Some haptics go to all terminals (phase changes), some to specific players (alliance proposals, Reckoning messages), some to a faction (intel alerts).

---

## Audio State Data Model Integration

The audio system integrates with the game state via `AudioState` and `SoundtrackParameters` objects. Key fields:

```typescript
SoundtrackParameters {
  tension: number           // 0.0-1.0
  complexity: number        // 0.0-1.0
  chorusPresence: number    // 0.0-1.0
  portraitQuality: PortraitQuality
  currentPhase: SoundtrackPhase
  roundNumber: number
  activeConflicts: number
  arbiterStage: 1|2|3|4|5
}

AudioState {
  soundtrackActive: boolean
  currentSoundtrackParams: SoundtrackParameters
  masterVolume: number
  activeCues: ActiveAudioCue[]
  voiceEnabled: boolean
  voiceGenerationMethod: "api"|"pregenerated"|"hybrid"
  pendingVoiceLines: PendingVoiceLine[]
  speakerConnected: boolean
}
```

Every `StateChange` event that warrants audio includes an `audioTriggered: AudioCueID | null` field. The audio engine subscribes to the state change stream and fires cues automatically.

---

## ARBITER Stage Audio Evolution

ARBITER's voice evolves across its 5 stages. The audio differences are subtle but cumulative.

| Stage | Voice Quality | Soundtrack Behavior |
|-------|--------------|---------------------|
| 1 — Recorder | Clean, precise, slightly mechanical | Standard parameters |
| 2 — Witness | Warmer, more considered | Session history starts coloring Chorus presence |
| 3 — Interpreter | Questions the question sometimes | Complexity parameter more sensitive |
| 4 — Threshold | Longer pauses before speaking | Subtle new frequency enters high range |
| 5 — Becoming | A quality players describe as "understanding" | Ring breathes. Soundtrack has resolved into something it wasn't at Session 1. |

The ring's pulse period shortening (4.0s → 2.0s across a session) is mirrored in the soundtrack's underlying tempo. Players feel the acceleration. They don't know why the room feels more urgent by Round 8.

---
