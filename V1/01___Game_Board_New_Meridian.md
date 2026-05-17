# 01 — Game Board: New Meridian
## THE SIGNAL P1 — Paper Prototype

**Version:** 1.2 Signed Off  
**Status:** Signed Off — Stable Draft  
**Depends on:** 00 — Factions, World & Narrative Context  
**Supersedes:** setup_guide (board sections), board_layout (visual reference only)

---

## 1. Overview

### Problem This Document Solves
The game needs a physical space where all activity takes place and all information is displayed. Without a fully specified board, no other artifact can define where actions target, where resources generate, where presence is tracked, or where the narrative of the session unfolds. This document defines every district, every track, every zone, and every piece of information the board must communicate — in sufficient detail that visual design and physical production can proceed without ambiguity.

### Deliverable
A complete specification of the New Meridian game board: 21 districts across three rings (Sprawl, Infrastructure, Core) plus the Chorus Node, five shared information tracks, dedicated zones for ARBITER materials and active agreements, and the starting configuration that opens every session.

### Success Criteria
- Any player can look at the board mid-session and calculate every faction's current resource income without assistance
- ARBITER can manage all board-state changes from their position without needing to touch player areas
- The board's visual organization reflects the narrative geography of New Meridian — the Chorus Node at the top, the city spreading outward and downward
- A visual designer can produce the board layout from this document alone without ambiguity

---

## 2. Index

1. Overview
2. Index
3. Game Purpose
4. Narrative Function
5. Design Principles
6. Rules & Constraints
7. Component Description
8. Special Conditions & Gameplay Impacts
9. Examples & Exceptions

---

## 3. Game Purpose

The board serves four simultaneous functions:

**Economic ledger:** All resource generation is readable from the board. Presence tokens, influence levels, and structure tokens together determine every faction's income each round. No hidden calculations required.

**Territorial record:** The current state of contested and controlled districts is always visible. Any player can assess the balance of power at a glance.

**Information display:** All shared tracks — World Conditions, round progress, initiative order, active Situation Report, Public Standing, active Accords — are displayed on or adjacent to the board surface and updated in real time.

**Narrative stage:** New Meridian is not an abstract grid. It is a city with history and geography. The board's layout tells a story: who arrived first, what they built, and what the city became around the Chorus Node at its center.

---

## 4. Narrative Function

The Chorus Node sits at the top of New Meridian, north of the city. Everything that followed — every institution, every district, every faction — grew southward from that point over thirty years. The board's shape reflects that history: an inverted arc, the city spreading east and west and south from the transmission source, like a signal propagating outward.

The rings are not concentric circles. They are sediment layers — each one representing a wave of growth as the city expanded away from the Node. The Core districts formed first, close to the source. The Infrastructure ring grew to support them. The Sprawl was last, the city's outermost layer where most of New Meridian's people actually live.

District placement within each ring follows geographic and narrative logic. Districts that depend on one another are adjacent. Districts whose factions have historical relationships are near each other. The map should be readable as a city, not as a game board.

---

## 5. Design Principles

1. **The board is always honest.** All presence tokens, operational markers, structure tokens, and influence level markers are visible at all times. No board state is ever hidden from any player.

2. **Geography creates consequences.** A district's ring determines its resource generation value. A district's neighbors determine Incursion Battlefield Strength zones and operational marker placement eligibility. Position on the map is never arbitrary.

3. **The center is always relevant.** The Chorus Node's strategic incentives — Chorus Activity suppression, Chorus Portrait amplifier, Chorus Question access, Translation rate scaling — ensure it remains a contested objective throughout the session regardless of its lack of resource output.

4. **Rings are not equal.** Sprawl districts are accessible and low-value. Infrastructure districts are the economic engine of the mid-game. Core districts are high-value and require commitment to enter. This creates natural strategic progression across a session.

5. **Resource type is immediately readable.** Each resource type has a distinct background color applied to the district. A player can identify the resource type of any district across the table without reading text.

