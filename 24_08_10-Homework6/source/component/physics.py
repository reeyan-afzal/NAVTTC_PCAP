import math
import pygame as pg
import pymunk as pm
from pymunk import Vec2d
from .. import tool
from .. import constants as c

COLLISION_BIRD = 1
COLLISION_PIG = 2
COLLISION_BLOCK = 3
COLLISION_LINE = 4
COLLISION_EXPLODE = 5
COLLISION_EGG = 6

BIRD_IMPULSE_TIMES = 3
MIN_DAMAGE_IMPULSE = 300


def to_pygame(p):
    """Convert position of pymunk to position of pygame"""
    return int(p.x), int(-p.y + 600)


def to_pymunk(x, y):
    return (x, -(y - 600))


class Physics():
    def __init__(self):
        self.reset()

    def reset(self, level=None):
        self.level = level
        self.space = pm.Space()
        self.space.gravity = (0.0, -700.0)
        self.dt = 0.002
        self.birds = []
        self.pigs = []
        self.blocks = []
        self.explodes = []
        self.eggs = []
        self.path_timer = 0
        self.check_collide = False
        self.explode_timer = 0
        self.setup_lines()
        self.setup_collision_handler()

    def setup_lines(self):
        # Static Ground
        x, y = to_pymunk(c.SCREEN_WIDTH, c.GROUND_HEIGHT)
        static_body = pm.Body(body_type=pm.Body.STATIC)
        static_lines = [pm.Segment(static_body, (0.0, y), (x, y), 0.0)]

        for line in static_lines:
            line.elasticity = 0.95
            line.friction = 1
            line.collision_type = COLLISION_LINE

        # Add both the body and the shapes to the space at the same time
        self.space.add(static_body, *static_lines)
        self.static_lines = static_lines

    def setup_collision_handler(self):
        def post_solve_bird_line(arbiter, space, data):
            if self.check_collide:
                bird_shape = arbiter.shapes[0]
                my_phy.handle_bird_collide(bird_shape, True)

        self.space.add_collision_handler(
            COLLISION_BIRD, COLLISION_LINE).post_solve = post_solve_bird_line

    def enable_check_collide(self):
        self.check_collide = True

    def add_bird(self, bird, distance, angle, x, y):
        x, y = to_pymunk(x, y)
        radius = bird.get_radius()
        phybird = PhyBird(distance, angle, x, y, self.space, bird.get_radius(), bird.mass)
        bird.set_physics(phybird)
        self.birds.append(bird)

    def update(self, game_info, level, mouse_pressed):
        birds_to_remove = []

        self.current_time = game_info[c.CURRENT_TIME]

        for x in range(5):
            self.space.step(self.dt)

        for bird in self.birds:
            bird.update(game_info, level, mouse_pressed)
            if (bird.phy.shape.body.position.y < 0 or bird.state == c.DEAD
                    or bird.phy.shape.body.position.x > c.SCREEN_WIDTH * 2):
                birds_to_remove.append(bird)
            else:
                poly = bird.phy.shape
                # the postion transferred from pymunk is the center position of pygame
                p = to_pygame(poly.body.position)
                x, y = p
                w, h = bird.image.get_size()
                # change to [left, top] position of pygame
                x -= w * 0.5
                y -= h * 0.5
                angle_degree = math.degrees(poly.body.angle)
                bird.update_position(x, y, angle_degree)
                self.update_bird_path(bird, p, level)

        for bird in birds_to_remove:
            self.space.remove(bird.phy.shape, bird.phy.shape.body)
            self.birds.remove(bird)
            bird.set_dead()

    def update_bird_path(self, bird, pos, level):
        if bird.path_timer == 0:
            bird.path_timer = self.current_time
        elif (self.current_time - bird.path_timer) > 50:
            bird.path_timer = self.current_time
            if not bird.collide:
                level.bird_path.append(pos)

    def handle_bird_collide(self, bird_shape, is_ground=False):
        for bird in self.birds:
            if bird_shape == bird.phy.shape:
                if is_ground:
                    if not (bird.name == c.BIG_RED_BIRD and bird.jump):
                        bird.phy.body.velocity = bird.phy.body.velocity * 0.7
                elif bird.name == c.BIG_RED_BIRD:
                    bird.jump = False
                bird.set_collide()

    def draw(self, surface):
        # Draw static lines

        for bird in self.birds:
            bird.draw(surface)


class PhyBird():
    def __init__(self, distance, angle, x, y, space, radius, mass):
        self.life = 10
        inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        body = pm.Body(mass, inertia)
        body.position = x, y
        power = distance * 53
        impulse = power * Vec2d(1, 0)
        angle = -angle
        body.apply_impulse_at_local_point(impulse.rotated(angle))

        shape = pm.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = COLLISION_BIRD
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def get_pygame_pos(self):
        return to_pygame(self.body.position)


# global parameter
my_phy = Physics()
