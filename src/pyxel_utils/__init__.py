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


_cursor_visible = False


def cursor_visible(visible: bool) -> None:
    """
    Sets the visibility of the cursor.
    """
    global _cursor_visible
    _cursor_visible = visible


def cursor_update(*, toggle_key=pyxel.KEY_T) -> None:
    """
    Toggles the visibility of the cursor when the given key is pressed.

    :param int toggle_key: The key that toggles the cursor visibility.
    """
    global _cursor_visible
    if pyxel.btnp(toggle_key):
        _cursor_visible = not _cursor_visible


def cursor_draw(col_bg: int = 0, col_fg: int = 1) -> None:
    """
    The cursor is a small circle with the current mouse position displayed
    next to it.

    :param int col_bg: The color of the background behind the cursor position text.
    :param int col_fg: The color of the cursor position text.
    """
    if not _cursor_visible:
        return

    text = f"{pyxel.mouse_x} {pyxel.mouse_y}"
    text_width = len(text) * pyxel.FONT_WIDTH

    x = pyxel.mouse_x
    y = pyxel.mouse_y + pyxel.FONT_HEIGHT
    if x + text_width > pyxel.width:
        x = pyxel.width - text_width
    if y + pyxel.FONT_HEIGHT > pyxel.height:
        y = pyxel.height - pyxel.FONT_HEIGHT * 2

    pyxel.rect(x - 1, y - 1, text_width + 1, pyxel.FONT_HEIGHT + 1, col_bg)
    pyxel.text(x, y, text, col_fg)
    pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 2, col_bg)
    pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, 1, col_fg)


def text_centered(
    x: int, y: int, text: str, col: int, font: pyxel.Font | None = None
) -> None:
    """
    Draws text horizontally centered at the given x, y position.
    """
    pyxel.text(x - (len(text) * pyxel.FONT_WIDTH / 2), y, text, col, font)
