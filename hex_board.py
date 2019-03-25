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
        workable_area = tuple(np.subtract(self.size, start))

        # Figure out the exact area of the screen we want to work in.
        cells_horizontal = int(workable_area[0] / (1.5 * self.cell_radius))
        cells_vertical = int(workable_area[1] / self.cell_height)

        # These caught values are speed improvements for centering the grid.
        x_caught = False
        y_caught = False
        x_offset = 0
        y_offset = 0

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
                    if y_pos + int(self.cell_height/2) < self.size[0]:
                        # This is important to keep initial y pos clean.
                        new_y_pos = y_pos
                        # If here is for offset hex grid.
                        if x % 2 is not 0:
                            new_y_pos = y_pos + int(self.cell_height/2)
                        new_pos = (x_pos, new_y_pos)
                        self.point_cloud[x, y] = new_pos
                    elif x_caught is False:
                        # we are here to capture values for centering the grid
                        x_caught = True
                        x_offset = x_pos
            elif y_caught is False:
                # now that we have overflown the screen, lets center the grid.
                y_caught = True
                y_offset = y_pos
        self.__center_cloud(x_offset, y_offset)
        self.draw_grid()

    def __center_cloud(self, x_dis, y_dis):
        temp_x = 0
        temp_y = 0
        x_offset = 0
        y_offset = 0
        if x_dis != 0:
            temp_x = abs(x_dis - self.size[0])
            if x_dis > self.size[0]:
                x_offset = int((self.cell_radius - temp_x) / 2)
            else:
                x_offset = int((temp_x + (self.cell_radius / 2)) / 2)

        if y_dis != 0:
            temp_y = abs(y_dis - self.size[1])
            if y_dis > self.size[1]:
                y_offset = int(((self.cell_height / 2) - temp_y / 2))
            else:
                y_offset = int((temp_y + (self.cell_height / 2)) / 2)

        print(x_dis, temp_x)
        print(y_dis, temp_y)

        print(x_offset, y_offset)
        for loc_key, pos_value in self.point_cloud.items():
            new_pos = tuple(np.add(pos_value, (x_offset, y_offset)))
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

        # An interesting drawing that I dont want to loose.
        # pg.draw.circle(self.screen, colors.RED, pos, self.cell_height, 1)

    # Todo: Change this name to a better one.
    def convert_pos_to_cloud(self, pos):
        try:
            x = int(pos[0] / (self.cell_radius * 1.5))
            temp_y = pos[1]
            if x % 2 is not 0:
                temp_y += int(self.cell_height / 2)
            y = int(temp_y / self.cell_height)
            neighbors = self.cell_neighbors((x, y))

            largest = max(self.point_cloud)
            measured_dis = 1000000
            final_value = (x, y)
            for value in neighbors:
                # First two If's check neighbor list for good dict keys.
                if not 0 <= value[0] <= largest[0]:
                    pass
                elif not 0 <= value[1] <= largest[1]:
                    pass
                else:
                    temp_pos = self.point_cloud[value]
                    distance = math.hypot((temp_pos[0] - pos[0]),
                                          temp_pos[1] - pos[1])
                    if distance < measured_dis:
                        final_value = value
                        measured_dis = distance

            pg.draw.circle(self.screen,
                           colors.GREEN,
                           self.point_cloud[final_value],
                           int(self.cell_height/2),
                           3)
        except KeyError:
            pass

    def cell_neighbors(self, cell_key):
        # outputs a list of cell neighbor keys.
        # Can be iter through to check each cell
        # Output[0] is cell_key. The rest are arbitrary.
        output = list()
        output.append(cell_key)
        if cell_key[0] % 2 is 0:
            output.append((cell_key[0] - 1, cell_key[1] - 1))
            output.append((cell_key[0] + 1, cell_key[1]))
            output.append((cell_key[0] - 1, cell_key[1]))
            output.append((cell_key[0] + 1, cell_key[1] - 1))
        else:
            output.append((cell_key[0] - 1, cell_key[1]))
            output.append((cell_key[0] + 1, cell_key[1] + 1))
            output.append((cell_key[0] - 1, cell_key[1] + 1))
            output.append((cell_key[0] + 1, cell_key[1]))
        output.append((cell_key[0], cell_key[1] + 1))
        output.append((cell_key[0], cell_key[1] - 1))
        return output
