import os.path
from constants import *

import pygame


class Helikopter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wysokosc = 30
        self.szerokosc = 50
        self.ksztalt = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.grafika = pygame.image.load(os.path.join('helikopter.png'))

    def rysuj(self):
        screen.blit(self.grafika, (self.x, self.y))

    def ruch(self, v):
        self.y = self.y + v
        self.ksztalt = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
