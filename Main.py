# Was initially a function visualizer.
# Now its a game \o/
# Using https://www.pygame.org/docs/
# Emerson Maki
# 03/06/2019

import pygame as pg
import math
import random
import hex_board
import colors
import characters
import time


def distance(start, end):
    # Todo: This is broken. Does it even need to be here? Pull into something?
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
pg.font.init()

size_X = 800
size_Y = 600
size = [size_X, size_Y]
background_color = colors.BLACK

screen = pg.display.set_mode(size)
screen.fill(background_color)
pg.display.set_caption('Functions')
pg.mouse.set_cursor(*pg.cursors.diamond)
gameboard = hex_board.Board(screen, colors.WHITE, cell_size=26, wall_thickness=3)

done = False
clock = pg.time.Clock()

key_F = False
key_J = False
key_C = False
key_N = False
key_K = False
key_T = False

mouse_previous_pos = pg.mouse.get_pos()

player_exists = False

count = 1
mouse_press = (None, None)
mouse_current_pos = mouse_press

while not done:
    mouse_press = pg.mouse.get_pressed()
    mouse_current_pos = pg.mouse.get_pos()
    mouse_distance = distance(mouse_current_pos,
                              mouse_previous_pos)

    # todo: Understand how to pull event logging into its own file.
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
            elif event.key == pg.K_n:
                key_N = True
            elif event.key == pg.K_k:
                key_K = True
            elif event.key == pg.K_t:
                key_T = True

        elif event.type == pg.KEYUP:
            if event.key == pg.K_f:
                key_F = False
            elif event.key == pg.K_j:
                key_J = False
            elif event.key == pg.K_c:
                key_C = False
            elif event.key == pg.K_n:
                key_N = False
            elif event.key == pg.K_k:
                key_K = False

    if mouse_press[0]:
        # Create player
        mouse_cloud = gameboard.convert_pos_to_cloud(mouse_current_pos)
        if not player_exists:
            Player = characters.Player(screen, mouse_cloud)
            player_exists = True

        # If player exists, Move player onto mouse location
        elif player_exists:
            Player.move_player(gameboard.convert_pos_to_cloud(mouse_current_pos))

    if key_J:
        pg.draw.circle(screen, colors.JENNAS,
                       (random.randint(0, size_X),
                        random.randint(0, size_Y)),
                       random.randint(40, 100),
                       random.randint(0, 39))

    if key_C:
        screen.fill(background_color)
        gameboard.draw_grid()

    if key_N:
        pass

    if key_K and player_exists:
        Player.kill_player()
        player_exists = False

    if player_exists:
        Player.pos
        gameboard.cell_neighbors(gameboard.convert_pos_to_cloud(Player.pos))

    pg.draw.circle(screen,
                   colors.JENNAS,
                   gameboard.cell_select(mouse_current_pos),
                   int(gameboard.cell_height / 2),
                   3)

    mouse_previous_pos = mouse_current_pos
    pg.display.flip()

    clock.tick(60)


pg.quit()
