# Schema Cleanup Log

Running log of Art 04 §6.1–§6.3 (Card Data Schema — field groups, enum vocabularies, Modifier Subclass Field Constraints) issues, questions, and normalization candidates surfacing during the 09-16 design review pass. Scope extended S141 from ModReactCard-only to the CA/PA review phase — same log, same format.

**Working premise (Andy, S141):** The CA/PA review pass (and design review passes generally, per [[feedback-review-pass-scope]]) is scaffold + flag, not fix. Findings logged here are flagged for a later normalization/fix pass, not resolved in place during the review itself.

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

**Status:** Open, now **5 confirmed instances** — SYN.CA.7, SYN.CA.10, SYN.CA.11, SYN.CA.12 (S141), and **SYN.PA.3 Data Acquisition** (S142, Syndicate PA review — `portrait = {Syndicate: flat=+1, Network: flat=-1, Directorate: flat=-1}`, all three `flat`). SYN.PA.3 is a genuinely new angle: its acting faction (Syndicate) is fully public, not covert — the card is a loud, public table demand — so it doesn't fit hypothesis C's "public-effect/covert-actor" framing at all, yet still uses `flat=` for the submitter's own entry (SYN.CA.7/10/11/12's pattern) *and* for Network/Directorate, who only react narratively and never act. This is a broader pattern than the original DIR.MOD.2 finding: it's not just "should a target get a portrait entry for being acted upon" — SYN.CA.7/10/11/12/PA.3 all use `flat=` for the *submitter's own* portrait entry, where `submitter=` (the semantically-matching field, "fires only for the submitting faction") would seem to be the correct choice. All five instances are in the same faction (Syndicate CA and PA both), suggesting a deliberate authorial convention specific to this faction's cards rather than scattered drift — but SYN.CA.7's own Outstanding Issues already flags uncertainty about whether `flat` is even the right field here, so it wasn't asserted with confidence at authoring time either. Needs Andy's read on the underlying principle (both the target-faction question from the original finding, and the submitter-should-use-`submitter`-not-`flat` question this batch raises) before deciding whether to sweep.

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