6. **The board must be readable at speed.** During Resolution, ARBITER makes board changes quickly. Component shapes, colors, and placement conventions must allow ARBITER to update the board state without pausing to interpret what they are looking at.

---

## 6. Rules & Constraints

### Board Shape and Orientation

New Meridian is printed as an organic, non-hexagonal map in an inverted arc (half-circle) shape. The Chorus Node is placed at the top center. Districts radiate outward and downward — Core districts immediately below the Node, Infrastructure ring below that, Sprawl at the outer edges.

District shapes are organic rather than geometric — they represent actual city districts, not abstract game spaces. Borders between adjacent districts are clearly marked. Each district is large enough to accommodate up to 6 presence tokens, 2 operational markers, and 1 structure token per faction without becoming unreadable.

Resource type is conveyed through background color. The resource icon and district name are printed on each district. Base generation value is printed as a number. All of this information is always visible regardless of tokens placed on the district.

### Ring Structure and Entry Requirements

| Ring | Districts | Base Generation |
|------|-----------|----------------|
| Sprawl | 9 | 1 per round |
| Infrastructure | 7 | 2 per round |
| Core | 4 | 3 per round |
| Chorus Node | 1 | None |

**Entry Rule A — Free entry from inner ring:**
If a faction is Established or Dominant in any district on a more inner ring that is adjacent to the target district, they may place an operational marker in the target district freely during the Placement phase. No difficulty penalty applies.

**Entry Rule B — Outer ring entry without inner adjacency:**
If a faction has no Established or Dominant presence on any adjacent district from a more inner ring, all operations targeting that district suffer a Challenging difficulty penalty. This applies regardless of whether the faction has Present-level presence or an operational marker in the district.

**Second marker and temporary presence:**
Operational markers count as temporary presence tokens for all purposes during the quarter they are placed, including entry requirement calculations. *This is the canonical global definition — operational markers are presence tokens for all purposes during their placement quarter. Not restated on individual cards. See 02a §6 Global Presence Convention.* A faction's first marker placed during the Placement phase may create or improve their influence level in a district. Their second marker placed later in the same Placement phase may reference that temporary influence when evaluating entry requirements. A faction that places their first marker to establish temporary Established presence in a Sprawl district may use that presence to freely place their second marker in an adjacent Infrastructure district.

**Entry rule does not restrict operational marker placement in the Sprawl.** Any faction may place either or both operational markers in any Sprawl district at any time, regardless of prior presence.

**Entry to the Chorus Node:**
The Chorus Node ignores Entry Rules A and B entirely. Regardless of adjacency, ring relationship, or any other condition, placing an operational marker at the Chorus Node requires that the placing faction already holds **Established or Dominant** presence in at least one Core district adjacent to the Node — either through permanent presence tokens or through temporary presence created by an operational marker placed earlier in the same Placement phase.

This means the minimum path to the Chorus Node in a single Placement phase is:
1. Place first operational marker in an adjacent Core district where the faction has at least 1 permanent presence token (creating temporary Established presence if the marker brings them to 2 effective tokens with no competing faction at higher count)
2. Place second operational marker at the Chorus Node, referencing the Established status just created

If a faction has no permanent presence tokens in any adjacent Core district, they cannot reach the Chorus Node in that Placement phase regardless of what their first marker does — a single marker alone creates only Present-level temporary presence (1 token equivalent), which does not satisfy the Established requirement.

### District Information Requirements

Every district on the board must simultaneously display:

| Information | Display Method | Visible To |
|-------------|---------------|------------|
| District name | Printed text on district | All |
| Ring | Visual treatment — border weight, or position in arc | All |
| Resource type | Background color of district | All |
| Base generation value | Printed number on district | All |
| Faction presence tokens | Physical tokens placed on district | All |
| Influence level | Dominant marker on controlling faction's stack; Contested marker on district | All |
| Structures present | Structure tokens on district (distinct shape from presence tokens) | All |
| Operational markers this round | Large distinct pieces placed during Placement phase | All |
| Special rules | Distinct icon printed on district (Chorus Node, Residential Quarter) | All |

