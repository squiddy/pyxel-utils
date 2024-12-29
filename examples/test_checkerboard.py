import pyxel
import pyxel_utils

pyxel.init(100, 100)


def update():
    pass


def draw():
    pyxel_utils.checkerboard(5, 9, 10)


pyxel.run(update, draw)
