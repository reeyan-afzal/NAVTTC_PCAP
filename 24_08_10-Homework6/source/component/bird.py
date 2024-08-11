import random
import pygame as pg
from .. import tool
from .. import constants as c


def create_bird(type, x, y):
    bird = None
    if type == c.RED_BIRD:
        bird = RedBird(x, y)

    return bird


class Bird():
    def __init__(self, x, y, name):
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.animate_interval = 100

        self.name = name
        self.load_images()
        self.frame_num = len(self.frames)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.angle_degree = 0
        self.state = c.IDLE
        self.old_pos = (self.rect.x, self.rect.y)
        self.pos_timer = 0
        self.path_timer = 0
        self.collide = False  # collided with ground or shape if it is True
        self.mass = 5.0

    def load_frames(self, sheet, frame_rect_list, scale, color=c.WHITE):
        frames = []
        for frame_rect in frame_rect_list:
            frames.append(tool.get_image(sheet, *frame_rect, color, scale))
        return frames

    def load_images(self):
        pass

    def update(self, game_info, level, mouse_pressed):
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state(level, mouse_pressed)
        self.animation()

    def handle_state(self, level, mouse_pressed):
        if self.state == c.IDLE:
            pass
        elif self.state == c.ATTACK:
            self.attacking(level, mouse_pressed)

    def attacking(self, level, mouse_pressed):
        pass

    def animation(self):

        image = self.frames[self.frame_index]
        self.image = pg.transform.rotate(image, self.angle_degree)

    def change_image(self, frames):
        self.frames = frames
        self.frame_num = len(self.frames)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.animate_timer = self.current_time

    def set_attack(self):
        self.state = c.ATTACK

    def set_physics(self, phy):
        self.phy = phy

    def set_collide(self):
        self.collide = True

    def set_dead(self):
        self.state = c.DEAD

    def get_radius(self):
        return self.rect.w // 2

    def update_position(self, x, y, angle_degree=0):
        self.rect.x = x
        self.rect.y = y
        self.angle_degree = angle_degree

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class RedBird(Bird):
    def __init__(self, x, y):
        Bird.__init__(self, x, y, c.RED_BIRD)

    def load_images(self):
        sheet = tool.GFX[c.BIRD_SHEET]
        frame_rect_list = [(184, 32, 66, 66), (258, 32, 66, 66), (332, 32, 66, 66),
                           (404, 32, 66, 66), (472, 32, 66, 66)]
        self.frames = self.load_frames(sheet, frame_rect_list, c.BIRD_MULTIPLIER)