### Track Zones

**World Condition Tracks** (right edge of board or adjacent panel):
Three parallel tracks with numbered scales:
- Disclosure: 1–6
- Consensus: 1–6
- Chorus Activity: 1–10, with Chorus Question threshold marked (default: 6)

Each track uses a single clip or bead marker. ARBITER moves markers during Beat 1 and Beat 5 of Resolution.

**Round Tracker** (top edge of board):
Eight numbered positions (Rounds 1–8) with a single marker. ARBITER advances at start of each Upkeep.

**Initiative Strip** (adjacent to Round Tracker):
Five labeled slots showing current faction order. Updated by ARBITER at start of each Placement phase.

**Active Situation Report Zone** (right side of board or adjacent panel):
Card-sized display area where the current Broadcast Card sits face-up for the round duration. Replaced each round by ARBITER.

**Public Standing Tracks** (bottom edge of board or separate laminated strips):
One track per faction showing the 0–20 scale with named band labels. All factions start at 10. Markers move when ARBITER processes Public Standing changes.

**Active Accords Zone:**
Registered Accord documents displayed face-up and visible to all players. This zone may be placed off the mat if table space requires it — on a designated area of the table adjacent to the board. Accords do not need to be physically on the board surface; they need to be visible to all players.

---

## 7. Component Description

### District Map — Placement and Narrative Rationale

Districts are listed from north (top of map) to south (bottom), then west to east within each ring. Adjacency is described narratively — visual design will confirm exact borders.

**CENTER**

| # | District | Resource | Color | Narrative Placement |
|---|----------|----------|-------|---------------------|
| 21 | Chorus Node | None | Distinct — no resource color; neutral or cosmic treatment | The origin point of everything. Placed at the top center of the map. All other districts grow from here. |

**CORE RING** (immediately south of Chorus Node, curving east-west)

| # | District | Resource | Color | Narrative Placement |
|---|----------|----------|-------|---------------------|
| 17 | Government Citadel | Mandate | Mandate color | West of center below the Node. The first permanent institution established after the readings were classified. Directorate presence here predates the city. |
| 18 | Military Installation | Mandate | Mandate color | Far west of Core, adjacent to Government Citadel. Built to secure the Node perimeter. Positioned at the edge of the Core ring facing outward — a barrier between the city and the source. |
| 19 | Chorus Research | Findings | Findings color | East of center below the Node, adjacent to the Node itself. The primary scientific facility. Built as close to the Node as physically possible. |
| 20 | Financial Sanctum | Capital | Capital color | Far east of Core. Arrived after the research institutions — capital follows significance. Positioned at the edge of the Core ring facing outward toward the financial infrastructure below. |

