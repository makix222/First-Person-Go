import pygame as pg
import math


class Board:
    point_cloud = []

    def __init__(self, screen, color, cell_size=20, cell_count=1):
        # Generate a board with a hex grid.
        self.screen = screen
        self.size = screen.get_size()
        self.color = color
        self.cell_size = cell_size
        self.cell_count = cell_count
        self.generate_point_cloud()

    def generate_point_cloud(self):
        # Used to generate the center points for all further grid development

        cell_width = self.cell_size * 2
        cell_height_radius = (self.cell_size * math.sqrt(3))
        cell_working_height = cell_height_radius / 2
        cells_horizontal = int(self.size[0] / (1.5 * cell_width)) + 1
        cells_vertical = int( self.size[1] / cell_working_height)

        for y in range(cells_vertical):
            y_pos = int((y * (cell_height_radius/2)) + cell_working_height)
            for x in range(cells_horizontal):
                x_pos = (x * int((cell_width * 1.5))) + int(cell_width / 2)
                if y % 2 != 0:
                    x_pos += int(self.cell_size * 1.5)
                new_pos = (x_pos, y_pos)
                self.point_cloud.append(new_pos)

        self.draw_grid(self.point_cloud)

    def draw_grid(self, point_cloud):
        for pos in point_cloud:
            self.__draw_hex(pos)

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

        # pg.draw.circle(self.screen, self.color, pos, 1, 1)

        pg.draw.line(self.screen, self.color, pos0, pos1)
        pg.draw.line(self.screen, self.color, pos1, pos2)
        pg.draw.line(self.screen, self.color, pos2, pos3)
        pg.draw.line(self.screen, self.color, pos3, pos4)
        pg.draw.line(self.screen, self.color, pos4, pos5)
        pg.draw.line(self.screen, self.color, pos5, pos0)
