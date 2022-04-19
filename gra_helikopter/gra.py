from helikopter import Helikopter
from constants import *
from przeszkoda import Przeszkoda

import pygame
import os

pygame.init()


def napisz(tekst, rozmiar):
    cz = pygame.font.SysFont("Arial", rozmiar)
    rend = cz.render(tekst, True, (70, 228, 191))
    x = (szer - rend.get_rect().width) / 2
    y = (wys - rend.get_rect().height) / 2
    screen.blit(rend, (x, y))


copokazuje = "rozgrywka"
przeszkody = []
for i in range(21):
    przeszkody.append(Przeszkoda(i * szer / 20, szer / 20))

gracz = Helikopter(250, 275)

dy = 0

# przyciski

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

            # kolizja

            if p.kolizja(gracz.ksztalt):
                copokazuje = "koniec"
        for p in przeszkody:
            if p.x <= -p.szerokosc:
                przeszkody.remove(p)
                przeszkody.append((Przeszkoda(szer, szer / 20)))
        gracz.rysuj()
        gracz.ruch(dy)
    pygame.display.update()
