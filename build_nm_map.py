import math

# CANVAS SETTINGS - 1M EDGE BOARD
# 1px = 0.25mm physical scale. 
# Map is 4.0 meters wide by 2.15 meters tall! (At 0.25mm -> 1.0M x 0.53M)
CX, CY = 2000, 100
WIDTH, HEIGHT = 4000, 2150

# Expanded Uniform Ring Thickess (500px height) to add generous padding
# Ring 0 expanded by 1.5x! (270 -> 405)
R0_MAX = 405
R1_MIN, R1_MAX = 425, 925
R2_MIN, R2_MAX = 945, 1445
R3_MIN, R3_MAX = 1465, 1965

# Angles mapping Left (0) to Right (180)
R1_START, R1_END = 0, 180
R2_START, R2_END = 5, 175
R3_START, R3_END = 10, 170

FACTIONS = [
    ("GUILD", "#d4622a"),
    ("GHOST", "#6a9978"),
    ("DIRECTORATE", "#3a6ea8"),
    ("NETWORK", "#39d353"),
    ("SYNDICATE", "#c9a84c")
]

COLORS = {
    "Mandate": "#3a6ea8",
    "Findings": "#6a9978",
    "Capital": "#c9a84c",
    "Capacity": "#d4622a",
    "Exposure": "#39d353",
    "None": "#fffff0"
}

RING1 = [
    ("Military Installation", "1.0", "Year 1", "Mandate", "3"),
    ("Government Citadel", "1.1", "Year 2", "Mandate", "3"),
    ("Chorus Research", "1.2", "Year 3", "Findings", "3"),
    ("Financial Sanctum", "1.3", "Year 4", "Capital", "3")
]
RING2 = [
    ("Regulatory District", "2.0", "Year 7", "Mandate", "2"),
    ("Power Grid", "2.1", "Year 8", "Capacity", "2"),
    ("Logistics Center", "2.2", "Year 9", "Capacity", "2"),
    ("Research Institute", "2.3", "Year 10", "Findings", "2"),
    ("Data Exchange", "2.4", "Year 11", "Findings", "2"),
    ("Communications Hub", "2.5", "Year 12", "Exposure", "2"),
    ("Financial Clearinghouse", "2.6", "Year 13", "Capital", "2")
]
RING3 = [
    ("Industrial Fringe", "3.0", "Year 17", "Capacity", "1"),
    ("Transit Hub", "3.1", "Year 18", "Capacity", "1"),
    ("Civic Center", "3.2", "Year 19", "Mandate", "1"),
    ("Residential Quarter", "3.3", "Year 20", "Mandate", "1"),
    ("University Perimeter", "3.4", "Year 21", "Findings", "1"),
    ("Media District", "3.5", "Year 23", "Exposure", "1"),
    ("Broadcast Tower", "3.6", "Year 24", "Exposure", "1"),
    ("Observation Post", "3.7", "Year 25", "Exposure", "1"),
    ("Commercial Strip", "3.8", "Year 27", "Capital", "1")
]

def get_point(r, deg):
    # 0 = Left, 90 = Down, 180 = Right
    rad = math.radians(180 - deg)
    return CX + r * math.cos(rad), CY + r * math.sin(rad)

def get_wedge_path(r1, r2, start_deg, end_deg):
    p1_in = get_point(r1, start_deg)
    p2_in = get_point(r1, end_deg)
    p1_out = get_point(r2, start_deg)
    p2_out = get_point(r2, end_deg)
    return f"M {p1_in[0]} {p1_in[1]} L {p1_out[0]} {p1_out[1]} A {r2} {r2} 0 0 0 {p2_out[0]} {p2_out[1]} L {p2_in[0]} {p2_in[1]} A {r1} {r1} 0 0 1 {p1_in[0]} {p1_in[1]} Z"

svg_elements = []

