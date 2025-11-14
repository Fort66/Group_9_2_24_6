from ..units.class_Player import Player
from ..units.class_Clouds import Clouds
from ..units.class_Enemies import Enemies

from random import choice


clouds_list = [
    'images/cloud2.png',
    'images/cloud3.png',
    'images/cloud4.png',
    'images/cloud5.png',
]


class CreateObject:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def create(self):
        self.player = Player()
        self.enemies = [Enemies() for _ in range(15)]
        self.clouds = [Clouds(choice(clouds_list)) for _ in range(15)]


create_object = CreateObject()