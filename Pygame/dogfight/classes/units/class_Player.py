from pygame.key import get_pressed
from pygame.locals import K_w, K_a, K_s, K_d, K_UP, K_LEFT, K_DOWN, K_RIGHT, K_c
from pygame.image import load
from pygame.transform import scale_by
from pygame.sprite import Sprite, groupcollide

from time import time

from ..groups.class_AllSprites import all_sprites
from ..groups.class_SpritesGroups import groups
from .class_PlayerShoots import PlayerShoots
from .class_Explosions import Explosions
from ..logic.class_Signals import signals

from ..screens.class_Screen import win

from icecream import ic

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = scale_by(load('images/su-33.png').convert_alpha(), .2)
        self.rect = self.image.get_rect(center=(
            win.screen.get_width() // 2,
            win.screen.get_height() // 2
        ))
        self._layer = 2
        self.speed = 5
        self.shoot_time = 1
        self.permission_shoot = 1
        groups.player_group.add(self)
        all_sprites.add(self)

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

        if keys[K_c]:
            if not self.shoot_time:
                self.shoot_time = time()
            if time() - self.shoot_time >= self.permission_shoot:
                shoot = PlayerShoots(
                    pos=(
                        self.rect.centerx - 46,
                        self.rect.centery + 10
                    ),
                    speed=10
                )
                groups.player_shoots_group.add(shoot)
                all_sprites.add(shoot)
                self.shoot_time = time()

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= win.screen.get_width():
            self.rect.right = win.screen.get_width()

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= win.screen.get_height():
            self.rect.bottom = win.screen.get_height()

    def collision(self):
        rockets_collide = groupcollide(groups.player_shoots_group, groups.enemies_group, True, True)
        if rockets_collide:
            hits = list(rockets_collide.keys())[0]
            self.rocket_explosion = Explosions(hits.rect.center, 1)
            self.rocket_explosion.speed = self.speed * -1

        player_collide = groupcollide(groups.player_group, groups.enemies_group, True, True)
        if player_collide:
            signals.change_signals('game_over')


    def update(self):
        self.move()
        self.check_position()
        self.collision()
        win.screen.blit(self.image, self.rect)
