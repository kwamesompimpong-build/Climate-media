#!/usr/bin/env python3
"""Draw the two era maps (AD 306 and AD 786) as themable inline SVG.

Coastlines, rivers and lakes come from Natural Earth (50m) GeoJSON, pulled
from the natural-earth-vector GitHub mirror on first run. The projection is
a Lambert azimuthal equal-area centred on Africa, computed here directly, so
the only dependency is the standard library.

    python3 make_maps.py --data ./data --out ../illustrations

The SVGs use CSS classes (land, coast, river, lake, site-wa, ...) and no
fixed colours, so the page's light and dark tokens style them.
"""
import argparse, json, math, os, urllib.request

NE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/"
FILES = {
    "land": "ne_50m_land.geojson",
    "rivers": "ne_50m_rivers_lake_centerlines.geojson",
    "lakes": "ne_50m_lakes.geojson",
}
RIVERS = {"Niger", "Nile", "Congo", "Benue", "Volta", "Zambezi", "Limpopo", "Orange", "Victoria Nile", "Albert Nile"}
LAKES = {"Lake Chad", "Lake Victoria", "Lake Tanganyika", "Lake Malawi", "Lake Turkana"}

# Projection: Lambert azimuthal equal-area, centre (lon0, lat0), scale in px per unit
LON0, LAT0, SCALE = 17.0, 5.0, 300.0
W, H = 720, 780
FRAME = (-22, 54, -37, 47)   # lon min, lon max, lat min, lat max (for clipping features)


def project(lon, lat):
    lam, phi = math.radians(lon - LON0), math.radians(lat)
    phi0 = math.radians(LAT0)
    k = math.sqrt(2 / (1 + math.sin(phi0) * math.sin(phi) + math.cos(phi0) * math.cos(phi) * math.cos(lam)))
    x = k * math.cos(phi) * math.sin(lam)
    y = k * (math.cos(phi0) * math.sin(phi) - math.sin(phi0) * math.cos(phi) * math.cos(lam))
    return W / 2 + x * SCALE, H / 2 - y * SCALE + 10


def in_frame(coords):
    xs = [c[0] for c in coords]; ys = [c[1] for c in coords]
    return not (max(xs) < FRAME[0] or min(xs) > FRAME[1] or max(ys) < FRAME[2] or min(ys) > FRAME[3])


def ring_path(ring):
    pts = []
    last = None
    for lon, lat in ring:
        x, y = project(lon, lat)
        p = (round(x, 1), round(y, 1))
        if p != last:
            pts.append(p)
            last = p
    if len(pts) < 3:
        return ""
    return "M" + " L".join(f"{x},{y}" for x, y in pts) + " Z"


def line_path(line):
    pts = [project(lon, lat) for lon, lat in line]
    return "M" + " L".join(f"{round(x,1)},{round(y,1)}" for x, y in pts)


def load(data_dir, key):
    path = os.path.join(data_dir, FILES[key])
    if not os.path.exists(path):
        os.makedirs(data_dir, exist_ok=True)
        urllib.request.urlretrieve(NE + FILES[key], path)
    with open(path) as f:
        return json.load(f)


def geometry_paths(geom, kind):
    t = geom["type"]
    if kind == "poly":
        polys = geom["coordinates"] if t == "MultiPolygon" else [geom["coordinates"]]
        out = []
        for poly in polys:
            if in_frame(poly[0]):
                out.append(" ".join(ring_path(r) for r in poly if in_frame(r)))
        return out
    lines = geom["coordinates"] if t == "MultiLineString" else [geom["coordinates"]]
    return [line_path(l) for l in lines if in_frame(l)]


