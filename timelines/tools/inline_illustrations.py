#!/usr/bin/env python3
"""Inline the generated SVG illustrations into genealogy-timeline.html.

Looks for  <!-- illus:NAME --> ... <!-- /illus -->  markers and replaces
whatever sits between them with ../illustrations/NAME.svg. Run after
make_maps.py and make_fan.py.
"""
import os, re, sys

here = os.path.dirname(os.path.abspath(__file__))
html = os.path.join(here, "..", "genealogy-timeline.html")
ill = os.path.join(here, "..", "illustrations")

s = open(html, encoding="utf-8").read()
def repl(m):
    name = m.group(1)
    svg = open(os.path.join(ill, name + ".svg"), encoding="utf-8").read().strip()
    return f"<!-- illus:{name} -->\n{svg}\n<!-- /illus -->"
new, n = re.subn(r"<!-- illus:([\w-]+) -->.*?<!-- /illus -->", repl, s, flags=re.S)
open(html, "w", encoding="utf-8").write(new)
print(f"inlined {n} illustrations; {len(new)} bytes")
