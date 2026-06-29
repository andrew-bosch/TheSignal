import re

stub_pa = """---

### NET.PA.4 — GRASSROOTS PROTEST *(stub)*
[↑ Public Acts](#network-public-acts)

```python
NET.PA.4 = Card(
    id      = "NET.PA.4",  version = "v1.1",
    name    = "Grassroots Protest",
    tagline = "Mobilize the masses to physically drown out an opponent's influence.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Territory,  function = Remove,  subject = PresenceToken,
    beat    = 4,  resolution = d100,  threshold = 60,
    cost    = resource.faction(Network).exposure * 1 + district_native(target_district) * 1,
    success = "Remove 1 target_faction's Presence Token from target_district. Target faction loses 1 PS. Network gains +1 PS.",
    design_note = "A loud territorial disruption. Burns Exposure and local resources to physically remove an opponent's token while shifting the PR balance."
)
```

---

### NET.PA.5 — VIRAL OUTRAGE *(stub)*
[↑ Public Acts](#network-public-acts)

```python
NET.PA.5 = Card(
    id      = "NET.PA.5",  version = "v1.1",
    name    = "Viral Outrage",
    tagline = "Weaponize an opponent's own assets against them to tank their standing.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Standing,  function = Remove,  subject = PublicStanding,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Network).exposure * 2 + resource.faction(target_faction).native * 1,
    success = "Target faction loses 3 Public Standing. Network gains +1 PS.",
    design_note = "Pure PR assassination. Network burns the opponent's own native resource to fuel the smear campaign."
)
```

---

### NET.PA.6 — CROWDFUNDING CAMPAIGN *(stub)*
[↑ Public Acts](#network-public-acts)

```python
NET.PA.6 = Card(
    id      = "NET.PA.6",  version = "v1.1",
    name    = "Crowdfunding Campaign",
    tagline = "Convert public goodwill into hard resources.",
    type    = PublicAct,  subtype = FactionSpecific,  faction = Network,
    layer   = Economy,  function = Add,  subject = AnyResource,
    beat    = 4,  resolution = Automatic,
    cost    = resource.faction(Network).exposure * 1,
    success = "Network names a resource type. Network gains 1 of that resource type for every 4 points of positive Public Standing they currently have.",
    design_note = "Network's economy is driven by their audience. This rewards them for maintaining a high, positive PS track by converting it into any resource they need."
)
```

"""

stub_mod = """---

### NET.MOD.11 — CANCEL CAMPAIGN *(stub)*
[↑ Modifier & React Cards](#network-modifier-and-react-cards)

```python
NET.MOD.11 = Card(
    id      = "NET.MOD.11",  version = "v1.1",
    name    = "Cancel Campaign",
    tagline = "Hijack the narrative of an opponent's public action.",
    type    = ModReactCard,  subtype = FactionSpecific,  faction = Network,
    layer   = Standing,  function = Remove,  subject = PublicStanding,
    trigger = "public_act.submitted",
    cost    = resource.faction(Network).exposure * 1,
    success = "The target faction's PA resolves normally, but their PS is reduced by 2 due to extreme public backlash. Network gains 1 Exposure.",
    design_note = "Network doesn't block the legal act (Directorate's job). Instead, Network weaponizes the public's reaction to the act, ensuring the target pays a heavy PR price for whatever they just did."
)
```

"""

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "r") as f:
    content = f.read()

# Insert before NET.MOD.1
if "### NET.PA.4" not in content:
    match1 = re.search(r'(### NET\.MOD\.1 —)', content)
    if match1:
        content = content[:match1.start()] + stub_pa + content[match1.start():]
    else:
        print("Could not find ### NET.MOD.1")

if "### NET.MOD.11" not in content:
    match2 = re.search(r'(## Syndicate)', content)
    if match2:
        content = content[:match2.start()] + stub_mod + content[match2.start():]
    else:
        print("Could not find ## Syndicate")

with open("/home/abosch/Projects/TheSignal/V1/04___Card_System.md", "w") as f:
    f.write(content)

print("Network stubs injection complete.")
