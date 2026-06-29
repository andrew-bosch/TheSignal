import re

ghost_ca_15 = """---

### GHO.CA.15 — ROUTING OVERRIDE *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

```python
GHO.CA.15 = Card(
    id      = "GHO.CA.15",  version = "v1.0",
    name    = "Routing Override",
    tagline = "Blindly intercept and redirect an opponent's covert operation.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Corrupt,  subject = TargetProfile,
    beat    = 2,  resolution = Automatic,
    cost    = resource.faction(Ghost).findings * 1 + intel_token * 1,
    success = "Ghost corrupts the first CA in target faction's Beat 3 resolution queue if it matches Ghost's specified parameters.",
    arbiter_note = "At Covert Dispatch, Ghost writes a target field (e.g., 'target_district') and expected value (e.g., 'Core'), plus a replacement value (e.g., 'Baryo'), in their Target Profile freeform space. At Beat 2: ARBITER checks target faction's first CA in the ARG. If that CA's Target Profile contains the exact field and value Ghost named, ARBITER silently crosses it out and writes Ghost's new value. If it does not match, Ghost's operation fizzles. The target faction executes their CA at Beat 3 against the new corrupted target.",
    design_note = "Beat 2 positional wager against a Beat 3 CA. Ghost must correctly predict a parameter of the opponent's first queued operation. The corruption is entirely silent until the operation resolves at Beat 3."
)
```

"""

ghost_mod_11 = """---

### GHO.MOD.11 — MANUFACTURED EVIDENCE *(stub)*
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

```python
GHO.MOD.11 = Card(
    id      = "GHO.MOD.11",  version = "v1.0",
    name    = "Manufactured Evidence",
    tagline = "Hijack a public act before the ink dries.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Corrupt,  subject = TargetProfile,
    trigger = "public_act.placed_with_target_profile",
    cost    = resource.faction(Ghost).findings * 1 + resource.faction(Ghost).exposure * 1,
    success = "Replaces the PA's original Target Profile with a new Target Profile provided by Ghost.",
    arbiter_note = "Reacts at Art 03 §9.2.0 when an opponent places a PA with a face-down Target Profile. Ghost announces the React, discards the opponent's original face-down Target Profile, and places their own face-down Target Profile on the PA. At Beat 4 Apex Check, the PA resolves against Ghost's corrupted targets.",
    design_note = "A public hijacking. The table sees Ghost swap the paperwork, but because Target Profiles are placed face-down, no one (not even the table) knows what Ghost changed the target to until Beat 4."
)
```

"""

net_mod_12 = """---

### NET.MOD.12 — DOX TARGET *(stub)*
[↑ Modifier & React Cards](#network-modifier-and-react-cards)

```python
NET.MOD.12 = Card(
    id      = "NET.MOD.12",  version = "v1.0",
    name    = "Dox Target",
    tagline = "Broadcast their intended target before they are ready.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = TargetProfile,
    trigger = "public_act.placed_with_target_profile",
    cost    = resource.faction(Network).exposure * 1,
    success = "The Target Profile is immediately flipped face-up for the table to see.",
    arbiter_note = "Reacts at Art 03 §9.2.0 when an opponent places a PA with a face-down Target Profile. Network announces the React and spends 1 Exposure. The Target Profile is flipped face-up immediately. The PA is locked in and will resolve normally at Beat 4, but the target is now public knowledge for the rest of the round.",
    design_note = "A direct counter to hidden targets. By spending 1 Exposure, Network strips the opponent's tactical ambiguity for the entire round. This allows other factions to prepare defenses or negotiate before Beat 4."
)
```

"""

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

# Insert GHO.CA.15 at the end of Ghost CA section
if "### GHO.CA.15" not in content:
    match1 = re.search(r'(### Ghost — FULL TAKE.*?```\n)', content, flags=re.DOTALL)
    if match1:
        content = content[:match1.end()] + "\n" + ghost_ca_15 + content[match1.end():]
    else:
        print("Could not find Ghost CA 14 location")

# Insert GHO.MOD.11 at the end of Ghost MOD section
if "### GHO.MOD.11" not in content:
    match2 = re.search(r'(### GHO\.MOD\.10 — DATA WIPE.*?```\n)', content, flags=re.DOTALL)
    if match2:
        content = content[:match2.end()] + "\n" + ghost_mod_11 + content[match2.end():]
    else:
        print("Could not find GHO.MOD.10 location")

# Insert NET.MOD.12 at the end of Network MOD section
if "### NET.MOD.12" not in content:
    match3 = re.search(r'(### NET\.MOD\.11 — CANCEL CAMPAIGN.*?```\n)', content, flags=re.DOTALL)
    if match3:
        content = content[:match3.end()] + "\n" + net_mod_12 + content[match3.end():]
    else:
        print("Could not find NET.MOD.11 location")

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "w") as f:
    f.write(content)

print("Injection complete.")
