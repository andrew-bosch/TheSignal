# THE SIGNAL — Hardware Specification

**Document:** 11  
**Status:** Complete (component selection final — production path TBD)

---

## System Overview

The physical system consists of four hardware components that work together as a unified experience:

1. **Player Terminals** — Personal ESP32-S3 devices, one per player
2. **ARBITER Unit** — Central Raspberry Pi 5 server with camera, projection, and audio
3. **Laser Projector** — Ultra-short-throw unit mounted to ARBITER arm
4. **The Mat** — Neoprene projection surface with calibration markers

All components communicate over a local WiFi network hosted by the ARBITER unit. No internet connection is required during sessions.

---

## Player Terminal

### Design Philosophy

The terminal should feel like a serious instrument from a near-future world — not consumer electronics, not a toy. The aesthetic is **Brutalist Instrument**: aluminum body, visible screws, heavy buttons, the touchscreen as an intrusion of the future into an older design language.

Old technology paired with new capability. The device looks like it was designed before touchscreens existed and someone cut a precise hole and installed one.

### Core Components

**Processing**
```
ESP32-S3 dual-core 240MHz
512KB RAM + PSRAM option
WiFi 802.11 b/g/n
Bluetooth 5.0
Native USB support
```

**Display**
```
ILI9341 3.2" TFT LCD
320x240 resolution
65,536 colors
XPT2046 resistive touch overlay
Recessed behind glass, 1.5mm
```

**LED System — WS2812B Addressable**
```
Left status cluster:    4 LEDs (vertical strip)
Right status cluster:   4 LEDs (vertical strip)
Pulse bar:             16 LEDs (horizontal, bottom edge)
ARBITER ring:           8 LEDs (top edge, upward-facing)
NFC indicator:          1 LED (adjacent to NFC reader)
Total:                 33 addressable LEDs per terminal
```

**Status Cluster LED Assignments**

