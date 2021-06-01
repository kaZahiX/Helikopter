import pygame

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    napisz("Naciśnij spacje, aby zacząć", 20)
    pygame.display.update()

