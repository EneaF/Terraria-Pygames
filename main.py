import pygame, sys
from pygame.locals import *
from personaggio import Personaggio

sizeWindow=(1000,700)
screen=pygame.display.set_mode(sizeWindow)
screen.fill((0,255,255))
pygame.display.set_caption("Terraria")

clock = pygame.time.Clock()
fps = 60

player=Personaggio(screen, (500,350),(50,100))


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[K_d]:
        player.muovi_Destra()
    else:
        player.StopDestra()
    
    if keys[K_a]:
        player.muovi_Sinistra()
    else:
        player.StopSinistra()

    if keys[K_w]:
        player.Salto()

    screen.fill((0,255,255))
    player.muovi()
    player.draw()

    pygame.display.update()
    clock.tick(fps)