**Status:** Open, now **14 confirmed instances** (by card, not by term) across 7 card sets — **NET.PA.1 Public Disclosure** (S142, Network PA review) adds a 7th distinct notation (`intel_token(target=faction(target)).all_held`, spending every held token naming the target rather than a fixed count) — DIR.MOD.9 (ModReactCard, S138), STD.CA.12 (S141), DIR.CA.5 (S141), GHO.CA.2/6/9/10/11 (S141, 5 instances in one faction's CA set), SYN.CA.7 (S141 — `cost = IntelToken(any) * 1`, pure, no fungible resource paired), STD.PA.5 (S142 — `intel_token(target=faction(target))`), DIR.PA.8 (S142 — `intel_token(faction=target_faction)`), and **GHO.PA.1 (S142, 2 instances — one per target faction, `intel_token(target=faction(target1/2))`, same notation as STD.PA.5) + GHO.PA.3 (S142 — `boost = intel_token(holder=Ghost, status=Expired)`, a 6th distinct notation using `holder=`/`status=` keys)**. Six distinct cost-notation variants now confirmed for the same underlying concept, no two cards spelling it identically. Intel-Token-as-cost confirmed in both CA and PA phases, across Standard, Ghost, Directorate, and Syndicate — Ghost alone now accounts for 8 of the 14 instances. This volume of evidence argues fairly strongly for formalizing Intel Token as a second valid `cost` category (alongside native/Capital/Mandate/etc.) rather than treating every instance as an individual violation — but that's a normalization proposal, not made here. Andy's call once ready to look at it.

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

---

### 22. Category: `cost` expression term missing resource-type attribute — confirmed corpus pattern in Standard CA

**Surfaced by:** STD.CA.1 Build Structure (S141, first card of the CA/PA review phase — oldest CA in the system, signed off S63). `cost = resource.faction(acting) * 1 + resource.district(native) * 1` — the first term (`resource.faction(acting)`) has no resource-type attribute, unlike most cost expressions in the corpus, which specify one (e.g. STD.CA.13: `resource.faction(acting).native * 2`). Design Rationale states the intent plainly ("dual cost: 1 faction native + 1 district native"), so the likely correction is `resource.faction(acting).native * 1` — but per [[feedback-review-pass-scope]] this is flagged, not fixed, during the review pass.

**Confirmed corpus-wide (S141, full Standard CA set now reviewed):** same missing-attribute shape on **STD.CA.2, STD.CA.3, STD.CA.4** (all `resource.faction(acting) * 1 + resource.district(native) * 1`) and **STD.CA.5** (`resource.faction(acting) * 1`, mono-resource). 5 of 16 Standard CA cards affected — all clustered at the low card-ID end (CA.1–5), while CA.6 onward (Exposure, Capital, Mandate, IntelToken-typed costs) are all correctly typed with an explicit attribute (`.exposure`, `.capital`, `.mandate`, `.native`). Suggests an early-authoring-era gap (same "vintage correlates with drift" pattern seen in the ModReactCard corpus, schema_cleanup_log item #20A) rather than a random scatter.

**Deeper gap, same shape as item A (no confirmed MutationExpr vocabulary):** there is no confirmed `CostExpr` vocabulary in Art 04 §6.3 either — grepped directly, no enumerated list of valid `resource.*` call forms exists the way §6.3 enumerates TriggerExpr forms. So there's no canonical text to check `resource.faction(acting)` (bare) against; it may be that bare = native-by-default was an intentional early shorthand, later abandoned in favor of always-explicit typing once non-native cost resources (Capital, Exposure, Mandate) entered the set. Not resolved — this session's job was to flag, not decide.

**Contrast confirmed (S142, Directorate PA review):** all 11 Directorate PA cards are correctly typed — every `cost` expression carries an explicit resource attribute (`.mandate`, `.capacity`, `.capital`, `.findings`), including the two most complex costs seen in the corpus so far (DIR.PA.6's triple cross-resource Mandate+Capital+Findings, DIR.PA.5's Mandate+district-native+Capital). This confirms the untyped-cost bug is not universal — it's specific to the Standard set (both CA and PA) plus one isolated Directorate CA instance, not a general corpus habit.

**Status:** Open, previously 6 confirmed instances (STD.CA.1–5, DIR.CA.5). **Massively extended S142 (Standard PA review): all 8 Standard PA cards show the identical untyped shape** — STD.PA.1/2/4/6/7/8 (`resource.faction(acting) * n`, mono-resource) and STD.PA.3/5 (`resource.faction(acting) * 1 + ...`, dual/cross-resource). This breaks the earlier "clusters at the low card-ID end, CA.1–5 only" read (§ above, also synthesis item #34-A's claim that Standard's only bug was "confined to CA.1–5") — the untyped form isn't a legacy-vintage artifact scoped to five early CA cards, it's the default convention across the *entire* Standard PA set regardless of card ID, alongside its partial presence in Standard CA. 14 confirmed instances total now, across Standard CA (6/16) and Standard PA (8/8) plus Directorate (1). Standard PA's 8/8 rate is notably higher than Standard CA's 6/16 — worth checking whether PA cards as a category default to this shorthand more than CA cards do, once Directorate/Ghost/Guild/Network/Syndicate PA sets are reviewed. Candidate direction, not proposed: either normalize to explicit `.native` typing (matching the majority of the corpus), or confirm bare `resource.faction(acting)` as valid native-shorthand syntax and leave as-is — Andy's call, once a normalization/fix pass is scheduled.

**Related, broader gap confirmed (S141, Syndicate CA review):** beyond the missing-`.native`-attribute bug, the Syndicate Accord-manipulation cluster (SYN.CA.10/11/12, all S111–S130 vintage) uses a **third distinct cost-notation style** entirely: bare resource-type-as-callable (`Capital(3)`, `Capital(2)`, `Capital(1) + Mandate(1)`) with no `resource.faction()` wrapper at all — no explicit faction binding, unlike every other notation style in the corpus. **4th confirmed instance (S142, Syndicate PA review): SYN.PA.3's `cost = Capital(1)`** — same bare-callable style, same faction, now confirmed in both CA and PA phases for Syndicate specifically. Combined with the already-noted absence of a confirmed `CostExpr` vocabulary in Art 04 §6.3 (no enumerated valid forms the way TriggerExpr has one), the corpus now has at least three different cost-expression conventions coexisting: (1) `resource.faction(X).type * n` (majority), (2) bare `IntelToken(...) * 1` (item #10), (3) bare `Type(n)` (this note, now 4 instances, all Syndicate). Candidate direction, not proposed: confirm one canonical form in §6.3 and sweep the others — Andy's call.

---

### 25. Category: `function = Move` used as a Function value — not in the confirmed Function Vocabulary

**Surfaced by:** DIR.CA.2 Detain and DIR.CA.4 Tactical Redirection (S141, Directorate CA re-derivation). Both declare `function = Move`. Checked directly against `ref_taxonomy.md`'s Function Vocabulary table (§5.1): confirmed Function values are Add / Remove / Redirect / Modify / Protect / Block / Copy / Reveal / Shift / Corrupt — **Move is not among them.** "Move" is one of the 7 Physical Verb Primitives (Art 02 §13.1) — the underlying mechanical action, not a Function. Two Functions map to Move as their primitive: **Redirect** ("changes ownership, destination, or allegiance") and **Shift** (track values only, doesn't apply to physical tokens). Redirect looks like the correct Function for both cards' actual behavior (both relocate a component to a new owner/destination).

**Not a fresh authoring slip:** DIR.CA.2's own checklist states this was a deliberate correction — "function corrected S107 L226 (Remove → Move; success block uses game.move(), not game.remove())." Someone actively changed a valid Function (Remove) to an invalid one (Move) at S107, apparently reasoning from the physical-verb layer rather than the Function-vocabulary layer. `v_card_mechanical_alignment` (DB) shows both cards as `Abstract Function (No Mechanical Verb)` — consistent with Move having no `function_verb` entry, but this reads differently from the documented-safe "Abstract Function" pattern (Modify/Block/Protect meta-constraints with no primitive by design) — Move has a clear, defined primitive, it's just not a valid Function-layer term.

**Third instance confirmed directly (S141, Network CA review):** `04___Card_System___Part4d_Network.md:593` is **NET.CA.8 Fake News** — same `function = Move` on `subject = DeploymentMarker`, same `Abstract Function` DB flag. This was anticipated from the earlier Directorate-pass grep and is now confirmed by direct card review rather than just a corpus grep hit.

**Status:** Open, 3 confirmed instances (DIR.CA.2, DIR.CA.4, one Network card). Candidate direction, not proposed: normalize `function = Move` → `function = Redirect` on all three, matching the documented vocabulary — Andy's call, content/taxonomy decision not made here.

**Related, not identical (S141, Guild CA review):** GUI.CA.4 Construction Crew uses `function = RemoveRestriction` — also not in the Function Vocabulary, also DB-flagged Abstract Function. Different invalid value than `Move`, same underlying category (a card author reaching for a descriptive verb outside the confirmed 10-value vocabulary). `Modify` ("alters cost, value, or attribute without changing fundamental state") looks like the closer documented fit for "removing a restriction," but not changed here. Total: 4 confirmed invalid-Function instances across 2 different invented values (Move ×3, RemoveRestriction ×1).

---

### 26. Category: `game.active_permanents(faction=, ring=)` — new ARBITER-facing behavior not established as a general procedure

**Surfaced by:** DIR.CA.6 Institutional Audit and DIR.CA.7 Institutional Brief (S141, Directorate CA re-derivation). Both cards' yield scales with "count of active Directorate Permanent cards in the same ring as the target district" — both checklists claim `Supported by game procedure ✓ ... existing permanent card procedure`. Grepped all 8 Art 04 Part files and the Whiteboard reference set for `active_permanents` / any "count Permanents by ring" language: **it appears nowhere outside these two cards.** No Art 03/07 procedure defines this counting mechanism generally.

**Why this matters:** Governing Rule 6.1 ("ARBITER executes general procedures, not card-specific instructions... New ARBITER behavior must be defined as a generalizable procedure in Art 03 or Art 07 before the card is finalized") and Design Pillar 4.7b (ARBITER Cognitive Efficiency) both bear directly on this. The cards' own "existing procedure" claim doesn't hold up against a direct check — it's new, card-specific ARBITER-facing logic that hasn't been formalized as a general procedure elsewhere.

**Status:** Open, now **3 confirmed instances**. **DIR.PA.9 Charter Grant** (S142, Directorate PA review) reuses the identical `game.active_permanents(faction=, ring=)` call, and its design_note explicitly claims this is "the same counting mechanism as CA.6 Institutional Audit / CA.7 Institutional Brief" — checked directly and confirmed true (unlike DIR.PA.10's looser, imprecise version of the same kind of claim, logged separately). Not a card design flaw necessarily (the mechanism itself is simple enough it may not need heavy procedure), but the checklist's "existing procedure" claim is currently unsupported, now on a third card. Andy's call whether this needs a formal Art 03/07 procedure entry or is fine as-is given its simplicity.

---

### 27. Category: DIR.CA.8's subject `Difficulty` is an unregistered, non-component Subject term

**Surfaced by:** DIR.CA.8 Enhanced Scrutiny (S141, Directorate CA re-derivation). Taxonomy is `Resolution / Modify / Difficulty`. `v_card_mechanical_alignment` (DB) flags this card as `Non-component Subject` — distinct from the `Abstract Function` flag its sibling Modify/Block/Protect cards in this set correctly carry (which `ref_taxonomy.md`'s own gap-pattern table documents as an expected non-issue). "Difficulty" doesn't appear in `ref_taxonomy.md`'s Subject Vocabulary table at all, and per that same table's gap-pattern guidance, a `Non-component Subject` result means the string is missing from `card_subject_map` — a registration gap, not a known/expected pattern like the Abstract Function cases.

**Status:** Open, now **3 confirmed instances** — DIR.CA.8 (S141), **GHO.CA.15 Routing Override** (`subject = TargetProfile`, S141), and **GUI.CA.9 Works Guarantee** (`subject = Difficulty`, S141, Guild CA review — second card using this exact subject string, both DB-flagged `Non-component Subject`). Unlike "Difficulty," `TargetProfile` is a well-established, heavily-used component elsewhere in the game (Art 03 procedures reference it constantly, DB:48) — its absence from `card_subject_map` specifically for taxonomy purposes looks like a pure registration gap, not a conceptual question. "Difficulty" recurring on a second card (DIR.CA.8 and GUI.CA.9 are both threshold/difficulty-modifying cards) suggests it's a real, recurring concept that needs a home, not a one-off. Candidate direction, not proposed: register "Difficulty" and "TargetProfile" as valid Subjects in `card_subject_map`. Andy's call.

---

### 28. Category: variable-cost mechanic implemented with a bare undeclared variable instead of the schema's `boost` field

**Surfaced by:** GHO.CA.8 Full Take (S141, Ghost CA review). Cost/success/successcrit all scale with a bare `n` variable declared at submission ("Ghost declares n at submission"), with no `boost=` field anywhere in the spec. This is exactly what the schema's `boost: BoostExpr` field exists for (`design_reference_card_system.md` §6 Field Groups: "player submits additional resources beyond base cost; ARBITER detects at Beat 0; success fires (1+n) times") — and DIR.CA.5 Sanctioned Raid (reviewed same session) correctly uses `boost = True: resource.faction(acting)...` for the identical shape. GHO.CA.8 reimplements the same mechanic ad hoc instead of using the confirmed field.

**Status:** Open, single confirmed instance. Candidate direction, not proposed: normalize GHO.CA.8 to use `boost=` matching DIR.CA.5's pattern. Andy's call — content/schema-conformance decision, not made here.

---

### 29. Category: bare string-literal `success` fields on undesigned CA stubs — same fossil shape as the already-closed 04-n174 sweep, new instances

**Surfaced by:** GHO.CA.13 Phantom Accounts, GHO.CA.14 Ghost Protocol, GHO.CA.15 Routing Override (all S141, Ghost CA review, all marked `*(stub)*`). Each card's `success` field is a bare prose string ("Arbiter places 1 DA-02...", "The Arbiter invalidates and removes...", "Ghost corrupts the first CA...") rather than a MutationExpr — the same category of defect 04-n174 closed S140, but that sweep covered a specific list of ModReactCard fossils (GHO.MOD.9/10/11, GUI.MOD.1, NET.MOD.11/12, SYN.MOD.1) and didn't touch these three CA stubs. All three are also missing nearly the entire base-Card field set (`card_id`/`doctrine_mod`/`boost`/`ps_framing`/`persistence`/`portrait`/`perspectives`) — sparser than even the oldest Standard/Directorate stub cards.

**Status:** Open, now **12 confirmed instances** — GHO.CA.13/14/15, GUI.CA.7/8 (S141), DIR.PA.7/DIR.PA.8 (S142), and **GUI.PA.3 Heritage Registry, GUI.PA.4 Civic Unveiling, GUI.PA.5 Zoning Exemption, GUI.PA.6 Asset Transfer, GUI.PA.7 Eminent Domain Petition, GUI.PA.8 Structural Subsidy** (all S142, Guild PA review, all `*(stub)*`, all bare-string effect fields, all missing nearly the whole base-Card field set) — Guild PA's stub cluster is the largest single-set instance yet (6 of 10 cards). **New sub-variant confirmed on GUI.PA.6/GUI.PA.7:** the bare-string defect isn't confined to `success` — both cards' `restriction` field is also a bare string (`"district(target).faction(Guild).structure > 0 AND ..."`, using English `AND` rather than Python `and`). **Another new sub-variant on GUI.PA.4:** its `success` string reads as valid Python-expression syntax accidentally left inside quotes (`"faction(Guild).standing += ..."`), distinct from the plain-English-prose shape every other instance uses — suggesting at least two different authoring failure modes produce the same symptom. All instances got full per-row checklist assessments this pass (marking what the thin content *does* support vs. doesn't), per Andy's scaffold-all direction — not left as blank templates. Worth applying the same full-scaffold treatment retroactively to GHO.CA.13-15/GUI.CA.7-8 if a normalization pass revisits the CA phase. Candidate direction, not proposed: these likely all need the same full-rewrite treatment 04-n174 gave its 7 ModReactCard fossils — possibly worth a dedicated "stub CA/PA sweep" once the full CA/PA landscape has been seen. Andy's call on priority/timing — none of these are currently gating anything.

---

### 30. Category: `card_status` DB shows NULL taxonomy for a card whose actual spec has valid, correct taxonomy

**Surfaced by:** GUI.CA.10 Development Order (S141, Guild CA review). The card's own code correctly declares `layer=Territory, function=Add, subject=StructureBlock` — a valid, Legalized-shape taxonomy assignment matching its own checklist claim. But `card_status` (DB) shows `layer`/`function`/`subject` all `NULL` for this card, and `v_card_mechanical_alignment` reports `Abstract / No Subject` as a result — a false negative caused by DB/MD drift, not a card content problem. Per `feedback_card_status_sync.md`, `card_status` should stay in sync with Art 04 "immediately... never deferred" — this is a case where that didn't happen (or the row was created before the card's taxonomy fields were finalized and never back-filled).

**Status:** Open, now **2 confirmed instances, both Guild cards.** **GUI.PA.10 Joint Development** (S142, Guild PA review) shows the identical NULL-taxonomy-but-valid-code pattern — code correctly declares `layer=Territory, function=Add, subject=StructureBlock`, matching its own checklist claim, but `card_status` shows all three `NULL`. Both confirmed instances are Guild-set cards (one CA, one PA) — worth watching whether this is a Guild-specific DB sync gap rather than a random scatter, once the remaining PA sets are checked. Candidate direction, not proposed: sync `card_status.layer/function/subject` for both cards from the actual `.md` spec. Mechanical, no content judgment needed — but not done here per this pass's flag-only scope.

---

### 31. Category: cost value in code doesn't match cost stated in prose — genuine content mismatch, not a stale-annotation issue

**Surfaced by:** NET.CA.4 Network Cascade (S141, Network CA review). Both the Design Rationale ("pay NET.CA.4's Exposure×2 to extend that disruption") and the Balance checklist row ("Exposure×2 for adjacency extension") independently state the cost is Exposure×2. The actual code: `cost = resource.faction(acting).exposure * 1 + resource.faction(acting).findings * 1` — Exposure×1 + Findings×1. This is different from the already-tracked stale-checklist-prose pattern (DIR.CA.7/NET.CA.7's "PublicStanding" mentions, where the code was correct and only the label was outdated) — here, *two independent prose locations agree with each other* and *both disagree with the code*, so it's not obviously a copy-paste-forward error from one stale mention. Genuinely unclear which is right: was the design intent Exposure×2 and the code was miswritten, or was the design later changed to cross-resource (Exposure+Findings) and the prose never updated?

**Status:** Open, now **4 confirmed instances** — NET.CA.4, and three more from S141's Syndicate CA review: **SYN.CA.3 Hostile Acquisition** (prose: "Capital×5"; code: Capital×3 + Findings×1 + Exposure×1), **SYN.CA.5 Regulatory Capture** (prose: "Capital×3," stated twice; code: Capital×2 + Exposure×1), and **SYN.CA.9 Hostile Takeover** (prose: "Capital×4 + Intel/IntelToken," stated twice; code: Capital×3 + Mandate×2, no IntelToken in `cost` at all — Intel only gates `restriction`). All three Syndicate instances follow the same shape as NET.CA.4: the prose consistently overstates the pure-resource-type amount and doesn't mention (or undercounts) the actual cross-resource composition in the code. Four independent cards, same author-behavior pattern — reads less like isolated typos and more like a systematic habit of writing the "headline" cost in prose before the cross-resource cost model was finalized in code, with the prose never swept afterward. Not resolved — the correct cost for each card is a content decision for Andy, not inferable from prose.

---

### 33. Category: `Resource cost positioning` checklist row filled with the raw guidance template text instead of an actual assessment

**Surfaced by:** SYN.CA.10 Accord Transfer and SYN.CA.11 Redline (both S141, Syndicate CA review). Both cards already had a "Resource cost positioning" row (unlike most of the corpus, which was still missing it entirely as of this review) — but the row's content was the literal guidance question copied verbatim from `design_reference_card_system.md`/Art 04 §5 ("Is this card's cost mono-resource... *(P28)*"), with no Pass-column value and no actual per-card assessment. Functionally equivalent to the row not existing, but structurally different — a checklist audit that only checks "is the row present" would have missed this, where checking "does the row have real content" catches it. Scaffolded with real assessments in this pass (mono-resource for both, per their actual `Capital(n)` cost fields).

**Status:** Fixed as scaffolding during this pass (not a design decision, just filling in the missing assessment) — noted here because it's a distinct failure mode worth watching for elsewhere: a checklist row can exist and still be unfilled. Ran the suggested grep (`grep -rln "Is this card's cost mono-resource" 04___Card_System___Part*.md`) — one more hit confirmed: **GHO.PA.5 Agency Recruitment Fair**, in the Ghost Public Acts section (out of scope for this CA-only pass, not touched — flagged here so it isn't missed when PA review starts).

**GHO.PA.5 fixed S142 (Ghost PA review):** same treatment — real assessment written in (mono-resource, Findings × 1, correctly typed).

**SYN.PA.3 Data Acquisition fixed S142 (Syndicate PA review):** same treatment — real assessment written in (mono-resource, Capital × 1, floor-power). 4th confirmed instance total, all now scaffolded with real content across both CA and PA phases. All 4 instances now confirmed within/adjacent to the Syndicate faction (SYN.CA.10/11 + SYN.PA.3) plus GHO.PA.5 — worth checking whether the raw-template-text failure mode correlates with a specific authoring batch/session, same as other Syndicate-clustered findings this review (#7, #22's third notation).

---

### 23. Category: Portrait penalty for a faction acting against its own doctrine — coverage may be inconsistent corpus-wide

**Surfaced by:** STD.CA.1–16 re-derivation pass (S141), via the Guild "cannot operate covertly" doctrine question (§5b above, `ca_pa_review_notes.md`). Andy's framing: a faction submitting a card that runs against its own stated doctrine should generally carry `submitter=-1` on that card's portrait entry — this is already the pattern on some cards (STD.CA.2/4 give Guild `-1` for demolition/undermining against "we build, we do not unmake"; STD.CA.15/16 give Guild `-1` for taking what others gathered/built).

**The gap, per Andy (S141):** this may not be applied consistently — checked against the 5 identity-hidden CA cards that prompted the original question, only 2 (CA.15/16) actually carry the expected Guild penalty; **CA.9 Fund and CA.14 Disprove have no Guild portrait entry at all**, and **CA.11 Tort Interference has `portrait = {}`, no faction entries at all**. Whether those absences are each independently justified (matching the existing "no doctrinal stake" absence-justification convention used elsewhere on these same cards) or represent a real, systematic under-application of the off-doctrine-penalty principle is the open question. Andy's hypothesis: **this might be a gap across the whole card corpus**, not just these 3 cards — i.e., other cards where a faction's doctrine is in tension with the action it enables may be similarly missing the expected portrait penalty.

**Status:** Open, evidence-gathering (3 confirmed candidate-gaps: CA.9, CA.11, CA.14) — same organic-accumulation treatment as other categories in this log. Watch for more "faction acting against own stated doctrine, no portrait entry present" instances while reviewing the rest of the CA/PA set (Directorate onward) and note them here rather than deciding case-by-case. Not proposed as a fix; needs the fuller landscape before Andy can call whether this is systematic.

---

### 24. Category: entire Standard set missing the `card_id` field — confirmed corpus-wide, not just a "pending 04-n70" placeholder

**Surfaced by:** re-derivation pass (S141), after loading `design_reference_card_system.md` in full. §6 Field Groups (Identity) defines **two separate fields**: `card_id` (canonical `[FAC].[TYPE].n` ID, e.g. `"GHO.CA.4"`) and `id` (legacy sequence integer, e.g. `id=19`, "preserved for traceability" — implying it should hold an old numeric-era value, not the canonical string). Grepped all of Part2–4c: `card_id=` appears 132× in Part3 (Ring Modifiers, matches the 132-card set) and 26–30× in Part4a/4c (Guild/Directorate faction sets) — **zero times in `Part2_Standard.md`**. Every one of STD.CA.1–16 (and presumably the Standard PA set, not yet checked) uses only `id = "STD.CA.1"` — putting the canonical string ID in the legacy field and omitting `card_id` entirely.

**Distinction from the existing generic flag:** every Standard CA card's checklist already carries `Data schema validation ⚠ Pending 04-n70` — but that placeholder has been treated as a known, generic, already-tracked non-issue (per this pass's own §4 in `ca_pa_review_notes.md`). This is a specific, concretely-verified instance of what that placeholder is actually hiding, not a new category of gap — but it's more actionable than the placeholder suggested, since it's now grep-confirmed corpus-wide across an entire Part file rather than a vague "TBD."

**Status:** Open, confirmed corpus-wide on Part2 (Standard CA, 16/16; Standard PA not yet checked). Candidate direction, not proposed: add `card_id="STD.CA.n"` alongside the existing `id=` field on all Standard cards, matching the Part3/4a/4c convention — mechanical sweep, no content judgment required. Andy's call on timing/priority.

---

### 34. Full CA corpus synthesis (S141) — cross-cutting patterns across all 69 cards, all 6 sets

**Scope:** Standard (16) + Directorate (8) + Ghost (15) + Guild (10) + Network (8) + Syndicate (12) = 69 CA cards, the complete 09-16 CA phase. This entry looks across all six per-faction reviews (§5a–5g in `ca_pa_review_notes.md`) for patterns invisible at the single-set level, matching the treatment the ModReactCard corpus got in item 20.

**A. Every recurring defect category is FactionSpecific-only — Standard is clean of all of them.** Zero instances, across the entire Standard set, of: invalid Function values (#25), unregistered Subjects (#27), `flat=` misuse (#7), or the prose/code cost mismatch (#31). Standard's only real bugs were the untyped-cost-attribute gap (#22, confined to CA.1–5) and the missing `card_id` field (#24, corpus-wide but mechanical). Every genuinely *inventive* schema deviation — a new Function word, a new Subject, a new cost notation, a semantically-off Portrait field — happened in a faction-specific card. Plausible read: Standard cards get more eyes/precedent-checking (they set the pattern everyone else copies), while faction-specific cards are where individual authors reach for something new under less scrutiny.

**B. The prose/code cost mismatch (#31, 4 instances: NET.CA.4, SYN.CA.3/5/9) has a shared shape worth naming.** In every instance, the prose states a clean, memorable single-resource number ("Capital×5," "Exposure×2") that reads as the *headline* cost, while the actual code is cross-resource and the named resource's share is lower than claimed. Three of the four (SYN.CA.3/5/9) are cards whose Design Rationale explicitly compares cost to a sibling card ("Capital×5, the most expensive..."; "Capital×3 vs DIR.CA.1's Mandate×2"; "dual cost vs SYN.CA.3's Capital×5 only") — comparative framing that would break if the number changed. Working hypothesis, not confirmed: these cards were cost-balanced into cross-resource form at some point *after* the comparative prose was written, and the prose was never swept forward. If true, the fix isn't "correct 4 typos" — it's "any card with cost-comparison prose is a candidate for the same drift," which would be worth a targeted grep (`grep -B5 "Capital×[0-9]"` style) rather than assuming these 4 are exhaustive.

**C. Portrait `flat=` clusters specifically on "public effect, covert actor" cards.** SYN.CA.10 Accord Transfer and SYN.CA.11 Redline are both explicitly designed so "the effect is public... but the actor is covert" (both cards' own Design Rationale says this in nearly those words). Hypothesis: authors reach for `flat` ("fires on resolution regardless of submitter") specifically to model the *table's reaction* to a public event, without registering that this makes their own submitting faction's entry `flat`-typed too, when `submitter=` is likely what was actually meant for that one faction. This is a more specific, more actionable framing of item #7 than "flat is used on targets" — it's "flat gets reached for whenever a card's fictional premise is 'public outcome, hidden author.'" Worth checking any future Discovery/Corrupt/Redirect card with that same public-outcome-hidden-actor shape.

**D. Missing-field gaps (#24) are now fully mapped: universal except in cards touched at S111 or later.** Across all 69 cards, `ps_framing` and `boost` are missing on every card *except* ones explicitly redesigned S111+ (SYN.CA.10/11/12, GHO.CA.4/5). `card_id` (vs. legacy `id`) is missing on the entire Standard set and roughly half of Directorate/Ghost, present on Guild/Network/Syndicate's newer cards. This confirms the "vintage correlates with drift" finding from the ModReactCard pass (item 20A) generalizes to CA — but with a twist: **newer cards don't have fewer defects, they have different ones.** Old cards are missing required fields and use wrong taxonomy terms; new cards (Syndicate's S111–S130 cluster especially) have all the required fields but introduce brand-new notation styles (#22's third cost form) and semantically-imprecise Portrait fields (#7) that didn't exist in the older, more conservative cards. A sweep strategy that only targets "old = bad" would miss the new cards' issues entirely.

**E. Intel Token as cost (#10) is the single most-repeated finding of the whole pass — 9 instances, 4 of 5 factions.** No longer reasonably describable as drift; this is close to de facto design intent that the schema hasn't caught up to. Of everything in this log, this is the strongest single candidate for "stop flagging it as a violation and formalize it as a second cost category."

**F. One open thread from mid-pass not carried through to completion:** item #23 (portrait penalty for acting against own doctrine) was raised via a Guild-specific question during the Standard review and evidence-gathered against 3 Standard-set cards (CA.9/11/14). It was never systematically re-checked against the other four factions' *own* stated doctrines against their *own* cards — e.g., does Directorate ever get a portrait penalty for acting against "restraint and continuity," does Ghost ever get one for acting against "understanding must precede action"? That cross-check wasn't done this pass. Flagging so it isn't mistaken for closed — it's still a 3-card, Standard-only evidence base.

**Status:** Presented as a cross-cutting menu, same treatment as items 4 and 20's syntheses — none of A–F is a proposal, all await Andy's read on which (if any) warrant a dedicated normalization session before Directorate-onward PA review starts.

---

### 35. Category: cross-card "same cost/threshold as [CA card]" claim checked directly and found false — Standard set, not just FactionSpecific

**Surfaced by:** STD.PA.1 Open Operations and STD.PA.2 Disputed Claim (S142, Standard PA review, first PA set reviewed). Per the standing re-derive instruction (`ca_pa_review_notes.md` §2 — "a cross-card comparison in the card's own Design Rationale... open the other card and check"), both cards' claimed CA counterparts were opened directly:

- **STD.PA.1** claims "Public counterpart to STD.CA.3 (Campaign). Same cost (2 native)." Actual STD.PA.1 cost: `resource.faction(acting) * 2` (single-resource). Actual STD.CA.3 cost: `resource.faction(acting) * 1 + resource.district(native) * 1` (dual-resource). Not the same cost shape — the claim is false.
- **STD.PA.2** claims "Public counterpart to STD.CA.4 (Undermine). Same cost (2 native), slightly better base threshold (45 vs 40)." Actual STD.CA.4 cost is also dual-resource (same mismatch as above), and its actual threshold is **50**, not 40 — meaning STD.PA.2's 45 is *worse* (lower success chance), the opposite of "slightly better."
- **STD.PA.3** claims "Public counterpart to STD.CA.1 (Build Structure). Same cost" — checked directly, **confirmed true**: identical dual-resource expression on both cards, including the shared untyped-attribute bug (item #22).

**Why this matters:** this is the same failure mode the standard was written to catch (STD.MOD.1 Overture's factually-backwards claim, S140), now confirmed in the *Standard* set specifically — synthesis item #34-A's claim that "every recurring defect category is FactionSpecific-only, Standard is clean" was built on the CA-only corpus and doesn't hold once PA is included. 2 of 3 checked cross-card claims in Standard PA were wrong; the third was right — not a uniform pattern, genuinely needs the direct check every time, per the standing instruction.

**Status:** Open, 2 confirmed false claims (STD.PA.1↔STD.CA.3, STD.PA.2↔STD.CA.4), 1 confirmed true (STD.PA.3↔STD.CA.1), all in the first PA set reviewed. Not fixed — flagged per scope. Worth running the same direct-check discipline on every "public counterpart to STD.CA.n" claim in the remaining PA sets rather than assuming the pattern holds either way.

---

### 36. Category: dangling "Cost reasoning" design_note fragment doesn't match the card's own cost — copy-paste artifact, recurring

**Surfaced by:** SYN.CA.4 (S141, first instance — "Cost reasoning: Exposure and Findings..." appended to a design_note whose actual cost is Capital-only). **Now 2 more confirmed instances (S142, Directorate PA review):** DIR.PA.1 Regulatory Override's design_note ends "...Cost reasoning: Exposure is necessary to enforce the controls publicly..." though its actual cost is Mandate-only; DIR.PA.2 Convene an Inquiry's ends "...Cost reasoning: Findings provide the legal precedent and evidence required to sustain the injunction long-term" though its cost is Mandate-only *and* "the injunction" names a different card entirely (DIR.PA.6 Standing Injunction, not DIR.PA.2 itself).

**Why this matters:** DIR.PA.2's fragment is the clearest evidence yet that these are literal copy-paste artifacts, not just stale self-reference — it references another card's own mechanic by name. All three instances share the exact shape: a trailing "Cost reasoning: [resource] is/provides [justification]" sentence bolted onto an otherwise-coherent design_note, naming a resource type the card doesn't actually use.

**Status:** Open, 3 confirmed *mismatched* instances (SYN.CA.4, DIR.PA.1, DIR.PA.2), across 2 factions and both CA/PA phases. **Contrast cases keep accumulating:** GHO.PA.4 (S142) and, in the Guild PA review (S142), **GUI.PA.1, GUI.PA.3, GUI.PA.4, and GUI.PA.5 all carry the same "Cost reasoning: [resource breakdown]" sentence template — and all four are correct**, matching their actual cost expressions exactly. The template now shows 5 confirmed-correct instances against 3 confirmed-mismatched ones — strengthens the read that this is a widespread authoring habit (possibly a shared prompt/checklist step that got followed correctly most of the time) rather than evidence the phrase itself signals a defect. Every instance still needs the same direct check; assuming either "always wrong" or "usually fine" would be equally unfounded. Not fixed — flagged per scope. Pattern is specific and mechanical enough (trailing "Cost reasoning:" sentence) that a corpus-wide grep for the literal string `"Cost reasoning:"` would likely surface the remaining instances cheaply, if Andy wants that swept before a normalization pass — but each hit needs the same direct verification, not an assumption either way.

---

### 37. Category: `resolution_type = "Permanent public act"` — not in the confirmed str vocabulary

**Surfaced by:** DIR.PA.5 Zoning Freeze, DIR.PA.6 Standing Injunction, and DIR.PA.11 Public Hearing (all S142, Directorate PA review — all three are Permanent-persistence card-as-condition PAs). design_reference_card_system.md's confirmed `resolution_type` vocabulary is exactly two values: `"Probabilistic"` (d100) and `"Transactional"` (Automatic) — "Permanent public act" is neither, and doesn't appear anywhere in the confirmed vocabulary list.

**Why this matters:** all three cards using this value are `resolution = Automatic`, which per the documented rule should take `"Transactional"`. But all three are also specifically the Permanent/card-as-condition pattern, distinct in kind from a normal one-shot Automatic PA (STD.PA.1, STD.PA.7, etc.) — it's plausible an author deliberately reached for a third category to distinguish "this card IS a standing condition" from "this card resolves once and is done," and that distinction may be worth keeping, just not under an unconfirmed ad-hoc string.

**Status:** Superseded by the broader finding at item #41 — "Permanent public act" turns out to be one of *nine* undocumented `resolution_type` values in active use, not an isolated Permanent-PA gap. See #41.

---

### 38. Category: `outcome_type` missing or explicitly `None` on real PublicAct cards — confirmed defects from the PA-phase's flagged highest-priority check

**Surfaced by:** DIR.PA.10 Official Demonstrations (`outcome_type = None`, explicit) and DIR.PA.7 Curfew + DIR.PA.8 Subpoena (field absent entirely) — all S142, Directorate PA review. Per §6.2's data dictionary (flagged going into the PA phase as the single highest-yield schema check, `ca_pa_review_notes.md` §4): "Public act resolution process type; None for covert operations" — the clear implication being every PublicAct should carry a real value. DIR.PA.10 has a fully structured d100 resolution with all four tiers populated and no ambiguity about what kind of outcome it produces (a self-contained PS shift, matching its siblings' `Unilateral` value) — there's no structural reason for it to be `None`. DIR.PA.7/8's omission is part of their broader thin-stub incompleteness (see #29), not an isolated finding.

**Status:** Open, now **9 confirmed instances** across 2 factions. All 5 Ghost PA cards passed clean (§5j), but Guild PA (S142) added 6 more: **GUI.PA.3/4/5/6/7/8**, the entire thin-stub cluster — all had the field absent entirely, now scaffolded as explicit `None` per this session's spec-scaffolding pass, same treatment as DIR.PA.7/8. GUI.PA.1/2/9/10 (the non-stub Guild PA cards) all pass clean with real values. Likely correction for DIR.PA.10: `Unilateral`, matching every other Directorate PA card in the file. Not fixed — flagged per scope. Confirms the flagged check is genuinely productive but its yield correlates with content maturity (clean on well-developed cards, defective on thin stubs) rather than faction — worth continuing to run on every remaining PA set.

---

### 39. Category: `narrative`/`perspectives` fields entirely absent (not just sparse) — uniform across one S131 authoring cluster

**Surfaced by:** DIR.PA.4, DIR.PA.5, DIR.PA.9, DIR.PA.10, DIR.PA.11 (all S142, Directorate PA review) — all five are S131-vintage redesigns/new cards (v0.1 or v3.0) that each explicitly set `narrative = None` and `perspectives = None`. Every other card reviewed in the CA/PA phase so far (114+ cards) carries at least a Directorate-only `perspectives` entry, even on faction-specific cards with no aligned/opposed voice to show. This 5-card cluster is the only place in the corpus where both fields are uniformly, deliberately absent.

**Why this matters:** this isn't scattered drift — it's uniform across exactly the 5 cards from one authoring batch (all closing specific named PM05 gaps: 04-n104, 04-n89, 04-n108, 04-n142, the 54-card floor), suggesting the batch was written to solve structural/schema problems first, with narrative voice deferred wholesale rather than per-card. All 5 also lack a Card Story block (consistent with the corpus-wide `04-n79` pending status), but go further than that — even the base `perspectives` dict, which doesn't depend on Card Story being written, is missing.

**Confirmed as a real gap, not a stylistic option (Andy, S142):** the `perspectives` field on FactionSpecific cards is meant to carry three voices — the acting faction's own, one aligned, one opposed — as deliberate worldbuilding, on *every* FactionSpecific card (now documented in `ref_card_types.md`). This cluster's `perspectives = None`, along with the same gap on the genuinely-thin Guild/Network/Syndicate PA stubs (schema_cleanup_log.md #29's cluster — GUI.PA.3–8, NET.PA.4–6, SYN.PA.4/5, all missing `narrative`/`perspectives` too), is the same underlying defect repeating across every faction's PA stub batch, not five isolated cases. Roughly a third of the 45-card PA corpus is missing this by default.

**Status:** Open, 5 confirmed instances, all one authoring cluster. Not fixed — flagged per scope. Straightforward normalization candidate once narrative work resumes for this batch — these 5 need perspectives written from scratch, not swept-forward text like the "PublicStanding" pattern (item 4-F).

---

### 40. Category: "(stub)" header label stale on cards with complete content; DB `design_pass` flag desynced from blank .md Status table

**Surfaced by:** DIR.PA.4, DIR.PA.5, DIR.PA.9, DIR.PA.10, DIR.PA.11 (all S142, Directorate PA review) — all five carry a `*(stub)*` header suffix and a fully-blank 17-row checklist template, yet all five have complete, schema-conformant `Card()` blocks (structured cost/success/portrait, detailed design_note) representing real S131 design work that closed specific named gaps. Only DIR.PA.7 and DIR.PA.8 in the same file are genuine stubs matching their label (bare prose-string `success`, most fields absent). The "(stub)" header is not a reliable signal of content maturity in this file — 5 of 7 stub-tagged cards are stale-labeled.

**Compounding DB desync:** DIR.PA.4 and DIR.PA.5 specifically showed `design_pass=1` in `card_status` *prior to this session's review*, despite their .md Status tables being fully blank (no Design Pass ✓ anywhere) — a second, distinct DB/MD drift pattern alongside item #30's NULL-taxonomy version (there: DB missing data the .md has; here: DB claims a review-completion state the .md doesn't reflect at all).

---

### 41. Category: `resolution_type` vocabulary is far larger than documented — 9 values in active use, only 2 confirmed in schema

**Surfaced by:** DIR.PA.5/6/11's `"Permanent public act"` (originally logged narrowly as item #37) plus, on closer look during the Network PA review (S142), **NET.PA.1's `resolution_type = "Contested"`** — which prompted a full corpus grep rather than treating it as one more isolated instance. `design_reference_card_system.md` documents exactly two confirmed values (`"Probabilistic"` for d100, `"Transactional"` for Automatic). The actual corpus (`grep -rn 'resolution_type\s*=\s*"' *.md | sed -E 's/.*"([^"]+)".*/\1/' | sort | uniq -c`, all 8 Part files) shows:

| Value | Count |
|---|---|
| Transactional | 213 |
| Probabilistic | 53 |
| Positional wager | 14 |
| Contested | 10 |
| Permanent public act | 7 |
| Conditional | 4 |
| Deceptive | 2 |
| Predictive | 2 |
| Verification | 2 |
| PlayerChoice(target) | 1 |

**This is not a fresh discovery — it's an already-tracked, currently-open PM05 item.** `PM05___Active_Punch_List.md` item **04-25** ("Resolution type field — rationalize taxonomy after full card set") already names this exact gap: "C01–C15 populated with descriptive prose values — no enforced vocabulary... Known values in use: Transactional, Probabilistic, Positional wager, Conditional... Once C01–C35 and P01–P18 are complete: review all Resolution type values across the full set; rationalize into a formal taxonomy." **The CA/PA design review (09-16) is now that trigger condition** — C01–C35 and P01–P18 (i.e., the full CA+PA corpus) are at or near complete as of this session. PM05 item 04-n36 also separately pre-registers `"PlayerChoice(target)"` as an intentional future value for a specific card family (Directorate formal-inspection cards), confirming at least one of these 9 values is deliberate, not drift.

**Corpus-mismatch caught in this review specifically:** STD.PA.2/4/5/6 (all `"Contested"`) were reviewed in the Standard PA pass (§5h) without this being flagged — caught retroactively only once NET.PA.1's identical value prompted the full grep. Those four cards' checklists have been corrected after the fact. Worth treating as a lesson: a value not matching the documented 2-item list should always be checked against the corpus, not assumed to be an isolated typo, precisely because 04-25 already exists and this pass is its natural trigger.

**Status:** Open — this session's job was to surface the full picture for 04-25, not resolve it. All CA/PA review sessions from here should flag any `resolution_type` value outside the documented `"Probabilistic"`/`"Transactional"` pair as a 04-25 data point, not a one-off. Andy's call on when to schedule the actual rationalization pass — the review corpus itself (this log + `ca_pa_review_notes.md`) is now the input 04-25 was waiting for.

---

### 43. Category: `cost` expression draws from the *target* faction's resource pool, not the acting faction's own — blurs cost/effect distinction

**Surfaced by:** NET.PA.5 Viral Outrage (S142, Network PA review, thin stub). `cost = resource.faction(Network).exposure * 2 + resource.faction(target_faction).native * 1` — the second term draws from `target_faction`'s own native resource pool, not the acting faction's (Network's). Every other cost expression reviewed across the full CA/PA corpus (114+ cards) is paid entirely from the acting faction's own pool; §6 Field Groups defines `cost: CostExpr` without addressing whose pool it draws from, implicitly assuming the submitter's. The card's own design_note frames this as deliberate ("Network burns the opponent's own native resource to fuel the smear campaign") — this isn't an authoring slip, it's an intentional mechanic that the schema has no vocabulary for.

**Why this matters:** if a resource deduction from a non-acting faction is a valid `cost` term, that's a new category needing its own confirmed syntax and procedural backing (does the target faction have any say, is this even legal if they don't hold enough of that resource, what happens on partial availability). If it's not intended as `cost` at all, the mechanic probably belongs in `success` as an explicit effect on the target (`faction(target_faction).resource(native) -= 1`) instead, keeping `cost` scoped to what the submitter pays. Either way, this is a schema question, not a typing question — distinct from item #22 (untyped attribute) and item #10 (Intel Token as cost), both of which are about *what* a card pays, not *whose pool* it pays from.

**Status:** Open, single confirmed instance, on a genuinely thin stub card (not yet fully designed). Not fixed — flagged per scope. Worth watching for recurrence in the remaining PA sets (Syndicate) before treating this as an isolated card-specific idea vs. a broader "cost can draw from a target" pattern that needs formal support.

---

### 44. Category: `persistence = Transient` combined with prose describing an effect spanning a Quarter boundary — tension with the "no multi-Quarter temporaries" rule

**Surfaced by:** DIR.PA.7 Curfew (S142, Directorate PA review — "Places a Standing Condition on target_district until the end of Quarter+1") and **SYN.PA.5 Protection Racket** (S142, Syndicate PA review — "until Quarter+1"), both genuinely thin stub cards. Art 04 §5's duration discipline (P19–P21, design_reference_card_system.md) states "Effects are permanent or within-Quarter — multi-Quarter temporaries prohibited." `Transient` is documented as a valid persistence value (Immediate/Transient/Seasonal/Permanent), but both cards pair it with prose describing the effect lasting into the *following* Quarter — which reads as exactly the prohibited shape, if "Quarter+1" means what it appears to mean (the next Quarter, not "the remainder of this Quarter").

**Why this matters:** both instances are on thin, unstructured stub cards (bare-string `success`), so it's plausible this is just loose, not-yet-formalized prose rather than a deliberate design choice — unlike the "Permanent public act" resolution_type question (item #41), which recurred on well-developed cards. Still, two independent cards using the identical "Quarter+1" phrasing is enough to flag as a pattern rather than a one-off typo, especially since neither card defines what "Transient" actually bounds without a structured `persistence_condition`.

**Status:** Open, 2 confirmed instances, both thin stubs. Not fixed — flagged per scope. Worth checking whether "Quarter+1" is established shorthand elsewhere in the corpus for "remainder of this Quarter, extending into upkeep of the next" (which would resolve the tension) before assuming it's a genuine multi-Quarter violation.

---

### 45. Full PA corpus synthesis (S142) — cross-cutting patterns across all 45 cards, all 6 sets

**Scope:** Standard (8) + Directorate (11) + Ghost (5) + Guild (10) + Network (6) + Syndicate (5) = 45 PA cards, the complete 09-16 PA phase, mirroring item #34's treatment of the CA phase. Cross-references `ca_pa_review_notes.md` §5h–§5m (per-faction findings).

**A. Item #34-A's "Standard is clean of all FactionSpecific-only defect categories" claim does NOT survive the PA phase.** Standard PA turned out to be the single dirtiest set on two specific measures: the untyped-cost-attribute bug (#22) is 8/8 in Standard PA (vs. 6/16 in Standard CA), and 2 of 3 checked "same cost/threshold as the CA counterpart" cross-card claims (#35) were confirmed false — both defects the CA-only synthesis had pinned as either Standard-clean or FactionSpecific-only. The lesson isn't "Standard is secretly bad" — it's that a synthesis built on half a corpus (CA only) doesn't generalize to the other half, and shouldn't have been trusted to. Every remaining synthesis claim in this item should be read the same way: current best evidence, not a settled fact.

**B. The bare-string/undeveloped-stub defect (#29) exploded in scale and moved into new fields.** CA phase: 5 instances, all `success` fields, all clustered in Ghost/Guild CA stubs. PA phase: 12 instances (now 12 total across both phases, entirely new in PA), spreading to `restriction` (GUI.PA.6/7), `persistence_condition`/`persistence_effect` (NET.PA.3), and a distinct sub-shape — syntactically-valid Python left inside quotes rather than English prose (GUI.PA.4). Guild PA alone contributed 6 of the 12 total instances (the largest single-set concentration in the whole review) — Guild's PA stub cluster is bigger and more varied in failure mode than any CA-phase stub cluster.

**C. The "(stub)" header label is not a reliable signal either way — it has to be checked every time, in both directions.** Directorate PA: 5 of 7 stub-tagged cards were actually complete (mislabeled). Guild PA: 6 of 6 stub-tagged cards were genuinely thin (accurately labeled). Network PA: 3 of 3 accurately labeled. No faction-level or corpus-level prior predicts which way a given "(stub)" tag will go — this confirms the direct-check discipline (§2 of `ca_pa_review_notes.md`) was necessary, not belt-and-suspenders.

**D. `resolution_type` vocabulary sprawl (#41) was invisible until this phase, and directly triggers an already-open PM05 item.** 9 values in active use against 2 documented — caught only because NET.PA.1's `"Contested"` prompted a full grep, which then required retroactively correcting the Standard PA review (§5h) where the same value had already passed through unflagged. This is the single most consequential finding of the PA phase: it feeds directly into PM05 item 04-25, whose stated trigger condition ("once C01–C35 and P01–P18 are complete") is essentially met now.

**E. Intel Token as cost (#10) kept growing and diversifying, not converging.** 10 instances/4 notations at the end of the CA phase → 14 instances/7 notations at the end of the PA phase. No two cards across the entire 114-card corpus spell this identically. This is now unambiguously the single strongest formalization candidate in the whole log — not because any individual instance is a "violation" needing a fix, but because the sheer notational chaos (7 ways to say the same thing) is itself evidence the schema never gave authors a canonical form to converge on.

**F. `card_status` DB/MD desync is a recurring, multi-field, multi-faction pattern, not isolated incidents.** Four separate instances surfaced this session alone across three fields (`design_pass`, `issues_resolved`, `layer`/`function`/`subject`) and three factions (Directorate, Ghost, Guild) — on top of the two CA-phase instances (item #30). This reads as a systemic gap in whatever process is supposed to keep `card_status` synchronized with the `.md` source of truth, not five unrelated one-offs — worth a dedicated reconciliation pass rather than continuing to log individual instances as they're found.

**G. The dangling "Cost reasoning:" design_note fragment (#36) turned out to be a coin-flip, not a defect signal.** 3 confirmed mismatches (SYN.CA.4, DIR.PA.1, DIR.PA.2) vs. 5 confirmed-correct instances (GHO.PA.4, GUI.PA.1/3/4/5) found in the same pass. The phrase itself predicts nothing — every instance still needs the direct check, same lesson as item A above at a smaller scale.

**H. `flat=` portrait misuse (#7) is the one pattern that stayed genuinely faction-specific.** All 5 confirmed instances across both CA and PA phases are Syndicate cards (SYN.CA.7/10/11/12, SYN.PA.3) — no other faction shows this pattern anywhere in 114 cards. Unlike items A/B/C above, this one held up under the full-corpus check rather than collapsing.

**I. Corpus-wide scaffolding debt closed this session:** all 45 PA cards now carry `card_id`/`boost`/`ps_framing` explicitly (previously silently absent on roughly two-thirds of the set), matching the same fields' state in the Ring Modifier and faction ModAction/ModBattle corpora. All 45 now show `design_pass=1` in both `.md` and DB.

**Status:** Presented as a cross-cutting menu, same treatment as items 4, 20, and 34's syntheses — none of A–I is a proposal, all await Andy's read on which (if any) warrant a dedicated normalization session. Items D and E (resolution_type, Intel Token) are the two strongest candidates for near-term attention given they each connect to a concrete, already-recognized need (04-25's trigger condition; a de-facto second cost category). With this item, the full 09-16 design review pass (114 CA/PA cards + earlier ModReactCard/ModAction/ModBattle corpora) has now had a cross-cutting synthesis written for every phase.

**Addendum, checked after Andy's follow-up prompt (S142):** three further observations, verified by direct grep across all 6 PA files rather than recalled from memory:

- **`outcome_type` enum coverage is far narrower in practice than in schema.** §6.3 documents six values (`Binary`, `ElectPlayer`, `ElectDistrict`, `ElectFaction`, `BilateralAgreement`, `Unilateral`). Actual usage across all 45 PA cards: `Unilateral` ×24, `BilateralAgreement` ×2 (STD.PA.8, GUI.PA.2), `ElectPlayer` ×2 (SYN.PA.1, SYN.PA.3), `None` ×15 (mix of this session's scaffolded-placeholder `None`s on thin stubs and the confirmed real gaps in item #38). **`Binary`, `ElectDistrict`, and `ElectFaction` have zero instances anywhere in the PA corpus.** Either these three values describe design space nobody has built yet (plausible — a PA that lets a target pick among several *districts* or several *factions* to redirect an effect at is a real, unbuilt card shape), or they're aspirational/theoretical enum entries. Worth Andy's read on whether any planned-but-unwritten PA cards were meant to use them.
- **`boost` is essentially a dead field in the PA corpus.** Of 45 cards, only **GHO.PA.3** uses it for real (expired Intel Tokens scaling a BM-xx multiplier). Every other PA card's `boost` is `None` — either originally authored that way or scaffolded so this session. Contrast with the CA corpus, where DIR.CA.5 Sanctioned Raid uses `boost` as a core mechanic (scaling threshold and effect together). This may be structurally sound — PAs are already public/declared, so the "cannot see how big this move is until it resolves" tension `boost` seems designed for is a covert-ops concern — but it's worth naming explicitly rather than letting a fully-specified field sit unused across an entire card-type category without anyone having decided that's fine.
- **Card Story (P26) compliance across the PA corpus is very low** — the large majority of PA cards still carry "⚠ Story pending 04-n79" rather than real Card Story text (already-tracked via 04-n79, not a new gap) — but worth stating the scale plainly now that the full PA set has been read end to end: this is one of the largest concrete blockers standing between "Design Pass ✓" (done this session, corpus-wide) and any future sign-off pass, since P26 is a locked principle (S78) that a real design problem exists if the story can't be told plainly.

**Root-cause note on item #35 (cross-card claim mismatches) — superseded, see item #46.** The "public counterpart to STD.CA.n" relationship that produced 2 false claims in Standard PA is not a one-card fluke — it recurs throughout the PA corpus (STD.PA.1/2/3↔STD.CA.3/4/1, SYN.PA.1↔SYN.CA.3, GUI.PA.2 distinguished from STD.CA.9, DIR.PA.9/10 both cross-reference DIR.CA.6/7's counting mechanism) as a design methodology, not incidental prose. This entry originally floated a lightweight structured field to formalize the pairing for traceability. **Andy's direction (PM02 L276): the opposite — remove the cross-referencing practice from card content entirely, don't formalize it.** Cards must stand on their own; comparison/contrast across cards belongs in a separate strategy-guide-style artifact, if wanted at all, not inside individual card design_rationale/design_note/arbiter_note. See item #46.

---

### 42. Category: `card_status` DB/MD desync family — running tally across the PA phase

Consolidating the desync instances found across this session rather than scattering them further: STD.CA.12/GUI.CA.10 (S141, `layer`/`function`/`subject` NULL in DB despite valid code — #30), DIR.PA.4/5 (`design_pass=1` in DB despite blank .md Status — #40), GHO.PA.3/4/5 (`issues_resolved=1` in DB despite blank .md Status — noted under #40), GUI.PA.10 (NULL taxonomy again, second Guild-set instance — #30 extended). Four distinct fields now show the same underlying shape (DB claims a state the .md doesn't reflect), across 3 factions and both CA/PA phases. Not itself a new item — pointer for whoever eventually reconciles `card_status` against the `.md` source of truth, so all instances are found in one pass rather than trickling in card-by-card.

**Status:** Open. Andy's S142 direction: scaffold-all is the scope of this pass regardless of stub/non-stub status — applied here (all 5 mislabeled cards got full checklists this session; DIR.PA.7/8 also got full checklists per the same instruction, see item #29). Header text itself ("*(stub)*") was not corrected — flagged, not fixed, per scope; worth a quick pass to drop the stale label from DIR.PA.4/5/9/10/11 once a normalization sweep is scheduled.

**Recurred on a different field (S142, Ghost PA review):** GHO.PA.3, GHO.PA.4, GHO.PA.5 all show `issues_resolved=1` in `card_status` despite their .md Status tables showing a fully blank Issues Resolved cell — same desync shape as DIR.PA.4/5, but on `issues_resolved` rather than `design_pass`, and in a different faction/phase entirely. Now 5 confirmed instances of "DB flag claims a review-completion state the .md doesn't reflect" across 2 factions. Not reconciled either direction — flagged only, per scope.
