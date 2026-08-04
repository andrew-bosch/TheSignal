# Reference — Board Narrative & District Character (Art 01)
*Load when: district design, board layout questions, physical component placement, narrative anchoring.*

---

## The Overview — Physical & Narrative Identity

The Overview is the game mat placed in the Central Area of the table. In the fiction, it is MIRROR's projection — a live display of the Civic Grid in the chamber where The Table convenes. The physical table is not an abstraction of New Meridian; it *is* the room in the story.

The Civic Grid was designed by Dr. Jae-won Seo as a fluid topographic model built on population density, economic flow, and resource access. The Directorate Security Liaison vetoed it and demanded fixed zones defined by blast doors, riot barricades, and power-grid kill switches. MIRROR projects the Security Liaison's version. Accurate — not to geography, but to how the city can be partitioned, locked down, and violently controlled.

**Board shape:** Organic, non-hexagonal half-circle (inverted arc). Chorus Node sits at top center; districts radiate outward and downward. This is a visual and narrative statement, not an abstract convention.

**Track placement:** Session Timeline and Initiative Strip on the left (P1/P2 side); Chorus Activity Track and Situation Report Area on the right (P5 side); Public Standing Track at the bottom (P3 side).

**Starting configuration:** Directorate holds the only faction presence at the Chorus Node at game start (1 token, Present level).

---

## Chorus Node — Narrative Identity

The origin point of everything. All other districts grew outward from the transmission source. Its position at top center is geographic and narrative: the city radiates away from it. Presence here is the clearest signal that a faction intends to shape humanity's answer. ARBITER notes it. The Chronicle reflects it. No resource output; no structures permitted.

---

## Ring Narrative Character

**Ring 1 — Core:** The innermost ring, built first. Founding institutions — the Directorate's Government Citadel predates the city itself; the Military Installation was built to secure the Node perimeter and faces outward like a barrier. Chorus Research sits as close to the Node as physically possible. Financial Sanctum arrived late — capital follows significance.

**Ring 2 — The Mid:** The working layer. Infrastructure and operations: power systems, data networks, broadcast relays, supply chains, regulatory apparatus. Information generated in Data Exchange flows east through Communications Hub. Capital accumulates along the eastern corridor from Financial Sanctum down to Financial Clearinghouse.

**Ring 3 — Baryo:** The populated outer arc. Where most residents live, where the city is watched, where commerce follows media. University Perimeter is where Ghost and Network both started — academic infrastructure at the junction of intellectual and communications corridors. The Observation Post sits at the city's boundary, where New Meridian watches itself being watched by the outside world.

---

## District Faction Geography

| Faction | Home territory |
|---------|---------------|
| Guild | Power Grid (10) · Logistics Center (14) · Industrial Fringe (4) · Transit Hub (6) — the infrastructure and supply chain arc |
| Syndicate | Financial Clearinghouse (11) · Financial Sanctum (20) · Commercial Strip (5) — the eastern capital corridor |
| Ghost | Chorus Research (19) · Data Exchange (12) · Research Institute (15) · University Perimeter (1) — the analytical and research corridor |
| Network | Communications Hub (13) · Media District (2) · Broadcast Tower (8) · Observation Post (9) — the information broadcast arc |
| Directorate | Government Citadel (17) · Military Installation (18) · Regulatory District (16) · Civic Center (7) — institutional presence at every ring |

**Residential Quarter (DB:3) — Ring 3 · Mandate · base gen 1.** Not any faction's home territory. Neutral civic district; 5 adjacencies: Financial Clearinghouse (11), Regulatory District (16), Research Institute (15), Civic Center (7), University Perimeter (1). Special significance: PS amplifier mechanic (see PM05 02-n27 — unsigned/pending placement).

---

## Zone vs. Component Distinction

A **zone** is a named location in physical space — exists whether or not anything occupies it. A **component** is a portable physical object placed within a zone during play, returned to the Game Box at session end. A component and a zone may share the same physical footprint without being the same thing: The Overview (component) fills the Central Area (zone) during play, but Central Area exists when the mat is packed away.

---

## ARBITER Physical Position

Position P6, head of the table. Upright screen creating a concealed area behind it. ARBITER Tableau is a face-up reference surface visible to all players in front of the screen. Full Tableau specification pending Art 07/08 refinement.

---

## Adjacency Model

**Source:** Art 01 §6.5. Canonical table: `district_adjacency` in `the_signal_db` (101 bidirectional rows, all Allow Ingress/Egress = TRUE).

Adjacency governs action targeting and placement legality — a faction's valid operation targets are constrained by which districts are adjacent to their current footprint.

**Ring entry restrictions (ingress rules):**
- **Ring 3 → Ring 2 (The Mid):** subject to adjacency check + Ring Adjacency Penalty M-12 (difficulty modifier on crossing into The Mid)
- **Ring 2 → Ring 1 (Core):** requires Established or Dominant presence in an adjacent Ring 2 district at time of placement
- **Ring 1 → Ring 0 (Chorus Node):** requires Established or Dominant presence in an adjacent Ring 1 district at time of placement; excluded from normal adjacency rules

Full 101-row bidirectional table: Art 01 §6.5.

---

## Ring Modifier Decks

Rings 1, 2, and 3 only. The Chorus Node has no Ring Modifier Deck.