# --- Sites ---------------------------------------------------------------
# (name, lon, lat, lane, label-dx, label-dy, anchor)
SITES = {
    306: [
        ("Djenné-Djenno", -4.55, 13.89, "wa", -10, 4, "end"),
        ("Nok", 8.0, 9.5, "wa", 10, 4, "start"),
        ("Sao towns", 14.5, 12.4, "wa", 10, 4, "start"),
        ("Forest zone · Akan ancestors", -1.6, 6.5, "wa", -10, 12, "end"),
        ("Carthage", 10.32, 36.85, "ga", -10, 4, "end"),
        ("Alexandria", 29.9, 31.2, "ga", 10, -4, "start"),
        ("Antony's desert", 32.35, 28.9, "ga", 10, 10, "start"),
        ("Meroë", 33.72, 16.93, "ga", 10, 4, "start"),
        ("Aksum", 38.72, 14.13, "ga", 10, 12, "start"),
        ("Garama", 13.0, 26.5, "ga", 10, 4, "start"),
        ("Silver Leaves", 30.5, -23.5, "ga", 10, 4, "start"),
        ("Rome", 12.5, 41.9, "wo", 10, 4, "start"),
        ("Nicomedia", 29.92, 40.77, "wo", 10, 4, "start"),
    ],
    786: [
        ("Kumbi Saleh (Ghana)", -8.0, 15.77, "wa", -10, 4, "end"),
        ("Djenné-Djenno", -4.55, 13.89, "wa", -10, 12, "end"),
        ("Gao", -0.05, 16.27, "wa", 8, -6, "start"),
        ("Kanem", 15.5, 13.5, "wa", 10, 4, "start"),
        ("Ilé-Ifẹ̀", 4.56, 7.48, "wa", 10, -4, "start"),
        ("Igbo-Ukwu", 7.02, 6.02, "wa", 10, 10, "start"),
        ("Forest zone · proto-Akan", -1.6, 6.5, "wa", -10, 12, "end"),
        ("Sijilmasa", -4.28, 31.28, "ga", -10, 4, "end"),
        ("Fez", -5.0, 34.03, "ga", -10, 4, "end"),
        ("Tahert", 1.32, 35.37, "ga", 10, -4, "start"),
        ("Kairouan", 10.1, 35.67, "ga", 10, 6, "start"),
        ("Fustat", 31.23, 30.0, "ga", 10, 4, "start"),
        ("Dongola", 30.75, 18.2, "ga", 10, 4, "start"),
        ("Aksum", 38.72, 14.13, "ga", 10, 12, "start"),
        ("Shanga", 41.1, -2.1, "ga", 10, 4, "start"),
        ("Madagascar settled", 47.0, -19.0, "ga", -10, -8, "end"),
        ("Lydenburg", 30.45, -25.1, "ga", 10, 4, "start"),
        ("Córdoba", -4.78, 37.88, "wo", 10, -6, "start"),
        ("Constantinople", 28.98, 41.0, "wo", 10, -4, "start"),
        ("Baghdad", 44.4, 33.3, "wo", 10, 4, "start"),
        ("Mecca", 39.8, 21.4, "wo", 10, 4, "start"),
    ],
}

CAPTIONS = {
    306: "Sites named in the AD 306 snapshot",
    786: "Sites named in the AD 786 snapshot",
}


def build(year, land, rivers, lakes):
    out = [f'<svg viewBox="0 0 {W} {H}" class="map" role="img" aria-label="{CAPTIONS[year]}">']
    out.append(f'<rect class="sea" x="0" y="0" width="{W}" height="{H}"/>')
    # graticule every 10 degrees
    for lat in range(-30, 50, 10):
        pts = [project(lon, lat) for lon in range(-25, 60, 2)]
        out.append('<path class="grat" d="M' + " L".join(f"{round(x,1)},{round(y,1)}" for x, y in pts) + '"/>')
    for lon in range(-20, 60, 10):
        pts = [project(lon, lat) for lat in range(-40, 50, 2)]
        out.append('<path class="grat" d="M' + " L".join(f"{round(x,1)},{round(y,1)}" for x, y in pts) + '"/>')
    out.append('<g class="land-g">')
    for f in land["features"]:
        for d in geometry_paths(f["geometry"], "poly"):
            if d.strip():
                out.append(f'<path class="land" d="{d}"/>')
    out.append('</g><g class="lake-g">')
    for f in lakes["features"]:
        if (f["properties"].get("name") or "") in LAKES:
            for d in geometry_paths(f["geometry"], "poly"):
                if d.strip():
                    out.append(f'<path class="lake" d="{d}"/>')
    out.append('</g><g class="river-g">')
    for f in rivers["features"]:
        if (f["properties"].get("name") or "") in RIVERS:
            for d in geometry_paths(f["geometry"], "line"):
                out.append(f'<path class="river" d="{d}"/>')
    out.append('</g>')
    # Sahara label and a few sea labels
    def lbl(lon, lat, text, cls="geo"):
        x, y = project(lon, lat)
        out.append(f'<text class="{cls}" x="{x:.1f}" y="{y:.1f}" text-anchor="middle">{text}</text>')
    lbl(10, 22, "S A H A R A")
    lbl(-14, 32, "Atlantic", "geo sea-lbl")
    lbl(47, 3, "Indian Ocean", "geo sea-lbl")
    lbl(18, 36, "Mediterranean", "geo sea-lbl")
    out.append('<g class="sites">')
    for name, lon, lat, lane, dx, dy, anchor in SITES[year]:
        x, y = project(lon, lat)
        out.append(f'<circle class="site site-{lane}" cx="{x:.1f}" cy="{y:.1f}" r="6"/>')
        out.append(f'<text class="site-lbl" x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anchor}">{name}</text>')
    out.append('</g></svg>')
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data")
    ap.add_argument("--out", default="../illustrations")
    a = ap.parse_args()
    land, rivers, lakes = load(a.data, "land"), load(a.data, "rivers"), load(a.data, "lakes")
    os.makedirs(a.out, exist_ok=True)
    for year in (306, 786):
        svg = build(year, land, rivers, lakes)
        path = os.path.join(a.out, f"map-{year}.svg")
        with open(path, "w") as f:
            f.write(svg)
        print(path, len(svg), "bytes")


if __name__ == "__main__":
    main()
