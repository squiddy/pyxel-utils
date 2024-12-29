import pyxel


def blt_topleft(
    x: float,
    y: float,
    img: int | pyxel.Image,
    u: float,
    v: float,
    w: float,
    h: float,
    colkey: int | None = None,
    *,
    rotate: float | None = None,
    scale: float | None = None,
) -> None:
    """
    Similar to `pyxel.blt`, but always places the image so that the top-left
    corner of the image is at the given x, y position.

    Does not support the `rotate` parameter.
    """
    if rotate is not None:
        raise ValueError("rotate is not supported")

    if scale is not None and scale != 1:
        x += w / 2.0 * (scale - 1)
        y += h / 2.0 * (scale - 1)

    pyxel.blt(x, y, img, u, v, w, h, colkey, rotate=rotate, scale=scale)
