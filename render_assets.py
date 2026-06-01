"""Render the Naiad add-on logo.png from naiad/logo.svg.

logo.svg is the source of truth for the brand artwork (petrol water drop with
wave lines, grass blades and the "Naiad" wordmark). Home Assistant apps/add-ons
display PNG branding only — the Supervisor and store do not render SVG — so this
script rasterises the SVG to naiad/logo.png. Run it whenever logo.svg changes.

The SVG has a transparent background and a near-white wordmark, so it is
composited onto the brand's dark "pond" colour (#0c1413) to keep the wordmark
legible, matching the previous logo.png treatment.

Requires cairosvg + Pillow:  pip install cairosvg Pillow
"""

from __future__ import annotations

import io
import re

import cairosvg
from PIL import Image

SVG = "naiad/logo.svg"
PNG = "naiad/logo.png"
DARK = (12, 20, 19)  # --n-bg, the brand's dark background
SCALE = 2            # render the 680x300 viewBox at 2x -> 1360x600


def _viewbox(svg_text: str) -> tuple[float, float]:
    m = re.search(r'viewBox\s*=\s*"([\d.\s-]+)"', svg_text)
    _, _, w, h = (float(v) for v in m.group(1).split())
    return w, h


def main() -> None:
    with open(SVG, encoding="utf-8") as fh:
        svg_text = fh.read()
    vbw, vbh = _viewbox(svg_text)
    width, height = round(vbw * SCALE), round(vbh * SCALE)

    png_bytes = cairosvg.svg2png(
        bytestring=svg_text.encode("utf-8"),
        output_width=width,
        output_height=height,
    )
    rgba = Image.open(io.BytesIO(png_bytes)).convert("RGBA")

    # composite onto the dark brand background so the light wordmark stays legible
    bg = Image.new("RGBA", rgba.size, (*DARK, 255))
    Image.alpha_composite(bg, rgba).convert("RGB").save(PNG, "PNG", optimize=True)
    print(f"wrote {PNG} ({width}x{height})")


if __name__ == "__main__":
    main()
