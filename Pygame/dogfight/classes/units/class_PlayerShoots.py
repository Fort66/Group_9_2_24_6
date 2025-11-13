import gif_pygame as gif
from gif_pygame import load
from gif_pygame.transform import flip, scale_by
from pygame.sprite import Sprite

from .class_Screen import win


class PlayerShoots(Sprite):
    def __init__(self, pos, speed):
        Sprite.__init__(self)
        self.speed = speed
        self.image = scale_by(
            flip(
                load('images/rocket.gif'),
                True,
                False,
                new_gif=True
                ),
            .4,
            new_gif=True
            )
        self._layer = 2
        self.rect = self.image.get_rect(center=pos)

    def move(self):
        self.rect.move_ip(self.speed, 0)

    def check_position(self):
        if self.rect.right >= win.screen.get_width() + 500:
            self.kill()

    def update(self):
        self.move()
        self.check_position()
        self.image.render(win.screen, self.rect)