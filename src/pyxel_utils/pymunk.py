from typing import Sequence

import pyxel
import pymunk


class DrawOptions(pymunk.SpaceDebugDrawOptions):
    def __init__(self, color, *args, **kwargs):
        self.color = color
        super().__init__(*args, **kwargs)

    def draw_circle(
        self,
        pos: pymunk.Vec2d,
        angle: float,
        radius: float,
        outline_color: pymunk.space_debug_draw_options.SpaceDebugColor,
        fill_color: pymunk.space_debug_draw_options.SpaceDebugColor,
    ) -> None:
        pyxel.circb(pos.x, pos.y, radius, self.color)

    def draw_segment(
        self,
        a: pymunk.Vec2d,
        b: pymunk.Vec2d,
        color: pymunk.space_debug_draw_options.SpaceDebugColor,
    ) -> None:
        pyxel.line(a.x, a.y, b.x, b.y, self.color)

    def draw_fat_segment(
        self,
        a: pymunk.Vec2d,
        b: pymunk.Vec2d,
        radius: float,
        outline_color: pymunk.space_debug_draw_options.SpaceDebugColor,
        fill_color: pymunk.space_debug_draw_options.SpaceDebugColor,
    ) -> None:
        direction = b - a
        perp = direction.perpendicular_normal()

        xx, yy = a + perp * radius
        xx3, yy3 = b + perp * radius
        pyxel.line(xx, yy, xx3, yy3, self.color)

        xx2, yy2 = a - perp * radius
        xx24, yy4 = b - perp * radius
        pyxel.line(xx2, yy2, xx24, yy4, self.color)

        pyxel.circb(a.x, a.y, radius, self.color)
        pyxel.circb(b.x, b.y, radius, self.color)

    def draw_polygon(
        self,
        verts: Sequence[pymunk.Vec2d],
        radius: float,
        outline_color: pymunk.space_debug_draw_options.SpaceDebugColor,
        fill_color: pymunk.space_debug_draw_options.SpaceDebugColor,
    ) -> None:
        for i in range(len(verts)):
            self.draw_fat_segment(
                verts[i],
                verts[(i + 1) % len(verts)],
                radius,
                outline_color,
                fill_color,
            )

    def draw_dot(
        self,
        size: float,
        pos: pymunk.Vec2d,
        color: pymunk.space_debug_draw_options.SpaceDebugColor,
    ) -> None:
        pyxel.pset(pos.x, pos.y, self.color)
