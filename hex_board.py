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
        self.draw_grid()

    def generate_point_cloud(self):
        # Used to generate the center points for all further grid development
        start = self.point_cloud[(0, 0)]
        # Workable finds largest area where a hex cell looks the best.
        workable_area = tuple(np.subtract(self.size, start))

        # Figure out the exact area of the screen we want to work in.
        cells_horizontal = int(workable_area[0] / (1.5 * self.cell_radius))
        cells_vertical = int(workable_area[1] / self.cell_height)

        for y in range(cells_vertical):
            # figure out the y position component
            y_pos = int(y * self.cell_height) + start[1]
            # make sure a cell drawn at this pos will not overflow the screen
            if y_pos + int(self.cell_height/2) <= self.size[1]:
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

    def __convert_centered_pos(self, input_pos):
        # Return a tuple that's been centered.

        last_key = max(self.point_cloud)
        last_value = self.point_cloud[last_key]

        # take last_point and figure out the horizontal point.
        # find difference between edge of last cell and screen edge
        horz_edge = last_value[0] + self.cell_radius
        horz_diff = abs(int((self.size[0] - horz_edge) / 2))

        # Now do the same check to see what the largest value[1] is
        # get the distance between cell edge and screen wall
        vert_edge = last_value[1] + int(self.cell_height / 2)
        if last_key[0] % 2 is 0:
            vert_edge = int(vert_edge + (self.cell_height / 2))
        vert_diff = abs(int((self.size[1] - vert_edge) / 2))

        if self.tuple_range(input_pos, self.size):
            new_pos = tuple(np.add(input_pos, (horz_diff, vert_diff)))
            return new_pos
        else:
            return input_pos

    def cell_select(self, mouse):
        # Take in the mouse pos, figure out the pos, transform it to centered
        temp = self.convert_pos_to_cloud(mouse)
        if temp is not None:
            return temp
        else:
            inhert_return = self.point_cloud[(0,0)]
            return inhert_return
        # return self.__convert_centered_pos(temp)

    def draw_grid(self):
        for loc_key, pos_value in self.point_cloud.items():
            # self.__draw_hex(self.__convert_centered_pos(pos_value))
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
        # Todo: Make this a loop?
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
        # Returns the tuple position of the cell which the given pos is in.
        try:
            # convert the pos to a point cloud position
            x = int(pos[0] / (self.cell_radius * 1.5))
            temp_y = pos[1]
            if x % 2 is not 0:
                temp_y += int(self.cell_height / 2)
            y = int(temp_y / self.cell_height)
            # now that is been converted, check for its neighbors
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

            return self.point_cloud[final_value]
        except KeyError:
            return None

    @staticmethod
    def cell_neighbors(cell_key):
        # outputs a list of cell neighbor keys.
        # Can be iter through to check each cell
        # Output[0] is cell_key. The rest are arbitrary.
        # Todo: Clean this up. It was made at midnight and I was not clever.
        output = list()
        output.append(cell_key)
        # Odd numbered cell columns look at neighbors differently.
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

    @staticmethod
    def tuple_range(input_tuple, range_tuple):
        # will output boolean if input is inside the range_tuple
        # assumes range starts at 0
        in_x = input_tuple[0]
        in_y = input_tuple[1]
        range_x = range_tuple[0]
        range_y = range_tuple[1]
        if 0 <= in_x <= range_x and 0 <= in_y <= range_y:
            return True
        else:
            return False
