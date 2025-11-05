from pygame import Surface

from .class_Screen import Screen

from random import uniform

scr = Screen()

class Enemies:
    def __init__(self):
        self.image = Surface((25, 5))
        self.image.fill('DarkRed')
        self.check_position()
        self.speed = 10

    def move(self):
        if self.rect.left > - 100:
            self.rect.move_ip(-self.speed, 0)
        else:
            self.check_position()


    def check_position(self):
        self.rect = self.image.get_rect(center=(
            uniform(
                scr.screen.get_width(), scr.screen.get_width() + 500),
            uniform(0, scr.screen.get_height())
        ))

    def update(self):
        self.move()
        self.check_position()
        scr.screen.blit(self.image, self.rect)
