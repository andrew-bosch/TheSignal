import re

stub_pa = """---

### DIR.PA.7 — CURFEW *(stub)*
[↑ Public Acts](#directorate-public-acts)

```python
DIR.PA.7 = Card(
    id      = "DIR.PA.7",  version = "v1.1",
    name    = "Curfew",
    tagline = "Lock down a district to freeze physical movement.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Territory,  function = Block,  subject = DeploymentMarker,
    beat    = 4,  resolution = Automatic,  persistence = Transient,
    cost    = resource.faction(Directorate).mandate * 2,
    success = "Places a Standing Condition on target_district until the end of Quarter+1: Deployment Markers cannot be moved into this district.",
    design_note = "A massive territorial denial tool. Blocks physical movement (which is public and enforceable) rather than targeting blind covert space."
)
```

---

### DIR.PA.8 — SUBPOENA *(stub)*
[↑ Public Acts](#directorate-public-acts)

```python
DIR.PA.8 = Card(
    id      = "DIR.PA.8",  version = "v1.2",
    name    = "Subpoena",
    tagline = "Weaponize target-keyed intelligence into a public audit that bleeds an opponent's finances or reputation.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Directorate,
    layer   = Economy,  function = Remove,  subject = Capital,
    beat    = 4,  resolution = d100,  threshold = 40,
    cost    = resource.faction(Directorate).mandate * 1 + intel_token(faction=target_faction) * 1,
    success = "Target faction must pay 2 Capital or 2 of their Native Resource to the supply. If they do not, they lose 2 Public Standing.",
    design_note = "Cost uses a faction-keyed Intel Token: Directorate 'found out something' that justifies the legal action. The target has the choice to pay the fine or take the PR hit."
)
```

"""

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

# Insert before DIR.MOD.1
if "### DIR.PA.7" not in content:
    match1 = re.search(r'(### DIR\.MOD\.1 —)', content)
    if match1:
        content = content[:match1.start()] + stub_pa + content[match1.start():]
    else:
        print("Could not find ### DIR.MOD.1")

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "w") as f:
    f.write(content)

print("Directorate stubs injection complete.")