def draw_ring0():
    r0_start = -30
    r0_end = 210
    
    p1_out = get_point(R0_MAX, r0_start)
    p2_out = get_point(R0_MAX, r0_end)
    
    bg_path = f"M {p1_out[0]} {p1_out[1]} A {R0_MAX} {R0_MAX} 0 1 0 {p2_out[0]} {p2_out[1]} Z"
    svg_elements.append(f'<path d="{bg_path}" fill="#05070A" stroke="#fffff0" stroke-width="4" filter="url(#glow)" />')
    svg_elements.append(f'<path d="{bg_path}" fill="url(#grid)" opacity="0.3" />')
    
    # Arbiter (solid white circle) with label moved above the token
    svg_elements.append(f'<circle cx="{CX}" cy="{CY + 130}" r="21" fill="#fffff0" filter="url(#glow)" />')
    svg_elements.append(f'<text x="{CX}" y="{CY + 95}" class="r0-arbiter" filter="url(#glow)">ARBITER INFLUENCE</text>')
    
    # Titles
    svg_elements.append(f'<text x="{CX}" y="{CY - 20}" class="r0-title" filter="url(#glow)">CHORUS NODE</text>')
    svg_elements.append(f'<text x="{CX}" y="{CY + 30}" class="r0-address">ORIGIN</text>')
    
    # Factions in Ring 0
    fr2 = R0_MAX - 5
    fr1 = fr2 - 160
    w_angle = math.degrees(56 / fr1) / 2
    f_offset = w_angle * 3.1
    start_f = 90 - (2 * f_offset)
    
    for fi, (fname, fcolor) in enumerate(FACTIONS):
        a = start_f + fi * f_offset
        fpath = get_wedge_path(fr1, fr2, a - w_angle, a + w_angle)
        svg_elements.append(f'<path d="{fpath}" fill="#0a0c0f" stroke="{fcolor}" stroke-width="2" />')
        
        icon_rot = 90 - a
        svg_elements.append(f"""
        <g transform="rotate({icon_rot}, {CX}, {CY}) translate({CX}, {CY + fr1})">
          <circle class="stack-zone" cx="0" cy="24" r="21" stroke="{fcolor}" />
          <!-- Deploy octagons (50x50) -->
          <polygon class="deployment-zone" points="-14,50 14,50 25,61 25,89 14,100 -14,100 -25,89 -25,61" stroke="{fcolor}" />
          <polygon class="deployment-zone" points="-14,105 14,105 25,116 25,144 14,155 -14,155 -25,144 -25,116" stroke="{fcolor}" />
        </g>
        """)

    # Tension Marker (Straight horizontal line from Arbiter, right of gold wedge)
    svg_elements.append(f"""
    <g transform="translate({CX + 320}, {CY + 130})">
      <polygon class="tension-zone" points="0,-21 21,-10 21,10 0,21 -21,10 -21,-10" filter="url(#glow)" />
      <text x="0" y="35" class="text-tension">TENSION</text>
    </g>
    """)

