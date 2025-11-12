from pygame.image import load
from pygame.transform import scale_by
from pygame.sprite import Sprite

from .class_Screen import win
from ..groups.class_AllSprites import all_sprites

from random import uniform, randint, choice


clouds_list = [
    'images/cloud2.png',
    'images/cloud3.png',
    'images/cloud4.png',
    'images/cloud5.png',
]


class Clouds(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = scale_by(load(choice(clouds_list)).convert_alpha(), .4)
        self.generate()
        self._layer = 2
        self.speed = randint(1, 2)
        all_sprites.add(self)

    def move(self):
        if self.rect.left > - 1000:
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
