import os
import json
import math
import pygame as pg
from .. import tool

from .. import constants as c

bold_font = pg.font.SysFont("arial", 30, bold=True)


def vector(p0, p1):
    """return the vector of the points p0 = (x0, y0) and p1 = (x1, y1)"""
    a = p1[0] - p0[0]
    b = p1[1] - p0[1]
    return (a, b)


def unit_vector(v):
    """magnitude"""
    h = ((v[0] ** 2) + (v[1] ** 2)) ** 0.5

    if h == 0:
        h = 0.000_000_000_000_000_1
    ua = v[0] / h
    ub = v[1] / h

    return (ua, ub)


class Level(tool.State):
    def __init__(self):
        tool.State.__init__(self)
        self.player = None

    def startup(self, current_time, persist):
        self.game_info = persist
        self.persist = self.game_info
        self.game_info[c.CURRENT_TIME] = current_time
        self.reset()

    def reset(self):
        self.state = c.IDLE
        self.load_map()
        self.setup_background()
        self.setup_sling()
        self.over_timer = 0

    def load_map(self):
        map_file = "level_" + str(self.game_info[c.LEVEL_NUM]) + ".json"
        file_path = os.path.join("source", "data", "map", map_file)
        f = open(file_path)
        self.map_data = json.load(f)
        f.close()

    def setup_background(self):
        self.background = tool.GFX["background"]
        self.bg_rect = self.background.get_rect()
        self.background = pg.transform.scale(
            self.background,
            (
                int(self.bg_rect.width * c.BACKGROUND_MULTIPLER),
                (int(self.bg_rect.height * c.BACKGROUND_MULTIPLER)),
            ),
        )

        self.bg_rect = self.background.get_rect()
        self.bg_rect.y = -40

    def feather_edges(self, image, feather_width=5):
        width, height = image.get_size()
        for x in range(width):
            for y in range(height):
                alpha = image.get_at((x, y)).a
                if alpha > 0:
                    distance_to_edge = min(x, y, width - x - 1, height - y - 1)
                    if distance_to_edge < feather_width:
                        new_alpha = int(alpha * (distance_to_edge / feather_width))
                        image.set_at((x, y), (*image.get_at((x, y))[:3], new_alpha))
        return image

    def setup_sling(self):
        image = tool.get_image(tool.GFX["sling"], 0, 0, 50, 140, c.BLACK, 1)

        upscale_factor = 2
        new_width = int(image.get_width() * upscale_factor)
        new_height = int(image.get_height() * upscale_factor)

        upscaled_image = pg.transform.smoothscale(image, (new_width, new_height))
        downscaled_image = pg.transform.smoothscale(
            upscaled_image, (image.get_width(), image.get_height())
        )

        self.sling_image = self.feather_edges(downscaled_image, feather_width=2)
        self.sling_rect = self.sling_image.get_rect()
        self.sling_rect.x = 130
        self.sling_rect.y = 415

        self.sling_click = False
        self.mouse_distance = 0
        self.sling_angle = 0

    def update(self, surface, current_time, mouse_pos, mouse_pressed):
        self.game_info[c.CURRENT_TIME] = self.current_time = current_time
        self.handle_states(mouse_pos, mouse_pressed)
        self.draw(surface)

    def handle_states(self, mouse_pos, mouse_pressed):
        if self.state == c.IDLE:
            self.handle_sling(mouse_pos, mouse_pressed)

    def handle_sling(self, mouse_pos, mouse_pressed):
        if not mouse_pressed:
            if self.sling_click:
                self.sling_click = False

        elif not self.sling_click:
            if mouse_pos:
                mouse_x, mouse_y = mouse_pos

                if 100 < mouse_x < 250 and 370 < mouse_y < 550:
                    self.sling_click = True

    def draw_sling_and_active_bird(self, surface):
        sling_x, sling_y = 135, 440
        sling2_x, sling2_y = 160, 440

        rope_length = 90
        bigger_rope = 102

        if self.sling_click:
            mouse_x, mouse_y = pg.mouse.get_pos()
            v = vector((sling_x, sling_y), (mouse_x, mouse_y))

            uv_x, uv_y = unit_vector(v)

            mouse_distance = tool.distance(sling_x, sling_y, mouse_x, mouse_y)

            if mouse_distance > rope_length:
                mouse_distance = rope_length

                pu2 = (uv_x * bigger_rope + sling_x, uv_y * bigger_rope + sling_y)

                pg.draw.line(surface, (0, 0, 0), (sling2_x, sling2_y), pu2, 5)
                pg.draw.line(surface, (0, 0, 0), (sling_x, sling_y), pu2, 5)


            else:
                mouse_distance += 10
                pu3 = (uv_x * mouse_distance + sling_x, uv_y * mouse_distance + sling_y)
                pg.draw.line(surface, (0, 0, 0), (sling2_x, sling2_y), pu3, 5)
                pg.draw.line(surface, (0, 0, 0), (sling_x, sling_y), pu3, 5)


        else:
            pg.draw.line(surface, (0, 0, 0), (sling_x, sling_y), (sling2_x, sling2_y), 5)

    def draw(self, surface):
        surface.fill(c.GRASS_GREEN)
        surface.blit(self.background, self.bg_rect)

        self.draw_sling_and_active_bird(surface)

        surface.blit(self.sling_image, self.sling_rect)
