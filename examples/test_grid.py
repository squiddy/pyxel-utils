import pyxel
import pyxel_utils

pyxel.init(100, 100)


def update():
    pass


def draw():
    pyxel.cls(1)
    pyxel_utils.point_grid(5, 5, 3)


pyxel.run(update, draw)
