# Card Design Research Notes
## Research for: The Signal — Card Data Structure Review
**Date:** 2026-05-19  
**Scope:** Deep research into published card game data structures, deckbuilding principles, negotiation/political game mechanics, MTG/Scryfall schema, hidden simultaneous action mechanics, and design literature.  
**Purpose:** Identify fields or principles genuinely missing from The Signal's card schema — not confirming what's already there.  
**Status:** Non-artifact reference document. Filed in `Projects/Whiteboard/`. Informs Artifact 04 §6 (Card Data Structure). Not part of the project artifact set.

---

## Methodology & Attribution

**Research conducted by:** Claude Sonnet (Anthropic) — AI-assisted structured analysis, session 23 (2026-05-19), commissioned by Andy Bosch for The Signal project.

**Method:** Comparative schema analysis. Published card game databases and design documentation were reviewed for fields present in those systems but absent from The Signal's card data structure. Each finding was evaluated against L108 (Database Translatable Data Design) compliance requirements and The Signal's V1 paper prototype scope. Fields already present in The Signal under Signal-specific names were mapped and excluded from recommendations.

**External sources referenced:**

| Source | What was examined | Reference format used in notes |
|--------|------------------|-------------------------------|
| MTG/Scryfall API | Full card object schema — `set`, `collector_number`, `oracle_id`, `oracle_text`, `keywords`, `type_line`, `released_at`, `reprint`, `variation_of`, `reserved`, `legalities`, `prices` | "MTG/Scryfall" |
| Netrunner DB (NRDB) | Community card database — `card_cycle_ids`, `card_set_ids`, `deck_limit`, `is_unique`, `card_abilities`, `date_release`, `num_printings`, `printing_ids`, `updated_at` | "Netrunner/NRDB" |
| Arkham Horror LCG (Fantasy Flight Games) | Card structure — encounter set symbol, card number within set, investigator level pips, timing windows (When/After/Forced), signature card eligibility | "Arkham Horror LCG" |
| Marvel Champions (Fantasy Flight Games) | Card timing tags — `Interrupt`, `Response`, `Forced Response`, `When Revealed`, `After` | "Marvel Champions" |
| Slay the Spire (Mega Crit Games) | Card flags — `Innate`, `Exhaust`, `Ethereal`, `Retain` | "Slay the Spire" |
| Aeon's End (Indie Boards & Cards) | Breach/nemesis tier mechanics | "Aeon's End" |
| Dominion (Rio Grande Games) | Hand limit / deck cycling / mid-game acquisition model | "Dominion-style" |

**AI generation note:** This document was produced by a language model (Claude Sonnet) through a single structured research session. Citations represent the model's training knowledge of publicly documented game systems and APIs as of its knowledge cutoff. Schema field names cited from Scryfall and NRDB reflect those databases' documented structures; they have not been independently verified against live API endpoints. Field names and counts may have changed in subsequent updates to those systems.

---

## Preliminary: What The Signal Already Covers (Do Not Recommend)

Before the gap analysis, map apparent standard fields to what The Signal already implements. Several commonly recommended fields are already present under Signal-specific names:

| Standard concept | Signal equivalent | Location |
|---|---|---|
| Timing/priority/speed | Beat (numbered resolution beat) | Art 04 §6 |
| Keyword/trait grouping | Taxonomy — Category/Function/Target | Art 04 §6, Art 04b |
| Faction affinity / cross-faction cost | Faction affinity + Affinity bonus | Art 04 §6 |
| Asymmetric reputation tracking | Per-faction Portrait fields (×5 factions, ×4 sub-fields = 20 fields) | Art 04 §6 |
| Outcome tiering beyond pass/fail | Effect on crit success / success / failure / crit failure | Art 04 §6 |
| Flavor text vs. rules text | Tagline (flavor), Narrative anchor (in-world), separate effect fields | Art 04 §6 |
| Visibility/information scope | VS-xx table | 00b §5.9 |
| No-persistent-cross-round effects | Design Principle 11 | Art 04 §5; Art 04b §3.8 |
| React/trigger conditions | Action — React function in taxonomy | Art 04b §4 |
| Gap analysis / design space tracking | Coverage analysis with priority ratings | Art 04b §6 |

These do not need to be added.

---

## 1. Fields Present in Published Games, Absent from The Signal

### 1.1 Version / Revision Identifier

**What it is:** Every printed card in every living game system carries a set code, printing identifier, or revision number that identifies which iteration of the card is in play.

**Published examples:**
- MTG/Scryfall: `set` (e.g., "lea"), `collector_number`, `released_at`, `reprint` (boolean), `oracle_id` (stable across reprints), `variation_of` (links to original printing). Oracle text is the authoritative current ruling; printed text is what the card says in a specific edition. These are explicitly *separate fields*.
- Netrunner/NRDB: `card_cycle_ids`, `card_set_ids`, `date_release`, `updated_at`, `printing_ids`, `num_printings`.
- Arkham Horror LCG: Encounter set symbol + card number within set (e.g., "3/15") appear on every card.

