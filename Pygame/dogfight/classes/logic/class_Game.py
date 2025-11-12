import pygame as pg
from pygame.locals import QUIT, RESIZABLE, KEYDOWN, MOUSEBUTTONDOWN, K_ESCAPE, FULLSCREEN

from ..units.class_Screen import win

from ..units.class_Player import Player
from ..units.class_Enemies import Enemies
from ..units.class_Clouds import Clouds
from ..groups.class_AllSprites import all_sprites


from icecream import ic


player = Player()

enemies = [Enemies() for _ in range(15)]
clouds = [Clouds() for _ in range(15)]


class Game:
    def __init__(self):
        self.loop = True
        self.fps = 60
        self.clock = pg.time.Clock()

    def run(self):
        while self.loop:
            win.screen.fill('SkyBlue')

            for event in pg.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.loop = False

            all_sprites.update()


            pg.display.update()
            self.clock.tick(self.fps)


