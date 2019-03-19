import pygame as pg
import math
import numpy as np
import colors


class Board:
    point_cloud = {}
    # Keys are the cells in the locations and the value is the position (x, y)

    def __init__(self,
                 screen,
                 color,
                 cell_size=20,  # size is radius.
                 wall_thickness=1):
        # Generate a board with a hex grid.
        self.screen = screen
        self.size = screen.get_size()
        self.color = color
        self.cell_radius = cell_size
        self.wall_thickness = wall_thickness

        self.cell_width = 2 * self.cell_radius
        self.cell_height = int((self.cell_width / 2 * math.sqrt(3)))
        self.point_cloud[(0, 0)] = (int(self.cell_radius),
                                    int(self.cell_height / 2))

        # Functions to build a grid
        self.generate_point_cloud()

    def generate_point_cloud(self):
        # Used to generate the center points for all further grid development
        start = self.point_cloud[(0, 0)]
        # Workable finds largest area where a hex cell looks the best.
        workable_area = tuple(np.add(self.size, start))

        # Figure out the exact area of the screen we want to work in.
        cells_horizontal = int(workable_area[0] / (1.5 * self.cell_radius))
        cells_vertical = int(workable_area[1] / self.cell_height)

        # These caught values are speed improvements for centering the grid.
        x_caught = False
        y_caught = False
        x_offset = 0
        y_offset = 0
        # Todo: Figure out the centering function
        for y in range(cells_vertical):
            # figure out the y position component
            y_pos = int(y * self.cell_height) + start[1]
            # make sure a cell drawn at this pos will not overflow the screen
            if y_pos + int(self.cell_height/2) < self.size[1]:
                for x in range(cells_horizontal):
                    # set up useful variables
                    width_addition = x * int(self.cell_radius * 1.5)
                    x_pos = width_addition + int(self.cell_radius)
                    # Again, make sure to check screen overflow
                    if x_pos + self.cell_radius < self.size[0]:
                        # This is important to keep initial y pos clean.
                        new_y_pos = y_pos
                        # If here is for offset hex grid.
                        if x % 2 is not 0:
                            new_y_pos = y_pos + int(self.cell_height/2)
                        new_pos = (x_pos, new_y_pos)
                        self.point_cloud[x, y] = new_pos
                    elif x_caught is False:
                        # Todo: Why is this coming up neg?
                        # we are here to capture values for centering the grid
                        x_caught = True
                        x_temp = abs(self.size[0] - x_pos)
                        x_offset = int(x_temp - int(self.cell_radius / 2) / 2)
            elif y_caught is False:
                # todo: X came up neg, will this one to?
                # now that we have overflown the screen, lets center the grid.
                y_caught = True
                y_temp = abs(self.size[1] - y_pos)
                y_offset = int(y_temp - int(self.cell_height / 2) / 2)
        print(x_offset, y_offset)
        # todo: Fix the center stuff. It has not worked yet.
        # self.__center_cloud(x_offset, y_offset)
        self.draw_grid()

    def __center_cloud(self, x_dis, y_dis):
        for loc_key, pos_value in self.point_cloud.items():
            new_pos = tuple(np.add(pos_value, (x_dis, y_dis)))
            self.point_cloud[loc_key] = new_pos

    def draw_grid(self):
        for loc_key, pos_value in self.point_cloud.items():
            self.__draw_hex(pos_value)

    def __draw_hex(self, pos):
        # First figure out the 6 positions of the hex.
        # numbered 0-5 from left most point going clockwise.
        r = self.cell_radius
        wall = self.wall_thickness
        height = math.sin(math.radians(60))
        pos0 = (pos[0] - r, pos[1])
        pos1 = (pos[0] - (r/2), pos[1] + (r * height))
        pos2 = (pos[0] + (r/2), pos[1] + (r * height))
        pos3 = (pos[0] + r, pos[1])
        pos4 = (pos[0] + (r/2), pos[1] - (r * height))
        pos5 = (pos[0] - (r/2), pos[1] - (r * height))

        pg.draw.line(self.screen, self.color, pos0, pos1, wall)
        pg.draw.line(self.screen, self.color, pos1, pos2, wall)
        pg.draw.line(self.screen, self.color, pos2, pos3, wall)
        pg.draw.line(self.screen, self.color, pos3, pos4, wall)
        pg.draw.line(self.screen, self.color, pos4, pos5, wall)
        pg.draw.line(self.screen, self.color, pos5, pos0, wall)

    def select_cell(self, mouse_pos):
        # Todo: The entire block here is broken. Fix it.
        # Highlight the cell where the mouse position is above
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        rounded_x = round(mouse_x / self.cell_width)
        wanted_cell_x = rounded_x * self.cell_width
        print(wanted_cell_x)
        temp = [(x, y) for x, y in self.point_cloud if x == mouse_x]
        # print(temp)
        if [(x, y) for x, y in self.point_cloud if x == mouse_x]:
            pg.draw.circle(self.screen, colors.GREEN, (mouse_x, mouse_y), 1, 1)
        # theory_x = int(mouse_x / self.cell_width)
        # theory_y = int(mouse_y / self.cell_height)
        # theory_pos = (theory_x, theory_y)
        # print(theory_pos)
        # pg.draw.circle(self.screen, self.color, theory_pos, 1, 1)

        pass

    def convert_pos_to_center(self, pos):
        # Todo: Convert the pos into the point_cloud key's and get key's value
        temp_x = 0
        temp_y = 0
        for x,y in pos:
            temp_x = x / self.cell_width




