# Was initially a function visualizer.
# Now its a game \o/
# Using https://www.pygame.org/docs/
# Emerson Maki
# 03/06/2019

import pygame as pg
import math
import random
import board


def draw_small_circle(pos, key, radius):
    pg.draw.circle(screen, GREEN, pos, radius, 1)
    if key:
        pg.draw.circle(screen, RED, pos, 5, 5)


def distance(start, end):
    dist = 0
    if len(start) == len(end) == 1:
        dist = abs(start - end)
    elif len(start) == len(end) == 2:
        # two points, (x1,y1) (x2,y2)
        # abs(x1 - x2)**2 + abs(y1 - y2)**2 = dist**2
        dist = math.sqrt((abs(start[0] - end[0]) ** 2) +
                         (abs(start[1] - end[1]) ** 2))
    return dist


pg.init()

BLACK =  (0  , 0  , 0  )
WHITE =  (255, 255, 255)
GREEN =  (0  , 255, 0  )
RED =    (255, 0  , 0  )
BLUE =   (0  , 0  , 255)
JENNAS = (153, 50 , 204)


size_X = 700
size_Y = 500
size = [size_X, size_Y]
background_color = BLACK

screen = pg.display.set_mode(size)
screen.fill(background_color)
pg.display.set_caption('Functions')
pg.mouse.set_cursor(*pg.cursors.ball)

done = False
clock = pg.time.Clock()
key_F = False
key_J = False
key_C = False

mouse_previous_pos = pg.mouse.get_pos()

while not done:
    board.DrawBoard(screen)
    mouse_press = pg.mouse.get_pressed()
    mouse_current_pos = pg.mouse.get_pos()
    mouse_distance = distance(mouse_current_pos,
                              mouse_previous_pos)

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
        radius = 3
        pg.draw.line(screen, GREEN,
                     mouse_previous_pos,
                     mouse_current_pos,
                     radius)

    if key_J:
        pg.draw.circle(screen, JENNAS,
                       (random.randint(0, size_X),
                        random.randint(0, size_Y)),
                       random.randint(40, 100),
                       random.randint(0, 39)
                       )

    if key_C:
        screen.fill(background_color)

    mouse_previous_pos = mouse_current_pos
    pg.display.flip()

    clock.tick(60)


pg.quit()
