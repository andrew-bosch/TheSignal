import os

def create_svg():
    width = 1200
    height = 1600
    
    # Colors
    bg_color = "#0B0F19"
    panel_bg = "#111827"
    panel_border = "#374151"
    text_color = "#9CA3AF"
    text_highlight = "#F3F4F6"
    accent_color = "#3B82F6"
    supply_border = "#4B5563"
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">',
        f'  <defs>',
        f'    <style>',
        f'      .bg {{ fill: {bg_color}; }}',
        f'      .panel {{ fill: {panel_bg}; stroke: {panel_border}; stroke-width: 2; rx: 8; ry: 8; }}',
        f'      .panel-dash {{ fill: transparent; stroke: {supply_border}; stroke-width: 2; stroke-dasharray: 6 6; rx: 8; ry: 8; }}',
        f'      .title {{ fill: {text_highlight}; font-family: "Inter", "Segoe UI", sans-serif; font-size: 16px; font-weight: 600; text-anchor: middle; }}',
        f'      .subtitle {{ fill: {text_color}; font-family: "Inter", "Segoe UI", sans-serif; font-size: 13px; text-anchor: middle; }}',
        f'      .city-placeholder {{ fill: #080b13; stroke: {accent_color}; stroke-width: 2; rx: 16; ry: 16; }}',
        f'    </style>',
        f'  </defs>',
        f'  <rect class="bg" width="{width}" height="{height}" />'
    ]

    def add_panel(x, y, w, h, title, subtitle=""):
        svg.append(f'  <rect class="panel" x="{x}" y="{y}" width="{w}" height="{h}" />')
        text_y = y + (h/2) if not subtitle else y + (h/2) - 10
        svg.append(f'  <text class="title" x="{x + w/2}" y="{text_y}" dominant-baseline="middle">{title}</text>')
        if subtitle:
            svg.append(f'  <text class="subtitle" x="{x + w/2}" y="{text_y + 20}" dominant-baseline="middle">{subtitle}</text>')

    # Top Left Track Stack
    add_panel(60, 100, 220, 80, "SESSION TIMELINE", "zone_session_timeline")
    add_panel(60, 200, 220, 80, "INITIATIVE STRIP", "zone_initiative_strip")

    # Top Right Track Stack
    add_panel(920, 100, 220, 80, "SITUATION REPORT", "zone_situation_report")
    add_panel(920, 200, 220, 80, "CHORUS ACTIVITY", "zone_chorus_activity")

    # Top Center - Supply Zone
    svg.append(f'  <rect class="panel-dash" x="300" y="100" width="600" height="220" />')
    svg.append(f'  <text class="subtitle" x="600" y="130" text-anchor="middle">SUPPLY ZONE (zone_supply)</text>')
    add_panel(340, 150, 240, 140, "RESERVOIR")
    add_panel(620, 150, 240, 140, "BACKLOG")

    # Modifiers: North of City Map, left half (centerline = 600)
    # R1 at right (near center), R2 left of that, R3 far left.
    add_panel(420, 420, 160, 100, "RING 1 MODS", "zone_ring_1_modifier")
    add_panel(240, 420, 160, 100, "RING 2 MODS", "zone_ring_2_modifier")
    add_panel(60, 420, 160, 100, "RING 3 MODS", "zone_ring_3_modifier")

    # Middle - City Map Placeholder
    svg.append(f'  <rect class="city-placeholder" x="40" y="560" width="1120" height="640" />')
    svg.append(f'  <text class="title" x="600" y="880" dominant-baseline="middle" style="font-size: 24px; fill: {accent_color};">CITY MAP</text>')
    
    # Bottom Center - Accord Placement
    add_panel(200, 1250, 800, 100, "ACCORD PLACEMENT AREA", "zone_accord_area")

    # Bottom Center - Public Standing Track
    add_panel(200, 1400, 800, 100, "PUBLIC STANDING TRACK", "zone_public_standing")

    # Add framing lines for Central Area boundary
    svg.append(f'  <rect x="40" y="40" width="1120" height="1520" fill="none" stroke="{accent_color}" stroke-width="1" stroke-opacity="0.3" rx="16" ry="16" />')
    svg.append(f'  <text x="600" y="70" class="subtitle" text-anchor="middle" style="fill: {accent_color};">CENTRAL AREA (zone_central_area)</text>')

    # Add a visual centerline guide inside the frame
    svg.append(f'  <line x1="600" y1="40" x2="600" y2="1560" stroke="{accent_color}" stroke-width="1" stroke-dasharray="4 8" stroke-opacity="0.1" />')

    svg.append('</svg>')
    
    with open('/home/abosch/Projects/TheSignal/V1/Central_Area_Layout.svg', 'w') as f:
        f.write('\n'.join(svg))
        
    print("SVG generated at /home/abosch/Projects/TheSignal/V1/Central_Area_Layout.svg")

if __name__ == "__main__":
    create_svg()
