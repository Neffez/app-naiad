"""Generate the Naiad add-on icon.png and logo.png from the brand tokens.

Draws the petrol/teal water drop with two wave lines on the dark "pond" background
(matching design/assets/naiad_logo.svg and the --n-* tokens), then composes the
square icon and the wide logo with wordmark. Run once; the PNGs are committed.
"""

from __future__ import annotations

from PIL import Image, ImageDraw, ImageFont

# Brand tokens (from naiad-tokens.css)
BG = (12, 20, 19)  # --n-bg dark
DROP = (26, 122, 138)  # --n-teal-600
WAVE1 = (94, 200, 216)  # --n-teal-300
WAVE2 = (184, 234, 242)
TEXT = (250, 249, 245)  # --n-card light / wordmark
SS = 4  # supersample factor for smooth edges


def _drop_polygon(cx: float, cy: float, w: float, h: float) -> list[tuple[float, float]]:
    """A teardrop outline: pointed apex at the top, rounded bulb at the bottom.

    The two straight sides leave the apex along the tangent lines to the bulb
    circle, so the silhouette is smooth where the sides meet the curve.
    """
    import math

    r = w / 2.0
    bulb_cy = cy + h / 2.0 - r  # centre of the round bottom
    apex_y = cy - h / 2.0
    d = bulb_cy - apex_y  # apex distance to bulb centre (> r)
    theta = math.acos(max(-1.0, min(1.0, r / d)))  # half-angle of the tangent contacts

    pts: list[tuple[float, float]] = [(cx, apex_y)]  # apex
    steps = 120
    a0, a1 = theta, 2 * math.pi - theta  # arc from right contact, round the bottom, to left
    for i in range(steps + 1):
        a = a0 + (a1 - a0) * i / steps
        pts.append((cx + r * math.sin(a), bulb_cy - r * math.cos(a)))
    return pts


def _draw_drop(draw: ImageDraw.ImageDraw, cx: float, cy: float, w: float, h: float) -> None:
    draw.polygon(_drop_polygon(cx, cy, w, h), fill=DROP)
    # two stylised waves across the bulb
    bw = w * 0.62
    for dy, color, width in ((0.10, WAVE1, max(2, int(w * 0.045))),
                             (0.26, WAVE2, max(1, int(w * 0.03)))):
        y = cy + h * dy
        x0 = cx - bw / 2
        draw.line(
            [
                (x0, y),
                (x0 + bw * 0.28, y - h * 0.05),
                (cx, y),
                (cx + bw * 0.28, y + h * 0.05),
                (x0 + bw, y),
            ],
            fill=color,
            width=width,
            joint="curve",
        )


def make_icon(path: str, size: int = 256) -> None:
    s = size * SS
    img = Image.new("RGBA", (s, s), (*BG, 255))
    draw = ImageDraw.Draw(img)
    _draw_drop(draw, cx=s / 2, cy=s / 2 - s * 0.02, w=s * 0.52, h=s * 0.66)
    img = img.resize((size, size), Image.LANCZOS)
    img.convert("RGB").save(path, "PNG")


def _font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for name in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def make_logo(path: str, width: int = 400, height: int = 160) -> None:
    w, h = width * SS, height * SS
    img = Image.new("RGBA", (w, h), (*BG, 255))
    draw = ImageDraw.Draw(img)
    dw, dh = h * 0.5, h * 0.64
    _draw_drop(draw, cx=h * 0.55, cy=h / 2, w=dw, h=dh)
    font = _font(int(h * 0.42))
    draw.text((h * 1.05, h / 2), "Naiad", font=font, fill=TEXT, anchor="lm")
    img = img.resize((width, height), Image.LANCZOS)
    img.convert("RGB").save(path, "PNG")


if __name__ == "__main__":
    make_icon("naiad/icon.png")
    make_logo("naiad/logo.png")
    print("wrote naiad/icon.png and naiad/logo.png")
