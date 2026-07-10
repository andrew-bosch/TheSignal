import math

CX, CY = 400, -200
R1 = 250
R2 = 700
ANGLE = 22  # half angle in degrees (44 total for Ring 1)

def get_point(r, deg):
    # deg < 0 means LEFT side (angle > 90)
    # deg > 0 means RIGHT side (angle < 90)
    rad = math.radians(90 - deg)
    return CX + r * math.cos(rad), CY + r * math.sin(rad)

p1_in = get_point(R1, -ANGLE)
p2_in = get_point(R1, ANGLE)
p1_out = get_point(R2, -ANGLE)
p2_out = get_point(R2, ANGLE)

# Wedge path (narrow on top, wide on bottom)
wedge_path = f"M {p1_in[0]} {p1_in[1]} L {p1_out[0]} {p1_out[1]} A {R2} {R2} 0 0 0 {p2_out[0]} {p2_out[1]} L {p2_in[0]} {p2_in[1]} A {R1} {R1} 0 0 1 {p1_in[0]} {p1_in[1]} Z"

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
      .bg {{ fill: #05070A; stroke: #3a6ea8; stroke-width: 4; }}
      .text-title {{ fill: #F8FAFC; font-family: "Inter", "Segoe UI", sans-serif; font-size: 20px; font-weight: 800; letter-spacing: 2px; text-anchor: middle; }}
      .text-address {{ fill: #94A3B8; font-family: "Courier New", monospace; font-size: 14px; font-weight: 600; letter-spacing: 1px; text-anchor: middle; }}
      .text-gen {{ fill: #64748B; font-family: "Courier New", monospace; font-size: 12px; font-weight: 600; letter-spacing: 2px; text-anchor: middle; }}
      .text-resource {{ fill: #93c5fd; font-family: "Inter", sans-serif; font-size: 12px; font-weight: 700; text-anchor: middle; }}
      .tension-zone {{ fill: #2a0a0a; stroke: #EF4444; stroke-width: 2; stroke-dasharray: 6 4; }}
      .text-tension {{ fill: #FCA5A5; font-family: "Inter", sans-serif; font-size: 10px; font-weight: 700; text-anchor: middle; letter-spacing: 1px; }}
      .text-faction {{ font-family: "Inter", sans-serif; font-size: 11px; font-weight: 700; text-anchor: middle; }}
      .stack-zone {{ fill: none; stroke-width: 1.5; stroke-dasharray: 3 3; }}
      .stack-label {{ font-family: "Inter", sans-serif; font-size: 8px; font-weight: 600; text-anchor: middle; }}
      .structure-zone {{ fill: none; stroke-width: 1.5; }}
      .deployment-zone {{ fill: none; stroke-width: 1; stroke-dasharray: 2 2; rx: 2; ry: 2; }}
    </style>
    
    <!-- Curved Text Paths -->
    <path id="curve-title" d="M {get_point(410, -ANGLE)[0]} {get_point(410, -ANGLE)[1]} A 410 410 0 0 0 {get_point(410, ANGLE)[0]} {get_point(410, ANGLE)[1]}" fill="none" />
    <path id="curve-address" d="M {get_point(435, -ANGLE)[0]} {get_point(435, -ANGLE)[1]} A 435 435 0 0 0 {get_point(435, ANGLE)[0]} {get_point(435, ANGLE)[1]}" fill="none" />
    <path id="curve-gen" d="M {get_point(455, -ANGLE)[0]} {get_point(455, -ANGLE)[1]} A 455 455 0 0 0 {get_point(455, ANGLE)[0]} {get_point(455, ANGLE)[1]}" fill="none" />
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="550" fill="#020305" />
  <rect width="800" height="550" fill="url(#grid)" />

  <!-- Wedge Tile Base -->
  <path d="{wedge_path}" class="bg" filter="url(#glow)" />
  <path d="{wedge_path}" fill="url(#grid)" opacity="0.3" />

  <!-- HEADER (Curved) -->
  <text class="text-title"><textPath xlink:href="#curve-title" startOffset="50%">GOVERNMENT CITADEL</textPath></text>
  <text class="text-address"><textPath xlink:href="#curve-address" startOffset="50%">Ring: Core || Address 1.1</textPath></text>
  <text class="text-gen"><textPath xlink:href="#curve-gen" startOffset="50%">Generation: 1</textPath></text>

  <!-- TENSION ZONE (Inner Core) -->
  <g transform="rotate(0, {CX}, {CY}) translate({CX}, {CY + 290})">
    <polygon class="tension-zone" points="0,-20 18,-10 18,10 0,20 -18,10 -18,-10" filter="url(#glow)" />
    <text x="0" y="32" class="text-tension">TENSION</text>
  </g>

  <!-- RESOURCE BASELINE -->
  <g transform="rotate(0, {CX}, {CY}) translate({CX}, {CY + 360})">
    <rect x="-40" y="-15" width="80" height="30" fill="#0f172a" stroke="#3a6ea8" stroke-width="1.5" rx="4" filter="url(#glow)" />
    <text x="0" y="-3" class="text-resource">MANDATE</text>
    <text x="0" y="10" class="text-resource" font-size="9">Base: 1</text>
  </g>

  <!-- FACTION ARRAYS (Interlocking Arc Segments) -->
"""

factions = [
    ("GUILD", "#d4622a", -16.8),
    ("GHOST", "#6a9978", -8.4),
    ("DIRECTORATE", "#3a6ea8", 0),
    ("NETWORK", "#39d353", 8.4),
    ("SYNDICATE", "#c9a84c", 16.8)
]

FR1 = 490
FR2 = 690
W_ANGLE = 4.2  # width spans 8.4 degrees per faction, 42 total

for name, color, angle in factions:
    fp1_in = get_point(FR1, angle - W_ANGLE)
    fp2_in = get_point(FR1, angle + W_ANGLE)
    fp1_out = get_point(FR2, angle - W_ANGLE)
    fp2_out = get_point(FR2, angle + W_ANGLE)
    
    # Path of the individual faction wedge
    f_path = f"M {fp1_in[0]} {fp1_in[1]} L {fp1_out[0]} {fp1_out[1]} A {FR2} {FR2} 0 0 0 {fp2_out[0]} {fp2_out[1]} L {fp2_in[0]} {fp2_in[1]} A {FR1} {FR1} 0 0 1 {fp1_in[0]} {fp1_in[1]} Z"

    svg += f"""
    <!-- Boundary -->
    <path d="{f_path}" fill="#0a0c0f" stroke="{color}" stroke-width="2" />
    
    <!-- UI Elements -->
    <g transform="rotate({-angle}, {CX}, {CY}) translate({CX}, {CY + 490})">
      <text x="0" y="28" class="text-faction" fill="{color}">{name}</text>
      
      <!-- Influence Stack -->
      <circle class="stack-zone" cx="0" cy="65" r="18" stroke="{color}" />
      <text x="0" y="93" class="stack-label" fill="{color}">INFLUENCE</text>
      
      <!-- Structure -->
      <rect class="structure-zone" x="-14" y="106" width="28" height="28" rx="4" stroke="{color}" />
      <text x="0" y="145" class="stack-label" fill="{color}">STRUCTURE</text>
      
      <!-- Deployment -->
      <rect class="deployment-zone" x="-30" y="158" width="28" height="28" stroke="{color}" />
      <rect class="deployment-zone" x="2" y="158" width="28" height="28" stroke="{color}" />
      <text x="0" y="196" class="stack-label" fill="{color}">DEPLOY</text>
    </g>
"""

svg += "</svg>"

with open("V1/District_Tile_Ring1_Spec.svg", "w") as f:
    f.write(svg)

print("Ring 1 Wedge SVG generated successfully.")
