# Illustration tools

The genealogy timeline page carries four programmatic illustrations.

**Python (standard library only)** writes themable SVG that is inlined into the page:

- `make_maps.py` draws the AD 306 and AD 786 site maps from Natural Earth 50m
  coastlines, rivers and lakes (downloaded on first run into `data/`), projected
  with a Lambert azimuthal equal-area centred on Africa.
- `make_fan.py` draws the pedigree-collapse fan: one ring per generation back
  from 1986, doubling each time, with the crossover generations marked.
- `inline_illustrations.py` pastes the generated SVGs between the
  `<!-- illus:NAME -->` markers in `../genealogy-timeline.html`.

```sh
python3 make_maps.py --data data --out ../illustrations
python3 make_fan.py --out ../illustrations
python3 inline_illustrations.py
```

**JavaScript (in the page itself)** draws the rest live on canvas: the
6,000-year loom, the fifty-six-thread descent strip, and the north-star
precession chart. Both canvases re-render on theme change.
