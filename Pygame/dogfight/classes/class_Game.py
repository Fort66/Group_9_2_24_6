import pygame as pg
from pygame.locals import QUIT, RESIZABLE, KEYDOWN, MOUSEBUTTONDOWN, K_ESCAPE, FULLSCREEN

from .class_Screen import Screen

from .class_Player import Player

from icecream import ic


player = Player()


scr = Screen()

class Game:
    def __init__(self):
        self.loop = True
        self.fps = 60
        self.clock = pg.time.Clock()

    def run(self):
        while self.loop:
            scr.screen.fill('SkyBlue')

            for event in pg.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.loop = False

            player.update()


            pg.display.update()
            self.clock.tick(self.fps)


