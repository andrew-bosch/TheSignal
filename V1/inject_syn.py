import re

stub_content = """---

### SYN.PA.3 — LOBBYIST PUSH *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.3 = Card(
    id      = "SYN.PA.3",  version = "v1.0",
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

### SYN.PA.4 — BAILOUT PACKAGE *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.4 = Card(
    id      = "SYN.PA.4",  version = "v1.0",
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

### SYN.PA.5 — MARKET FREEZE *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.5 = Card(
    id      = "SYN.PA.5",  version = "v1.0",
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

### SYN.PA.6 — PUBLIC MERGER *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.6 = Card(
    id      = "SYN.PA.6",  version = "v1.0",
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

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

match = re.search(r'(### SYN\.MOD\.2 —)', content)
if match:
    content = content[:match.start()] + stub_content + "\n" + content[match.start():]
    print(f"Successfully injected SYN_PA")
else:
    print(f"Failed to find injection point for SYN_PA")

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "w") as f:
    f.write(content)
