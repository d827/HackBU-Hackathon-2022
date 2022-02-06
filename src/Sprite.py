import sys
import pygame as pg
from pygame import *

class Sprite(pg.sprite.Sprite):
    def __init__(self, name, x, y, img):
        super().__init__()
        #pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(img)#.convert()
        self.name = ""
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def updateImg(self, img):
        self.image = pg.image.load(img)#.convert()

    def updateName(self, name):
        self.name = name;
