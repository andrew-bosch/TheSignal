# Network Card Set Re-Audit — S156 (PM05 09-16 step 4)

**Status:** First-pass analysis, awaiting Andy checkpoint before the final faction (Syndicate) and step 5.
**Trigger to delete:** once findings are triaged via the consolidated review (PM05 09-17) and the faction verdict is logged to PM02.
**Denominator:** 14 Network operations (8 CA + 6 PA) + 30 Network MOD (12 Action, 4 Battle, **14 React — most in the game**) + universal STD CA/PA pool. STD ring mods conditional.
**Substrate:** `card_body` / `v_card_body` / `card_status` / `card_checklist`, re-derived, checked against `card_analysis_summary_S119-128.md` (S123, 04-n90) — baseline treated as an S119 snapshot, re-validated.
**Doctrine source:** Art 04 Part1_Core §5a (Network); win = *wide Presence, Baryo outward.* "No one decides this in the dark." Broadcast-derived presence; Exposure economy; modifier-deck self-feed is the "true engine."

---

## Dimension verdicts

| Dimension | Verdict | Note |
|-----------|---------|------|
| Deck feel | ✓ (was "Partial/L1 gap" at S123) | Distributed, reactive (14 React), **increasingly loud** — the self-feed that was unbuilt at L1 now exists. Broadcaster identity strong (highest Reveal concentration: CA.1/3, PA.1/3, MOD.12). |
| Doctrine coherence | ✓ Strong | Broadcaster/transparency; credibility-as-capital (CA.6 Sacrifice: PS→Intel); reactive spread. |
| Layer coverage | ✓ | Information (broadcaster) + Economy (Exposure/Intel/ModifierCard/AnyResource) + Territory (add/remove/redirect) + Standing + Submission. Resolution empty — doctrinally correct (Network broadcasts, doesn't manipulate dice). |
| Win-path support | ✓ (was a gap at S123) | Reactive presence engine + self-feed make Q6–8 self-sustaining. See below. |
| §9.2 economics | ◐ **cross-ceiling exception, Ghost-gated** | Network is the one faction with operational cross-resource ceilings — but they're **Findings-gated** (Ghost's native), now across CA.1/2/4/8. Degrades toward mono in Ghost-absent games. |
| **Implied strategies** | mostly THICK | Largest baseline gap (self-feed) closed; tripwire the one to verify. |
| **Leverageable strategies** | rich, snowballing | Self-feeding React engine; standing warfare; disclosure control. |

---

## Win path — reactive engine now self-sustaining (primary finding)

Win = wide Presence, Baryo outward. At S123 this "structurally depended on STD.CA.3/CA.8" and the modifier self-feed was "largely unbuilt — largest §5a gap." Both are now addressed:

- **Broadcast-derived presence (reactive expansion), BUILT:** React MOD.1/4/5/6/8 add presence triggered by public/broadcast events — presence spreads as the city gets loud, *reactively* (doctrinally correct: "how far the voice carries," not deliberate placement). Plus CA.5 (Baryo entry), PA.2 (consolidate established), and the STD pool.
- **Modifier-deck self-feed ("true engine"), BUILT:** MOD.7 ("the louder the city gets, the more they listen"), MOD.9 ("conflict = the ultimate engagement metric"), MOD.14 ("the audience grows, so does the signal") all Add ModifierCard; CA.2 makes Exposure self-sustaining. Each Quarter the deck grows → more React triggers → louder → more presence/standing. The Q6–8 self-sustaining loop §5a describes now actually exists.
- **Territorial response, ADDED:** PA.4 (remove presence — "drown out"), MOD.10 (redirect — "they sent operatives, we sent neighbors"), CA.8 (redirect deployment). Baseline's "zero territorial response" — closed.

---

## §9.2 economics — the Ghost-gated cross-ceiling (validation finding)

Network is the **only faction with genuine operational cross-resource ceilings**, but they are **Findings-gated** — and *more* so than baseline recorded: CA.1 (Exposure+Findings), CA.2 (Findings, mono-but-Ghost-native), CA.4 (Exposure+Findings), CA.8 (Exposure+Findings). Network's *core broadcaster identity cards* — expose (CA.1), extend interference (CA.4), plant a false story (CA.8) — structurally require **Ghost's native resource**.