**Why it matters for The Signal:** The Signal is in active playtest development. Cards are revised between sessions. Artifact 04 currently has no field for tracking which version of a card is in circulation. If C10 is revised between sessions 21 and 22, there is no way to distinguish old printproof copies from new ones on the table. When misplay occurs during testing, there is no field to cite as the authoritative version.

**Gap:** The Signal card schema has no `Card version` or `Last revised` field. The design note field exists below the data block, but it is prose, not a structured version identifier. This is a genuine L108 gap: version is a typed value that should be a controlled field, not embedded in prose.

**Recommendation:** See §7.1.

### 1.2 Trigger Condition as a Structured Field (for Reactive Card Types)

**What it is:** The condition that must be true before a reactive card can be played. In many card game systems this is a machine-readable or at least formally structured field separate from effect text.

**Published examples:**
- Marvel Champions: Cards carry explicit timing tags — `Interrupt`, `Response`, `Forced Response`, `When Revealed`, `After`. These are distinct named timing windows that determine *when* a card fires. A Forced Response fires whether the player wants it to or not; a Response fires only if the player chooses to.
- Arkham Horror LCG: Same taxonomy — "When X would happen" (interrupt window) vs "After X happens" (response window) vs "Forced: After X" (mandatory response). These are not just text patterns — they are structural timing positions.
- Netrunner: Cards carry a `card_abilities` boolean flag set (e.g., `rez_effect`, `interrupt`), enabling programmatic identification of timing behavior.
- Art 04b §3.5: The Signal's taxonomy has a `React` function that fires "automatically when a named publicly-observable condition is met." But the schema carries no structured `Trigger condition` field — the condition is embedded in card effect text prose.

**Gap:** The Signal has Countermeasure cards (played during Phase 5) and React-function cards (C12 Materials Acquisition). Both have trigger conditions. Currently, the trigger condition is embedded in the `Restriction` field or the `Effect on success` prose. There is no structured `Trigger condition` field that separates *when* from *what*.

For V1 paper prototype, this may be workable. For L2+ database translation (L108 compliance), embedded-prose trigger conditions cannot be queried, validated, or enforced programmatically. A card like C12 whose React fires "when a named action resolution outcome" occurs needs that condition as a typed value, not buried in narrative text.

**Recommendation:** See §7.2.

### 1.3 Deck Limit / Copies-Per-Deck Constraint

**What it is:** An explicit field stating how many copies of a card may appear in a constructed deck.

**Published examples:**
- Netrunner/NRDB: `deck_limit` (typically 3, or 1 for identity cards). This is a card-level field, not a rule-level inference.
- MTG: No explicit deck-limit field on the card face, but the database tracks `reserved` (Reserved List) and `is_unique` equivalent fields. The "legendary rule" (max 1 in play at a time) is tracked via the `Legendary` supertype.
- Slay the Spire: Cards can be `Innate` (starts in first hand) — a constraint that modifies deck-composition behavior without a copies-per-deck number.
- Arkham Horror LCG: `Level` (0–5 pips) defines which investigator decks may include the card — a deck eligibility constraint.

**Gap:** The Signal describes setup pool sizes (30 covert / select 24; 20 political / select 12) and states that each faction's pool contains 2 copies of each standard type. But the card schema has no `Deck limit` or `Pool copies` field. The quantity available per faction is only documented in Art 04 prose (§7 header text), not as a per-card field.

For playtest prototype management and L2+ card management, this is a practical gap: when printing playtesting copies, there is no card-level field that says "print 2 of this" vs "print 1 of this" vs "print 1 per faction."

**Recommendation:** See §7.3.

### 1.4 Unique / Singleton Constraint

**What it is:** A boolean or constraint field indicating that at most one copy of this card may be in play simultaneously, regardless of how many copies exist in decks.

**Published examples:**
- Netrunner/NRDB: `is_unique` (boolean). Unique cards have a diamond symbol. If a second copy would enter play, the first is trashed.
- MTG: `Legendary` supertype — the Legendary Rule limits one of a given legendary permanent in play per player. `Reserved` (boolean) — Reserved List cards will not be reprinted.
- Arkham Horror LCG: Investigator-signature cards are implicitly unique by deck construction.

**Gap:** The Signal has Emergency Response cards (one per faction), which are functionally singleton — a faction has exactly one. But the schema carries no `Unique` flag. Similarly, if future card design produces one-per-session effects (currently prevented by Principle 11 but not impossible at Permanent scope), a unique constraint would be needed.

The gap is low-urgency at V1 but creates an L108 compliance issue: uniqueness is currently a design-principle inference, not a machine-readable field.

**Recommendation:** See §7.3 (can be combined with Deck Limit as a single constraint field).

### 1.5 Intra-Beat Priority / Tie-Breaker

**What it is:** When multiple cards resolve in the same Beat against the same or overlapping targets, what is the resolution order?

