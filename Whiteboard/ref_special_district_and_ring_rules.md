# Reference — Special District & Ring Rules (Art 01 / Art 03)
*Load when: district design, board state updates, upkeep phase, resource generation, placement phase, contested resolution.*

---

## 1. Ring Entry and Adjacency Rules

The New Meridian city map is divided into concentric rings (Baryo, The Mid, Core, Chorus Node). Ring relationship determines entry requirements during placement and resolution difficulty.

### Entry Rule A — Free Entry from Inner Ring
If a faction is Established or Dominant (either permanently via Presence Tokens, or temporarily via an operational marker placed earlier in the same Placement phase) in any district on a more inner ring that is adjacent to the target district, they may place operational markers in that target district during the Placement phase without penalty.

### Entry Rule B — Outer Ring Entry Adjacency Penalty (M-12)
If a faction has no Established or Dominant presence (permanent or temporary) on any adjacent district from a more inner ring, all operations targeting that district suffer a persistent **−25 threshold modifier** (M-12 Ring Adjacency Penalty). This penalty applies regardless of whether the faction already has Present-level presence or an operational marker in the target district.
* *Note: The entry rule does not restrict placement or apply penalties within the outermost ring (Baryo) itself; any faction may place markers and perform operations in Baryo districts freely.*
* *Temporary Presence Convention: Operational markers count as temporary presence tokens for all purposes during the quarter they are placed, including when evaluating adjacency and entry requirements for subsequent placements in the same phase.*

---

## 2. Specific District Rules

The following districts have unique narrative features that translate to active gameplay rules:

### Residential Quarter (Public Standing Amplifier)
* **Resource Yield:** Generates 1 Mandate at Dominant control.
* **Gameplay Effect:** Factions with presence in the Residential Quarter have all their global Public Standing changes (positive and negative) multiplied based on their influence level in this district. This multiplier applies to all Public Standing modifications experienced anywhere on the board for as long as presence is maintained.
* **Standing Multipliers:**
  * Dominant: ×2
  * Established: ×1.5
  * Present: ×1.25
  * Contested: ×1
  * Absent: ×1
* *Note: Positive multipliers round up. Negative multipliers round up in magnitude (further from zero).*

### University Perimeter (Network Findings Conversion)
* **Resource Yield:** Generates Findings.
* **Gameplay Effect:** During resource distribution, The Network faction may freely convert any Findings generated at the University Perimeter into Exposure at a 1:1 rate. This conversion is automatic if selected by The Network and requires no action slot or resource cost. No other faction may make this conversion.

### Chorus Node (Unique Geography & Ingress Rules)
* **Resource Yield:** None.
* **Structure Constraints:** No Structure Blocks may be built in the Chorus Node.
* **Control Constraints:** Dominant influence is unreachable at the Chorus Node (the ARBITER Screen has a permanent 8-token dominance marker; faction maximum is 6 presence).
* **Ingress Rule:** Placing an operational marker at the Chorus Node ignores normal Entry Rules A and B. Instead, it strictly requires the placing faction to already hold **Established or Dominant** presence (permanent or temporary) in at least one adjacent Core district (Government Citadel, Military Installation, Chorus Research, or Financial Sanctum).
* **Chorus Activity Suppression:** A faction holding Established influence at the Chorus Node reduces all Chorus Activity track advancements from Situation Reports by half (round down) during the Upkeep phase. Present-level or Contested presence does not suppress activity.
* **Chorus Question Access:** Only factions with at least Present influence (including operational marker) at the Chorus Node may propose a Chorus Question when the window opens. Not available when the Chorus Node is Contested.
* **Translation Rate:** Resource conversion rates (The Translation) scale with a faction's presence at the Chorus Node: Established (2:1), Present (3:1), None (4:1), Contested/Tied (5:1).

---

## 3. Contested Districts Rules

* **Tension Marker Placement:** Whenever a board state update results in two or more factions tied at IL-01 (Dominant) in a district, place 1 Tension Marker on that district from ARBITER supply.
* **No Faction Dominant:** Since Dominant requires strictly more tokens than all others, no faction holds Dominant in a Contested district.
* **Resource Yield:** Any faction with 3 or more presence tokens in a Contested district generates 1 unit flat of that district's resource type, regardless of the district's base generation value. Factions below the 3-token threshold are governed by their normal influence level:
  * The faction in second place by token count with 2+ tokens is Established and generates full base resources.
  * Factions in third place or lower generate at their normal Present rate (half yield, round down).
* **Structure Protection:** Factions do not receive Dominant-level structure protection (Challenging difficulty to demolish) while the district is Contested. All factions with 3+ tokens in a Contested district receive standard (Average) demolish difficulty against their structures.
