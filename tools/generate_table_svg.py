import os

def create_svg():
    width = 1600
    height = 1400
    
    # Colors
    bg_color = "#0B0F19"
    panel_bg = "#111827"
    panel_border = "#374151"
    table_bg = "#1F2937"
    table_border = "#4B5563"
    text_color = "#9CA3AF"
    text_highlight = "#F3F4F6"
    accent_color = "#3B82F6"
    
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">',
        f'  <defs>',
        f'    <style>',
        f'      .bg {{ fill: {bg_color}; }}',
        f'      .table-area {{ fill: {table_bg}; stroke: {table_border}; stroke-width: 4; rx: 24; ry: 24; }}',
        f'      .panel {{ fill: {panel_bg}; stroke: {panel_border}; stroke-width: 2; rx: 8; ry: 8; }}',
        f'      .chair {{ fill: {bg_color}; stroke: {panel_border}; stroke-width: 2; stroke-dasharray: 4 4; rx: 12; ry: 12; }}',
        f'      .central-area {{ fill: #080b13; stroke: {accent_color}; stroke-width: 2; rx: 16; ry: 16; }}',
        f'      .title {{ fill: {text_highlight}; font-family: "Inter", "Segoe UI", sans-serif; font-size: 20px; font-weight: 600; text-anchor: middle; }}',
        f'      .subtitle {{ fill: {text_color}; font-family: "Inter", "Segoe UI", sans-serif; font-size: 14px; text-anchor: middle; }}',
        f'    </style>',
        f'  </defs>',
        f'  <rect class="bg" width="{width}" height="{height}" />'
    ]

    def add_rect(x, y, w, h, title, subtitle="", css_class="panel"):
        svg.append(f'  <rect class="{css_class}" x="{x}" y="{y}" width="{w}" height="{h}" />')
        text_y = y + (h/2) if not subtitle else y + (h/2) - 12
        svg.append(f'  <text class="title" x="{x + w/2}" y="{text_y}" dominant-baseline="middle">{title}</text>')
        if subtitle:
            svg.append(f'  <text class="subtitle" x="{x + w/2}" y="{text_y + 24}" dominant-baseline="middle">{subtitle}</text>')

    # TABLE ZONE
    svg.append(f'  <rect class="table-area" x="300" y="300" width="1000" height="800" />')
    svg.append(f'  <text x="420" y="350" class="title" style="fill: {text_highlight}; font-size: 24px;">TABLE (zone_table)</text>')

    # CENTRAL AREA (inside table)
    svg.append(f'  <rect class="central-area" x="500" y="450" width="600" height="500" />')
    svg.append(f'  <text class="title" x="800" y="700" dominant-baseline="middle" style="font-size: 28px; fill: {accent_color};">CENTRAL AREA</text>')
    svg.append(f'  <text class="subtitle" x="800" y="735" dominant-baseline="middle" style="fill: {accent_color};">(zone_central_area)</text>')

    # PLAYER AREAS (inside table)
    add_rect(600, 320, 400, 110, "P6 AREA (ARBITER)", "zone_p6_area", "panel")
    add_rect(600, 970, 400, 110, "P3 AREA", "zone_p3_area", "panel")
    
    add_rect(320, 450, 160, 220, "P1 AREA", "zone_p1_area", "panel")
    add_rect(320, 730, 160, 220, "P2 AREA", "zone_p2_area", "panel")
    
    add_rect(1120, 450, 160, 220, "P5 AREA", "zone_p5_area", "panel")
    add_rect(1120, 730, 160, 220, "P4 AREA", "zone_p4_area", "panel")

    # CHAIRS (outside table)
    add_rect(650, 100, 300, 120, "P6 CHAIR", "zone_chairs", "chair")
    add_rect(650, 1180, 300, 120, "P3 CHAIR", "zone_chairs", "chair")
    
    add_rect(50, 450, 200, 220, "P1 CHAIR", "zone_chairs", "chair")
    add_rect(50, 730, 200, 220, "P2 CHAIR", "zone_chairs", "chair")
    
    add_rect(1350, 450, 200, 220, "P5 CHAIR", "zone_chairs", "chair")
    add_rect(1350, 730, 200, 220, "P4 CHAIR", "zone_chairs", "chair")

    # GAME BOX (outside table)
    add_rect(1350, 100, 200, 120, "GAME BOX", "zone_game_box", "panel")

    svg.append('</svg>')
    
    with open('/home/abosch/Projects/TheSignal/V1/Table_Layout.svg', 'w') as f:
        f.write('\n'.join(svg))
        
    print("SVG generated at /home/abosch/Projects/TheSignal/V1/Table_Layout.svg")

if __name__ == "__main__":
    create_svg()
