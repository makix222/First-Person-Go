# Function display using pygame. Following the rough layout within this tutorial series
# http://programarcadegames.com/index.php?lang=en&chapter=bitmapped_graphics_and_sound
# and https://www.pygame.org/docs/
# Emerson Maki
# 03/06/2019

import pygame as pg


def drawSmallCircle(screen, x, y, key):
    pg.draw.circle(screen, GREEN, (x, y), 10, 10)
    if key:
        pg.draw.circle(screen, RED, (x, y), 5, 5)


pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = [700, 500]
screen = pg.display.set_mode(size)
pg.display.set_caption('Functions')
pg.mouse.set_visible(False)

done = False
clock = pg.time.Clock()
keyF = False

while not done:

    mousePress = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()

    # screen.fill(WHITE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                keyF = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_f:
                keyF = False

    if mousePress[0]:
        drawSmallCircle(screen, pos[0], pos[1], keyF)

    pg.display.flip()

    clock.tick(60)


pg.quit()
