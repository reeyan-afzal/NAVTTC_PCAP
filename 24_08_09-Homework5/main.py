import pygame, pymunk, pymunk.pygame_util, math

pygame.init()

WIDTH, HEIGHT = 1024, 768

window = pygame.display.set_mode((WIDTH, HEIGHT))


def draw(space, window, draw_option, line):
    window.fill("white")
    pygame.display.update()


def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps

    space = pymunk.Space()
    space.gravity = (0, 981)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    pressed_pos = None
    ball = None

    while run:
        line = None
        if ball and pressed_pos:
            line = [pressed_pos, pygame.mouse.get_pos()]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(space, window, draw_options, line)
        space.step(dt)
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)
