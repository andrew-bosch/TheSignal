import re

stub_ca = """---

### GHO.CA.13 — PHANTOM ACCOUNTS *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

```python
GHO.CA.13 = Card(
    id      = "GHO.CA.13",  version = "v1.1",
    name    = "Phantom Accounts",
    tagline = "Siphon a shadow copy of an opponent's influence-based resource generation.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Economy,  function = Add,  subject = DebriefActionCard,
    beat    = 3,  resolution = d100,  threshold = 50,
    cost    = resource.faction(Ghost).findings * 2,
    success = "Arbiter places 1 DA-02 (PhantomRecord) in Ghost's Dispatch Case. At debrief, Ghost gains district native resources equal to target_faction's influence-based generation.",
    design_note = "A financial twin to SCIF. Instead of generating Modifier cards off of structural density, this converts Findings into a mirrored payout of the target's passive district income."
)
```

---

### GHO.CA.14 — GHOST PROTOCOL *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

```python
GHO.CA.14 = Card(
    id      = "GHO.CA.14",  version = "v1.1",
    name    = "Ghost Protocol",
    tagline = "Completely erase an opponent's operation from existence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Submission,  function = Block,  subject = CovertOperation,
    beat    = 2,  resolution = Automatic,
    cost    = resource.faction(Ghost).findings * 2 + resource.faction(Ghost).exposure * 1 + resource.faction(Ghost).capital * 1 + intel_token * 1,
    success = "The Arbiter invalidates and removes the first Covert Operation submitted by target_faction in Beat 3.",
    design_note = "Massive multi-resource cost to justify an unblockable, blind veto of an opponent's action."
)
```

"""

stub_mod = """---

### GHO.MOD.9 — BURN NOTICE *(stub)*
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

```python
GHO.MOD.9 = Card(
    id      = "GHO.MOD.9",  version = "v1.1",
    name    = "Burn Notice",
    tagline = "Incinerate an opponent's intelligence assets as they try to use them.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Submission,  function = Remove,  subject = ModifierCard,
    trigger = "public_act.submitted(uses_intel_token=True)",
    cost    = resource.faction(Ghost).findings * 1,
    success = "Remove all Modifier cards submitted with the target PA.",
    design_note = "Punishes factions trying to aggressively brute-force a PA using Intel Tokens."
)
```

---

### GHO.MOD.10 — DATA WIPE *(stub)*
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

```python
GHO.MOD.10 = Card(
    id      = "GHO.MOD.10",  version = "v1.1",
    name    = "Data Wipe",
    tagline = "A devastating cyber-attack that cripples a faction's operational hand.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Remove,  subject = FactionHand,
    trigger = "public_act.submitted",
    cost    = resource.faction(Ghost).findings * 2 + intel_token * 1,
    success = "Target faction must discard their entire hand of unplayed CA and PA cards. (They will redraw normally at Debrief).",
    design_note = "Hugely disruptive. Clears their operational runway for the rest of the quarter."
)
```

"""

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

# Insert CA.13 and CA.14 before Ghost - Public Acts
if "### GHO.CA.13" not in content:
    match1 = re.search(r'(### Ghost — Public Acts)', content)
    if match1:
        content = content[:match1.start()] + stub_ca + content[match1.start():]
    else:
        print("Could not find ### Ghost — Public Acts")

# Insert MOD.9 and MOD.10 before Directorate
if "### GHO.MOD.9" not in content:
    match2 = re.search(r'(## Directorate)', content)
    if match2:
        content = content[:match2.start()] + stub_mod + content[match2.start():]
    else:
        print("Could not find ## Directorate")

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "w") as f:
    f.write(content)

print("Ghost stubs injection complete.")
