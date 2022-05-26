import os
import math

from constants import *
from helikopter import Helikopter
from przeszkoda import Przeszkoda

pygame.init()


def napisz(tekst, x, y, rozmiar):
    cz = pygame.font.SysFont("Arial", rozmiar)
    rend = cz.render(tekst, True, napis_wartosci["kolor"])
    screen.blit(rend, (x, y))


copokazuje = "menu"
przeszkody = []
for i in range(21):
    przeszkody.append(Przeszkoda(i * szer / 20, szer / 20))

gracz = Helikopter(250, 275)

dy = -0.1

# przyciski

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -predkosc
                print("gora")
            if event.key == pygame.K_DOWN:
                dy = predkosc
                print("dol")
            if event.key == pygame.K_SPACE:
                if copokazuje != "rozgrywka":
                    gracz = Helikopter(250, 275)
                    # dy = 0
                    copokazuje = "rozgrywka"
                    punkty = 0

    screen.fill(kolor_tla)
    if copokazuje == "menu":
        napisz("Naciśnij spacje, aby zacząć", napis_wartosci["szerekosc"], napis_wartosci["wysokosc"], napis_wartosci["rozmiar"])
        grafika = pygame.image.load(os.path.join("logo.png"))
        screen.blit(grafika, (800, 400))
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
                punkty = punkty + math.fabs(dy*2.5)
        gracz.rysuj()
        gracz.ruch(dy)
        napisz(str(punkty), 500, 500, 40)
    elif copokazuje == "koniec":
        grafika = pygame.image.load(os.path.join('logo.png'))
        screen.blit(grafika, (800, 400))
        napisz("Słabiutki jestes, poćwicz", napis_wartosci["szerekosc"], napis_wartosci["wysokosc"], napis_wartosci["rozmiar"])
        napisz("zdobyłes " + str(punkty) + " punktów",  napis_wartosci["szerekosc"], napis_wartosci["wysokosc"] + 50, napis_wartosci["rozmiar"])
    pygame.display.update()
