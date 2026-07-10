import math

CX, CY = 400, -200
R1 = 250
R2 = 700

factions = [
    ("GUILD", "#d4622a"),
    ("GHOST", "#6a9978"),
    ("DIRECTORATE", "#3a6ea8"),
    ("NETWORK", "#39d353"),
    ("SYNDICATE", "#c9a84c")
]

rings = [
    {
        "file": "V1/District_Tile_Ring1_Spec.svg",
        "angle": 22,
        "w_angle": 4.2,
        "title": ["GOVERNMENT CITADEL"],
        "ring": "Ring: Core",
        "address": "Address: 1.1",
        "gen": "Generation: 1",
        "resource": "MANDATE",
        "base": "Base: 3",
        "color": "#3a6ea8",
        "f_offset": 4.2 * 2
    },
    {
        "file": "V1/District_Tile_Ring2_Spec.svg",
        "angle": 12,
        "w_angle": 2.2,
        "title": ["COMMUNICATIONS", "HUB"],
        "ring": "Ring: The Mid",
        "address": "Address: 2.5",
        "gen": "Generation: 2",
        "resource": "EXPOSURE",
        "base": "Base: 2",
        "color": "#39d353",
        "f_offset": 2.2 * 2
    },
    {
        "file": "V1/District_Tile_Ring3_Spec.svg",
        "angle": 8.75,
        "w_angle": 1.55,
        "title": ["INDUSTRIAL", "FRINGE"],
        "ring": "Ring: Baryo",
        "address": "Address: 3.0",
        "gen": "Generation: 3",
        "resource": "CAPACITY",
        "base": "Base: 1",
        "color": "#d4622a",
        "f_offset": 1.55 * 2
    }
]

def get_point(r, deg):
    rad = math.radians(90 - deg)
    return CX + r * math.cos(rad), CY + r * math.sin(rad)

