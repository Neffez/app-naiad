"""Render the Naiad add-on logo.png and icon.png from naiad/logo.svg.

logo.svg is the source of truth for the brand artwork (petrol water drop with
wave lines, grass blades and the "Naiad" wordmark). Home Assistant apps/add-ons
display PNG branding only — the Supervisor and store do not render SVG — so this
script rasterises the SVG to PNG. Run it whenever logo.svg changes.

  * logo.png  — the full wide logo (drop + waves + grass + wordmark).
  * icon.png  — the square app icon: just the mark (drop + waves + grass),
                with the wordmark stripped and the artwork centred.

Both have a transparent background in the SVG (and the wordmark is near-white),
so they are composited onto the brand's dark "pond" colour (#0c1413) to stay
legible, matching the previous PNG treatment.

Requires cairosvg + Pillow:  pip install cairosvg Pillow
"""

from __future__ import annotations

import io
import re
import sys

import cairosvg
from PIL import Image

SVG = "naiad/logo.svg"
LOGO_PNG = "naiad/logo.png"
ICON_PNG = "naiad/icon.png"
DARK = (12, 20, 19)  # --n-bg, the brand's dark background
LOGO_SCALE = 2       # render the 680x300 viewBox at 2x -> 1360x600
ICON_SIZE = 256      # Home Assistant app icon is square

# Bounding box (in SVG user units) of the mark — the drop plus the grass blades
# below it, excluding the "Naiad" wordmark. The drop group sits at translate(185,
# 55) with local extents x:8..116, y:0..153 (-> 193..301, 55..208 global); the
# grass/ground occupies roughly x:218..278, y:170..210.
MARK_BOX = (193.0, 55.0, 301.0, 210.0)  # (minx, miny, maxx, maxy)
ICON_PAD = 18.0  # padding around the mark, in SVG user units


def _svg_size(svg_text: str) -> tuple[float, float]:
    m = re.search(r'viewBox\s*=\s*"([\d.\s-]+)"', svg_text)
    _, _, w, h = (float(v) for v in m.group(1).split())
    return w, h


def _render(svg_text: str, width: int, height: int) -> Image.Image:
    png_bytes = cairosvg.svg2png(
        bytestring=svg_text.encode("utf-8"),
        output_width=width,
        output_height=height,
    )
    return Image.open(io.BytesIO(png_bytes)).convert("RGBA")


def _flatten(rgba: Image.Image) -> bytes:
    """Composite onto the dark brand background, drop alpha, return PNG bytes."""
    bg = Image.new("RGBA", rgba.size, (*DARK, 255))
    flat = Image.alpha_composite(bg, rgba).convert("RGB")
    buf = io.BytesIO()
    flat.save(buf, "PNG", optimize=True)
    return buf.getvalue()


def logo_png(svg_text: str) -> bytes:
    vbw, vbh = _svg_size(svg_text)
    width, height = round(vbw * LOGO_SCALE), round(vbh * LOGO_SCALE)
    return _flatten(_render(svg_text, width, height))


def icon_png(svg_text: str) -> bytes:
    # Drop the wordmark and reframe to a square viewBox tightly around the mark.
    icon_svg = re.sub(r"<text\b.*?</text>", "", svg_text, flags=re.DOTALL)
    minx, miny, maxx, maxy = MARK_BOX
    cx, cy = (minx + maxx) / 2, (miny + maxy) / 2
    side = max(maxx - minx, maxy - miny) + 2 * ICON_PAD
    vb = f"{cx - side / 2} {cy - side / 2} {side} {side}"
    icon_svg = re.sub(r'viewBox\s*=\s*"[^"]*"', f'viewBox="{vb}"', icon_svg, count=1)
    return _flatten(_render(icon_svg, ICON_SIZE, ICON_SIZE))


# Each target PNG and the function that produces its bytes from the SVG.
TARGETS = ((LOGO_PNG, logo_png), (ICON_PNG, icon_png))


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    check = "--check" in argv

    with open(SVG, encoding="utf-8") as fh:
        svg_text = fh.read()

    stale = []
    for path, build in TARGETS:
        data = build(svg_text)
        if check:
            # Compare decoded pixels, not raw bytes: PNG is lossless, so this
            # ignores harmless encoder/zlib differences across environments.
            fresh = Image.open(io.BytesIO(data))
            try:
                committed = Image.open(path)
                committed.load()
            except FileNotFoundError:
                committed = None
            if committed is None or committed.tobytes() != fresh.tobytes():
                stale.append(path)
                print(f"OUT OF DATE: {path}")
            else:
                print(f"ok: {path}")
        else:
            with open(path, "wb") as fh:
                fh.write(data)
            print(f"wrote {path}")

    if check and stale:
        print(
            "\nPNG assets are out of date with logo.svg. "
            "Run `python render_assets.py` and commit the result.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