**INFRASTRUCTURE RING** (below and outside the Core, the city's working layer)

| # | District | Resource | Color | Narrative Placement |
|---|----------|----------|-------|---------------------|
| 10 | Power Grid | Capacity | Capacity color | West side, adjacent to Military Installation. The Guild built the power systems that run the entire Node complex. Positioned close to the Directorate's military presence — the working relationship between them is geographic. |
| 11 | Financial Clearinghouse | Capital | Capital color | East side, below Financial Sanctum. The Syndicate's primary operational anchor. Positioned on the east side to mirror the Financial Sanctum above it — capital accumulates along the eastern corridor. |
| 12 | Data Exchange | Findings | Findings color | Center, below Chorus Research. The data infrastructure that processes everything coming from the Node. Ghost's analytical networks run through here. |
| 13 | Communications Hub | Exposure | Exposure color | Center-east, adjacent to Data Exchange and Communications flowing eastward. The broadcast and relay infrastructure. The Network's established foothold in the Infrastructure ring — information generated in the Data Exchange flows east through here. |
| 14 | Logistics Center | Capacity | Capacity color | West-center, adjacent to Power Grid. Supply chain and distribution infrastructure supporting the Guild's operations. Positioned between the Power Grid and the Sprawl's Industrial Fringe. |
| 15 | Research Institute | Findings | Findings color | Center-west, adjacent to Data Exchange and Chorus Research. Secondary research facility — overflow from the Core's research capacity, populated as the Chorus study expanded beyond what the Core could hold. |
| 16 | Regulatory District | Mandate | Mandate color | Far west, adjacent to Power Grid. The Directorate's administrative presence in the Infrastructure ring — where institutional authority extends into the city's working systems. |

**SPRAWL RING** (the outer arc, the city's populated layer)

| # | District | Resource | Color | Narrative Placement |
|---|----------|----------|-------|---------------------|
| 4 | Industrial Fringe | Capacity | Capacity color | Far west, adjacent to Logistics Center. Where manufacturing and heavy construction happens. The Guild's Sprawl foothold — the outer edge of their operational territory. |
| 6 | Transit Hub | Capacity | Capacity color | West-center, adjacent to Industrial Fringe and Logistics Center. Transportation infrastructure connecting the Sprawl to the Infrastructure ring. Strategically placed between Guild-adjacent districts. |
| 7 | Civic Center | Mandate | Mandate color | Center-west, adjacent to Regulatory District. Public-facing institutional presence — local government offices, civic services. The Directorate's most visible presence in the civilian population. |
| 3 | Residential Quarter | Mandate | Mandate color | Center, the most populated district. Adjacent to Civic Center and University Perimeter. Where most of New Meridian's residents live. Amplifies Public Standing effects — see Special Conditions. |
| 1 | University Perimeter | Findings | Findings color | Center, adjacent to Residential Quarter. Academic and research community. Ghost and The Network both began building here — it sits between the intellectual and communications corridors of the city. |
| 2 | Media District | Exposure | Exposure color | Center-east, adjacent to University Perimeter and Communications Hub. The Network's primary anchor. Positioned at the junction of the academic and communications corridors — where research becomes broadcast. |
| 8 | Broadcast Tower | Exposure | Exposure color | East, adjacent to Media District. Secondary broadcast infrastructure, extending The Network's reach toward the city's eastern edge. |
| 9 | Observation Post | Exposure | Exposure color | Far east, at the outer edge of the arc. A media monitoring and public intelligence facility at the city's boundary — where New Meridian watches itself being watched by the outside world. |
| 5 | Commercial Strip | Capital | Capital color | Far east, adjacent to Observation Post. Commercial and retail infrastructure. The Syndicate's Sprawl presence — positioned at the eastern edge where commerce follows media and information. |

### Starting Configuration

| District | Ghost | Network | Syndicate | Guild | Directorate | Starting Level |
|----------|-------|---------|-----------|-------|-------------|----------------|
| University Perimeter | 1 | 1 | — | — | — | Both Present |
| Media District | — | 2 | — | — | — | Network Established |
| Residential Quarter | — | — | — | — | — | Empty |
| Industrial Fringe | — | — | — | 1 | — | Guild Present |
| Commercial Strip | — | — | 1 | — | — | Syndicate Present |
| Transit Hub | — | — | — | — | — | Empty |
| Civic Center | — | — | — | — | 1 | Directorate Present |
| Broadcast Tower | — | 1 | — | — | — | Network Present |
| Observation Post | — | — | — | — | — | Empty |
| Power Grid | — | — | — | 3 | — | Guild Dominant ★ |
| Financial Clearinghouse | — | — | 3 | — | — | Syndicate Dominant ★ |
| Data Exchange | 2 | — | — | — | — | Ghost Established |
| Communications Hub | — | 2 | — | — | — | Network Established |
| Logistics Center | — | — | — | 1 | — | Guild Present |
| Research Institute | 1 | — | — | — | — | Ghost Present |
| Regulatory District | — | — | — | — | 1 | Directorate Present |
| Government Citadel | — | — | — | — | 1 | Directorate Present |
| Military Installation | — | — | — | — | 2 | Directorate Established |
| Chorus Research | 2 | — | — | — | — | Ghost Established |
| Financial Sanctum | — | — | 2 | — | — | Syndicate Established |
| Chorus Node | — | — | — | — | 1 | Directorate Present |

★ Dominant markers placed at setup for Power Grid (Guild) and Financial Clearinghouse (Syndicate).

### Starting Round 1 Income

| Faction | Income Calculation | Total |
|---------|-------------------|-------|
| Ghost | Data Exchange Established (2) + Research Institute Present (1) + Chorus Research Established (3) + passive (1) | **7 Findings** |
| Network | Media District Established (1) + University Perimeter Present (0) + Broadcast Tower Present (0) + Communications Hub Established (2) + passive (1) | **4 Exposure** |
| Syndicate | Financial Clearinghouse Dominant + affinity (3) + Commercial Strip Present (0) + Financial Sanctum Established (3) + passive (1) | **7 Capital** |
| Guild | Power Grid Dominant + affinity (3) + Industrial Fringe Present (0) + Logistics Center Present (1) + passive (1) | **5 Capacity** |
| Directorate | Military Installation Established (3) + Government Citadel Present (1) + Regulatory District Present (1) + Civic Center Present (0) + Chorus Node Present (0) + passive (1) | **6 Mandate** |

---

## 8. Special Conditions & Gameplay Impacts

### Residential Quarter — Public Standing Amplifier

Residential Quarter generates 1 Mandate at Dominant control — the lowest economic return of any district. Its strategic value is entirely political.

All global Public Standing effects for factions with presence in Residential Quarter are multiplied based on that faction's influence level there. This applies to every Public Standing change that faction experiences anywhere on the board, for as long as they maintain presence.

| Influence Level | Multiplier |
|----------------|-----------|
| Dominant | ×2 |
| Established | ×1.5 (round toward stronger effect) |
| Present | ×1.25 (round toward stronger effect) |
| Contested condition active | ×1 |
| Absent | ×1 |

Positive multipliers round up. Negative multipliers round up in magnitude (further from zero). Factions with positive Public Standing trajectories want Residential presence. Factions with Discovery risk want to avoid it.

### University Perimeter — Network Resource Conversion

University Perimeter generates Findings for all factions. The Network may freely convert any Findings generated here into Exposure at a 1:1 rate during resource distribution. This conversion is automatic if Network chooses it — no action cost, no resource cost. It reflects The Network's operational reality: information gathered at academic institutions is immediately broadcast rather than held as intelligence. No other faction may make this conversion. No other district offers resource conversion of any kind.

### Chorus Node — Strategic and Narrative Value Only

The Chorus Node generates no resources. No structures may be built here. Its value is strategic and narrative:

**Chorus Activity Suppression:** Any faction with Established or higher influence at the Chorus Node reduces Chorus Activity track advancement from Situation Reports by half (round down) each round. Present-level presence does not suppress. Contested condition does not suppress.

**Chorus Portrait Amplifier:** Each quarter a faction holds Established at the Chorus Node, ARBITER moves their Portrait marker one step further in its current direction — +1 if currently positive, −1 if currently negative. No movement if at zero (Ambiguous). Not available during Contested condition. ARBITER administers per 00a R01.

**Chorus Question Access:** Only factions with at least Present influence (including operational marker) at the Chorus Node may propose a Chorus Question when the window opens. Not available when the Chorus Node is Contested — the window does not open that quarter.

**Translation Rate:** The conversion rate for The Translation (resource conversion via ARBITER) scales with the requesting faction's presence at the Chorus Node: Established = 2:1, Present = 3:1, no presence = 4:1 (standard), Contested = 5:1. The Contested rate is ARBITER's response to factions bringing conflict into the Chorus Node. Rate table: Artifact 02a §8 (D02a-01).

**Narrative Significance:** Presence at the Chorus Node is the clearest signal that a faction intends to shape humanity's answer. ARBITER notes it. The Chronicle reflects it.

### Contested Condition

The Contested condition is a board state, not an influence level. It applies when two or more factions are tied for the highest presence token count in a district at 3 or more tokens — meaning multiple factions simultaneously qualify for Dominant. Because Dominant requires strictly more tokens than all others, no faction can hold Dominant while a tie exists.

**No faction can be Dominant in a Contested district.**

ARBITER places a Contested marker (neutral chip) on the district when this condition arises and removes it the moment one faction pulls strictly ahead.

**Resource generation under Contested condition:**

Any faction with 3 or more tokens in a Contested district generates 1 unit flat regardless of that district's base generation value. This applies to all factions at 3+ tokens — including any faction that would otherwise become Dominant in the power vacuum created by the tie.

Factions below the 3-token threshold are governed by their normal influence level:
- The faction in second place by token count with 2+ tokens is Established and generates full resources — even while higher-count factions are Contested above them
- Factions in third place or lower generate at their normal Present rate

**Structure protection under Contested condition:**

No faction receives Dominant-level structure protection (Challenging difficulty to demolish) while the district is Contested. All factions with 3+ tokens under Contested condition receive standard (Average) demolish difficulty against their structures.

Full influence level rules and all Contested examples are specified in Artifact 02a — Resource Systems: Board State.

---

## 9. Examples & Exceptions

### Entry Requirements — Second Marker Using First Marker's Temporary Presence

Round 3 Placement phase. The Network has no permanent presence in the Infrastructure ring. During the Placement phase, The Network places their first operational marker in Communications Hub (Infrastructure). This marker counts as 1 temporary presence token — The Network now has 1 effective presence token in Communications Hub, making them Present there temporarily.

The Network places their second operational marker in Data Exchange (Infrastructure), which is adjacent to Communications Hub. Entry Rule A asks: is The Network Established or Dominant in any adjacent inner-ring district? No — Communications Hub is Infrastructure, the same ring as Data Exchange, not more inner. Entry Rule B applies: Challenging difficulty on operations targeting Data Exchange.

However: if The Network had placed their first marker in Chorus Research (Core) — adjacent to Data Exchange — that would satisfy Entry Rule A for the Data Exchange placement. The temporary presence in a Core district (more inner ring) adjacent to the Infrastructure target would allow free placement of the second marker.

### Contested Condition — Second Place Benefits

Round 5. Ghost and The Syndicate both have 4 presence tokens at Data Exchange. The Guild has 2 presence tokens at Data Exchange.

Ghost and The Syndicate are tied at 4 tokens — both qualify for Dominant but neither can hold it. Contested marker is placed. Both generate 1 Findings flat.

The Guild has 2 tokens — second place by count, 2-token minimum met. The Guild is Established. The Guild generates full Data Exchange value: 2 Findings.

The Guild, with only 2 tokens, is the most productive faction in Data Exchange while Ghost and Syndicate fight. This state persists until one of the tied factions gains a token.

### Chorus Node — Reaching It in a Single Placement Phase

The Chorus Node requires Established or Dominant presence in an adjacent Core district — temporary presence counts, but only if it reaches Established level.

**Condition that makes this possible:** A faction has at least 1 permanent presence token in an adjacent Core district before the Placement phase begins. Placing their first operational marker in that district brings their effective token count to 2. If no other faction has 2 or more tokens there, that faction is temporarily Established. Their second marker may now be placed at the Chorus Node.

**Example:** Round 4 Placement. The Guild has 1 permanent presence token in Government Citadel (Core), placed in a prior round. During Placement, The Guild places their first operational marker in Government Citadel — their effective count rises to 2 tokens. The Directorate has only 1 token there. The Guild is temporarily Established in Government Citadel. Government Citadel is adjacent to the Chorus Node. The Guild places their second operational marker at the Chorus Node. Entry requirement satisfied.

At Upkeep, both markers convert to permanent tokens if not blocked — giving The Guild 2 permanent tokens in Government Citadel and 1 at the Chorus Node.

**Condition that prevents this:** If The Guild had no permanent tokens in any adjacent Core district before Placement, their first marker would create only 1 effective token — Present level only. Present does not satisfy the Chorus Node entry requirement. The second marker cannot go to the Chorus Node that phase regardless of adjacency.
