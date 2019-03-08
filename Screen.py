# Function display using pygame. Following the rough layout within this tutorial series
# http://programarcadegames.com/index.php?lang=en&chapter=bitmapped_graphics_and_sound
# and https://www.pygame.org/docs/
# Emerson Maki
# 03/06/2019

import pygame as pg
import math
import random


def draw_small_circle(screen, x, y, key):
    pg.draw.circle(screen, GREEN, (x, y), 10, 10)
    if key:
        pg.draw.circle(screen, RED, (x, y), 5, 5)


def distance(start, end):

    dist = 0
    if len(start) == len(end) == 1:
        dist = abs(start - end)
    elif len(start) == len(end) == 2:
        # two points, (x1,y1) (x2,y2)
        # abs(x1 - x2)**2 + abs(y1 - y2)**2 = dist**2
        dist = math.sqrt(abs(start[0] - end[0]) ** 2 +
                         abs(start[1] - end[1]) ** 2)
    return dist


pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
JENNAS = (153, 50, 204)


sizeX = 700
sizey = 500
size = [sizeX, sizey]

screen = pg.display.set_mode(size)
pg.display.set_caption('Functions')
pg.mouse.set_visible(False)

done = False
clock = pg.time.Clock()
key_F = False
key_J = False
key_C = False

mouse_previous_pos = []

while not done:
    mouse_press = pg.mouse.get_pressed()
    mouse_current_pos = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                key_F = True
            elif event.key == pg.K_j:
                key_J = True
            elif event.key == pg.K_c:
                key_C = True

        elif event.type == pg.KEYUP:
            if event.key == pg.K_f:
                key_F = False
            elif event.key == pg.K_j:
                key_J = False
            elif event.key == pg.K_c:
                key_C = False

    if mouse_press[0]:
        draw_small_circle(screen, mouse_current_pos[0], mouse_current_pos[1], key_F)
        circleDistance = distance(mouse_current_pos, mouse_previous_pos)
        if circleDistance > 2:
            incrementDistance = circleDistance/10
            for val in range(math.ceil(circleDistance/10)):
                draw_small_circle(screen,
                                  mouse_current_pos[0]+val,
                                  mouse_current_pos[1]+val,
                                  key_F)

    if key_J:
        pg.draw.circle(screen,
                       JENNAS,
                       (random.randint(0, sizeX), random.randint(0, sizey)),
                       random.randint(40, 100),
                       random.randint(0, 39)
                       )

    if key_C:
        screen.fill(BLACK)

    previous_mouse_pos = mouse_current_pos
    pg.display.flip()

    clock.tick(160)


pg.quit()
