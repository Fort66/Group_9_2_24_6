from pygame.image import load
from pygame.transform import scale_by
from pygame.sprite import Sprite

from ..screens.class_Screen import win
from ..groups.class_AllSprites import all_sprites
from ..groups.class_SpritesGroups import groups

from random import uniform, randint


class Enemies(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = scale_by(load('images/rocket.gif').convert_alpha(), .4)
        self.generate()
        self._layer = 2
        self.speed = randint(5, 10)
        groups.enemies_group.add(self)
        all_sprites.add(self)

    def move(self):
        if self.rect.left > - 100:
            self.rect.move_ip(-self.speed, 0)
        else:
            self.generate()


    def generate(self):
        self.rect = self.image.get_rect(center=(
            uniform(
                win.screen.get_width() + 1000, win.screen.get_width() + 5000),
            uniform(0, win.screen.get_height())
        ))

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)
