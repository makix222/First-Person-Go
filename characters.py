import pygame as pg
import colors


class Player:
    status = 'dead'
    player_size = 10

    def __init__(self, screen, pos):
        self.status = 'alive'
        self.screen = screen
        self.pos = pos
        self.__draw_player()

    def kill_player(self):
        self.__draw_deathmark(style='cross')
        self.status = 'dead'

    def __draw_player(self):
        if self.status == 'alive':
            pg.draw.circle(self.screen, colors.WHITE, self.pos, self.player_size)

    def __draw_deathmark(self, style):
        if style == 'cross':
            center_pos = self.pos
            cross_1_start = (center_pos[0] - self.player_size,
                             center_pos[1] + self.player_size)
            cross_1_end = (center_pos[0] + self.player_size,
                           center_pos[1] - self.player_size)
            cross_2_start = (center_pos[0] - self.player_size,
                             center_pos[1] - self.player_size)
            cross_2_end = (center_pos[0] + self.player_size,
                           center_pos[1] + self.player_size)

            pg.draw.line(self.screen,
                         colors.RED,
                         cross_1_start,
                         cross_1_end, 4)
            pg.draw.line(self.screen,
                         colors.RED,
                         cross_2_start,
                         cross_2_end, 4)

