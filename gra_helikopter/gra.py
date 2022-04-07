import random

import pygame
import os

pygame.init()

szer = 600
wys = 600
screen = pygame.display.set_mode((szer, wys))


def napisz(tekst, rozmiar):
    cz = pygame.font.SysFont("Arial", rozmiar)
    rend = cz.render(tekst, True, (70, 228, 191))
    x = (szer - rend.get_rect().width) / 2
    y = (wys - rend.get_rect().height) / 2
    screen.blit(rend, (x, y))


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


class Przeszkoda:
    def __init__(self, x, szerokosc):
        self.x = x
        self.szerokosc = szerokosc
        self.y_gora = 0
        self.wys_gora = random.randint(150, 250)
        self.odstep = 200
        self.y_dol = self.wys_gora + self.odstep
        self.wys_dol = wys - self.y_dol
        self.kolor = (160, 140, 190)
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wys_dol)

    def rysuj(self):
        pygame.draw.rect(screen, self.kolor, self.ksztalt_gora, 0)
        pygame.draw.rect(screen, self.kolor, self.ksztalt_dol, 0)

    def ruch(self, v):
        self.x = self.x - v
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wys_dol)


copokazuje = "rozgrywka"
przeszkody = []
for i in range(21):
    przeszkody.append(Przeszkoda(i * szer / 20, szer / 20))

gracz = Helikopter(250, 275)

dy = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -1
            if event.key == pygame.K_DOWN:
                dy = 1
    screen.fill((0, 0, 0))
    if copokazuje == "menu":
        napisz("Naciśnij spacje, aby zacząć", 20)
        grafika = pygame.image.load(os.path.join("logo.png"))
        screen.blit(grafika, (80, 30))
    elif copokazuje == "rozgrywka":
        for p in przeszkody:
            p.ruch(1)
            p.rysuj()
        for p in przeszkody:
            if p.x <= -p.szerokosc:
                przeszkody.remove(p)
                przeszkody.append((Przeszkoda(szer, szer / 20)))
        gracz.rysuj()
        gracz.ruch(dy)
    pygame.display.update()
