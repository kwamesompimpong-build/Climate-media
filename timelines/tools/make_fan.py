#!/usr/bin/env python3
"""Draw the pedigree-collapse fan as themable inline SVG.

One ring per generation back from 1986 (30 years each). Ring n has 2^n
ancestor slots; the fan marks the generation where those slots outnumber
everyone alive at the time, and the one where they outnumber everyone who
has ever lived. Standard library only.

    python3 make_fan.py --out ../illustrations
"""
import argparse, math, os

BIRTH = 1986
GEN = 30
MATTHEW, LUKE = 40, 56
EVER_LIVED = 117e9

# World population, rough (year, people)
POP = [(300, 190e6), (786, 250e6), (1000, 300e6), (1200, 400e6), (1500, 460e6),
       (1700, 600e6), (1800, 1.0e9), (1900, 1.6e9), (1986, 4.9e9)]


def pop_at(year):
    if year <= POP[0][0]:
        return POP[0][1]
    for (y0, p0), (y1, p1) in zip(POP, POP[1:]):
        if y0 <= year <= y1:
            return p0 + (p1 - p0) * (year - y0) / (y1 - y0)
    return POP[-1][1]


def human(n):
    if n < 1e6:
        return f"{int(n):,}"
    for unit, name in ((1e15, "quadrillion"), (1e12, "trillion"), (1e9, "billion"), (1e6, "million"), (1e3, "thousand")):
        if n >= unit:
            v = n / unit
            return (f"{v:.0f}" if v >= 10 else f"{v:.1f}") + " " + name
    return f"{int(n)}"


def arc(cx, cy, r, a0, a1):
    """Arc from angle a0 to a1 (degrees, 0 = east, counterclockwise on screen means angles measured with y up)."""
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    large = 1 if abs(a1 - a0) > 180 else 0
    return f"M{x0:.1f},{y0:.1f} A{r:.1f},{r:.1f} 0 {large} 1 {x1:.1f},{y1:.1f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="../illustrations")
    a = ap.parse_args()

    W, H = 1160, 640
    cx, cy = W / 2, H - 60
    r0, dr = 22, 9.2

    # crossover generations
    cross_alive = next(n for n in range(1, LUKE + 1) if 2 ** n > pop_at(BIRTH - GEN * n))
    cross_ever = next(n for n in range(1, LUKE + 1) if 2 ** n > EVER_LIVED)

    out = [f'<svg viewBox="0 0 {W} {H}" class="fan" role="img" aria-label="Pedigree fan: one ring per generation back from 1986, showing where ancestor slots outnumber the living">']
    out.append(f'<line class="fan-base" x1="{cx - r0 - LUKE*dr - 10:.0f}" y1="{cy}" x2="{cx + r0 + LUKE*dr + 10:.0f}" y2="{cy}"/>')

    for n in range(1, LUKE + 1):
        r = r0 + n * dr
        slots = 2 ** n
        cls = "ring"
        if n >= cross_ever:
            cls += " ring-ever"
        elif n >= cross_alive:
            cls += " ring-alive"
        if n > MATTHEW:
            cls += " ring-luke"
        if slots <= 256:
            gap = 1.2  # degrees of surface gap between segments
            seg = 180 / slots
            for i in range(slots):
                a0 = 180 - i * seg - gap / 2
                a1 = 180 - (i + 1) * seg + gap / 2
                if a0 - a1 < 0.4:
                    break
                out.append(f'<path class="{cls}" d="{arc(cx, cy, r, a0, a1)}"/>')
        else:
            out.append(f'<path class="{cls} ring-solid" d="{arc(cx, cy, r, 180, 0)}"/>')

    # "you" at the origin
    out.append(f'<circle class="fan-you" cx="{cx}" cy="{cy}" r="7"/>')
    out.append(f'<text class="fan-lbl" x="{cx}" y="{cy + 26}" text-anchor="middle">you · {BIRTH}</text>')

    # Labelled rings along the vertical spoke, alternating sides
    marks = [1, 10, 20, cross_alive, cross_ever, MATTHEW, LUKE]
    notes = {
        1: "your parents",
        10: "",
        20: "",
        cross_alive: "more slots than people alive that year",
        cross_ever: "more slots than humans who have ever lived",
        MATTHEW: "Matthew · your Abraham",
        LUKE: "Luke · your Abraham",
    }
    side = 1
    for n in marks:
        r = r0 + n * dr
        y = cy - r
        year = BIRTH - GEN * n
        x_dot = cx
        x_txt = cx + side * 16
        anchor = "start" if side > 0 else "end"
        out.append(f'<circle class="fan-mark" cx="{x_dot}" cy="{y:.1f}" r="3.5"/>')
        out.append(f'<line class="fan-lead" x1="{cx + side*6}" y1="{y:.1f}" x2="{cx + side*12}" y2="{y:.1f}"/>')
        head = f"gen {n} · AD {year} · {human(2**n)} slots"
        out.append(f'<text class="fan-lbl" x="{x_txt}" y="{y + 4:.1f}" text-anchor="{anchor}">{head}</text>')
        if notes[n]:
            out.append(f'<text class="fan-note" x="{x_txt}" y="{y + 18:.1f}" text-anchor="{anchor}">{notes[n]}</text>')
        side = -side

    out.append('</svg>')
    os.makedirs(a.out, exist_ok=True)
    path = os.path.join(a.out, "pedigree-fan.svg")
    with open(path, "w") as f:
        f.write("\n".join(out))
    print(path, "cross_alive", cross_alive, BIRTH - GEN * cross_alive, "cross_ever", cross_ever, BIRTH - GEN * cross_ever)


if __name__ == "__main__":
    main()
