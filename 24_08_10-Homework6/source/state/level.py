import os
import json
import math
import pygame as pg
from .. import tool

from .. import constants as c

bold_font = pg.font.SysFont("arial", 30, bold=True)


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
        map_file = 'level_' + str(self.game_info[c.LEVEL_NUM]) + '.json'
        file_path = os.path.join('source', 'data', 'map', map_file)
        f = open(file_path)
        self.map_data = json.load(f)
        f.close()

    def setup_background(self):
        self.background = tool.GFX['background']
        self.bg_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background, (int(self.bg_rect.width * c.BACKGROUND_MULTIPLER),
                                                               (int(self.bg_rect.height * c.BACKGROUND_MULTIPLER))))

        self.bg_rect = self.background.get_rect()
        self.bg_rect.y = -40

    def feather_edges(self, image, feather_width=5):
        """Feather the edges of an image to reduce harsh boundaries."""
        width, height = image.get_size()
        for x in range(width):
            for y in range(height):
                alpha = image.get_at((x, y)).a  # Directly access the alpha value
                if alpha > 0:
                    distance_to_edge = min(x, y, width - x - 1, height - y - 1)
                    if distance_to_edge < feather_width:
                        # Gradually reduce alpha closer to the edge
                        new_alpha = int(alpha * (distance_to_edge / feather_width))
                        image.set_at((x, y), (*image.get_at((x, y))[:3], new_alpha))
        return image

    def setup_sling(self):
        image = tool.get_image(tool.GFX['sling'], 0, 0, 50, 140, c.BLACK, 1)

        upscale_factor = 2
        new_width = int(image.get_width() * upscale_factor)
        new_height = int(image.get_height() * upscale_factor)

        upscaled_image = pg.transform.smoothscale(image, (new_width, new_height))
        downscaled_image = pg.transform.smoothscale(upscaled_image, (image.get_width(), image.get_height()))

        self.sling_image = self.feather_edges(downscaled_image, feather_width=2)

        self.sling_rect = self.sling_image.get_rect()
        self.sling_rect.x = 160
        self.sling_rect.y = 410


    def update(self, surface, current_time, mouse_pos, mouse_pressed):
        self.game_info[c.CURRENT_TIME] = self.current_time = current_time
        self.draw(surface)

    def draw(self, surface):
        surface.fill(c.GRASS_GREEN)
        surface.blit(self.background, self.bg_rect)

        surface.blit(self.sling_image, self.sling_rect)
