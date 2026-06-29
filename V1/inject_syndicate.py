import re

stub_pa = """---

### SYN.PA.4 — CHARITY GALA *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.4 = Card(
    id      = "SYN.PA.4",  version = "v1.0",
    name    = "Charity Gala",
    tagline = "A massive display of wealth that forces rivals to pay up or lose face.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Standing,  function = Add,  subject = PublicStanding,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Syndicate).capital * 2,
    success = "Syndicate gains +2 PS. Every opponent must either pay 1 Capital to the supply or immediately lose 1 PS.",
    design_note = "A public flex of pure capital. Weaponizes Syndicate's wealth to farm PR while forcing opponents to bleed money or take a PR hit just to keep up appearances."
)
```

---

### SYN.PA.5 — PROTECTION RACKET *(stub)*
[↑ Public Acts](#syndicate-public-acts)

```python
SYN.PA.5 = Card(
    id      = "SYN.PA.5",  version = "v1.1",
    name    = "Protection Racket",
    tagline = "Publicly leverage capital to extort physical expansion.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Syndicate,
    layer   = Territory,  function = Remove,  subject = StructureBlock,
    beat    = 4,  resolution = Automatic,  persistence = Transient,
    cost    = resource.faction(Syndicate).capital * 2 + resource.faction(Syndicate).mandate * 1,
    success = "Places a Standing Condition on target_district until Quarter+1: Whenever a Structure Block or Presence Token is placed here, the faction that owns it must pay 1 Capital to Syndicate. If they do not, the structure or token is immediately removed.",
    design_note = "Fixes the covert targeting issue. Physical placement of chips and blocks is public knowledge. Syndicate sets up a toll booth on the district: the owner of the structure pays, or their asset is destroyed."
)
```

"""

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

# Insert before SYN.MOD.1
if "### SYN.PA.4" not in content:
    match1 = re.search(r'(### SYN\.MOD\.2 —)', content)
    if match1:
        content = content[:match1.start()] + stub_pa + content[match1.start():]
    else:
        print("Could not find ### SYN.MOD.2")

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "w") as f:
    f.write(content)

print("Syndicate stubs injection complete.")
