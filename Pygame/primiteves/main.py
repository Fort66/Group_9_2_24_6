import pygame as pg

from pygame.locals import QUIT, RESIZABLE, KEYDOWN, MOUSEBUTTONDOWN, K_ESCAPE, FULLSCREEN

from pygame.display import set_mode, set_caption


pg.init()


# width = 1024
# height = 768

size = [1024, 768]


scr = set_mode(size)
set_caption('MyGame')


loop = True

while loop:

    # scr.fill('DarkOliveGreen')


    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    pg.draw.rect(scr, 'DarkRed', [100, 100, 100, 100], 1)
    pg.draw.line(scr, 'green', [50, 50], [250, 250], 1)
    pg.draw.aaline(scr, 'blue', [250, 50], [50, 250])

    pg.draw.lines(scr, 'orange', True, [[300, 300], [350, 300], [350, 350]], 1)
    pg.draw.aalines(scr, 'orange', True, [[300, 300], [350, 300], [350, 350]])

    pg.draw.polygon(scr, 'yellow', [[150, 210], [180, 250], [90, 290], [30, 230]], 1)


    pg.display.update()
pg.quit()
