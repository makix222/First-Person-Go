import pygame as pg
BLUE =   (0  , 0  , 255)


class DrawBoard():
    def __init__(self, screen):
        size = screen.get_size()
        spot_size = 20
        for x in range(int(size[0]/spot_size) + 1):
            x_pos = x * spot_size
            pg.draw.line(screen, BLUE, (x_pos, 0), (x_pos, size[1]), 1)

        for y in range(int(size[1] / spot_size) + 1):
            y_pos = y * spot_size
            pg.draw.line(screen, BLUE, (0, y_pos), (size[0], y_pos), 1)




