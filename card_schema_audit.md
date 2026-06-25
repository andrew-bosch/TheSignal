# Card Schema and Enum Validation Audit Report
## THE SIGNAL P1 — Paper Prototype (Artifact 04)

This report validates the card specifications defined in [04___Card_System.md](file:///home/abosch/Projects/TheSignal/V1/04___Card_System.md) against the class definitions (§6.1), data dictionary (§6.2), and enum vocabularies (§6.3).

---

### 1. Audit Summary

* **Total Card Specifications Scanned:** 92
* **Schema Conformance Rate:** High (All core functional fields present)
* **Enum Violations Found:** 14 (Excluding modifier card placeholders pending their own schema)
* **Data Dictionary Cost Violations:** 0 (All costs use valid fungible resources)
* **ElectPlayer Fields Consistency:** 100% compliant (no mismatched `on_accept`/`on_decline` fields)

---

### 2. Key Findings & Enum Violations

The audit initially flagged deviations which have been resolved or deferred per alignment on modifier card schemas:

| Card ID / Line | Field | Status / Value as Written | Resolution / Description |
|----------------|-------|--------------------------|--------------------------|
| **STD.CA.11** (L5417)<br>*Tort Interference* | `persistence` | ✅ **Resolved** | Updated `persistence` to `Permanent` and moved the condition to `persistence_condition = not (game.end OR Accord(named).breach_by_party)`. |
| **Overture** (L8833) | `subtype` | `Instant` | *Deferred:* Under §11.1, modifier card taxonomy and schemas are excluded and will be dealt with in a future modifier card schema pass. |
| | `layer` | `None` | *Deferred:* Taxonomy fields should be omitted in the future. |
| **NET.MOD.1** (L8976)<br>*Signal Break* | `type`/`subtype` | `ModifierCard`/`React` | *Deferred:* Pending modifier card schema pass (04-n4). |
| **GUI.MOD.1** (L9022)<br>*Return to Site* | `type`/`subtype` | `ModifierCard`/`React` | *Deferred:* Pending modifier card schema pass (04-n4). |
| **GHO.MOD.1** (L9082)<br>*Clarify Misinformation* | `type`/`subtype` | `ModifierCard`/`React` | *Deferred:* Pending modifier card schema pass (04-n4). |
| | `resolution` | `Prediction` | *Deferred:* Guessing-resolution logic matches notes. |

#### Stubs / Placeholders:
* **Accord Leverage Stub** (L8235): uses `type = ModifierCard` and `subtype = Instant` (deferred to modifier card schema pass).
* **Reputational Strike Stub** (L8922): uses `type = ModifierCard` and `subtype = React` (deferred to modifier card schema pass).

---

### 3. Schema & Data Dictionary Completeness Analysis

#### Optional/Default Fields
The constructor of the `Card` class defines several fields that are logically optional (defaulting to `None`). Across the 92 parsed cards, these fields are consistently omitted when not in use:
* **`boost` and `ps_framing`:** Omitted in the vast majority of covert operations that do not scale with additional resources or affect public standing.
* **`persistence_condition` and `persistence_effect`:** Correctly omitted for all non-`Permanent` cards.
* **`doctrine_mod`:** Omitted for operations that do not target other factions.

#### Identity Field Inconsistency (`card_id` vs `id`)
* **Standard Cards** (e.g. `STD.CA.1` to `STD.CA.10`) populate `id` with legacy sequence integers (e.g. `id = 1`) and omit `card_id`.
* **Faction Cards** (e.g. `GHO.CA.1`) populate `card_id` with the canonical string ID (e.g. `card_id = "GHO.CA.1"`) and omit the legacy `id`.
* This matches the Data Dictionary description, which classifies `id` as a legacy integer preserved for traceability.
