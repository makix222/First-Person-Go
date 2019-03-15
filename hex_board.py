import pygame as pg
import math


class Board:

    def __init__(self, screen, color, cell_size, cell_count):
        # Generate a board with a hex grid.
        self.screen = screen
        self.size = screen.get_size()
        self.color = color
        self.cell_size = cell_size
        self.cell_count = cell_count

    def define_grid(self):
        # From the center of the screen, build the first hex.
        center = (int(self.size[0] / 2), int(self.size[1] / 2))
        print(center)  # todo: remove this
        self.__draw_hex(center)
        pass

    def __draw_hex(self, pos):
        # First figure out the 6 positions of the hex.
        # numbered 0-5 from left most point going clockwise.
        r = self.cell_size
        height = math.sin(math.radians(60))
        pos0 = (pos[0] - r, pos[1])
        pos1 = (pos[0] - (r/2), pos[1] + (r * height))
        pos2 = (pos[0] + (r/2), pos[1] + (r * height))
        pos3 = (pos[0] + r, pos[1])
        pos4 = (pos[0] + (r/2), pos[1] - (r * height))
        pos5 = (pos[0] - (r/2), pos[1] - (r * height))

        pg.draw.circle(self.screen, self.color, pos, 1, 1)

        pg.draw.line(self.screen, self.color, pos0, pos1)
        pg.draw.line(self.screen, self.color, pos1, pos2)
        pg.draw.line(self.screen, self.color, pos2, pos3)
        pg.draw.line(self.screen, self.color, pos3, pos4)
        pg.draw.line(self.screen, self.color, pos4, pos5)
        pg.draw.line(self.screen, self.color, pos5, pos0)
