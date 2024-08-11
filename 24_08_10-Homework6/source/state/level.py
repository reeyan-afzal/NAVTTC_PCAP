import os
import json
import math
import pygame as pg
from .. import tool
from .. import constants as c
from ..component import bird

from ..component import physics

bold_font = pg.font.SysFont("arial", 30, bold=True)


def vector(p0, p1):
    """Return the vector of the points
       p0 = (xo,yo), p1 = (x1,y1)"""
    a = p1[0] - p0[0]
    b = p1[1] - p0[1]
    return (a, b)


def unit_vector(v):
    """Return the unit vector of the points
       v = (a,b)"""
    h = ((v[0] ** 2) + (v[1] ** 2)) ** 0.5
    if h == 0:
        h = 0.000000000000001
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
        self.score = self.game_info[c.SCORE]
        self.state = c.IDLE

        self.physics = physics.my_phy
        self.physics.reset(self)

        self.load_map()
        self.setup_background()
        self.setup_sling()

        self.setup_birds()

        self.over_timer = 0

    def load_map(self):
        map_file = 'level_' + str(self.game_info[c.LEVEL_NUM]) + '.json'
        file_path = os.path.join('source', 'data', 'map', map_file)
        f = open(file_path)
        self.map_data = json.load(f)
        f.close()

    def setup_background(self):
        self.background = tool.GFX['background']
        self.bg_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.bg_rect.width * c.BACKGROUND_MULTIPLER),
                                              int(self.bg_rect.height * c.BACKGROUND_MULTIPLER)))
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

    def setup_birds(self):
        self.birds = []
        y = c.GROUND_HEIGHT

        for i, data in enumerate(self.map_data[c.BIRDS]):
            x = 120 - (i * 35)
            tmp = bird.create_bird(data[c.TYPE], x, y)
            if tmp:
                self.birds.append(tmp)
        self.bird_path = []
        self.bird_old_path = []
        self.active_bird = None
        self.select_bird()

    def update(self, surface, current_time, mouse_pos, mouse_pressed):
        self.game_info[c.CURRENT_TIME] = self.current_time = current_time
        self.handle_states(mouse_pos, mouse_pressed)
        self.draw(surface)

    def handle_states(self, mouse_pos, mouse_pressed):
        if self.state == c.IDLE:
            self.handle_sling(mouse_pos, mouse_pressed)


        # ------------------------- bird path
        elif self.state == c.ATTACK:
            if self.active_bird.state == c.DEAD:
                self.active_bird = None
                self.select_bird()
                self.swith_bird_path()
                self.state = c.IDLE

        for bird in self.birds:
            bird.update(self.game_info, self, mouse_pressed)
        self.physics.update(self.game_info, self, mouse_pressed)

    def select_bird(self):
        if len(self.birds) > 0:
            self.active_bird = self.birds[0]
            self.active_bird.update_position(130, 426)

    def handle_sling(self, mouse_pos, mouse_pressed):
        if not mouse_pressed:
            if self.sling_click:
                self.sling_click = False

                xo = 154
                yo = 444
                self.physics.add_bird(self.active_bird, self.mouse_distance,
                                      self.sling_angle, xo, yo)

                self.active_bird.set_attack()
                self.birds.remove(self.active_bird)

                self.physics.enable_check_collide()
                self.state = c.ATTACK
        elif not self.sling_click:
            if mouse_pos:
                mouse_x, mouse_y = mouse_pos
                if (100 < mouse_x < 250 and
                        370 < mouse_y < 550):
                    self.sling_click = True

    def draw_sling_and_active_bird(self, surface):
        sling_x, sling_y = 135, 455
        sling2_x, sling2_y = 160, 455
        rope_length = 90
        bigger_rope = 102

        if self.sling_click:
            mouse_x, mouse_y = pg.mouse.get_pos()
            v = vector((sling_x, sling_y), (mouse_x, mouse_y))
            uv_x, uv_y = unit_vector(v)
            mouse_distance = tool.distance(sling_x, sling_y, mouse_x, mouse_y)
            pu = (uv_x * rope_length + sling_x, uv_y * rope_length + sling_y)

            if mouse_distance > rope_length:
                mouse_distance = rope_length
                pux, puy = pu
                pux -= 20
                puy -= 20
                pul = pux, puy
                pu2 = (uv_x * bigger_rope + sling_x, uv_y * bigger_rope + sling_y)
                pg.draw.line(surface, (0, 0, 0), (sling2_x, sling2_y), pu2, 5)

                self.active_bird.update_position(pux, puy)
                self.active_bird.draw(surface)

                pg.draw.line(surface, (0, 0, 0), (sling_x, sling_y), pu2, 5)

            else:
                mouse_distance += 10
                pu3 = (uv_x * mouse_distance + sling_x, uv_y * mouse_distance + sling_y)
                pg.draw.line(surface, (0, 0, 0), (sling2_x, sling2_y), pu3, 5)

                self.active_bird.update_position(mouse_x - 20, mouse_y - 20)
                self.active_bird.draw(surface)

                pg.draw.line(surface, (0, 0, 0), (sling_x, sling_y), pu3, 5)

            # angle of impulse
            dy = mouse_y - sling_y
            dx = mouse_x - sling_x

            if dx == 0:
                dx = 0.000000000000001
            self.sling_angle = math.atan((float(dy)) / dx)
            if mouse_x < sling_x + 5:
                self.mouse_distance = mouse_distance

            else:
                self.mouse_distance = -mouse_distance


        else:
            pg.draw.line(surface, (0, 0, 0), (sling_x, sling_y - 8), (sling2_x, sling2_y - 7), 5)

            if self.active_bird.state == c.IDLE:
                self.active_bird.draw(surface)

    def swith_bird_path(self):
        self.bird_old_path = self.bird_path.copy()
        self.bird_path = []

    def draw(self, surface):
        surface.fill(c.GRASS_GREEN)
        surface.blit(self.background, self.bg_rect)

        self.draw_sling_and_active_bird(surface)
        for bird in self.birds:
            bird.draw(surface)

        surface.blit(self.sling_image, self.sling_rect)
        self.physics.draw(surface)
