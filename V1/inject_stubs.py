import re

stubs = {
    "GUI_CA": """---

### GUI.CA.8 — BUILDING INSPECTION *(stub)*
[↑ Covert Operations](#guild-covert-operations)

```python
GUI.CA.8 = Card(
    id      = "GUI.CA.8",  version = "v1.0",
    name    = "Building Inspection",
    tagline = "Use zoning bureaucracy to audit an opponent's covert play.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,
    layer   = Information,  function = Reveal,  subject = CovertOperation,
    beat    = 3,  resolution = d100,  threshold = 60,
    cost    = resource.faction(Guild).capacity * 1 + resource.faction(Guild).mandate * 1,
    success = "Reveal target covert operation. Target must pay 1 Capacity or the operation is cancelled.",
    design_note = "Guild information/disruption layer. Using red tape as a weapon."
)
```
""",
    "GUI_PA": """---

### GUI.PA.6 — PUBLIC WORKS EXHIBITION *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.6 = Card(
    id      = "GUI.PA.6",  version = "v1.0",
    name    = "Public Works Exhibition",
    tagline = "A massive display of construction prowess that yields high PS.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Standing,  function = Add,  subject = PublicStanding,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Guild).capacity * 3,
    success = "faction(Guild).standing += 4",
    design_note = "Heavy Capacity investment for pure PS."
)
```

---

### GUI.PA.7 — EMINENT DOMAIN PETITION *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.7 = Card(
    id      = "GUI.PA.7",  version = "v1.0",
    name    = "Eminent Domain Petition",
    tagline = "Force a district into contention to pave the way for expansion.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Territory,  function = Modify,  subject = District,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Guild).capacity * 2 + resource.faction(Guild).mandate * 1,
    success = "arbiter.place(contested_marker, district=target_district)",
    design_note = "Allows Guild to legally break an opponent's Established status."
)
```

---

### GUI.PA.8 — STRUCTURAL SUBSIDY *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.8 = Card(
    id      = "GUI.PA.8",  version = "v1.0",
    name    = "Structural Subsidy",
    tagline = "Build a structure for an opponent in exchange for diplomatic leverage.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Economy,  function = Add,  subject = AccordAgreement,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Guild).capacity * 2,
    success = "target_faction gains 1 structure in target_district. Guild gains 1 AccordAgreement with target_faction and +2 PS.",
    design_note = "The ultimate 'we build for everyone' flex. Trading concrete for Accords."
)
```
""",
    "GHO_CA": """---

### GHO.CA.9 — DEAD DROP *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

```python
GHO.CA.9 = Card(
    id      = "GHO.CA.9",  version = "v1.0",
    name    = "Dead Drop",
    tagline = "Covertly transfer Intel without leaving a trace.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Modify,  subject = IntelToken,
    beat    = 3,  resolution = Automatic,
    cost    = resource.faction(Ghost).findings * 1,
    success = "game.transfer(IntelToken, count=1, from=Ghost, to=target_faction)",
    design_note = "Allows Ghost to feed intel to proxies silently."
)
```

---

### GHO.CA.10 — GHOST PROTOCOL *(stub)*
[↑ Covert Operations](#ghost-covert-operations)

```python
GHO.CA.10 = Card(
    id      = "GHO.CA.10",  version = "v1.0",
    name    = "Ghost Protocol",
    tagline = "Completely erase an opponent's operation from existence.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Submission,  function = Remove,  subject = CovertOperation,
    beat    = 3,  resolution = d100,  threshold = 40,
    cost    = resource.faction(Ghost).findings * 2 + resource.faction(Ghost).exposure * 1,
    success = "Remove target CovertOp from the dispatch before resolution. Resources are not refunded.",
    design_note = "High-tier disruption. Prevents an action from ever occurring."
)
```
""",
    "GHO_MOD": """---

### GHO.MOD.9 — BURN NOTICE *(stub)*
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

```python
GHO.MOD.9 = Card(
    id      = "GHO.MOD.9",  version = "v1.0",
    name    = "Burn Notice",
    tagline = "Incinerate an opponent's intelligence assets as they try to use them.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Information,  function = Remove,  subject = IntelToken,
    trigger = "public_act.submitted",
    cost    = resource.faction(Ghost).findings * 1,
    success = "Target faction loses 1 Intel Token. If they cannot, their PA suffers -20 boost.",
    design_note = "Punishing factions that rely on Intel without Ghost's permission."
)
```

---

### GHO.MOD.10 — PHANTOM SUBMITTER *(stub)*
[↑ Modifier & React Cards](#ghost-modifier-and-react-cards)

```python
GHO.MOD.10 = Card(
    id      = "GHO.MOD.10",  version = "v1.0",
    name    = "Phantom Submitter",
    tagline = "Hijack the critical success of an opponent's operation.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Ghost,
    layer   = Resolution,  function = Modify,  subject = CovertOperation,
    trigger = "covert_op.crit_success",
    cost    = resource.faction(Ghost).findings * 2,
    success = "The target faction receives the standard success effect. Ghost receives the crit success bonus instead of the target.",
    design_note = "Ghost steals the upside of brilliant opponent plays."
)
```
""",
    "DIR_PA": """---

### DIR.PA.8 — MARTIAL LAW DECLARATION *(stub)*
[↑ Public Acts](#directorate-public-acts)

```python
DIR.PA.8 = Card(
    id      = "DIR.PA.8",  version = "v1.0",
    name    = "Martial Law Declaration",
    tagline = "Freeze all presence placement in a district.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Modify,  subject = District,
    beat    = 4,  resolution = Automatic,  persistence = Permanent,
    cost    = resource.faction(Directorate).mandate * 3 + resource.faction(Directorate).capital * 1,
    success = "Places standing condition: No faction may place presence chips in target_district.",
    design_note = "The ultimate territorial lockdown."
)
```
""",
    "DIR_MOD": """---

### DIR.MOD.9 — CURFEW ENFORCEMENT *(stub)*
[↑ Modifier & React Cards](#directorate-modifier-and-react-cards)

```python
DIR.MOD.9 = Card(
    id      = "DIR.MOD.9",  version = "v1.0",
    name    = "Curfew Enforcement",
    tagline = "Punish covert operations occurring in Directorate-controlled zones.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Resolution,  function = Modify,  subject = CovertOperation,
    trigger = "covert_op.submitted(district=Established)",
    cost    = resource.faction(Directorate).mandate * 1,
    success = "Target covert operation suffers -30 to its threshold.",
    design_note = "Makes operating in DIR space mathematically disastrous."
)
```
""",
    "NET_PA": """---

### NET.PA.4 — VIRAL OUTRAGE *(stub)*
[↑ Public Acts](#network-public-acts)

```python
NET.PA.4 = Card(
    id      = "NET.PA.4",  version = "v1.0",
    name    = "Viral Outrage",
    tagline = "Weaponize public anger against a faction's structural footprint.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Standing,  function = Remove,  subject = PublicStanding,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Network).exposure * 2,
    success = "Target faction loses 1 PS for every Structure Block they own in the target district.",
    design_note = "Punishes heavy builders (Guild, Directorate) using their own footprint against them."
)
```

---

### NET.PA.5 — OPEN SOURCE INITIATIVE *(stub)*
[↑ Public Acts](#network-public-acts)

```python
NET.PA.5 = Card(
    id      = "NET.PA.5",  version = "v1.0",
    name    = "Open Source Initiative",
    tagline = "Force all covert operations into the public light.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Information,  function = Reveal,  subject = CovertOperation,
    beat    = 4,  resolution = Automatic,  persistence = Immediate,
    cost    = resource.faction(Network).exposure * 1 + resource.faction(Network).findings * 1,
    success = "All factions must immediately reveal the targets of their dispatched Covert Ops.",
    design_note = "Network's ultimate transparency play. Tears down everyone's operational security."
)
```

---

### NET.PA.6 — PLATFORM DEPLATFORMING *(stub)*
[↑ Public Acts](#network-public-acts)

```python
NET.PA.6 = Card(
    id      = "NET.PA.6",  version = "v1.0",
    name    = "Platform Deplatforming",
    tagline = "Revoke a faction's ability to speak publicly.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Submission,  function = RemoveRestriction,  subject = PublicAct,
    beat    = 4,  resolution = Automatic,  persistence = Seasonal,
    cost    = resource.faction(Network).exposure * 3,
    success = "Target faction cannot submit Public Acts next Quarter.",
    design_note = "Total social silencing. A devastating PR execution."
)
```
""",
    "NET_MOD": """---

### NET.MOD.11 — DDOS ATTACK *(stub)*
[↑ Modifier & React Cards](#network-modifier-and-react-cards)

```python
NET.MOD.11 = Card(
    id      = "NET.MOD.11",  version = "v1.0",
    name    = "DDoS Attack",
    tagline = "Flood an opponent's operation with junk data.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Network,
    layer   = Resolution,  function = Modify,  subject = CovertOperation,
    trigger = "covert_op.submitted",
    cost    = resource.faction(Network).exposure * 1,
    success = "Target covert operation suffers -20 threshold.",
    design_note = "Standard reactive interference."
)
```

---

### NET.MOD.12 — TREND HIJACK *(stub)*
[↑ Modifier & React Cards](#network-modifier-and-react-cards)

```python
NET.MOD.12 = Card(
    id      = "NET.MOD.12",  version = "v1.0",
    name    = "Trend Hijack",
    tagline = "Steal the spotlight from an opponent's public success.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Network,
    layer   = Standing,  function = Add,  subject = PublicStanding,
    trigger = "public_act.success",
    cost    = resource.faction(Network).exposure * 2,
    success = "Network gains +2 PS. The target faction's PS reward is halved (rounded down).",
    design_note = "Parasitic PR. Network rides the coattails of others' announcements."
)
```
""",
    "SYN_PA": """---

### SYN.PA.2 — LOBBYIST PUSH *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.2 = Card(
    id      = "SYN.PA.2",  version = "v1.0",
    name    = "Lobbyist Push",
    tagline = "Blunt-force PR generation via heavy spending.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Standing,  function = Add,  subject = PublicStanding,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Syndicate).capital * 3,
    success = "faction(Syndicate).standing += 3",
    design_note = "Direct conversion of Capital to PS."
)
```

---

### SYN.PA.3 — BAILOUT PACKAGE *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.3 = Card(
    id      = "SYN.PA.3",  version = "v1.0",
    name    = "Bailout Package",
    tagline = "Save a bankrupt faction in exchange for total compliance.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Add,  subject = AccordAgreement,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Syndicate).capital * 2,
    restriction = "faction(target).capital == 0",
    success = "Target faction receives 2 Capital. Syndicate receives 1 un-corruptible AccordAgreement with target.",
    design_note = "Predatory lending at its finest."
)
```

---

### SYN.PA.4 — MARKET FREEZE *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.4 = Card(
    id      = "SYN.PA.4",  version = "v1.0",
    name    = "Market Freeze",
    tagline = "Halt all covert spending.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Economy,  function = Modify,  subject = CovertOperation,
    beat    = 4,  resolution = Automatic,  persistence = Seasonal,
    cost    = resource.faction(Syndicate).capital * 3 + resource.faction(Syndicate).mandate * 1,
    success = "Next Quarter, Covert Operations that cost Capital cannot be dispatched.",
    design_note = "Economic lockdown that cripples factions relying on money for covert play."
)
```

---

### SYN.PA.5 — PUBLIC MERGER *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.5 = Card(
    id      = "SYN.PA.5",  version = "v1.0",
    name    = "Public Merger",
    tagline = "Buy an opponent's structure in broad daylight.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Modify,  subject = StructureBlock,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Syndicate).capital * 4 + resource.faction(Syndicate).exposure * 1,
    success = "Target faction receives 4 Capital. Syndicate takes ownership of target Structure Block.",
    design_note = "Unblockable hostile takeover via overwhelming Capital application."
)
```
"""
}

# We will inject these before the start of the next section.
injections = [
    ("GUI_CA", r'(### GUI\.PA\.1 —)'),
    ("GUI_PA", r'(### GUI\.MOD\.1 —)'),
    ("GHO_CA", r'(### GHO\.PA\.1 —)'),
    ("GHO_MOD", r'(### DIR\.CA\.1 —)'),
    ("DIR_PA", r'(### DIR\.MOD\.1 —)'),
    ("DIR_MOD", r'(### NET\.CA\.1 —)'),
    ("NET_PA", r'(### NET\.MOD\.1 —)'),
    ("NET_MOD", r'(### SYN\.CA\.1 —)'),
    ("SYN_PA", r'(### SYN\.MOD\.1 —)')
]

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

for key, regex_marker in injections:
    stub_content = stubs[key]
    # find the marker
    match = re.search(regex_marker, content)
    if match:
        # inject just before the marker
        content = content[:match.start()] + stub_content + "\n" + content[match.start():]
        print(f"Successfully injected {key}")
    else:
        print(f"Failed to find injection point for {key}")

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "w") as f:
    f.write(content)
