# THE SIGNAL — agy Outbound Consulting Report

*Pruned S130 — report ingested. Ready for next agy report.*

## 1. Execution of the §9.2 Cross-Resource Ceiling Pass
A major sweep was executed to fix the §9.2 cross-resource ceiling gap (where factions were playing ceiling-power cards at purely mono-native costs).

**Specific Card Cost Adjustments:** High-power cards across four factions were converted from mono-native costs to cross-faction (or district-native) costs to force the intended economic tension:
*   **Ghost:** Several high-power abilities now explicitly require `Capacity` or `Capital` alongside `Findings`.
*   **Directorate:** PAs and CAs now require `Findings`, `Exposure`, or `Capital` alongside `Mandate`.
*   **Network:** `NET.CA.5`, `NET.PA.1`, `NET.PA.3`, `NET.PA.5`, and `NET.MOD.9` now explicitly demand cross-resources like `Capital`, `Findings`, or `district_native` resources alongside `Exposure`.
*   **Syndicate:** `SYN.CA.3`, `SYN.CA.4`, `SYN.CA.5`, `SYN.MOD.5`, `SYN.MOD.8`, and `SYN.PA.5` were heavily restructured to require `Findings`, `Exposure`, or `Mandate` alongside `Capital` (reflecting Syndicate outsourcing or leveraging other factions' domains).

**Status:** The §9.2 gap identified in `04-n118/119/123/126` has been successfully implemented into the Art 04 DB for Ghost, Directorate, Network, and Syndicate. Guild's cross-faction costs should be reviewed as part of their missing 4 cards.

## 2. Phase 1 Design Strategy: Filling the Deficit
We have mathematically validated that 4 out of 5 factions currently fail to hit the 53-card minimum draftable palette (Standard=25, requiring 28 faction-specific cards).

**Strategy for Claude/Opus:**
1. **Variations:** To hit the floor without unnecessarily bloating mechanical complexity, the deficits for **Network (-3), Syndicate (-4), and Guild (-4)** should primarily be filled by designing **variations** of their existing PA and Mod cards (e.g., inverted triggers, alternate costs, or shifted targets).
2. **Shared Action Spaces:** Explore the same action space across different factions, implemented through their unique doctrines. (For example, how `NET.MOD.12` and `GHO.MOD.11` both manipulate Target Profiles, but one uses public doxing and the other uses blind corruption).
3. **Directorate (-6)** may require more substantial net-new design due to the larger gap, making Strategy 2 particularly useful for them (e.g., Directorate surveillance cards that also play in the Target Profile space).
