# Function display using pygame. Following the rough layout within this tutorial series
# http://programarcadegames.com/index.php?lang=en&chapter=bitmapped_graphics_and_sound
# and https://www.pygame.org/docs/
# Emerson Maki
# 03/06/2019

import pygame as pg


def drawSmallCircle(screen, x, y):
    pg.draw.circle(screen, BLACK, (x, y), 10, 10)


pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = [700, 500]
screen = pg.display.set_mode(size)
pg.display.set_caption('Functions')

done = False
clock = pg.time.Clock()

while not done:
    lineF = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                lineF = True

    if lineF:
        drawSmallCircle(screen, 100, 100)

    screen.fill(WHITE)

    pg.display.flip()

    clock.tick(60)


pg.quit()