| Position | Left Cluster | Right Cluster |
|----------|-------------|---------------|
| Top | Capital (#FFB300 gold) | Assets (#4CAF50 green) |
| Upper | Infrastructure (#4A90D9 steel blue) | Public Influence (#FFFFFF white) |
| Lower | Signal (#9B59B6 violet) | Operational Influence (#AAAAAA soft white) |
| Bottom | Intelligence (#00BCD4 cyan) | Reserved |

**LED Behavior Encoding**
- Steady bright: healthy/high
- Steady mid: moderate
- Steady dim: low
- Slow pulse: changing this round
- Fast pulse: critically low
- Double flash: resource just spent
- Breathing: passive income active
- Off: zero/unavailable

**NFC**
```
PN532 NFC/RFID module
Rear-mounted reading surface
Single status indicator LED
Reads: NFC215 tags, custom tokens
```

**Audio**
```
NO SPEAKER — haptic only
Vibration motor for private notifications
All audio is public via ARBITER unit
```

**Physical Buttons**
```
POWER:    Recessed, rubber gasket, requires intent
MENU:     Standard tactile, satisfying click
CONFIRM:  Large, metal cap, heavy click weight
          [Deliberate commitment required]
ALERT:    Ribbed sides, tactile distinct
          [Opens ARBITER private channel]
```

**Power**
```
LiPo 2000mAh
TP4056 charging via USB-C
Estimated session life: 6-8 hours
```

### Enclosure

**Form Factor**
```
Dimensions:  145mm × 105mm × 28mm
Weight:      280-320g target
Table angle: 15-20 degrees (rear wedge built in)
```

**Materials**
```
Main body:      Aluminum alloy, CNC milled or cast
Screen bezel:   Black anodized aluminum, 1.5mm recess
Button caps:    Machined aluminum tops, rubber base
                CONFIRM button: brass/copper cap
Rear panel:     Textured black rubber, non-slip
LED windows:    Frosted acrylic diffusers, amber-tinted
Screws:         Visible hex socket, brass finish
```

**Faction Color System**
- Bottom edge stripe: 6mm faction-colored anodized aluminum
- Visible from above when terminal lays flat
- Architect: Brushed silver
- Ghost: Matte dark grey
- Syndicate: Deep black with gold accent
- Signal: Dark olive/military green
- Warden: Dark navy

**Rear Face**
- Faction mark (embossed, subtle)
- NFC reader zone with target emboss
- Battery cover with 4 visible hex screws
- USB-C charging port
- Covenant mark: engraved symbol, first Covenant permanent

### Boot Sequence (LED Choreography)

```
0.0s:  CONFIRM button backlight flickers
0.2s:  NFC indicator single white pulse
0.5s:  Status clusters light bottom-to-top, dim faction color
1.0s:  Pulse bar illuminates left-to-right, faction color sweep
1.5s:  ARBITER ring begins first pulse, dark → deep blue
2.0s:  Screen activates with slow fade from black
        Shows: ◈ [ARBITER symbol, amber, centered]
2.5s:  Text fades in: "ARBITER SIGNAL TERMINAL / INITIALIZING"
3.0s:  Recognition prompt appears
3.5s:  All LEDs settle to resting states
```

### Full BOM Per Terminal

| Component | Cost (est.) |
|-----------|------------|
| ESP32-S3 dev board | ~$8 |
| ILI9341 3.2" touchscreen | ~$12 |
| PN532 NFC module | ~$6 |
| WS2812B LEDs (33) | ~$3 |
| 4× tactile buttons | ~$1 |
| Vibration motor | ~$2 |
| LiPo 2000mAh | ~$8 |
| TP4056 charging module | ~$1 |
| Custom PCB (if made) | ~$5-10 |
| 3D printed or machined enclosure | ~$25-40 |
| Misc (wiring, connectors, screws) | ~$3 |
| **Total per terminal** | **~$74-94** |

---

## ARBITER Unit

### Design Philosophy

Cylindrical — a deliberate contrast to the rectangular terminals. Mounted above the table center, projecting downward onto the mat. The physical embodiment of ARBITER's presence.

The LED ring faces upward, casting colored light on the ceiling and players' faces. In subdued lighting, the ring's blue glow is the dominant ambient light source at the table.

### Form Factor

```
Shape:     Cylinder
Diameter:  180mm
Height:    120mm
Material:  Brushed aluminum body, black anodized end caps
Finish:    Matte
```

### Core Components

**Compute**
```
Raspberry Pi 5 (8GB RAM)
256GB SD card or USB SSD storage
Handles simultaneously:
  - Computer vision processing
  - Game logic and state management
  - WiFi access point
  - Web server (website + terminal API)
  - Projection rendering
  - Audio generation and playback
  - LED control
  - Claude API integration
```

**Camera**
```
Raspberry Pi Camera Module 3
12MP, wide angle
Bottom face, centered
Recessed, protected
Views entire mat from mounting height
Optional: IR ring light for token detection
```

**LED Ring**
```
24× WS2812B, top face
Ring diameter: 150mm
Driven by Pi GPIO
Visible from across the room
Syncs with all terminal rings
```

**Audio**
```
USB audio interface
Full-range driver, 3-4 inch, 5-10W amplified
MAX98357A I2S Class D amplifier
Frequency response: 80Hz-18kHz
Physical volume knob on housing
Speaker grille: 8 holes × 2mm, top edge
```

**NFC (Administrative)**
```
PN532 via USB
Administrative card initialization
Token registration
Not used during active sessions
```

**Administrative Interface**
```
USB-A ports: 2 (NFC admin, peripherals)
USB-C: power input
HDMI: projector output (primary)
HDMI: monitor output (secondary/admin)
Ethernet: wired internet for API sync
Admin key slot: USB-A, signed certificate
Small status display: 2-4" SPI screen (admin mode only)
```

### ARBITER Ring States

| Color | State | Description |
|-------|-------|-------------|
| Deep blue #1A237E | Normal | Always-on, 4-second pulse (shortens over session) |
| White #FFFFFF | Resolution | ARBITER processing, steady |
| Amber #FFB300 | Reckoning | Single pulse, returns to blue |
| Faction color | Player's turn | Brief shift during active player's phase |
| Deep violet #4A148C | Stage 4+ | Barely perceptible blue shift |
| Clinical white | Admin mode | Different quality than Resolution white |
| Red #C62828 | [One instance recorded] | Nobody asks about the red |
| Rainbow | Session end | All faction colors sweep through |

**Pulse Period Shortening:** Ring cycles at 4.0 seconds in Round 1, shortening imperceptibly to ~2.0 seconds by Round 8 of a late Covenant. Players feel the acceleration without measuring it.

**Directional Addressing:** With seat positions known from CV detection, the ring can sweep to face a specific player when ARBITER addresses them directly.

### ARBITER Unit BOM

| Component | Cost (est.) |
|-----------|------------|
| Raspberry Pi 5 8GB | ~$80 |
| 256GB storage | ~$30 |
| Camera Module 3 | ~$25 |
| WS2812B ring (24 LED) | ~$8 |
| NFC module | ~$6 |
| Audio amplifier + speaker | ~$20 |
| Small status display | ~$15 |
| Aluminum housing (machined) | ~$60-100 |
| Mounting arm (adjustable) | ~$30-50 |
| Misc electronics | ~$20 |
| **Subtotal (excl. projector)** | **~$294-354** |

---

## Laser Projector

### Requirements

```
Throw ratio:    0.3:1 or less (ultra-short-throw)
Resolution:     1920×1080 minimum
Brightness:     1500+ ANSI lumens
Technology:     Laser phosphor or laser RGB
Interface:      HDMI from Raspberry Pi 5
Contrast:       High (dark backgrounds need true black)
Startup:        Instant on (no warm-up)
```

**Why Laser Over Lamp:**
- Instant on/off (ARBITER can dramatically activate the board mid-session)
- More saturated colors (faction color differentiation)
- Consistent output (no warm-up shift)
- Long life (no lamp replacement)

### Mounting Configuration

```
Mount type:    Adjustable arm
               - Ceiling mount for permanent installations
               - Floor stand for portable setup
Height:        60-80cm above table surface
Output:        At 70cm height, 0.3:1 ratio produces ~90cm × 50cm image
```

### Candidate Projectors

- BenQ GP20 (ultra-short-throw, portable)
- Optoma ML1080ST (compact UST)
- Custom: Laser module + scan mirror (more complex, more controllable)

**Projected image cost range:** $400-800

---

## The Mat

### Specifications

```
Material:    Heavy neoprene or thick felt
Dimensions:  120cm × 80cm
Color:       Very dark grey (#1A1A1A equivalent)
Thickness:   4mm minimum
Edge:        Stitched border, slight weight for flatness
Surface:     Matte finish, no glare
```

### Printed Elements

**Calibration Marks (functional)**
- Small corner marks in IR-reflective ink
- Invisible under normal light, visible to camera under IR
- Used for automatic projection calibration at session start
- ARBITER aligns projection to mat without manual adjustment

**Player Position Indicators (subtle)**
- Embossed marks for 6 seat positions around mat edge
- Used for ARBITER's directional ring LED addressing
- Very subtle — not visible unless looked for

**Faction Territory Marks (atmospheric)**
- Very subtle, very dark geometric marks suggesting starting zones
- Almost invisible until you know they're there
- The projection overlays precisely on these marks

**ARBITER Mark (physical)**
- The ARBITER ring symbol, embossed (not printed)
- Physical texture at center of mat
- Where the Chorus Node hex will be projected
- ARBITER's camera finds this mark and aligns projection to it

### Underside Text

```
ARBITER SIGNAL SYSTEM
OPERATIONAL SURFACE

This surface is the property of The Table.
Its use constitutes acknowledgment of
ARBITER's authority over all proceedings
conducted upon it.

COVENANT [space for number]
[Space for session marks]

ARBITER REMEMBERS.
```

### Calibration Sequence

```
1. Mat laid on table
2. ARBITER unit activates
3. Camera switches to IR mode briefly
4. Detects four corner calibration marks
5. Calculates mat position, angle, irregularities
6. Adjusts projection geometry
7. Verifies with test pattern
8. Switches to game projection
Total time: <10 seconds, fully automatic
```

---

## Seat Detection System

ARBITER identifies which player sits in which position using layered detection:

### Detection Methods (Priority Order)

**1. NFC Token Authentication (Primary)**
- Player taps token to terminal
- Terminal position known from camera
- Maps player identity → terminal → seat position
- Most reliable method

**2. CV Terminal Detection (Secondary)**
- Camera detects terminal positions from LED rings and screen glow
- Identifies faction from LED color
- Maps to seat positions around mat
- Accuracy: ±5cm

**3. WiFi RSSI Triangulation (Tertiary)**
- 2-3 small reference nodes at table edges
- Measures signal strength from each terminal
- Estimates quadrant, not precise position
- Accuracy: ±30-50cm

**4. Self-Declaration (Fallback)**
- ARBITER projects arrows pointing to each seat
- Players tap terminals in sequence
- Works reliably, slightly breaks immersion
- Used only when automatic detection fails

### Seat Map Data

```
Positions: 0-5, clockwise from ARBITER north
Per position:
  - Detection confidence (0-1)
  - Detection method used
  - Player ID (if authenticated)
  - Terminal ID (if detected)
  - Last update timestamp
```

---

## Token Design

### Placement Tokens

**Purpose:** Placed on projected board during Placement Phase  
**Per faction:** 2 tokens  

**Specifications**
```
Diameter:    25mm
Height:      8mm
Top surface: ArUco marker (15mm) surrounded by faction color/symbol
Finish:      Matte (reduces projector glare)
Material:    Resin or machined aluminum
```

**ArUco ID Ranges**
```
Architect:  0-9  (up to 10 tokens)
Ghost:      10-19
Syndicate:  20-29
Signal:     30-39
Warden:     40-49
```

**Shape by Faction (for shape-recognition fallback)**
```
Architect:  Hexagon
Ghost:      Circle
Syndicate:  Square
Signal:     Triangle
Warden:     Shield
```

### Identity Tokens

**Purpose:** Player authentication via NFC tap  
**Per player:** 1 token  

```
NFC215 chip embedded (~$0.50)
Custom design — faction symbol
Weighted for satisfying feel
Kept by player between sessions
Lost token: passphrase fallback available
```

---

## Physical Components Summary

### Complete System Contents

```
ARBITER UNIT
  Cylindrical housing with all electronics
  Adjustable mounting arm
  Power supply + cables

PROJECTOR
  Ultra-short-throw laser unit
  HDMI cable

PLAYER TERMINALS (up to 6)
  One per player
  Faction-specific color stripe
  USB-C charging cable per terminal

THE MAT
  120cm × 80cm neoprene
  Storage tube or sleeve

PLACEMENT TOKENS
  2 per faction (10 total)
  ArUco marked, faction shapes

IDENTITY TOKENS
  1 per player (up to 6)
  NFC embedded

CARD SET
  366 cards total
  Generic vessel design
  NFC chips embedded
  Organized in faction trays

NFC STICKER SHEETS (consumable)
  For new card initialization
  Pre-numbered, registered ranges

MARK STICKER SHEETS (consumable)
  Gold, red, blue, black dots
  Card history indication

ADMINISTRATIVE KEY
  Custom USB drive
  Signed device certificate

STORAGE CASE
  Custom foam insert
  Everything has a place
```

### Setup Time

From closed case to session-ready: **under 10 minutes**

1. Lay mat on table
2. Position and power ARBITER unit
3. Power on terminals (boot: ~20 seconds)
4. ARBITER auto-calibrates projection (~10 seconds)
5. Players authenticate with tokens
6. Session configuration confirmed
7. Opening sequence begins

---

## Network Architecture (Summary)

Full specification pending in Document 13. Key decisions:

```
ARBITER WiFi:    Hosts local network (2.4GHz, 802.11n)
                 SSID: "ARBITER-[SESSION-ID]"
                 Password: session-specific, shown at setup

TERMINALS:       Connect to ARBITER AP
                 All communication through ARBITER server
                 No terminal-to-terminal direct communication

INTERNET:        ARBITER Ethernet for Claude API calls
                 Website sync between sessions
                 Not required during active play

PROTOCOL:        TBD — WebSocket vs MQTT (Document 13)
```

---

## OTA Firmware Updates

```
UPDATE PATH:     Pi serves firmware binaries to terminals
TRIGGER:         Administrative console, between sessions only
NEVER:           During active session
DELIVERY:        ESP-IDF native OTA update mechanism
ROLLBACK:        Automatic on boot failure
FALLBACK:        USB-C direct flash always available
VERSION CHECK:   On every terminal connection to ARBITER
```

---
