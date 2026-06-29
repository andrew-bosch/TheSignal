import re

stub_ca = """---

### GUI.CA.8 — BUILDING INSPECTION *(stub)*
[↑ Covert Operations](#guild-covert-operations)

```python
GUI.CA.8 = Card(
    id      = "GUI.CA.8",  version = "v1.1",
    name    = "Building Inspection",
    tagline = "Condemn an opponent's building via weaponized zoning code.",
    type    = CovertOperation,  subtype = FactionSpecific,  faction = Guild,
    layer   = Territory,  function = Remove,  subject = StructureBlock,
    beat    = 3,  resolution = d100,  threshold = 60,
    cost    = resource.faction(Guild).capacity * 1 + resource.faction(Guild).mandate * 1,
    success = "Remove 1 target Structure Block. Guild gains +1 PS.",
    design_note = "A thematic variant of STD.CA.2 (Demolish). Bribe removed to keep resolution strictly blind via Arbiter."
)
```

"""

stub_pa = """---

### GUI.PA.6 — ASSET TRANSFER *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.6 = Card(
    id      = "GUI.PA.6",  version = "v1.1",
    name    = "Asset Transfer",
    tagline = "Liquidate Guild property into another faction's hands for massive resource injection.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Territory,  function = Modify,  subject = StructureBlock,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Guild).capacity * 1,
    restriction = "district(target).faction(Guild).structure > 0 AND district(target).faction(target_faction).presence > 0",
    success = "Guild removes 1 of their Structure Blocks in target_district and replaces it with 1 Structure Block of the target_faction. Guild gains 3 of the target_faction's native resource from the supply.",
    design_note = "A powerful, legal asset flip. Leverages existing footprint to extract deep foreign resource pockets."
)
```

---

### GUI.PA.7 — EMINENT DOMAIN PETITION *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.7 = Card(
    id      = "GUI.PA.7",  version = "v1.1",
    name    = "Eminent Domain Petition",
    tagline = "Force massive influence into a district to pave the way for expansion.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Territory,  function = Add,  subject = PresenceToken,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Guild).capacity * 2 + resource.faction(Guild).mandate * 1,
    restriction = "district(target).faction(Guild).presence > 0",
    success = "Place 2 Guild Presence Tokens in target_district.",
    design_note = "Requires existing foothold. A blunt-force legal maneuver to crack an opponent's Established status."
)
```

---

### GUI.PA.8 — STRUCTURAL SUBSIDY *(stub)*
[↑ Public Acts](#guild-public-acts)

```python
GUI.PA.8 = Card(
    id      = "GUI.PA.8",  version = "v1.1",
    name    = "Structural Subsidy",
    tagline = "Turn a district's development into a PR engine.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Guild,
    layer   = Standing,  function = Add,  subject = PublicStanding,
    beat    = 4,  resolution = Automatic,  persistence = Permanent,
    cost    = resource.faction(Guild).capacity * 2,
    success = "Places standing condition on target_district: 'Whenever an opponent places a Structure Block here, Guild gains +1 PS.'",
    design_note = "A standing effect. Guild weaponizes other factions' construction efforts to build their own prestige."
)
```

"""

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

# Insert CA.8 before PA.1
match1 = re.search(r'(### GUI\.PA\.1 —)', content)
if match1:
    content = content[:match1.start()] + stub_ca + content[match1.start():]
else:
    print("Could not find GUI.PA.1")

# Insert PA.6,7,8 before MOD.1
match2 = re.search(r'(### GUI\.MOD\.1 —)', content)
if match2:
    content = content[:match2.start()] + stub_pa + content[match2.start():]
else:
    print("Could not find GUI.MOD.1")

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "w") as f:
    f.write(content)

print("Guild stubs injected successfully.")
