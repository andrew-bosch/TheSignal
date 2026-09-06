> **Status:** retained evidence record for `schema_cleanup_log` #64 (CLOSED S159). The rulings,
> the 8 recategorisations and the open GUI.CA.9 question all live in #64's closure and PM02 L368;
> what only lives here is the **per-card call and its evidence for all 72 cards** — including the
> 64 held `Transactional`. #64 establishes that a query cannot reproduce this, so deleting the file
> means re-reading 72 card bodies to answer any later "was X checked?".
> **Trigger for deletion:** when the CA/PA corpus has changed enough that the per-card calls would
> need re-deriving anyway — at which point this is superseded, not merely finished. Andy may of
> course call it sooner.

# #64 PositionalWager re-derivation — running classification (S159)

Population: 72 non-React Automatic cards = 39 CovertOperation + 33 PublicAct
(verified two ways: card_status.card_type and v_card_body.type — no mismatch;
all 92 Automatic MOD cards are literally type=ModReactCard).

## Test applied
PositionalWager if, at commitment (Dispatch), the payoff depends on whether/what
another faction submits or does later in the Quarter — information not revealed at
commitment. Three recognised shapes:
  W1 explicit forward-slate reference in code (game.ops(beat=N), resolution_grid.*)
  W2 existence wager — targets an op/asset whose presence in the unrevealed slate is
     uncertain (Andy S157: "the wager is that an operation to impact exists")
  W3 semantic wager — no beat named in code; payout only lands if a rival takes a
     specific action later in the Quarter (GUI.CA.2/6 precedent)
NOT a wager: resolves against board state visible at commitment; or uncertainty is a
bilateral accept/decline (SYN.CA.4 ruling: accept/decline is not the mechanism —
that is what outcome_type covers).

---

## STD (11)
| card | current | call | evidence |
|---|---|---|---|
| STD.CA.1 Build Structure | Transactional | HOLD | own build against visible board state |
| STD.CA.3 Campaign | Transactional | HOLD | own presence deepening, visible state |
| STD.CA.6 Broadcast Interference | PositionalWager | HOLD | W1 `game.ops(beat=4, type=PublicAct...)` |
| STD.CA.7 Amplify | PositionalWager | HOLD | W1 `faction(acting).op(beat=4...)`; rationale: "if no Public Act is submitted, Amplify fizzles" |
| STD.CA.10 Protect | PositionalWager | HOLD | W1/W2 `game.ops(beat=3, at=..., targeting=acting.assets)` — attack may not materialise |
| STD.CA.11 Tort Interference | Transactional | HOLD | named Accord is executed + on table at commitment |
| STD.CA.12 Absolute Compromise | Transactional | **CANDIDATE → PositionalWager** | W2. Beat 2 sweep of the named district's Beat 2 row; `restriction = beat2_row.has_block_or_protect_card == True` is evaluated at Beat 2, not at commitment. Rationale: "the acting faction commits a blanket sweep without disclosing what was removed." Intel Token spent for nothing if no Block/Protect card is there. **Boundary note:** targets the *same* beat's row, not a later beat — needs Andy's read on whether same-beat-but-unrevealed counts (§6.3's "future beat" is phrased as an e.g.). |
| STD.PA.1 Open Operations | Transactional | HOLD | own declaration |
| STD.PA.3 Public Commission | Transactional | HOLD | own build, restriction checked at Beat 0 |
| STD.PA.7 Public Address | Transactional | HOLD | own PS gain |
| STD.PA.8 Table an Accord | Transactional | HOLD | accept/decline is bilateral, not a slate wager (SYN.CA.4 precedent) |

