# Schema Cleanup Log

Running log of Art 04 §6.1–§6.3 (Card Data Schema — field groups, enum vocabularies, Modifier Subclass Field Constraints) issues, questions, and normalization candidates surfacing during the 09-16 design review pass.

**Working premise (Andy, S137):** §6.1–§6.3 reflect what was needed when drafted, not a locked ceiling. A card/schema mismatch is an open question in either direction — the card may need to change, or the schema section may be behind the pattern that real content now requires. Don't default to "the card is wrong."

**Working method (Andy, S137):** Don't go hunting for extra examples to force a decision early — let them surface organically while working through the full ModReactCard set (all rings + all factions). Wait until that full landscape has been reviewed before proposing any schema normalization — the language different cards use to express the same underlying need is visibly inconsistent even in the handful of examples pulled so far, and the shape of the real fix will be clearer once the whole set has been seen. Until then: keep logging and *categorizing* — what is each card's spec language actually trying to accomplish that the schema doesn't natively support — rather than solving as we go. No §6 edits until Andy calls it.

Each entry: the category of underlying need, which cards surfaced it, the inconsistent language each one reached for, and current status (open / evidence-gathering / ready-to-propose / resolved).

---

## Open Items

### 1. Portrait validity — ModReactCard should NOT be hardcoded to `None`

**Surfaced by:** STD.MOD.98 review (Ring 1 ModReactCard pattern-setter). Nearly proposed extending §6.2's Modifier Subclass Field Constraints table to mark `portrait: None` for ModReactCard the same way it already does for ModBattleCard (any-faction-committable, no doctrine to score).

**Resolution (Andy, S137):** Don't hardcode. ModReactCard is closer to an action card than ModBattleCard/ModActionCard — per §6.1's own framing, it's "the only subclass that routinely carries real Layer/Function/Subject (it's action-like)." Keep `portrait` genuinely open per §6.2 (live/per-card) and assess Portrait implications on a per-card basis during review, same as any Standard/faction card.

**Status:** Direction locked. Not a schema edit — the schema already permits per-card Portrait on ModReactCard (§6.2 lists it as "—", not None); the correction is to actually *do* the per-card assessment during review instead of defaulting every stub to `portrait=None` unexamined. Applies going forward to all 36 Ring ModReactCard cards and the faction ModReactCard sets.

---

### 2. Category: expressing "what ends a standing condition" — no consistent schema language for it

**Surfaced by:** Ring 1 ModReactCard batch (98–109) — `persistence`/`persistence_condition`/`persistence_effect` absent from all 12 specs, which raised the question of whether these fields should be schema-required explicit per-card, or implicit-default for the common case. Andy's response reframed the question one level deeper.

**The deeper issue (Andy, S137):** Some ModReactCards — especially in the faction sets — create a standing condition (`persistence = Seasonal` or `Permanent`) that itself clears via its own trigger, distinct from the trigger that fired the card in the first place. Concrete example pulled: **DIR.MOD.9 Fiscal Sanction** —
- Firing trigger: `standing_marker.decreased(faction=Any)` — fires the card, creates the sanction.
- Clearing "trigger": `persistence_condition = faction(trigger.faction).pays(2, resource.native, to=Reservoir)` — this is written into a field whose declared semantics (§6 Field Groups) are `BoolExpr | None`, continuously evaluated, "card discarded immediately when False." But what's actually being expressed is an *event* (the sanctioned faction pays the fine), not a continuously-true/false board state. The field is being used as a trigger wearing a BoolExpr's clothes.

