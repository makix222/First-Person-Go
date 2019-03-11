import pygame as pg
import colors

border_padding = 3
border_thickness = 2
edge_dim = border_thickness + border_padding

class DrawBoard:

    def __init__(self, screen, cell_type):
        size = screen.get_size()

        work_area = (edge_dim,
                     edge_dim,
                     size[0] - edge_dim,
                     size[1] - edge_dim)

        draw_border(screen, size)
        if cell_type == 'square':
            spot_size = 20
            for x in range(int(size[0]/spot_size) + 1):
                x_pos = x * spot_size
                pg.draw.line(screen,
                             colors.BLUE,
                             (x_pos, edge_dim),
                             (x_pos, size[1]-edge_dim),
                             1)

            for y in range(int(size[1] / spot_size) + 1):
                y_pos = y * spot_size
                pg.draw.line(screen,
                             colors.BLUE,
                             (edge_dim, y_pos),
                             (size[0]-edge_dim, y_pos),
                             1)

        elif cell_type == 'hex':
            pass


def draw_border(screen, size):
    border_dimensions = (border_padding,
                         border_padding,
                         size[0] - (2 * border_padding),
                         size[1] - (2 * border_padding))
    pg.draw.rect(screen,
                 colors.WHITE,
                 border_dimensions,
                 border_thickness)



