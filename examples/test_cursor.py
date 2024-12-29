import pyxel
import pyxel_utils

pyxel.init(100, 100)

pyxel_utils.cursor_visible(True)


def update():
    pyxel_utils.cursor_update()


def draw():
    pyxel.cls(2)
    pyxel_utils.cursor_draw()


pyxel.run(update, draw)