- Doctrinally coherent: transparency runs on raw intelligence; Network needs Findings to have something to broadcast.
- But it means Network's ceiling degrades toward mono in **Ghost-absent games** (2–4p without Ghost), and creates a hard Network→Ghost dependency (acquired via holding Ghost-native districts, free trade Art 03 §11.0, or 4:1 conversion). **Design question (04-n126, still live): is Network intended to be structurally Ghost-linked, and is the Ghost-absent degradation acceptable?** Step-5 relevant.

**Also (persists from baseline):** NET.PA.3 Live Coverage — Seasonal covert-disable at mono Exposure×2 is a borderline §9.2 inversion, and toothless vs Guild specifically (no covert ops to forfeit). Validate in the §9.2 pass.

---

## Implied strategies — §5a claims rated

| §5a claim | Rating | Evidence |
|-----------|--------|----------|
| Broadcast-derived (reactive) presence | **THICK (now)** | React MOD.1/4/5/6/8. |
| Modifier-deck self-feed = "true engine" | **THICK (now)** | MOD.7/9/14 + CA.2. **Largest baseline gap — CLOSED.** |
| Exposure economy + standing damage | **THICK** | CA.2 (Exposure), CA.7/PA.5/MOD.2/3/11 (standing). |
| Credibility-as-capital | **PRESENT** | CA.6 Sacrifice (PS→Intel). |
| Tripwire (declared public condition → Exposure+standing+presence on fire) | **VERIFY** | No dedicated tripwire *card* visible; the React engine covers much of the behavior. Confirm the tripwire declaration mechanic is implemented as a rule/procedure or flag as an unbuilt §5a element — the one potentially-open Network gap. |

---

## Leverageable strategies — emergent (feed step-5 cross-faction)

**Faction-internal:**
1. **Self-feeding snowball.** MOD.7/9/14 grow the deck → more React presence/standing each Quarter → Q6–8 runaway "loudness." The signature Network engine; rewards surviving to late game.
2. **Standing warfare.** CA.7, PA.5 (vr4), MOD.2/3/11 (vr4) broadcast-driven standing damage — and MOD.3 defends Network's *own* standing reactively. Stacks with STD.PA.4/PA.5 (accuse/attribute) for a heavy PS-attack lane.
3. **Total disclosure/reveal control.** CA.1/3 (reveal covert ops), PA.1 (attribution), PA.3 (reveal hand), MOD.12 (reveal target) — Network sees and exposes everything; the informational counter to Ghost.

**Cross-faction (step-5):**
4. **Network↔Ghost (dependency + rivalry).** Network *needs* Ghost's Findings for its core cards (trade/proxy), yet Ghost is its informational rival (CA.1/3 expose covert ops, PA.3 opens hands). A supply relationship laid over an attack vector.
5. **Network↔Syndicate proxy funding (§5a "lateral bypass around Directorate visibility").** PA.6 (convert goodwill → AnyResource) and the shadow funding relationship — a step-5 economic link neither announces.

---

## Flags (→ running log `audit_findings_log_S156.md`)

- ~~[verify] Tripwire mechanic~~ → ✅ **RESOLVED (S156, PM02 L355):** "tripwire" was stale pre-ModReact terminology, not a missing mechanic. §5a Network rewritten to center the React modifier engine; tripwire bullet dropped. No card/procedure to build.
- **[design/§9.2]** Structural Findings-dependency (Ghost-linked) across CA.1/2/4/8 — Network's core cards need Ghost's native resource; degrades in Ghost-absent games (04-n126). Intended? Step-5.
- **[design/§9.2]** NET.PA.3 borderline inversion (Seasonal covert-disable at mono Exposure) + toothless vs Guild. Validate in §9.2 pass.
- **[schema/stub]** NET.CA.8 Fake News (`cost` amount NULL; known stub, 04-n217); NET.MOD.3 (`cost_primary_amount` NULL).

---

## Convergence with S123 baseline

- Deck feel — **upgraded** Partial/L1-gap → ✓ (self-feed built).
- Doctrine ✓ — **agree, re-derived.**
- **Modifier self-feed "true engine" (largest §5a gap)** — **CLOSED** (MOD.7/9/14 + CA.2). Headline delta.
- **Win-path expansion gap** — **addressed** (React presence engine MOD.1/4/5/6/8; less STD-dependent than baseline).
- **No territorial response** — **CLOSED** (PA.4, MOD.10, CA.8).
- **Findings-gated cross-ceiling (04-n126)** — **persists and deepened** (CA.1/2/4/8); elevated to a step-5 Network↔Ghost concern.
- **NET.PA.3 inversion / anti-Guild toothlessness** — **persists**; validate in §9.2 pass.
