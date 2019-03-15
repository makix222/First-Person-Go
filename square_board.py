import pygame as pg
import colors
import numpy as np


class Board:
    border_padding = 3
    border_thickness = 2
    edge_dim = border_thickness + border_padding
    cell_size = 20
    center_of_cells = np.array([])
    board_grid = np.array([])

    def __init__(self, screen, board_type):
        self.size = screen.get_size()
        self.screen = screen
        self.board_type = board_type
        self.usable_size = (self.edge_dim, self.edge_dim)
        self.draw_board()
        self.draw_border()

    def draw_board(self):
        # todo: Draw the lines based upon the array board_grid
        pass
        # Todo:The entire block below me needs to be parsed into the
        #  two functions draw_board and define_board_grid

        # if self.cell_type == 'square':
        #     spot_size = 20
        #     for x in range(int(self.size[0]/spot_size) + 1):
        #         x_pos = x * spot_size
        #         pg.draw.line(self.screen,
        #                      colors.BLUE,
        #                      (x_pos, self.edge_dim),
        #                      (x_pos, self.size[1]-self.edge_dim),
        #                      1)
        #         self.center_of_cells = np.append(self.center_of_cells,
        #                   [x_pos - (spot_size/2)])
        #
        #     for y in range(int(self.size[1] / spot_size) + 1):
        #         y_pos = y * spot_size
        #         pg.draw.line(self.screen,
        #                      colors.BLUE,
        #                      (self.edge_dim, y_pos),
        #                      (self.size[0]-self.edge_dim, y_pos),
        #                      1)
        # elif self.board_type == 'hex':
        #     pass

    def __define_board_grid(self):
        # ToDo: Generate define_board_grid
        # Measure the size of the Surface
        # Calculate the usable area based upon the padding
        # Generate the board_grid array of starting and ending line locations
        # board_grid needs a component of which type of board.
        # Generate center_of_cells array during board_grid generation

        rows = self.size[0] / self.cell_size
        pass

    def draw_border(self):
        # ToDo: Figure out when to implement draw_border with hex
        #  and square grids

        # Here is a thought: What if we draw the border after the grid has
        # been made?
        border_dimensions = (self.border_padding,
                             self.border_padding,
                             self.size[0] - (2 * self.border_padding),
                             self.size[1] - (2 * self.border_padding))
        pg.draw.rect(self.screen,
                     colors.WHITE,
                     border_dimensions,
                     self.border_thickness)

    def __cell_position(self, mouse_pos):
        # todo: Figure out the cell which the mouse is over
        # returns the center pos of which cell the mouse is over
        # using center_of_cell array. Compare existing with mouse pos
        # with array values.

        pass



