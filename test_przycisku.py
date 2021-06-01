import pygame
pygame.init()
szer = 600
wys = 600
screen = pygame.display.set_mode((szer, wys))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Wyłączone za pomocą krzyżyka.")
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            print(f"wciśnięto przycisk ${pygame.key.key_code('return')}")
        elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
            print("Zwolniono przycisk K_UP")
            #pygame.quit()
            #quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            print("Wciśnięto przycisk K_UP")
            print(pygame.key.get_pressed())