**Published examples:**
- Libertalia: Each character card has a `rank` (1–30). Day abilities resolve in ascending rank order; Dusk abilities in descending rank order. The rank field serves dual duty as identity and priority — it is the single field that determines who goes first in every phase.
- Marvel Champions: Among simultaneous triggers, `Forced` responses take priority over `Response`; player-chosen ordering applies within the same priority tier.
- MTG: The LIFO stack — last card played is first to resolve. Priority passes between players.
- Netrunner: Timing charts define ordered resolution within simultaneous triggers.

**Gap:** Art 03 §7 Initiative Patterns (IP-xx) determine which faction resolves first in a given Quarter. But initiative determines faction order globally — it does not resolve intra-Beat conflicts between two factions submitting the same card type to the same target in the same Beat. Art 04 §6 lists Beat as a card field but does not carry a sub-Beat priority field.

This gap surfaces when, for example, two factions both submit C04 Undermine targeting the same district in Beat 3. The current schema has no card-level field indicating which resolves first when beats collide on the same target. The Initiative Pattern handles this at the faction level, but only if Art 03 explicitly specifies that the initiative order also governs intra-Beat target conflicts. If it does, this is already covered. If it does not, the card schema needs an explicit note or the Art 03 rule needs a cross-reference on the card.

**Recommendation:** See §7.4.

### 1.6 Outcome Mode for Political Acts (Structured Vote Type)

**What it is:** A typed field distinguishing the *kind* of outcome a political act produces — binary (for/against), elect (choose a player), elect-target (choose a district or entity).

**Published examples:**
- Twilight Imperium Agenda Cards: Each agenda has an `outcome_type` that is either "For/Against" (binary vote), "Elect player," or "Elect planet/faction/technology." This determines how votes are cast and how the winning outcome is identified. It is a fundamental structural field, not narrative description.
- Root: Cards have a `suit` field (Fox/Rabbit/Mouse/Bird) that determines which factions can craft them and how they interact with faction abilities — a categorical type field that creates structured cross-card interactions.

**Gap:** The Signal's Political Acts are declared publicly, but the schema has no `Outcome type` field. Looking at the current card set: P08 Propose Accord creates a bilateral agreement (functionally "elect player" + agreement terms). P04 Denounce affects a named faction (functionally "elect player" targeting Public Standing). P07 Invoke the Table blocks all players (functionally "no-elect"). These are structurally distinct patterns, but the schema treats them as free-form effect text.

For V1 paper prototype, the ARBITER manages this through card text. For L2+ enforcement, the political resolution system needs to know what *type* of outcome to collect votes on. An `Outcome type` field on political acts would make political act resolution programmatically enforceable.

**Recommendation:** See §7.5.

### 1.7 Per-Field Visibility Scope Tagging

**What it is:** Application of the VS-xx Visibility Scope classification to specific fields within the card schema — not just to the card as a whole.

**Published examples:**
- Grand Archive TCG rules: "Face-up cards, their attributes, properties, stats, rules text, and other information are considered public. Face-down cards are considered private information." This is card-level, not field-level.
- MTG/Scryfall: Does not apply field-level visibility — a card is either face-up (all fields public) or face-down (no fields visible). The Signal's asymmetric design (some fields public, others ARBITER-only) has no equivalent in published systems.

