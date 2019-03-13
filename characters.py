import pygame as pg
import colors


class Character:
    def __init__(self, screen, location):
        # Todo: understand what functions may be shared between player and enemy
        # Todo: how does the location interact with the mouse pos?
        # todo: generate move sets. Find a way to pass moves into the character.
        # todo: make Character an ABC (abstract base class)
        pass


class Player:
    status = 'dead'
    player_size = 10

    def __init__(self, screen, pos):
        # todo: mouse is passed in for pos, should we set pos as a standard?
        self.status = 'alive'
        self.playerExists = True
        self.screen = screen
        self.pos = pos
        self.__draw_player()

    def kill_player(self):
        self.status = 'dead'
        self.__draw_player()
        self.__draw_deathmark(style='cross')

    def __draw_player(self):
        if self.status == 'alive':
            pg.draw.circle(self.screen,
                           colors.WHITE,
                           self.pos,
                           self.player_size)
        elif self.status == 'dead':
            pg.draw.circle(self.screen,
                           colors.BLACK,
                           self.pos,
                           self.player_size)

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


class Enemy:
    def __init__(self):
        pass

    # todo: Generate Enemy appearance
    # todo: Make enemy aware of player
