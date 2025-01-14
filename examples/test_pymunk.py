import pyxel
from pyxel_utils.pymunk import DrawOptions
import pymunk


pyxel.init(690, 400)
space = pymunk.Space()
space.gravity = pymunk.Vec2d(0, 2000)
draw_options = DrawOptions(10)

static = [
    pymunk.Segment(space.static_body, (10, 50), (300, 50), 3),
    pymunk.Segment(space.static_body, (300, 50), (325, 50), 3),
    pymunk.Segment(space.static_body, (325, 50), (350, 50), 3),
    pymunk.Segment(space.static_body, (350, 50), (375, 50), 3),
    pymunk.Segment(space.static_body, (375, 50), (680, 50), 3),
    pymunk.Segment(space.static_body, (680, 50), (680, 370), 3),
    pymunk.Segment(space.static_body, (680, 370), (10, 370), 3),
    pymunk.Segment(space.static_body, (10, 370), (10, 50), 3),
]
platforms = [
    pymunk.Segment(space.static_body, (170, 50), (270, 150), 3),
    pymunk.Segment(space.static_body, (400, 150), (450, 150), 3),
    pymunk.Segment(space.static_body, (400, 200), (450, 200), 3),
    pymunk.Segment(space.static_body, (220, 200), (300, 200), 3),
    pymunk.Segment(space.static_body, (50, 250), (200, 250), 3),
    pymunk.Segment(space.static_body, (10, 370), (50, 250), 3),
]
space.add(*static, *platforms)

for x in static + platforms:
    x.friction = 1

body = pymunk.Body(1, float("inf"))
body.position = 100, 100
shape = pymunk.Circle(body, 10)
shape.friction = 1
space.add(body, shape)


def update():
    if pyxel.btn(pyxel.KEY_LEFT):
        body.velocity = (-200, body.velocity.y)
    if pyxel.btn(pyxel.KEY_RIGHT):
        body.velocity = (200, body.velocity.y)
    if pyxel.btnp(pyxel.KEY_SPACE):
        body.apply_impulse_at_local_point((0, -400), (0, 0))

    space.step(1 / 60)


def draw():
    pyxel.cls(0)
    space.debug_draw(draw_options)


pyxel.run(update, draw)