**Open question:** Should the schema normalize two distinct trigger-type fields on persistent cards — (1) the play/fire trigger (already `trigger`), and (2) a clearing trigger for whatever standing condition the card leaves behind — rather than overloading `persistence_condition` to do double duty as both a state predicate and an event watcher? Related: does this mean `resolution_type`/explicit `persistence` lines are only meaningfully "required per card" for the Seasonal/Permanent minority, and Immediate/Transactional should be the implicit default for ModReactCard unless a card states otherwise (would eliminate the appearance of a 130-card compliance gap that's mostly just the common case going unstated)?

**Additional examples pulled (S137) — pattern confirmed, not a one-off:**

- **GUI.MOD.10 Contractor's Favor** (`persistence=Seasonal`): `persistence_condition=None`, `persistence_effect=None` — the actual clearing rule ("clears at Phase 21 End of Quarter regardless of outcome") exists only as a Python comment below the `success` line. Not encoded in any field at all.
- **SYN.MOD.6 Bounty Contract** (`persistence=Seasonal`): `persistence_condition`/`persistence_effect` omitted entirely. Clearing logic (Capital transfers when the target PA resolves, either direction) is buried inside the `success` field's prose string.
- **NET.PA.3 Live Coverage** (PublicAct, not ModReactCard, but same shape and useful cross-reference): `persistence_condition` is a prose string describing an *event* ("target complies for one Covert Dispatch → clears, or Quarter end"); `persistence_effect` is a separate prose string describing an ongoing per-Month procedural obligation. Same event-wearing-a-BoolExpr's-clothes issue as DIR.MOD.9, just in English instead of pseudo-code.

Four cards (DIR.MOD.9, GUI.MOD.10, SYN.MOD.6, NET.PA.3), four different improvised encodings of "what ends this standing condition," none actually using `persistence_condition` as §6 defines it (continuously-evaluated `BoolExpr`, discard on False). This is a real, repeated authoring gap — every card that needed this reached for something ad hoc instead of a clean schema mechanism, which is itself evidence no clean mechanism currently exists.

**A candidate idea surfaced while looking at these four** (not a proposal — just a shape worth watching against future examples): the "clearing" half of each of these reads as an *event* (a `TriggerExpr`, same vocabulary as the firing `trigger`), not a continuously-evaluated `BoolExpr` — none of the 4 examples actually needed a state predicate. Worth checking whether that holds or breaks as more Seasonal/Permanent cards turn up.

**Status:** Evidence-gathering, paused per Andy (S137) — do not force a decision on 4 examples. Resume once the full ModReactCard landscape (all rings + all faction sets) has been reviewed; more instances of this category will surface organically. No schema proposal drafted, no §6 edit made.

---

### 3. Category: TriggerExpr parameter gaps — `.removed()` forms used with `ring=` but only `district=` is confirmed

**Surfaced by:** STD.MOD.100 (`presence_chip.removed(faction=opponent, ring=1)`) and STD.MOD.106 (`presence_chip.removed(faction=holder, ring=1)`), Ring 1 ModReactCard batch.

**The gap:** §6.3's confirmed TriggerExpr vocabulary lists `presence_chip.placed(faction=X, district=Y, ring=Z)` — both `district` and `ring` available — but `presence_chip.removed(faction=X, district=Y)` — district only, no `ring` documented. Two Ring 1 cards use `ring=` on the `.removed()` form anyway. Plausible this is just an oversight in how §6.3 was written (symmetric `ring` support on `.removed()` is a reasonable, low-risk assumption), but it's not yet confirmed as written.

**Status:** Open, logged for the same organic-accumulation treatment as the other categories — watch for more `.removed()`/ring-parameter usage while reviewing the rest of the ModReactCard set (Ring 2/3, then faction decks) before deciding whether to just confirm the extension or handle it some other way.

---

### 4. Full-landscape synthesis (S137) — schema-as-a-whole recommendations

**Scope note:** this synthesis is grounded in the *taxonomy and schema-field usage* pass across all 36 Ring ModReactCards + all 5 factions' ModReactCard decks (~90 cards). It is NOT a full design review (Portrait/Card Story/22-row checklist) of the faction decks — only Layer/Function/Subject taxonomy was assigned there. Recommendations below are about schema structure and field-usage patterns, not per-card design quality.

**A. No confirmed MutationExpr vocabulary exists, unlike TriggerExpr.** Verified directly against canonical Art 04 §6 (Part1_Core.md), not just the Whiteboard reference: `MutationExpr` is a declared field type (§6 Field Groups, success/successcrit/fail/failcrit/persistence_effect) but there is no enumerated list of confirmed valid call forms the way §6.3 enumerates TriggerExpr forms (`presence_chip.placed(...)`, `structure_block.removed(...)`, etc.). Effect-side authors improvised freely: `arbiter.place`, `arbiter.remove`, `arbiter.deliver`, `arbiter.modify`, `arbiter.shift`, `arbiter.draw_modifier`, `arbiter.apply_modifier`, `arbiter.register_battlefield_modifier`, `arbiter.mark_acceptance`, `faction(X).resources.add`, `faction(X).standing.add/shift` — a wide, ungoverned set. This is one contributing factor (not the sole cause) behind: the Copy-vs-Add and Redirect-vs-Remove corrections made this session, and GUI.MOD.10's `register_battlefield_modifier` having no taxonomy home at all. Candidate direction: extend §6.3 with a confirmed MutationExpr vocabulary, mirroring the TriggerExpr treatment.

**B. Persistence/clearing-condition — see Item 2 above.** Now that the full landscape has been seen: this is real but low-frequency (4 examples total across ~90+ cards: DIR.MOD.9, GUI.MOD.10, SYN.MOD.6, NET.PA.3 — no new instances surfaced in the Guild/Network/Syndicate taxonomy pass, though that pass wasn't a full design review so more may exist unexamined). Every Seasonal/Permanent card that needed to express "what clears this" reached for something ad hoc — prose in `success`, a Python comment, an event dressed as `persistence_condition`'s `BoolExpr`. The candidate shape floated in Item 2 (a second `TriggerExpr`-typed clearing-trigger field, distinct from the firing `trigger`) still looks right against these 4, but is not a proposal — Andy's call once he's ready to look at it.

**C. Portrait-on-ModReactCard — direction already locked (Item 1), not re-opened here.** Note for accuracy: this session's faction taxonomy pass did not include Portrait assessment (out of scope, taxonomy-only), so Item 1's "assess per card" direction has only actually been executed on the Ring set so far, not the faction decks.

**D. Undeclared vs. explicit-None fields.** Several older cards (NET.MOD.1/2, GUI.MOD.1, the GHO.MOD.9/10/11 fossils) don't just leave `layer/function/subject = None` — they omit the fields from the `Card()` call entirely. A completeness checker can't distinguish "reviewed and correctly None" from "never touched" when the field isn't even declared. Candidate direction: require all schema fields explicitly declared (even as `None`) on every card as a baseline completeness gate.

**E. Nothing currently flags missing ModReactCard taxonomy as a distinct gap.** ~48 of ~54 faction ModReactCards had `layer=None` going into this session, undetected until a manual read-through. Candidate direction: extend whatever completeness/audit tooling exists (`v_card_mechanical_alignment` or similar) to flag `type=ModReactCard AND layer IS NULL` as its own check, so a future stub batch doesn't silently reintroduce the same gap.

**F. `PublicStanding` vs `StandingMarker` — already-documented rule, no enforcement.** `ref_taxonomy.md` already states not to use `PublicStanding` as a card subject (corrected S126); this session found and fixed 12+ cards still using it anyway (missed because nothing checks for it). Same shape as D/E: the rule exists, the enforcement doesn't. Not a new schema question — folds into whatever audit-tooling recommendation Andy wants to act on for D/E.

**Status:** Presented to Andy S137 as a prioritized menu, not decisions. None of A/B/D/E/F implemented — awaiting direction.

---

### 5. Category: TriggerExpr `faction=Any` — no confirmed semantics for self-inclusion

**Surfaced by:** DIR.MOD.1 Riot Squad (S138, Directorate ModReactCard review). Trigger is `presence_chip.placed(faction=Any)`. Sibling card DIR.MOD.7 (same author, same session) uses `faction=opponent` for a structurally identical shape. §6.3's confirmed TriggerExpr vocabulary documents `faction=X` parameterization but never states whether `Any` includes the reacting card's own owning faction or is implicitly "any other faction." No card-level fix applied — flagged as a vocabulary gap, not a DIR.MOD.1-specific bug, since the ambiguity could recur anywhere `faction=Any` is used on a self-triggering React.

**Status:** Open, evidence-gathering (1 example so far) — watch for more `faction=Any` usage during the remaining faction ModReactCard review passes before proposing whether §6.3 should define `Any` as inclusive or exclusive of the card's own faction by default.

---

### 6. Category: `arbiter.remove(presence_chip, ...)` doesn't distinguish protected vs. removable chips

**Surfaced by:** DIR.MOD.1 Riot Squad (S138). The MutationExpr call `arbiter.remove(presence_chip, district=X, faction=Y, count=1)` has no way to express "not a Deployment Marker's temporary chip" — GR 8.3a is hard: deployment markers are always moved, never removed. Any card using this same removal shape (DIR.MOD.1/2/3 all do) is silently ambiguous about whether it could target protected marker-linked chips. Same root cause as Item A (no confirmed MutationExpr vocabulary) — this is a concrete instance of that gap rather than a new category.

**Status:** Open, folds into Item A's "extend §6.3 with a confirmed MutationExpr vocabulary" candidate direction — a real vocabulary fix here would need `arbiter.remove(presence_chip, ...)` to either exclude marker-linked chips by definition or require an explicit flag. Not proposed yet; logging as supporting evidence for Item A.

---

### 7. Category: Portrait `flat` entry on a non-submitting (target) faction — schema-permitted, doctrinally unexamined

**Surfaced by:** DIR.MOD.2 Capital Suppression (S138). `portrait = {Directorate: submitter=+1, Syndicate: flat=-1}` — the `Syndicate: flat=-1` entry moves a faction's Portrait as a direct consequence of a rival's card resolving against them, not as a result of Syndicate's own choice or action. Schema-valid per L131 (`flat` documented as "fires on resolution regardless of submitter — faction-specific cards only"), so this isn't a vocabulary gap the way Items 5/6 are. The open question is doctrinal: Portrait Principle 11 ties movement to an action that strongly expresses *that faction's own* doctrine — does having something done to you count, or should target-faction portrait entries require the target's own agency? If the answer is "no, targets shouldn't get portrait entries for being acted upon," this could affect any existing card using the same pattern (not audited yet — this is the first instance flagged, not a confirmed one-off).

**Status:** Open, evidence-gathering (1 example). Needs Andy's read on the underlying principle before deciding whether to sweep for other target-faction `flat` entries across the card set.

---

### 8. Category: `portrait = {}` vs. `portrait = None` for "no portrait effect" — inconsistent across sets, not within Directorate

**Surfaced by:** Directorate ModReactCard review (S138). §6.1's class definition types `portrait` as a plain `dict[Faction, PortraitEntry]` — not `Optional`/`| None`. DIR.MOD.1–9 consistently use `{}` for "no entries" (DIR.MOD.5/6/7/8) vs. a populated dict otherwise — internally consistent within the Directorate set. But the Ring ModReactCard template (STD.MOD.98, reviewed S135) uses `portrait = None` for the same "no effect" case, which is arguably not type-correct against §6.1's declared field type. Two different authoring sessions independently picked different representations for the same empty case; neither is wrong per card, but the set as a whole isn't normalized.

**Status:** Open, low-priority — cosmetic/type-consistency question, not a design decision. Candidate direction: pick one canonical empty-value form (`{}`, matching the declared type) and sweep both Ring and faction ModReactCard sets to match, whenever a low-risk sweep session is scheduled (same category as 04-n30/31/32's prior field-sweep precedent).

---

### 9. Category: `where(...)` as a trigger parameter — not in confirmed TriggerExpr vocabulary

**Surfaced by:** DIR.MOD.8 Asset Seizure (S138). Trigger is `public_act.placed_on_frg(target_district=where(faction(Directorate).influence >= Established))`. §6.3's confirmed vocabulary shows `public_act.placed_on_frg(faction=X, ...)` with flat key=value parameters (faction, ring, district) — nothing showing a conditional/filtered parameter built from a `where(BoolExpr)` wrapper. This is a different shape from anything in the confirmed list: instead of matching a specific value, it's filtering by a live board-state condition evaluated at fire time. Possibly fine (the underlying event and condition are both well-defined elsewhere in the schema), but the parameterization pattern itself isn't confirmed vocabulary.

**Status:** Open, now 5 confirmed examples (GHO.MOD.2/3/4, DIR.MOD.8, GUI.MOD.5 — all S138) — same organic-accumulation treatment as Items 5/6/3. The recurrence across 3 factions makes this a strong candidate for formal §6.3 confirmation once the remaining faction sets (Network, Syndicate) are reviewed.

---

### 10. Category: Intel Token as `cost` — is a discrete, individually-tracked object a valid "fungible resource"?

**Surfaced by:** DIR.MOD.9 Fiscal Sanction (S138). `cost = intel_token(faction=trigger.faction, age__in=[Fresh, Stale]) * 1`. §6 Field Groups defines `cost: CostExpr` as "fungible resources only; PS and presence tiers are not valid cost values." Intel Tokens are individually tracked objects with per-token age/privacy state (Fresh/Stale/Expired, holder-keyed) — not a fungible pool the way native resources are. This may be an established, accepted pattern already (Intel Tokens function as a spendable resource type elsewhere — e.g., SCIF/Deep Cover economies), but it hasn't been checked against the literal "fungible resources only" constraint before. Not fixed — genuinely unclear whether this is a schema violation or whether Intel Tokens should simply be recognized as a second valid cost category alongside native resources.

**Status:** Open, single example flagged this session. Needs either a definitional clarification (does "fungible resources" include Intel Tokens?) or a sweep to check whether other cards already spend Intel Tokens as cost without the same scrutiny.

---

### 11. Category: `trigger.faction` self-reference on broad (`faction=Any`) React triggers — same root issue as Item 5, sharper consequence

**Surfaced by:** DIR.MOD.9 Fiscal Sanction (S138). `trigger = standing_marker.decreased(faction=Any)`, then `persistence_effect = PublicAct(submitter=trigger.faction).blocked_at(phase_b)`. If Directorate's own Public Standing drops and Directorate holds a matching Intel token on itself, this card would fire against Directorate itself — sanctioning its own faction, blocking its own PA submission, in exchange for +1 PS to itself. Same category of self-fire ambiguity as Item 5 (DIR.MOD.1), but here the consequence is actively self-harmful rather than merely a no-op, and the card's own design_note narrative ("holding tokens on rivals") implies the intended scope was always `faction=opponent`.

**Status:** Open. Recommend resolving Items 5 and 11 together once enough `faction=Any` self-fire examples have accumulated — same organic-accumulation approach as the other categories in this log.

---

### 12. Category: Invalid `resolution`/`resolution_type` enum values on a legacy (S110) card

**Surfaced by:** GHO.MOD.1 Sleeper Analyst (S138, Ghost ModReactCard review — format-migration case, `structure_pass=0`). Card uses `resolution = Prediction` and `resolution_type = "Conditional"`. Neither is a valid value: confirmed `Resolution` enum (Art 04 §6.3, verified directly against `Part1_Core.md`) is `d100 | Automatic` only; confirmed `resolution_type` vocabulary is `"Probabilistic"` (d100) or `"Transactional"` (Automatic) only. This card predates both confirmed vocabularies (S110, well before the S127+ enum lock-downs) and was never swept to match. The underlying mechanic (Ghost declares a faction name, ARBITER checks it against private Intel Token data, no dice) reads as a deterministic check — likely `resolution=Automatic` once corrected, but that's a content call, not made here.

**Status:** Open, flagged not fixed. First confirmed instance of a pre-S127 card using since-invalidated enum values — worth checking whether other S110-vintage-or-earlier cards have the same drift once the remaining faction ModReactCard sets are reviewed.

---

### 13. Category: Legacy TriggerExpr syntax (`faction(X).places(...)`) predates confirmed §6.3 vocabulary

**Surfaced by:** GHO.MOD.1 Sleeper Analyst (S138). `trigger = faction(opponent).places(PA, with=IntelToken(any), at=Art 03 §9.2.0)` — this construction style (method-call-on-faction-object, embedding an Art-section citation as a parameter) doesn't match any confirmed §6.3 form (which uses `event_noun.verb(param=value, ...)`, e.g. `public_act.placed_on_frg(faction=X, ...)`). Same root cause as Item 12 — a pre-S127 card that was never swept to current vocabulary. The closest modern equivalent is likely `public_act.placed_on_frg(faction=opponent, uses_intel_token=True)` or similar, but the exact reconciliation is a content decision, not made here.

**Status:** Open, flagged not fixed. Same "check for more pre-S127 drift" note as Item 12 — likely the same root cause, probably worth resolving together.

---

### 14. Category: `public_standing.shifted(direction=...)` — retired trigger term, missed instance

**Surfaced by:** GHO.MOD.5 False Flag (S138). Trigger is `public_standing.shifted(faction=Any, direction=Positive)`. PM05 04-n144 (closed S130) already normalized this exact term to `standing_marker.increased/decreased(faction=X)` — but that sweep's known instances were SYN.MOD.4/5 only. GHO.MOD.5 uses the identical retired form and was missed by the original sweep (it wasn't in the S128 stub batch that 04-n144 was scoped against, or was simply overlooked). Not fixed here — flagged as a gap in an already-closed item's sweep completeness.

**Status:** Confirmed single instance — grepped all 8 Art 04 Part files (S138); GHO.MOD.5 is the only remaining occurrence of `public_standing.shifted` in the entire card system. Flagged, not fixed (content decision — swap to `standing_marker.increased(faction=trigger.faction)` — belongs to whoever does GHO.MOD.5's own content pass, not a blanket sweep).

---

### 15. Category: `PA_success.where(...)` legacy trigger syntax + `acting` keyword (NET.MOD.1, S106-vintage)

**Surfaced by:** NET.MOD.1 Pirate Transmitter (S138, Network ModReactCard review — format-migration case, `structure_pass=0`). Trigger is `PA_success.where(effect.causes_board_state_change(district))` — same category as items 12/13 (GHO.MOD.1's legacy syntax), a pre-S127 construction that never got swept to confirmed §6.3 vocabulary. Also uses a bare `acting` keyword in `cost`/`successcrit`/`failcrit` (e.g. `resource.faction(acting).exposure`) to mean "the faction playing this card" — a third acting-faction reference form alongside `holder` (Ring cards) and `trigger.faction` (most faction cards), none formally reconciled against each other.

**Status:** Open, flagged not fixed. Same disposition as items 12/13 — likely worth a combined sweep of all pre-S127 legacy-syntax cards once the full ModReactCard landscape is reviewed.

---

### 16. Category: `status_marker.contested.placed()` — legacy trigger syntax, confirmed vocabulary is `tension_marker.placed`

**Surfaced by:** NET.MOD.9 Bandwidth Override (S138). Trigger is `status_marker.contested.placed()` — §6.3's confirmed vocabulary for this exact board event is `tension_marker.placed` (already used correctly by GUI.MOD.10 and others). This is a different, unreconciled term for the same underlying event, not a new mechanic.

**Status:** Open, flagged not fixed. Content decision to normalize to `tension_marker.placed` belongs to a future NET.MOD.9 content pass.

---

### 17. Category: Statement syntax (`-=`) used as a field value, not an expression

**Surfaced by:** NET.MOD.2 Troll Farm (S138). `success = faction(trigger.faction).standing -= 1,` — `-=` is a Python augmented-assignment *statement*, not a value expression; it cannot legally appear as the right-hand side of a `success=` keyword argument the way every other card's `success` field does (a callable mutation like `arbiter.shift(...)` or `faction(X).resources.add(...)`). This is a different, more severe category than the "string literal instead of Expr" fossil gap (04-n174) — it's not even valid pseudo-code, whereas the fossil cards' string literals at least parse as strings. Likely should read `arbiter.shift(standing_marker, faction=trigger.faction, amount=-1)` or `faction(trigger.faction).standing.remove(1)` (matching GHO.MOD.5/STD.MOD.10x precedent), but that's a content decision, not made here.

**Status:** Open, now 2 confirmed instances (SYN.MOD.9 Goodwill also uses `faction(Syndicate).standing += N`, S138) — same invalid statement-as-value problem. Worth checking whether other cards outside this session's review scope use the same pattern.

---

### 18. Category: `modifier_card.placed(faction=X)` — unconfirmed trigger term, plus a possible self-triggering loop

**Surfaced by:** NET.MOD.8 Frequency Splitter (S138). `trigger = modifier_card.placed(faction=Network)` isn't in the confirmed §6.3 TriggerExpr list. More significant: the design_note calls this a "chain enabler" that "replaces itself," but the trigger fires on *any* Network modifier card being placed — including, potentially, this card's own resolution. If so, this could be a self-sustaining recursive loop (fire → draw another modifier → possibly re-trigger → fire again) rather than a bounded chain. Not confirmed as a bug — may have an implicit once-per-Month limiter not written into the spec — but the mechanic as specced doesn't rule out the loop reading.

**Status:** Open, flagged not fixed. Needs a content decision on both the trigger term and whether self-inclusion is intentional (and if so, what bounds the chain).

---

### 19. Category: A ModReactCard that never discards has no fitting Persistence value

**Surfaced by:** SYN.MOD.9 Goodwill (S138). Design_note explicitly states "Card does not discard — remains active for further triggers." None of the 4 documented Persistence values fit this: `Immediate` is fire-and-consume; `Transient`/`Seasonal` clear at Month/Quarter end; `Permanent` requires an explicit `persistence_condition` that, when False, discards the card — but this card is meant to remain active indefinitely, forever, with no clearing condition at all (it's a standing reusable ability, not a standing condition awaiting removal). This is a different shape than the persistence/clearing-condition gap already logged (item 2/B, "what ends a standing condition") — item 2/B is about cards that DO eventually clear but whose clearing logic is expressed inconsistently; this card is about a card that structurally never clears, which the 4-value enum doesn't model at all.

**Status:** Open, single example. Worth watching for more "always-active, never-discards" ModReactCards while reviewing any remaining card sets, and considering whether this is a 5th Persistence value or a different mechanism entirely (e.g., a `permanent_card` flag distinct from the card-as-condition pattern).

---

### 20. Full ModReactCard corpus review synthesis (S138) — cross-cutting patterns

**Scope:** All 45 reviewable ModReactCards across Ring + 5 factions (09-16 step 2, this session). 8 cards skipped as pre-schema fossils (GHO.MOD.9/10/11, GUI.MOD.1, NET.MOD.11/12, SYN.MOD.1) — those need full re-authoring, not analysis. This entry looks across the ~45 reviewed cards for patterns invisible at the single-card level.

**A. Schema drift correlates with authoring vintage, not faction.** Every legacy-syntax/invalid-enum finding this session (items 12, 13, 15, 16, 17) came from S106–S110-vintage cards (GHO.MOD.1, NET.MOD.1/2, GUI.MOD.1) — the same generation that also used the abbreviated 8–14-row checklist and prose Status instead of the current 4-block format. The corpus has at least 3 distinct authoring eras (pre-S127 vocabulary, S128 stub-batch, S130+ mature), and the earliest era was never swept forward when the confirmed vocabulary locked in. Recommend a dedicated normalization pass over pre-S127 cards specifically, rather than catching them one at a time as review happens to reach them.

**B. `faction=Any` self-fire ambiguity is the single most repeated finding this session — ~9 cards, 3 factions** (DIR.MOD.1/3/9, GHO.MOD.2/6/7/8, NET.MOD.6/10). Telling detail: NET.MOD.2 already writes `except=Network` explicitly on its own `faction=Any` trigger — proof at least one author recognized the problem and hand-patched it locally, but the pattern was never generalized into confirmed vocabulary. Candidate direction: define `Any`'s default semantics in §6.3 (does it include the reacting card's own faction or not?), rather than requiring every card author to remember to exclude self manually.

**C. Cross-resource cost-holding is the second most repeated finding — ~10 cards, 4 factions** (GHO.MOD.5/6/7/8, GUI.MOD.6, NET.MOD.2/9/13, SYN.MOD.5/8/11). Many of these require a faction to spend a resource type it doesn't natively generate (Ghost spending Capital/Capacity, Network spending Mandate/Findings, Syndicate spending Exposure, etc.). This is a design-economy question, not a schema bug: is there a robust enough trade/conversion system that these costs are realistically payable, or are a meaningful fraction of ModReactCards effectively dead cards in practice because the faction never stockpiles the required resource? Worth a dedicated balance pass once counted precisely.

**D. String-literal `success` fields cluster on one specific unsupported effect shape, not on author carelessness.** DIR.MOD.6, NET.MOD.13, SYN.MOD.6, SYN.MOD.8 — 4 cards, 3 factions, all independently reached for prose instead of a real MutationExpr. All 4 share the same underlying shape: an effect whose actual resolution is contingent on a *separate, later* event (a standing condition that resolves when some other action concludes). This is strong evidence for item A's diagnosis (no confirmed MutationExpr vocabulary) rather than 4 unrelated authoring lapses — nothing in the current schema cleanly expresses "do X now, but the real effect depends on how Y resolves later," so every author who needed that shape independently fell back to prose.

**E. Firing-window overlaps are common and completely ungoverned.** Confirmed real overlaps this session: DIR.MOD.1/2/3 (enforcement family, same trigger event), GUI.MOD.6/7/8 (three-way overlap on Guild's own structure removal), NET.MOD.4/5 (broadcast family). No Art 03 procedure anywhere addresses what happens when a faction holds 2+ ModReactCards with overlapping or identical triggers and the triggering event fires once — sequential in submission order? Simultaneous? Player's choice? This is a missing procedural rule, not a per-card issue, and it recurred on every multi-card family reviewed.

**F. Stack behavior (2+ copies of the same ModReactCard) was flagged ⚠ on essentially every one of the ~45 cards reviewed.** This isn't 45 separate gaps — it's one gap, restated 45 times: there is no governing rule anywhere for whether holding multiple copies of a ModReactCard multiplies its effect when the shared trigger fires. Recommend resolving this once, as a single Art 03/§6 rule, rather than continuing to log it card-by-card.

**G. Positive finding — the S137 taxonomy sweep holds up completely.** Across all ~45 cards re-verified this session, zero Layer/Function/Subject mis-assignments were found; every "Taxonomy fit" row confirmed rather than corrected the prior sweep. Same for the core confirmed TriggerExpr vocabulary (`presence_chip.*`, `structure_block.*`, `standing_marker.*`, `accord.*`, `broadcast_card.placed`, `public_act.placed_on_frg`) — used correctly on the large majority of modern-era cards. The schema itself isn't broken; the gaps cluster in specific, identifiable pockets (B–F above) rather than being spread evenly across the corpus.

**Status:** Presented as a cross-cutting menu, same treatment as item 4's S137 synthesis — none of A–F implemented, awaiting Andy's read on which (if any) warrant a dedicated session before the remaining 09-16 steps (faction-level set analysis, cross-faction synthesis).

---

### 21. Category: `ps_shift(faction="target", ...)` ModActionCard has no restriction enforcing the host actually has a target — CLOSED, not a gap

**Surfaced by:** STD.MOD.34 Word to the Wise (S139, Ring 1 Portable ModActionCard review — first target-hinder `ps_shift` card reached). Originally logged as: `ps_shift(faction="target", delta=-1)` resolves against whichever faction the host CA/PA declares as `target_faction` (§6.1), and nothing enforces that the host has one — as specced, a faction could attach this card to a targetless host at Dispatch, leaving ARBITER nothing to shift against.

**Closed (Andy, S139):** Not a gap. A ModActionCard does not declare its own target — its target IS the host action card it's submitted with (Art 03 §9.1.1/§9.4.0.1 packet-pairing at Dispatch). It enhances the effect of the card it attaches to; `faction="target"` is definitionally the host's target, not a separately-validated field ModActionCard needs a `restriction` clause to police. A player simply wouldn't pair a target-hinder `ps_shift` card with a targetless host — same non-issue as pairing `cost_reduction` (PA-only) with a CA host. No schema fix needed; no restriction field, no Art 03 rule.

**Retroactive note (corrected):** DIR.MOD.20 Public Reprimand's `arbiter_note` (S135 stub-pass content) describes `faction="target"` resolving to whichever faction the host names — that description is correct as far as it goes; it does not describe an actual gap, and the S139 review's reading of it as evidence of an "unformalized" constraint was the error, not the note itself.

**Status:** Closed S139, not a gap. Affected 22 cards had an incorrect ⚠ flag added and removed in the same pass (STD.MOD.34/35/46/47/58/59/70/71/82/83/94/95, DIR.MOD.20/24, GHO.MOD.24/25, GUI.MOD.23/24, NET.MOD.27/28, SYN.MOD.24/25) — see PM02 entry revising L267. PM05 **04-n179** closed accordingly. GUI.MOD.23/24 retain a separate, still-valid note (Guild's own CA/PA mix skews self/territory-directed, so these two cards see fewer eligible hosts than Directorate/Syndicate's equivalents — confirmed by Andy as a distinct, surviving observation, not dissolved by this correction).