## Profile of the 13 confirmed instances (derived, not assumed)
All 13 are **beat = 2**, **CovertOperation**, **persistence = Immediate**
(GUI.CA.6 has no `persistence` field at all — side finding, absent-field family, same shape as #59).
This is the empirical basis for principle **P1** below: beat 2 is the only beat that
precedes other beats inside the Quarter's resolution sequence.

### P1 — the standing-condition boundary (derived this session, needs Andy's confirmation)
A card whose contingency is carried by a **standing condition** (`persistence` =
Seasonal/Permanent + `persistence_effect` / `game.world_condition`) or by a **delivered
instrument** (e.g. a Grant Deed) is **Transactional**: the card itself resolved
deterministically at its own beat, and the schema already expresses the downstream
contingency through the persistence fields. PositionalWager is reserved for a card whose
*own* resolution is decided by the unrevealed slate. All 13 confirmed instances are
`persistence = Immediate`, which supports this. Without P1 the label would swallow every
reactive board condition in the corpus and stop discriminating.
Affected calls: GUI.CA.10, GUI.PA.3, GUI.PA.8, and others below — all flagged for Andy.

## GUI (15)
| card | current | call | evidence |
|---|---|---|---|
| GUI.CA.1 Fortify Structure | PositionalWager | HOLD | W2 — immunity pays off only if a demolish is submitted; rationale: "betting a slot that your structure will be targeted" |
| GUI.CA.2 Materials Acquisition | PositionalWager | HOLD | W3 — `trigger = faction(target).completes(CovertOp, id=STD.CA.2)`; rationale: "betting a Beat 2 slot that this faction will execute STD.CA.2" |
| GUI.CA.5 Infrastructure Yield | Transactional | HOLD | control tier visible at commitment |
| GUI.CA.6 Labor Contract | PositionalWager | HOLD | W3 — trigger on named faction completing STD.CA.1 |
| GUI.CA.7 Buyout Clause | Transactional | HOLD | target presence visible; unblockable, unconditional |
| GUI.CA.9 Works Guarantee | PositionalWager | HOLD | W1 — operates on a named Beat 3 CA |
| GUI.CA.10 Development Order | Transactional | HOLD (P1) | delivers GD-01 Grant Deed; rationale says the deed's fire effect is "trigger-conditional, not a guaranteed payoff" — but the *card* always delivers the deed. Boundary case; pairs with SYN.CA.8 Land Title |
| GUI.PA.1 Civic Works Mandate | Transactional | HOLD | own double build |
| GUI.PA.2 Infrastructure Bond | Transactional | HOLD | Accord accept/decline ≠ slate wager |
| GUI.PA.3 Heritage Registry | Transactional | HOLD (P1) | Permanent board condition restoring the first structure removed by anyone — contingency carried by `persistence_effect` |
| GUI.PA.4 Civic Unveiling | Transactional | HOLD | scales off Guild's own visible structure count |
| GUI.PA.5 Zoning Exemption | Transactional | HOLD | Seasonal waiver for own use |
| GUI.PA.6 Asset Transfer | Transactional | HOLD | both sides' state visible |
| GUI.PA.7 Eminent Domain Petition | Transactional | HOLD | own foothold |
| GUI.PA.8 Structural Subsidy | Transactional | HOLD (P1) | Seasonal condition converting *others'* builds into Guild PS — same doctrine as GUI.CA.6 (a confirmed wager); differs only in being a standing condition rather than an Immediate contingent payout. **The sharpest P1 test case in the corpus** |

## Submission ordering (Art 03 §9, via ref_procedures.md) — load-bearing for the test
§9.1 Covert Dispatch (CA cases sealed, ARBITER-private) → §9.2 Public Declaration (PAs
face-up, Target Profiles face-down) → §9.3 Countermeasures → §9.4 Beats 0–4.
Consequences: a **CA is committed before any PA is declared**, so a CA that depends on the
PA slate is wagering; the covert grid is never revealed to players at all, so any card
depending on another faction's covert op is wagering; a **PA is declared after covert
dispatch**, so a PA depending on Beat 2/3 outcomes is also committed blind.

## GHO (12)
| card | current | call | evidence |
|---|---|---|---|
| GHO.CA.1 Pattern Match | Transactional | **CANDIDATE → PositionalWager (the pending #64 call)** | W1+W2. Beat 2; must name faction + district + operation in advance and redirect it out of the target's Beat 3 lane; "The risk of a wrong prediction — or an unexecutable steal — is real." #41's disqualifier ("deterministic declare-then-verify") is part of the PW definition, not a bar to it |
| GHO.CA.3 Dossier Breach | Transactional | **CANDIDATE → PositionalWager** | W2 existence wager, explicit in the card's own text: "Beat 2 commitment is the risk: 2 Findings spent before Ghost knows what the target will submit" / "If faction X has no Beat 3 operations, deliver an empty slip — Ghost's resources are spent" |
| GHO.CA.5 Misdirection | Transactional | **CANDIDATE → PositionalWager** | W2. Beat 3 CA committed at §9.1, before §9.2 — corrupts an Intel Token on the target's *active PA*, which is not declared yet at commitment. "If no qualifying token: card fizzles, 1 Findings spent" |
| GHO.CA.6 Synthesize | Transactional | HOLD | own held tokens |
| GHO.CA.9 SCIF | Transactional | HOLD | records the target's *current* structure count — visible board state; deferred payout is deterministic |
| GHO.CA.10 Flip | Transactional | HOLD | own token, fixed yield |
| GHO.CA.12 Source Substitution | Transactional | HOLD | own token |
| GHO.CA.14 Ghost Protocol | PositionalWager | HOLD | W2, Andy's S157 ruling |
| GHO.CA.15 Routing Override | PositionalWager | HOLD | W1/W2, Andy's S157 ruling |
| GHO.PA.1 Publish Analysis | Transactional | HOLD | own tokens, fixed PS swing |
| GHO.PA.2 Signal Review Request | Transactional | HOLD (P1) | Transient world condition penalising the target's covert ops in a district *next Month* — contingency carried by persistence, not by this card's own resolution |
| GHO.PA.4 Public Threat Assessment | Transactional | HOLD | ARBITER disclosure obligation; restriction checkable at declaration |

### P2 — mechanical dependence, not strategic anticipation
Every card in the game is submitted blind, so "I am guessing what my rivals will do" is
true of the whole corpus and cannot be the discriminator. PositionalWager requires the
card's *mechanism* to reference the unrevealed slate (an op, a submission, or the
existence of one). A card that merely rewards good anticipation while resolving entirely
against visible board state is Transactional — e.g. DIR.CA.4 Tactical Redirection
("Directorate anticipates the round's contested districts and pre-positions").

## DIR (14)
| card | current | call | evidence |
|---|---|---|---|
| DIR.CA.1 Invoke Jurisdiction | Transactional | **CANDIDATE → PositionalWager (the second pending #64 call)** | W2. Its own Design Rationale already says "Beat 2 Automatic **positional wager**". Blocks STD.CA.1/CA.3 in a district against an unrevealed Beat 3 slate; identical shape to SYN.CA.5, already `PositionalWager` |
| DIR.CA.3 Surveillance Placement | Transactional | **CANDIDATE → PositionalWager** | W2, same shape as GHO.CA.3: "If no Beat 3 operations target the district, deliver nothing — Directorate's resources are spent" |
| DIR.CA.4 Tactical Redirection | Transactional | HOLD (P2) | moves own presence between adjacent districts; anticipation only, no slate reference |
| DIR.CA.8 Enhanced Scrutiny | PositionalWager | HOLD | W1, fixed S157 |
| DIR.PA.1 Regulatory Override | Transactional | HOLD (P1) | Seasonal world condition |
| DIR.PA.2 Convene an Inquiry | Transactional | HOLD | yield counts *already public, already resolved* attributions — a gamble on past groundwork, all of it visible |
| DIR.PA.3 Entry/Exit Controls | Transactional | HOLD (P1) | Permanent board condition |
| DIR.PA.4 Regulatory Downgrade | Transactional | HOLD | removes one visible chip |
| DIR.PA.5 Zoning Freeze | Transactional | HOLD (P1) | Permanent card-as-condition |
| DIR.PA.6 Standing Injunction | Transactional | HOLD (P1) | Permanent condition blocking a *future* PA of a named taxonomy; wager-flavoured (the partial Mandate refund exists precisely because the deterrent may never fire) but the contingency is carried by `persistence_effect` |
| DIR.PA.7 Curfew | Transactional | HOLD (P1) | Permanent condition, fires next Placement phase |
| DIR.PA.8 Subpoena | Transactional | HOLD | ElectPlayer accept/decline ≠ slate wager (SYN.CA.4 precedent) |
| DIR.PA.9 Charter Grant | Transactional | HOLD | own placement, count off visible Permanents |
| DIR.PA.11 Public Hearing | Transactional | HOLD (P1) | Permanent game-wide institution |

## NET (8)
| card | current | call | evidence |
|---|---|---|---|
| NET.CA.1 Leak | Transactional | **CANDIDATE → PositionalWager** | W2, and the closest analogue to the already-confirmed GHO.CA.14: cancels the target's highest-cost unresolved Beat 3 op. "If no unresolved operations remain for target faction at time of Leak's resolution, operation has no effect — Network's resources spent." Also carries an explicit initiative-order fizzle risk |
| NET.CA.2 Disclosure Loop | Transactional | HOLD — but flag | pays out only if one of Network's *own* Reveal cards resolved this round. Network knows what it submitted, so the unknown is an outcome (a die), not unrevealed information. GUI.CA.9 (own Beat 3 CA, confirmed PW) cuts the other way — worth Andy's read |
| NET.CA.4 Network Cascade | Transactional | **CANDIDATE → PositionalWager** | W1. Extends STD.CA.6's PA cost penalty (STD.CA.6 is itself a confirmed instance) into an adjacent district; PAs are not declared until §9.2, after covert dispatch |
| NET.CA.5 Community Anchor | Transactional | HOLD | Baryo entry, visible restriction |
| NET.CA.6 Sacrifice | Transactional | HOLD | own PS traded for a token |
| NET.PA.2 Community Rally | Transactional | HOLD | own Established districts |
| NET.PA.5 Viral Outrage | Transactional | HOLD | bare-prose PA (04-n218); nothing in it references a slate |
| NET.PA.6 Crowdfunding Campaign | Transactional | HOLD | bare-prose PA (04-n218); scales off own visible PS |

## SYN (12)
| card | current | call | evidence |
|---|---|---|---|
| SYN.CA.1 Leveraged Acquisition | Transactional | HOLD | fixed Capital→native conversion |
| SYN.CA.4 Golden Parachute | PositionalWager | HOLD | Andy's S157 ruling |
| SYN.CA.5 Regulatory Capture | PositionalWager | HOLD | rescoped under #61; rationale: "Committing Capital at Beat 2 against a Beat 3 slate nobody has revealed is a positional bet" |
| SYN.CA.6 Parasitic | PositionalWager | HOLD | W2, explicit |
| SYN.CA.7 Corporate Blackmail | Transactional | HOLD | target presence visible; ElectPlayer |
| SYN.CA.8 Land Title | Transactional | HOLD (P1) | delivers a Grant Deed tripwire; rationale calls it "a positional play — registers claims on districts likely to develop, then reacts when the trigger fires". Pairs with GUI.CA.10 — decide both together |
| SYN.CA.12 Boilerplate | Transactional | HOLD | delivers a blank Accord form |
| SYN.PA.1 Acquisition Offer | Transactional | HOLD | ElectPlayer |
| SYN.PA.2 Public Dividend | Transactional | HOLD (P1) | Seasonal escrow condition |
| SYN.PA.3 Data Acquisition | Transactional | HOLD — but flag | "The demand is a guess — N is committed at §9.2" against the target's *hidden token count*. That is hidden **private state**, not an unrevealed **submission slate**; a third kind of uncertainty the §6.3 definition does not name. Permanent React phase is a persistence effect (P1) |
| SYN.PA.4 Charity Gala | Transactional | HOLD | bare-prose PA; table-wide toll, no slate reference |
| SYN.PA.5 Protection Racket | Transactional | HOLD (P1) | Seasonal standing condition; bare-prose PA |

---

# Summary

**Coverage: 72/72 read.** Enum check: the 72 split 13 `PositionalWager` / 59 `Transactional`,
no `Probabilistic` mislabels, and no d100 card carries a non-Probabilistic value.

**8 recategorisations proposed (Transactional → PositionalWager), 6 of them new this session:**
1. **GHO.CA.1** Pattern Match — the #64 pending call
2. **DIR.CA.1** Invoke Jurisdiction — the #64 pending call
3. **GHO.CA.3** Dossier Breach *(new)*
4. **DIR.CA.3** Surveillance Placement *(new)*
5. **GHO.CA.5** Misdirection *(new)*
6. **STD.CA.12** Absolute Compromise *(new)*
7. **NET.CA.1** Leak *(new)*
8. **NET.CA.4** Network Cascade *(new)*

If all 8 are applied the corpus goes **13 → 21**, and every instance is a CovertOperation
(no PublicAct qualifies — beat 4 is last, and PA-borne contingencies are all carried by
persistence fields).

**Two boundary rulings are needed before applying, because they decide ~10 cards each:**
- **P1** (standing conditions / delivered instruments are Transactional) — governs GUI.CA.10,
  SYN.CA.8, GUI.PA.3, GUI.PA.8, GHO.PA.2, DIR.PA.1/3/5/6/7/11, SYN.PA.2/PA.5.
- **Same-beat wagers** — STD.CA.12 (Beat 2 → Beat 2 row) and NET.CA.1 (Beat 3 → Beat 3 slate)
  bet on an unrevealed slate at their *own* beat rather than a later one. All 13 confirmed
  instances are cross-beat (2→3 or 2→4). §6.3's "future beat" is written as an *e.g.*, and
  the discriminator it names is "unknown information at the moment of commitment," which
  covers both.

**The 13 HOLD calls marked (P1) are contingent, not settled** — they flip together if Andy
rules the other way on P1.

**Possible over-inclusion in the confirmed 13 — GUI.CA.9 Works Guarantee.**
#64 groups it with GUI.CA.1/2/6 as cards that "wager semantically … paying at Beat 2 for an
effect that only pays off if a rival demolishes, develops, or builds later in the Quarter."
That description does not fit CA.9: it operates on **Guild's own** named Beat 3 CA
(`restriction = target_ca in game.dispatch.guild.beat3`), and district B's eligibility is
checked at Beat 0 against board state that is already visible at §9.1. Under the §6.3 test —
"unknown information at the moment of commitment" — there may be no unknown at all beyond the
residual risk (shared by every card) that a rival blocks or steals the named CA. Worth Andy's
look; the enumeration was never derived, which is the whole reason #64 exists, and it can be
wrong in this direction as easily as the other. If CA.9 does not hold, NET.CA.2's only
counter-argument goes with it and that HOLD gets stronger.

**Prose that has to change with the field (checked on all 8):**
Only **GHO.CA.1** argues for its current value in prose — its Design Rationale opens
"resolves deterministically (`resolution_type = Transactional`; the earlier `"Predictive"`
label was corrected, schema_cleanup_log #41 …)", and its "Outcome determinacy" checklist row
cites the value too. That paragraph needs a rewrite drafted for Andy, not a silent edit; it
also carries a `schema_cleanup_log #41` citation inside card prose, which item #54 says
should not be there. **DIR.CA.1** is the opposite case — its own Design Rationale already
says "Beat 2 Automatic **positional wager**" and two checklist rows repeat it, so the field
is mislabeled against the card's own text. The other six need no prose change.

**Side findings (not part of #64):**
- **GUI.CA.6** has no `persistence` field at all — absent-field family, same shape as #59.
- The fact that no PublicAct qualifies belongs in **this log entry, not §6.3** — per Andy's
  S157 ruling, §6 is specification, not corpus analysis. If anything goes into §6.3 it is the
  spec line "PositionalWager requires a later beat to exist within the Quarter's resolution
  sequence," which implies the beat-4 consequence without counting anything. Same test applies
  to P1/P2 if either is written into §6.