**Gap:** The VS-xx table exists in 00b §5.9 and is applied at the entity level. But the card schema's individual fields are not tagged with visibility scope. Consider:
- `Effect on crit failure` — is this VS-04 (ARBITER-Only) until resolution? Players submitting a covert operation do not know they'll critically fail.
- `Portrait — [Faction]` fields — are these VS-04 (ARBITER scores the Portrait, players don't see the exact number)?
- `Narrative anchor` — VS-01 (Public) since it appears on the card face.
- `Faction perspectives` — VS-01 (Public). The field is printed on the card face — all factions read all perspectives.

Currently the schema does not carry per-field visibility tags. For L2+ compliance the API contract must know which fields to return to which party. 00b §8 explicitly states: "The visibility rules are enforced by ARBITER discipline in V1 and by server-side API scoping in L2+." Per-field VS-xx tagging on the card schema is the mechanism that enables that API scoping.

**Recommendation:** See §7.6.

---

## 2. Deckbuilding-Specific Principles

### 2.1 Shuffle Timing and Deck Cycling

The canonical deckbuilding mechanic (Dominion, Aeon's End) is: play cards from hand → discard → when deck exhausted, shuffle discard to reform deck. This creates a "deck cycling" economy where card acquisition now affects future turns.

**The Signal's departure:** The Signal does not have a Dominion-style cycling deck. Players select from a pool into a fixed hand each Quarter (setup pool → select deck → draw hand). There is no reshuffle trigger because there is no mid-game acquisition that adds cards to the deck. This is a deliberate design choice, not a gap.

**Aeon's End's relevant innovation:** Aeon's End deliberately removed deck shuffling — players choose the order of their discard before it becomes the new deck. This preserves information about card cycling and enables planning. The Signal's setup-then-play structure achieves something similar (you build your deck before the session, so cycle-order is predictable). Not a gap.

**What deckbuilding research does flag:** The distinction between cards in a *selection pool* vs cards in a *constructed hand* should be explicit in the card schema. Currently the schema describes what a card does but not its role in the selection process. Aeon's End separates Gem / Relic / Spell as deck-composition archetypes with distinct acquisition and play rules. The Signal's card types (Covert Operation, Political Act, Pass, Countermeasure, Modifier, Emergency Response) serve a similar archetypical function — but pool size and selection ratio are not card-level fields.

### 2.2 Hand Limits and Draw Triggers

Slay the Spire: Cards carry `Innate` (always in opening hand), `Ethereal` (exhausted if still in hand at turn end), `Retain` (not discarded at turn end). These are deck-construction and hand-management keywords that affect play without being pure mechanical effects.

**The Signal's equivalent:** The Signal does not have a draw system in the same sense. There is no `Innate` equivalent — faction-specific cards are not guaranteed to appear. The setup pool selection is the hand. This is a design departure, not a gap.

**What this surfaces:** If any future card design produces "always available" effects or "guaranteed in hand" mechanics, the schema will need a `Draw constraint` or `Availability guarantee` field. Currently absent, currently not needed.

### 2.3 Card Economy and Acquisition Type

Aeon's End Nemesis deck: Cards are tiered (Tier 1/2/3) with increasing difficulty. The deck is explicitly not shuffled. Each tier maps to a phase of the encounter. This is a `tier` field enabling structured escalation.

**The Signal:** Cards are available at session start rather than acquired mid-game. However, the concept of card *availability window* — which Beats or Phases a card can be submitted in — is implicit in card type rather than explicit. Covert operations go in Phase 3; political acts are declared in Phase 2; Countermeasures in Phase 5. These are type-derived rules, not fields on the card. For L2+ enforcement, an explicit `Submission phase` or `Available in phases` field would be more reliable than type inference.

---

## 3. Negotiation and Political Game Elements

### 3.1 Twilight Imperium — Agenda Cards

TI Agenda cards have:
- **Outcome type:** "For/Against" (binary) vs "Elect [player/planet/faction/technology]" — a fundamental structural field.
- **Card type:** Law (permanent, modifies ongoing rules) vs Directive (one-time effect). This distinction matters for effect duration.
- **Effect per outcome:** Each card has at least two discrete outcomes with different effects. The structure is `outcome_options[]` — an array of possible results — not a single `Effect on success`.
- **Eligibility constraint:** Some agendas can only be voted on by factions meeting a named precondition.

**Signal relevance:** Political acts have a single `Effect on success` and `Effect on failure`. But some Signal political acts have faction-specific or conditional outcomes (e.g., P08 Propose Accord depends on whether the target faction accepts). The schema does not have a structured `Outcome options` array for political acts — just success/failure text. For political acts with negotiated or voted outcomes, the current binary structure may be insufficient.

### 3.2 Dune — Treachery Cards and Bidding

Dune treachery cards have weapons and defenses chosen in secret, then revealed simultaneously. Key design insight: **the card's power is asymmetric to information state** — a weapon is only powerful if the defender doesn't hold the matching defense. The card value is not intrinsic; it is relational to the opponent's hand.

**Signal relevance:** The Signal's hidden dispatch case mechanic has the same asymmetric-information property. A card that succeeds against undefended targets but fails against a Countermeasure. The Signal does not explicitly model "counter-pairing" — there is no field linking a covert operation to the countermeasures that nullify it. Countermeasure Type A blocks specific district operations; Type B blocks faction-targeting operations. This pairing logic lives in the Countermeasure's card text, not in the covert operation's schema.

**Potential field:** A `Vulnerable to` or `Blocked by` field on covert operations that lists the countermeasure types or conditions that void them — parallel to Dune's weapon/defense pairing. Currently this is implicit (players read both cards and infer the interaction). For L2+ enforcement, explicit cross-references would be needed.

### 3.3 Root — Suit System

Root cards have a `suit` field (Fox/Rabbit/Mouse/Bird) that creates cross-faction utility: any faction can play a card for its suit value. This is a secondary-use field enabling card utility beyond the card's primary effect.

**Signal relevance:** The Signal's `Card faction: All` / `Faction-specific` subtype is the equivalent of Root's suit — it indicates cross-faction availability. But Root's suit is more granular: a card doesn't just have "All" or "Faction-specific" — it has a specific suit that may or may not align with a given faction's needs. The Signal could benefit from a more granular eligibility encoding if future card design introduces cross-faction conditional availability (e.g., "any faction with Established presence in the Infrastructure ring").

### 3.4 Oath — Shared Tableau and Card Circulation

Oath's most distinctive card design principle: cards are placed in the world (on locations), not held in private hands. Ruling a location grants access to cards placed there. This creates a shared-card-pool dynamic where card access is a function of territorial control.

**Signal relevance:** This is not a gap — The Signal does not use shared card pools. But it surfaces a design question: should future Signal cards include a `Location-linked` flag for cards that persist on a district after play (e.g., a structure-linked modifier that remains available to whoever controls the district)? Currently not in the schema.

---

## 4. Hidden Simultaneous Action Mechanics

### 4.1 Libertalia — Priority as Timing

Libertalia's core insight: **rank number is the resolution order field**. Every character card has a rank (1–30) that determines activation order in every phase. Day abilities fire ascending; Dusk abilities fire descending. The same field governs both — the phase context flips the sort direction. This single field eliminates all tie-breaking ambiguity.

**Signal relevance:** The Signal's `Beat` field determines which beat a card resolves in. Within a Beat, if multiple factions submit cards resolving in the same Beat against overlapping targets, the Initiative Pattern (IP-xx) determines faction order. But this resolution path depends on Art 03 explicitly specifying that IP-xx governs intra-Beat conflicts — and it depends on the card schema or rules reference making this cross-reference explicit. Libertalia's model is elegant because the priority is *on the card*, requiring no external lookup.

### 4.2 Cosmic Encounter — Alien Power Timing

Cosmic Encounter alien powers specify *when* they activate: "after encounter cards are revealed," "after alliances are formed," "after winner is determined." Each power card has an implicit timing field embedded in its text.

**Signal relevance:** Countermeasure cards and React-function cards both have activation timing embedded in prose text rather than structured fields. The Cosmic Encounter model shows that even in a game with high card-text variance, timing position can be extracted as a structured field.

### 4.3 The Resistance / Avalon — Role Cards vs Mission Cards

The Resistance distinguishes role cards (hidden identity assignment, one-time distribution) from mission/quest cards (played secretly per mission, binary success/fail). The data structure for each is completely different: role cards carry identity + loyalty alignment; mission cards carry only a binary action choice.

**Signal relevance:** The Signal's card types are already well-differentiated. But the hidden-role design literature surfaces one principle applicable to the dispatch case: **the card played represents a commitment, not information**. A card's "value" is not what it says — it's what the other players believe about what it says. This is a design principle rather than a schema field, but it has a schema implication: cards submitted to the dispatch case should carry `Visibility scope: VS-06 (Conditional)` on the effect fields, meaning effect fields are only surfaced after resolution. Currently VS-xx is not applied per-field on card schemas.

---

## 5. MTG / Scryfall Full Data Structure Highlights

Scryfall's Card struct (as of 2025–2026) carries 70+ fields. The following are *design-relevant* to The Signal's schema considerations, filtered for relevance:

### 5.1 The oracle_id / oracle_text distinction

Scryfall maintains two identifiers:
- `id` (UUID): Unique to a specific *printing* of a card.
- `oracle_id` (UUID): Stable across all printings of a card. The same card reprinted 10 times has 10 `id` values but one `oracle_id`.

Separately, `oracle_text` (authoritative current rules text) and `printed_text` (what is physically on the card) are separate fields. They differ when errata has been issued.

**Design principle extracted:** Separate *the rule the card follows* from *the text printed on the card*. These diverge when corrections are made. A game that is iterating toward publication (as The Signal is) will issue errata. If the card schema conflates "what the card says" with "what the rule is," errata management becomes manual correction of physical cards. If they are separate fields, errata is a database update, not a reprint.

### 5.2 Keywords as a Structured Array Field

Scryfall carries `keywords: Vec<String>` — a deduplicated array of all keyword abilities on the card (Flying, Haste, Trample, etc.), separate from `oracle_text`. This enables programmatic card search, combo identification, and rules enforcement without parsing natural language.

**Signal relevance:** The Signal's taxonomy (Category/Function/Target) serves a similar purpose and is more sophisticated than MTG's keyword array. But the taxonomy is a triple, not an array. If a card spans multiple taxonomy entries (e.g., C12 is `Resource + Action / Recover + React / Native resource`), the current single-row taxonomy field cannot express that without compound values — which violates L108 requirement 1 (no compound cells). The current field description acknowledges this with forward-slash notation but does not resolve it structurally.

### 5.3 Content Warning and Security Stamp

`content_warning: bool` — sensitivity flag for cards depicting mature themes.
`security_stamp: Option<SecurityStamp>` — authentication mark type (oval, triangle, acorn, etc.).

**Signal relevance:** Content warning is not applicable. Security stamp is not applicable at V1 paper prototype. Both irrelevant.

### 5.4 Print-Side Fields (Irrelevant to Signal)

`border_color`, `frame`, `frame_effects`, `watermark`, `foil`, `booster`, `prices`, `purchase_uris` — all production/retail/collectibility metadata. Entirely irrelevant for a paper prototype not entering retail production.

### 5.5 Legalities and Format Restriction

`legalities` tracks card legal status in every constructed format (Standard, Legacy, Commander, etc.).
`in_restriction` (Netrunner/NRDB) — current restriction list status (banned, rotated, etc.).

**Signal relevance:** The Signal does not have format legality in the TCG sense. But the *concept* — is this card available in a given game configuration? — maps to the Signal's card subtype (Standard vs Faction-specific) and the setup pool selection rules. For digital enforcement at L2+, a `Configuration eligibility` field might be needed if The Signal ever introduces scenario-specific card restrictions (e.g., "faction cards for factions not in play are excluded from the pool").

### 5.6 Rulings as a Linked Endpoint

Scryfall carries `rulings_uri` — a link to official rules clarifications for that card. Netrunner/NRDB similarly carries `relationships.rulings` — official rulings associated with the card.

**Signal relevance:** The Signal's Art 04 `Design note` field (prose below the card data block) serves as the rulings-equivalent document. For L2+ the design note could become a linked entity with its own schema — a `Ruling` entity linked by card ID — rather than embedded prose.

---

## 6. Design Principles from Literature

### 6.1 Keywords as Hooks (Nerdlab-Games / critpoints.net)

Keywords function as "hooks" that enable n-to-1 card interactions rather than n-to-n. A card referencing "React" enables all future React-function cards to interact with it without naming any individual card. Keywords compress rules text and enable programmatic combo identification.

**Design principle for The Signal:** The taxonomy (Category/Function/Target) is already operating as a keyword-hook system. Cards can reference the function label ("React," "Block," "Reveal") rather than individual card names. This is sophisticated card architecture. The gap is that these taxonomy tags are not exposed on the card face — they are metadata. If players cannot read "React — Action outcome" on C12 without consulting Art 04b, the hook's utility as a player reference is limited.

### 6.2 Duration as a Structured Field, Not Effect Text

Game systems that need persistence tracking (e.g., Highlander TCG's Duration subtype) carry duration as a typed field with a numeric value, not embedded in "effect lasts for 2 rounds" prose. Design Principle 11 removes this need for The Signal — all effects are immediate or permanent. But the *permanent vs immediate* distinction itself is not a field on the card schema. It is inferrable from effect text ("Place 1 structure block" = permanent until removed; "Remove 1 presence token" = immediate with permanent consequence). Worth encoding explicitly.

### 6.3 The oracle_text / printed_text Split and Errata Management

MTG's errata system proves that "what the card says" and "what the rule is" must be separate fields in any game expecting iteration. The Signal is pre-publication and actively revising cards. The design note field currently serves as errata commentary, but it is unstructured prose. For L108 compliance and the stated goal of database-translatable design (L108), errata management should be a first-class concern.

### 6.4 Systems Architecture: Cards as Lifecycle Objects

critpoints.net article on card game systems architecture: effective card systems treat cards as objects with lifecycle hooks — entry events, exit events, state change callbacks. Effects attach to hooks rather than being evaluated at resolution. This aligns with The Signal's Beat-based resolution: each Beat is a lifecycle hook, and cards attached to that Beat fire their effects when the hook fires.

**Design implication:** The Signal's Beat field positions each card at a lifecycle hook. The gap is that the *type* of lifecycle event (resolve effect, trigger countermeasures, apply modifiers) is not explicit. Beat 1 is the voiding beat; Beat 2 is the modifier beat; Beat 3 is the primary resolution beat; Beat 4 is the outcome beat. These are described in Art 03 — but the card itself does not carry a field indicating which lifecycle event it participates in at its Beat. For a card like C10 Protect (Beat 3), the card participates at the "apply effect" event. For Countermeasures (Phase 5), the card participates at a different lifecycle phase entirely.

### 6.5 Separate flavor text, rules text, and reminder text

MTG formally distinguishes:
- Rules text (oracle text — authoritative mechanical effect)
- Reminder text (italicized parenthetical — reminder of a keyword rule)
- Flavor text (narrative text — no mechanical effect)

The Signal's schema already separates these well: Tagline ≈ flavor text; Effect fields ≈ rules text; Narrative anchor ≈ extended flavor text. The one gap: there is no `Reminder text` field for keyword shortcuts. Currently the Signal does not use card-face keywords that require reminders, so this is not an active gap.

---

## 7. Recommendations for The Signal

**Substantive additions — genuine gaps in the current schema:**

### 7.1 Add: `Card version` (Required — L108 Gap)

**Field:** `Card version`  
**Type:** Controlled string (e.g., "v1.0", "v1.1") or date-stamped revision identifier  
**Visibility:** VS-01 (Public) — printed on card  
**Purpose:** Identifies which revision of this card is in play. Enables post-session errata tracking, distinguishes old playtest copies from current copies on the table.  
**L108 rationale:** Version is a typed, stable value that should be a named field, not embedded in the prose design note. All other L108 entities carry version at the artifact level — cards should carry version at the card level for the same reasons.  
**Why card-level, not artifact-level only:** Artifact 04 carries v0.9.7 — but within a single artifact version, individual cards are revised independently. C10 was revised in session N without bumping the whole artifact version. The PM02 Change Log records artifact-level changes, not per-card revision history. When a physical playtest copy of C10 from session 18 is on the table alongside a revised copy from session 21, there is no field on either card to distinguish them. The artifact version does not help a player or ARBITER identify which physical card is current. Card-level version solves a problem that artifact-level version cannot.  
**Not to be confused with:** Card ID (permanent primary key). The Card ID never changes; the version tracks revision history. Multiple versions of C10 remain C10 — but v1.0 and v1.2 may have different effect text.  
**Per-faction expansion:** No — flat field, single value.

### 7.2 Add: `Trigger condition` (Recommended — L108 and L2+ Gap)

**Field:** `Trigger condition`  
**Type:** Controlled vocabulary (enum) or structured reference  
**Value set:** `[Submission-time | Beat-N | Phase-N | When condition X | N/A]`  
**Visibility:** VS-01 (Public) — printed on card  
**Purpose:** For React-function cards (C12), Countermeasure cards, and any future interrupt-window cards: separates *when the card activates* from *what it does when it activates*. Currently the activation condition is embedded in the `Restriction` or `Effect` prose.  
**L108 rationale:** Trigger condition is a typed, queryable value. "When a named action resolution outcome" cannot be programmatically enforced as prose.  
**Design note:** This field is N/A for standard covert operations (which activate at their Beat by default). It becomes required for any card that fires outside its default Beat. The existing Beat field handles *default* timing; Trigger condition handles *conditional* timing.  
**Per-faction expansion:** No — flat field.  
**Reference:** Marvel Champions' Interrupt/Response/Forced Response taxonomy; Art 04b §3.5 React function definition.

### 7.3 Add: `Pool copies` (Recommended — Operational Gap)

**Field:** `Pool copies`  
**Type:** Integer or per-faction object  
**Visibility:** VS-01 (Public) — printed on card or tracking sheet  
**Purpose:** States how many copies of this card are in the faction's setup pool. Standard cards: 2 copies per faction. Faction-specific cards: typically 2 per owning faction. Emergency Response: 1 per faction (singleton). Currently this information is only in Art 04 §7 prose.  
**Practical use:** Governs print quantities for playtesting. Enables programmatic validation of setup pool composition.  
**Companion field (optional):** `Unique: boolean` — whether at most one copy may be in play simultaneously (Emergency Response = true; standard cards = false). Could be a separate field or encoded as `Pool copies: 1 (Unique)`.  
**Per-faction expansion:** May need per-faction values if a card has different pool quantities across factions. At V1, likely flat.

### 7.4 Confirm and Cross-Reference: Intra-Beat Priority (Documentation Gap — Already Covered)

**Art 03 status (confirmed):** Art 03 §7 line 86 explicitly states: "Dispatch case submission order is the tiebreaker within resolution priority tiers." Political acts and all other initiative-ordered actions follow initiative order throughout Phase 6. This covers intra-Beat conflicts: when two factions submit same-Beat cards targeting the same district, submission order (dispatch case receipt time) governs resolution sequence within a Beat.

**No new field needed.** Art 03 provides the rule. The card schema does not need a `Resolution priority` field.

**Action required — documentation only:** The Beat field description in Art 04 §6 should add a cross-reference note: "Resolution order within a Beat: governed by dispatch case submission order per Art 03 §7 (and initiative order for political acts)." Without this note, the Beat field appears self-sufficient and does not direct the reader to the governing rule. The gap is in the cross-reference, not the field structure.

**Why no Libertalia-style priority number:** Libertalia encodes priority on the card because the priority is intrinsic to the character (a fixed rank 1–30). The Signal's priority is extrinsic — it derives from real-time player behavior (who submitted first). A static field cannot capture it. The Art 03 rule is the correct location for this mechanic.

### 7.5 Add: `Outcome type` (Recommended — L2+ Gap, Political Acts Only)

**Field:** `Outcome type` (Political Acts only — N/A for all other card types)  
**Type:** Controlled vocabulary enum  
**Value set:** `[Binary (For/Against) | Elect player | Elect district | Elect faction | Bilateral agreement | Unilateral | N/A]`  
**Visibility:** VS-01 (Public)  
**Purpose:** Structures what kind of outcome-collection the ARBITER conducts when a political act resolves. P04 Denounce = `Elect player` (which faction is targeted). P08 Propose Accord = `Bilateral agreement` (requires named target's consent). P07 Invoke the Table = `Unilateral` (no target selection). Currently all political act outcomes are free-form effect text; the ARBITER infers the outcome type from that text.  
**L2+ rationale:** The digital resolution engine needs to know what UI to present (target selector vs approval/rejection vs binary vote) before it can enforce the outcome. Outcome type is the key that unlocks the correct UI branch.  
**Per-faction expansion:** No — flat field on the card.

### 7.6 Apply: Per-Field Visibility Scope (VS-xx tagging) (Recommended — L108 and L2+ Gap)

**Action required:** For every field in the card schema, annotate which VS-xx scope applies. This does not add new fields — it adds visibility tags to existing fields.

**Proposed field-level assignments (draft — confirm with ARBITER design intent):**

| Field | Proposed VS-xx | Rationale |
|---|---|---|
| Card ID through Taxonomy | VS-01 (Public) | Printed on card face |
| Effect on crit success / success | VS-06 (Conditional) | Revealed at resolution; covert ops hidden until Beat 4 |
| Effect on failure / crit failure | VS-06 (Conditional) | Same — revealed only if the card fails |
| Portrait — [Faction] fields | VS-04 (ARBITER-Only) | ARBITER scores Portrait; players do not see the running tally |
| Portrait — [Faction] Condition | VS-01 (Public) if printed on card | The condition that triggers the Portrait change may be public even if the score isn't |
| Design note field | VS-04 (ARBITER-Only) | Internal design documentation; not surfaced to players |
| Narrative anchor | VS-01 (Public) | Printed on card |
| Faction perspectives | VS-01 (Public) | Printed on card face — all players read all faction perspectives. Schema says "one sentence per faction, optional for others." Not faction-gated. |

**L108 rationale:** 00b §5.9 states that VS-xx is the enforcement vocabulary for the information hierarchy. Per-field tagging on the card schema is what enables that hierarchy to be applied in L2+ API scoping. Currently VS-xx is defined but not applied at the card field level.

### 7.7 Flag: Compound Effect Text in Effect Fields (L108 Structural Gap — Deferred)

**The issue:** L108 Requirement 1 states: "no compound cells — no cell contains 'A / B' or mixed types." Several card effect fields carry multiple discrete effects in a single prose string. C01 `Effect on success` reads: "Place 1 structure block (faction color) in the target district. Generates +1 of the district's native resource during each Upkeep while standing." This is two effects — an immediate board placement and a persistent upkeep generator — encoded as a single freeform string. They cannot be individually queried, programmatically enforced, or sequenced by a game engine.

MTG/Scryfall addresses this by maintaining `keywords[]` (structured extract) alongside `oracle_text` (full prose). The structured extract enables combo identification and programmatic enforcement without replacing the human-readable text.

**The Signal's parallel gap:** The taxonomy triple (Category/Function/Target) is the structured extract — but it only captures the primary effect, and only at category level, not the specific effect values ("+1 resource," "1 presence token," "place 1 structure block"). For L2+ the engine needs to parse individual effect sub-components — target type, quantity, condition, duration — not just a prose description.

**Why this is deferred and not an immediate field addition:** Decomposing effect fields into structured sub-components (effect type, quantity, target, condition) would require redesigning every card's effect fields — a major structural change that should not happen until card content is locked. At V1 paper prototype, the prose fields are human-readable and ARBITER-resolved; L108 compound cell violation in effects is acceptable at this stage.

**Recommendation:** Flag as a known L108 violation in 00b §8 (Design Notes & Known Gaps). When card content is locked (post-D-04-01 decision on card set size), a structured effect decomposition pass should be performed before L2+ development begins. The taxonomy triple is already the model — extend it to carry effect quantity, target ID, and condition as typed sub-fields.

**Priority:** Deferred — do not add fields now. Document the gap in 00b.

---

### 7.8 Consider: `Submission phase` (Optional — Documentation Gap)

**Current state:** Card type implies submission phase (covert ops → Phase 3 dispatch case; political acts → Phase 2 declaration; Countermeasures → Phase 5). This is a type-inference rule, documented in Art 03.

**Recommendation:** At minimum, the Beat field description should cross-reference the Phase in which the card is submitted. At maximum, add a `Submission phase` field that states the Phase number explicitly, removing the inference dependency on card type.

**Priority:** Low at V1; becomes medium at L2+ when the engine must enforce submission rules.

---

---

## 8. What Was Researched But Is Not Recommended

The following were explicitly researched and found not to be gaps, for the stated reasons:

**Rarity / collector number / print variant fields:** Production/retail metadata (MTG border_color, frame, foil, booster, prices). Irrelevant for a paper prototype not entering retail production. The Signal's Card ID already serves the collector-number function.

**Duration / persistent effect field:** Art 04 Design Principle 11 explicitly constrains effects to immediate or permanent. A duration field would contradict established design. If the permanent/immediate distinction should be machine-readable, flag it as a sub-field of the existing effect fields, not a new top-level field.

**Keyword reminder text field:** The Signal does not use card-face keywords requiring reminder text. The taxonomy is metadata, not printed abbreviation. Not needed at V1.

**Hand limit / deck cycling mechanics (Dominion-style):** The Signal uses a fixed-selection model, not a mid-game acquisition deck. Shuffle timing and hand limits are properties of the acquisition/cycling model, which The Signal does not use.

**Slay the Spire keyword flags (Exhaust/Ethereal/Innate/Retain):** These are deck-cycling management keywords for a single-player roguelike. Inapplicable to The Signal's multiplayer hidden-action model.

**Aeon's End breach / nemesis tier mechanics:** Combat escalation structure for a cooperative boss-fight game. No equivalent in The Signal's architecture.

**Influence cost / deck inclusion penalty (Netrunner model):** The Signal's affinity bonus (positive discount for aligned factions) already addresses the cross-faction cost question from the opposite direction. No additional field needed.

**Legendary/unique constraint as top-level type:** The Signal does not have a "legendary rule" equivalent. Pool copies (§7.3) handles the singleton constraint adequately.

---

*Research complete. Six actionable recommendations (§7.1–7.3, §7.5–7.6, §7.8), one confirmed-covered requiring cross-reference only (§7.4), one structural gap deferred pending card content lock (§7.7). Each recommendation includes L108 rationale, visibility scope, and per-faction expansion status.*
