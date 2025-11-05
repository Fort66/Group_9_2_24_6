from pygame import Surface
from pygame.key import get_pressed
from pygame.locals import K_w, K_a, K_s, K_d, K_UP, K_LEFT, K_DOWN, K_RIGHT

from .class_Screen import Screen

scr = Screen()

class Player:
    def __init__(self):
        self.image = Surface((50, 50))
        self.image.fill('Navy')
        self.rect = self.image.get_rect(center=(
            scr.screen.get_width() // 2,
            scr.screen.get_height() // 2
        ))
        self.speed = 10

    def move(self):
        keys = get_pressed()
        if keys[K_w] or keys[K_UP]:
            self.rect.move_ip(0, -self.speed)

        if keys[K_a] or keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)

        if keys[K_s] or keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)

        if keys[K_d] or keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= scr.screen.get_width():
            self.rect.right = scr.screen.get_width()

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= scr.screen.get_height():
            self.rect.bottom = scr.screen.get_height()

    def update(self):
        self.move()
        self.check_position()
        scr.screen.blit(self.image, self.rect)