def draw_districts(districts, r1, r2, map_start, map_end):
    count = len(districts)
    total_span = map_end - map_start
    step = total_span / count
    pad = 0.5 
    
    for i, (name, addr, est_year, res, base) in enumerate(districts):
        d_start = map_start + i * step + (pad/2)
        d_end = map_start + (i + 1) * step - (pad/2)
        d_mid = (d_start + d_end) / 2
        color = COLORS[res]
        
        parts = name.split(" ")
        title1 = parts[0]
        title2 = " ".join(parts[1:]) if len(parts) > 1 else ""
        
        wpath = get_wedge_path(r1, r2, d_start, d_end)
        svg_elements.append(f'<path d="{wpath}" class="bg" stroke="{color}" filter="url(#glow)" />')
        svg_elements.append(f'<path d="{wpath}" fill="url(#grid)" opacity="0.3" />')
        
        cid0 = f"curve_{addr}_0"
        cid1 = f"curve_{addr}_1"
        c_ring = f"curve_{addr}_ring"
        c_addr = f"curve_{addr}_addr"
        c_gen = f"curve_{addr}_gen"
        
        # Left-Justified Text Block
        t_r1 = r1 + 45
        t_r2 = r1 + 75
        r_ring = r1 + 110
        r_addr = r1 + 130
        r_gen = r1 + 150
        
        svg_elements.append(f'<path id="{cid0}" d="M {get_point(t_r1, d_start)[0]} {get_point(t_r1, d_start)[1]} A {t_r1} {t_r1} 0 0 0 {get_point(t_r1, d_end)[0]} {get_point(t_r1, d_end)[1]}" fill="none" />')
        svg_elements.append(f'<text class="text-title-left"><textPath xlink:href="#{cid0}" startOffset="15">{title1.upper()}</textPath></text>')
        if title2:
            svg_elements.append(f'<path id="{cid1}" d="M {get_point(t_r2, d_start)[0]} {get_point(t_r2, d_start)[1]} A {t_r2} {t_r2} 0 0 0 {get_point(t_r2, d_end)[0]} {get_point(t_r2, d_end)[1]}" fill="none" />')
            svg_elements.append(f'<text class="text-title-left"><textPath xlink:href="#{cid1}" startOffset="15">{title2.upper()}</textPath></text>')
            
        svg_elements.append(f'<path id="{c_ring}" d="M {get_point(r_ring, d_start)[0]} {get_point(r_ring, d_start)[1]} A {r_ring} {r_ring} 0 0 0 {get_point(r_ring, d_end)[0]} {get_point(r_ring, d_end)[1]}" fill="none" />')
        svg_elements.append(f'<path id="{c_addr}" d="M {get_point(r_addr, d_start)[0]} {get_point(r_addr, d_start)[1]} A {r_addr} {r_addr} 0 0 0 {get_point(r_addr, d_end)[0]} {get_point(r_addr, d_end)[1]}" fill="none" />')
        svg_elements.append(f'<path id="{c_gen}" d="M {get_point(r_gen, d_start)[0]} {get_point(r_gen, d_start)[1]} A {r_gen} {r_gen} 0 0 0 {get_point(r_gen, d_end)[0]} {get_point(r_gen, d_end)[1]}" fill="none" />')
        
        svg_elements.append(f'<text class="text-address-left"><textPath xlink:href="#{c_ring}" startOffset="15">Ring: {addr.split(".")[0]}</textPath></text>')
        svg_elements.append(f'<text class="text-address-left"><textPath xlink:href="#{c_addr}" startOffset="15">Address: {addr}</textPath></text>')
        svg_elements.append(f'<text class="text-address-left"><textPath xlink:href="#{c_gen}" startOffset="15">Established: {est_year}</textPath></text>')
        
        # Base Resource Box (Top Right Justified, aligned with Ring metadata)
        res_r = r1 + 110
        angle_pad = math.degrees(65 / res_r)  # 65px physical padding from right edge
        res_angle = d_end - angle_pad
        res_rot = 90 - res_angle
        
        # Tension Zone (Top Right, stacked exactly above Resource Box - Diamond)
        tens_r = r1 + 50
        svg_elements.append(f"""
        <g transform="rotate({res_rot}, {CX}, {CY}) translate({CX}, {CY + tens_r})">
          <polygon class="tension-zone" points="0,-21 21,-10 21,10 0,21 -21,10 -21,-10" filter="url(#glow)" />
          <text x="0" y="35" class="text-tension">TENSION</text>
        </g>
        """)

        svg_elements.append(f"""
        <g transform="rotate({res_rot}, {CX}, {CY}) translate({CX}, {CY + res_r})">
          <rect x="-45" y="-18" width="90" height="40" fill="#0f172a" stroke="{color}" stroke-width="1.5" rx="4" filter="url(#glow)" />
          <text x="0" y="0" class="text-resource" fill="{color}">{res.upper()}</text>
          <text x="0" y="16" class="text-resource" fill="{color}" font-size="14">Base: {base}</text>
        </g>
        """)
        
        # Faction Wedges (Shifted Outward & Expanded Vertically)
        fr2 = r2 - 5
        fr1 = r2 - 216  # 211px wedge height to fit 15% larger tokens
        
        # Calculate exactly 56px angular width to wrap the massive 50px components
        w_angle = math.degrees(56 / fr1) / 2
        f_offset = w_angle * 3.1
        start_f = d_mid - (2 * f_offset)
        
        for fi, (fname, fcolor) in enumerate(FACTIONS):
            a = start_f + fi * f_offset
            fpath = get_wedge_path(fr1, fr2, a - w_angle, a + w_angle)
            svg_elements.append(f'<path d="{fpath}" fill="#0a0c0f" stroke="{fcolor}" stroke-width="1.5" />')
            
            icon_rot = 90 - a
            svg_elements.append(f"""
            <g transform="rotate({icon_rot}, {CX}, {CY}) translate({CX}, {CY + fr1})">
              <!-- Influence (Diameter 42px) -->
              <circle class="stack-zone" cx="0" cy="24" r="21" stroke="{fcolor}" />
              <!-- Structure (Block 50x50) -->
              <rect class="structure-zone" x="-25" y="50" width="50" height="50" rx="4" stroke="{fcolor}" />
              <!-- Deploy octagons (50x50) -->
              <polygon class="deployment-zone" points="-14,105 14,105 25,116 25,144 14,155 -14,155 -25,144 -25,116" stroke="{fcolor}" />
              <polygon class="deployment-zone" points="-14,160 14,160 25,171 25,199 14,210 -14,210 -25,199 -25,171" stroke="{fcolor}" />
            </g>
            """)

