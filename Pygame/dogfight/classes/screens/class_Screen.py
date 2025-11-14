import pygame as pg

from pygame.display import set_mode, set_caption

class Screen:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.screen = set_mode([1920, 768], pg.DOUBLEBUF)
        self.caption = set_caption("My Game")



win = Screen()