for ring in rings:
    ANGLE = ring["angle"]
    W_ANGLE = ring["w_angle"]
    f_offset = ring["f_offset"]
    
    p1_in = get_point(R1, -ANGLE)
    p2_in = get_point(R1, ANGLE)
    p1_out = get_point(R2, -ANGLE)
    p2_out = get_point(R2, ANGLE)

    wedge_path = f"M {p1_in[0]} {p1_in[1]} L {p1_out[0]} {p1_out[1]} A {R2} {R2} 0 0 0 {p2_out[0]} {p2_out[1]} L {p2_in[0]} {p2_in[1]} A {R1} {R1} 0 0 1 {p1_in[0]} {p1_in[1]} Z"
    
    # Title curves
    title_svg = ""
    if len(ring["title"]) == 1:
        title_svg += f'<path id="curve-title-0" d="M {get_point(445, -ANGLE)[0]} {get_point(445, -ANGLE)[1]} A 445 445 0 0 0 {get_point(445, ANGLE)[0]} {get_point(445, ANGLE)[1]}" fill="none" />\n'
        title_svg += f'<text class="text-title"><textPath xlink:href="#curve-title-0" startOffset="50%">{ring["title"][0]}</textPath></text>\n'
    else:
        title_svg += f'<path id="curve-title-0" d="M {get_point(435, -ANGLE)[0]} {get_point(435, -ANGLE)[1]} A 435 435 0 0 0 {get_point(435, ANGLE)[0]} {get_point(435, ANGLE)[1]}" fill="none" />\n'
        title_svg += f'<path id="curve-title-1" d="M {get_point(455, -ANGLE)[0]} {get_point(455, -ANGLE)[1]} A 455 455 0 0 0 {get_point(455, ANGLE)[0]} {get_point(455, ANGLE)[1]}" fill="none" />\n'
        title_svg += f'<text class="text-title"><textPath xlink:href="#curve-title-0" startOffset="50%">{ring["title"][0]}</textPath></text>\n'
        title_svg += f'<text class="text-title"><textPath xlink:href="#curve-title-1" startOffset="50%">{ring["title"][1]}</textPath></text>\n'

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 800 550" width="100%" height="100%">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1E293B" stroke-width="0.5" />
    </pattern>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <style>
      .bg {{ fill: #05070A; stroke: {ring["color"]}; stroke-width: 4; }}
      .text-title {{ fill: #F8FAFC; font-family: "Inter", "Segoe UI", sans-serif; font-size: 14px; font-weight: 800; letter-spacing: 2px; text-anchor: middle; }}
      .text-address {{ fill: #94A3B8; font-family: "Courier New", monospace; font-size: 10px; font-weight: 600; letter-spacing: 1px; text-anchor: middle; }}
      .text-resource {{ fill: {ring["color"]}; font-family: "Inter", sans-serif; font-size: 12px; font-weight: 700; text-anchor: middle; }}
      .tension-zone {{ fill: #1c1006; stroke: #d97736; stroke-width: 1.5; stroke-dasharray: 4 3; }}
      .text-tension {{ fill: #e58249; font-family: "Inter", sans-serif; font-size: 8px; font-weight: 700; text-anchor: middle; letter-spacing: 1px; }}
      .stack-zone {{ fill: none; stroke-width: 1.5; stroke-dasharray: 3 3; }}
      .structure-zone {{ fill: none; stroke-width: 1.5; }}
      .deployment-zone {{ fill: none; stroke-width: 1; stroke-dasharray: 2 2; }}
    </style>
    
    {title_svg}
    <path id="curve-ring" d="M {get_point(480, -ANGLE)[0]} {get_point(480, -ANGLE)[1]} A 480 480 0 0 0 {get_point(480, ANGLE)[0]} {get_point(480, ANGLE)[1]}" fill="none" />
    <path id="curve-address" d="M {get_point(492, -ANGLE)[0]} {get_point(492, -ANGLE)[1]} A 492 492 0 0 0 {get_point(492, ANGLE)[0]} {get_point(492, ANGLE)[1]}" fill="none" />
    <path id="curve-gen" d="M {get_point(504, -ANGLE)[0]} {get_point(504, -ANGLE)[1]} A 504 504 0 0 0 {get_point(504, ANGLE)[0]} {get_point(504, ANGLE)[1]}" fill="none" />
  </defs>

  <rect width="800" height="550" fill="#020305" />
  <rect width="800" height="550" fill="url(#grid)" />

  <path d="{wedge_path}" class="bg" filter="url(#glow)" />
  <path d="{wedge_path}" fill="url(#grid)" opacity="0.3" />

  {title_svg}
  <text class="text-address"><textPath xlink:href="#curve-ring" startOffset="50%">{ring["ring"]}</textPath></text>
  <text class="text-address"><textPath xlink:href="#curve-address" startOffset="50%">{ring["address"]}</textPath></text>
  <text class="text-address"><textPath xlink:href="#curve-gen" startOffset="50%">{ring["gen"]}</textPath></text>

  <!-- TENSION ZONE -->
  <g transform="rotate(0, {CX}, {CY}) translate({CX}, {CY + 290})">
    <polygon class="tension-zone" points="0,-12 10,-6 10,6 0,12 -10,6 -10,-6" filter="url(#glow)" />
    <text x="0" y="22" class="text-tension">TENSION</text>
  </g>

  <!-- RESOURCE BASELINE -->
  <g transform="rotate(0, {CX}, {CY}) translate({CX}, {CY + 366})">
    <rect x="-35" y="-15" width="70" height="30" fill="#0f172a" stroke="{ring["color"]}" stroke-width="1.5" rx="4" filter="url(#glow)" />
    <text x="0" y="-3" class="text-resource" fill="{ring["color"]}">{ring["resource"]}</text>
    <text x="0" y="10" class="text-resource" fill="{ring["color"]}" font-size="9">{ring["base"]}</text>
  </g>
"""

    FR1 = 520
    FR2 = 690

    # calculate starting angle for leftmost faction
    start_f_angle = -2 * f_offset

    for i, (name, color) in enumerate(factions):
        angle = start_f_angle + i * f_offset
        
        fp1_in = get_point(FR1, angle - W_ANGLE)
        fp2_in = get_point(FR1, angle + W_ANGLE)
        fp1_out = get_point(FR2, angle - W_ANGLE)
        fp2_out = get_point(FR2, angle + W_ANGLE)
        
        f_path = f"M {fp1_in[0]} {fp1_in[1]} L {fp1_out[0]} {fp1_out[1]} A {FR2} {FR2} 0 0 0 {fp2_out[0]} {fp2_out[1]} L {fp2_in[0]} {fp2_in[1]} A {FR1} {FR1} 0 0 1 {fp1_in[0]} {fp1_in[1]} Z"

        svg += f"""
    <path d="{f_path}" fill="#0a0c0f" stroke="{color}" stroke-width="2" />
    
    <!-- UI Layout -->
    <g transform="rotate({-angle}, {CX}, {CY}) translate({CX}, {CY + 520})">
      <circle class="stack-zone" cx="0" cy="30" r="11" stroke="{color}" />
      <rect class="structure-zone" x="-12" y="64" width="24" height="24" rx="4" stroke="{color}" />
      <polygon class="deployment-zone" points="-5,110 5,110 12,117 12,127 5,134 -5,134 -12,127 -12,117" stroke="{color}" />
      <polygon class="deployment-zone" points="-5,140 5,140 12,147 12,157 5,164 -5,164 -12,157 -12,147" stroke="{color}" />
    </g>
"""

    svg += "</svg>"

    with open(ring["file"], "w") as f:
        f.write(svg)
        
    print(f"Generated {ring['file']}")
