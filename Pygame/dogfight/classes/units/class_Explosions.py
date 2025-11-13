import gif_pygame as gif

from gif_pygame import load
from gif_pygame.transform import flip, scale_by
from pygame.sprite import Sprite

from .class_Screen import win
from ..groups.class_AllSprites import all_sprites

class Explosions(Sprite):
    def __init__(self, pos, types):
        Sprite.__init__(self)
        self._layer = 2
        self.speed = 0

        if types == 1:
            self.image = scale_by(load('images/rocket_explosion.gif', loops=0), .5, new_gif=True)
        self.rect = self.image.get_rect(center=pos)
        all_sprites.add(self)

    def move(self):
        self.rect.move_ip(self.speed, 0)

    def update(self):
        if not self.image._ended:
            self.image.render(win.screen, self.rect)
        else:
            self.kill()
        self.move()