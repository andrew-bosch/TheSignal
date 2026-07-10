import math

CX, CY = 800, 350
R2 = 550

factions = [
    ("GUILD", "#d4622a"),
    ("GHOST", "#6a9978"),
    ("DIRECTORATE", "#3a6ea8"),
    ("NETWORK", "#39d353"),
    ("SYNDICATE", "#c9a84c")
]

W_ANGLE = 4.2   # Same physical width as Ring 1
f_offset = 20   # Added generous padding between wedges!

def get_point(r, deg):
    rad = math.radians(90 - deg)
    return CX + r * math.cos(rad), CY + r * math.sin(rad)

# Draw 2/3 circle with top cut off
# A chord passing through CY - R2/2 gives exactly a 240-degree bottom arc.
dx = R2 * (math.sqrt(3) / 2)
dy = R2 * 0.5
p_left = (CX - dx, CY - dy)
p_right = (CX + dx, CY - dy)

# A sweep-flag of 0 draws the arc via the bottom from left to right.
wedge_path = f"M {p_left[0]} {p_left[1]} A {R2} {R2} 0 1 0 {p_right[0]} {p_right[1]} Z"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1600 1000" width="100%" height="100%">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1E293B" stroke-width="0.5" />
    </pattern>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <style>
      .bg {{ fill: #05070A; stroke: #fffff0; stroke-width: 4; }}
      .text-title {{ fill: #F8FAFC; font-family: "Inter", "Segoe UI", sans-serif; font-size: 36px; font-weight: 800; letter-spacing: 6px; text-anchor: middle; }}
      .text-address {{ fill: #94A3B8; font-family: "Courier New", monospace; font-size: 16px; font-weight: 600; letter-spacing: 3px; text-anchor: middle; }}
      .text-arbiter {{ fill: #fffff0; font-family: "Inter", sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 2px; text-anchor: middle; }}
      .tension-zone {{ fill: #1c1006; stroke: #d97736; stroke-width: 2; stroke-dasharray: 6 4; }}
      .text-tension {{ fill: #e58249; font-family: "Inter", sans-serif; font-size: 12px; font-weight: 700; text-anchor: middle; letter-spacing: 2px; }}
      .stack-zone {{ fill: none; stroke-width: 1.5; stroke-dasharray: 3 3; }}
      .deployment-zone {{ fill: none; stroke-width: 1; stroke-dasharray: 2 2; }}
    </style>
  </defs>

  <rect width="1600" height="1000" fill="#020305" />
  <rect width="1600" height="1000" fill="url(#grid)" />

  <g>
    <path d="{wedge_path}" class="bg" filter="url(#glow)" />
    <path d="{wedge_path}" fill="url(#grid)" opacity="0.3" />

    <!-- ARBITER INFLUENCE -->
    <circle cx="{CX}" cy="{CY - 150}" r="11" fill="#fffff0" filter="url(#glow)" />
    <text x="{CX}" y="{CY - 120}" class="text-arbiter" filter="url(#glow)">ARBITER INFLUENCE</text>

    <!-- FLAT TITLE DEAD CENTER -->
    <text x="{CX}" y="{CY}" class="text-title" filter="url(#glow)">CHORUS NODE</text>

    <!-- FLAT METADATA BLOCKS -->
    <text x="{CX}" y="{CY + 60}" class="text-address">Ring: Chorus Node</text>
    <text x="{CX}" y="{CY + 95}" class="text-address">Address: 0.0</text>
    <text x="{CX}" y="{CY + 130}" class="text-address">Generation: 0</text>

    <!-- TENSION ZONE (Moved Down) -->
    <g transform="rotate(0, {CX}, {CY}) translate({CX}, {CY + 210})">
      <polygon class="tension-zone" points="0,-18 15,-9 15,9 0,18 -15,9 -15,-9" filter="url(#glow)" />
      <text x="0" y="35" class="text-tension">TENSION</text>
    </g>
"""

# Faction bounds (Height = 170 to match Ring 1, 2, 3 components!)
FR1 = 360
FR2 = 530

# calculate starting angle for leftmost faction (centered at bottom)
start_f_angle = -2 * f_offset

for i, (name, color) in enumerate(factions):
    angle = start_f_angle + i * f_offset
    
    fp1_in = get_point(FR1, angle - W_ANGLE)
    fp2_in = get_point(FR1, angle + W_ANGLE)
    fp1_out = get_point(FR2, angle - W_ANGLE)
    fp2_out = get_point(FR2, angle + W_ANGLE)
    
    f_path = f"M {fp1_in[0]} {fp1_in[1]} L {fp1_out[0]} {fp1_out[1]} A {FR2} {FR2} 0 0 0 {fp2_out[0]} {fp2_out[1]} L {fp2_in[0]} {fp2_in[1]} A {FR1} {FR1} 0 0 1 {fp1_in[0]} {fp1_in[1]} Z"

    svg += f"""
    <!-- Faction: {name} -->
    <path d="{f_path}" fill="#0a0c0f" stroke="{color}" stroke-width="2" />
    
    <!-- UI Layout (No Structure Placements) -->
    <g transform="rotate({-angle}, {CX}, {CY}) translate({CX}, {CY + FR1})">
      <circle class="stack-zone" cx="0" cy="40" r="11" stroke="{color}" />
      <polygon class="deployment-zone" points="-5,90 5,90 12,97 12,107 5,114 -5,114 -12,107 -12,97" stroke="{color}" />
      <polygon class="deployment-zone" points="-5,120 5,120 12,127 12,137 5,144 -5,144 -12,137 -12,127" stroke="{color}" />
    </g>
"""

svg += """  </g>
</svg>"""

with open("V1/District_Tile_Ring0_Spec.svg", "w") as f:
    f.write(svg)
    
print("Generated V1/District_Tile_Ring0_Spec.svg")