draw_ring0()
draw_districts(RING1, R1_MIN, R1_MAX, R1_START, R1_END)
draw_districts(RING2, R2_MIN, R2_MAX, R2_START, R2_END)
draw_districts(RING3, R3_MIN, R3_MAX, R3_START, R3_END)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {WIDTH} {HEIGHT}" width="100%" height="100%" style="background-color: #0a0c0f;">
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1E293B" stroke-width="0.5" />
    </pattern>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <style>
      .bg {{ fill: #05070A; stroke-width: 2.5; }}
      .text-title {{ fill: #F8FAFC; font-family: "Inter", "Segoe UI", sans-serif; font-size: 22px; font-weight: 800; letter-spacing: 2px; text-anchor: middle; }}
      .text-title-left {{ fill: #F8FAFC; font-family: "Inter", "Segoe UI", sans-serif; font-size: 22px; font-weight: 800; letter-spacing: 2px; text-anchor: start; }}
      .text-address {{ fill: #94A3B8; font-family: "Courier New", monospace; font-size: 17px; font-weight: 600; letter-spacing: 1px; text-anchor: middle; }}
      .text-address-left {{ fill: #94A3B8; font-family: "Courier New", monospace; font-size: 17px; font-weight: 600; letter-spacing: 1px; text-anchor: start; }}
      .text-resource {{ font-family: "Inter", sans-serif; font-size: 18px; font-weight: 700; text-anchor: middle; }}
      
      .tension-zone {{ fill: #1c1006; stroke: #d97736; stroke-width: 2.5; stroke-dasharray: 6 4; }}
      .text-tension {{ fill: #e58249; font-family: "Inter", sans-serif; font-size: 10px; font-weight: 800; text-anchor: middle; letter-spacing: 2px; }}
      
      .stack-zone {{ fill: none; stroke-width: 2; stroke-dasharray: 4 4; }}
      .structure-zone {{ fill: none; stroke-width: 2; }}
      .deployment-zone {{ fill: none; stroke-width: 2; stroke-dasharray: 3 3; }}
      
      .r0-title {{ fill: #F8FAFC; font-family: "Inter", sans-serif; font-size: 52px; font-weight: 800; letter-spacing: 6px; text-anchor: middle; }}
      .r0-address {{ fill: #94A3B8; font-family: "Courier New", monospace; font-size: 24px; font-weight: 600; letter-spacing: 3px; text-anchor: middle; }}
      .r0-arbiter {{ fill: #fffff0; font-family: "Inter", sans-serif; font-size: 18px; font-weight: 700; letter-spacing: 2px; text-anchor: middle; }}
    </style>
  </defs>

  <rect width="{WIDTH}" height="{HEIGHT}" fill="#0a0c0f" />
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#grid)" />
  
  <text x="50" y="50" fill="#3a6ea8" font-family="Inter" font-size="24" font-weight="900" letter-spacing="4" filter="url(#glow)">NEW MERIDIAN // WAR ROOM MAP</text>
  <text x="50" y="80" fill="#6a9978" font-family="Courier New" font-size="14" font-weight="bold">PHYSICAL SCALE: 1PX = 0.25MM (0.95M WIDE)</text>

  {"".join(svg_elements)}
</svg>"""

with open("V1/NM_Overlay_Generated.svg", "w") as f:
    f.write(svg)

print("Generated V1/NM_Overlay_Generated.svg (Expanded Scale with Heavy Padding)")
