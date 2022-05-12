import os

from constants import *
from helikopter import Helikopter
from przeszkoda import Przeszkoda

pygame.init()


def napisz(tekst, x, y, rozmiar):
    cz = pygame.font.SysFont("Arial", rozmiar)
    rend = cz.render(tekst, True, (70, 228, 191))
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
                dy = -0.1
            if event.key == pygame.K_DOWN:
                dy = 0.1
            if event.key == pygame.K_SPACE:
                if copokazuje != "rozgrywka":
                    gracz = Helikopter(250, 275)
                    # dy = 0
                    copokazuje = "rozgrywka"

    screen.fill((0, 0, 0))
    if copokazuje == "menu":
        napisz("Naciśnij spacje, aby zacząć", 80, 150, 20)
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

    elif copokazuje == "koniec":
        grafika = pygame.image.load(os.path.join('logo.png'))
        screen.blit(grafika, (80, 30))
        napisz("Słabiutki jestes, poćwicz" ,  50, 290, 20)

    pygame.display.update()
