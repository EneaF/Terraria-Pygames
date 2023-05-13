import pygame, sys
from pygame.locals import *
from personaggio import Personaggio
from Mondo import MondoClass

sizeWindow=(1000,700)
screen=pygame.display.set_mode(sizeWindow)
pygame.display.set_caption("Terraria")

sfondorect=pygame.Rect((0,0),(1000,700))
sfondo=pygame.image.load("images/Sfondo.png")
sfondo=pygame.transform.scale(sfondo,sizeWindow)

Mondo = MondoClass((0,0), sizeWindow, screen)


clock = pygame.time.Clock()
fps = 60

player=Personaggio(screen, (500,350),(50,90))


def collisioneBlocchiSopra(player,Mondo):
    noCol=True
    for posBlocco in Mondo.blocchi:
        if player.rect.collidepoint(posBlocco[0]+49,posBlocco[1]):
            player.StopBasso(posBlocco[1])
            noCol=False
        if player.rect.collidepoint(posBlocco[0],posBlocco[1]):
            player.StopBasso(posBlocco[1])
            noCol=False
        if player.rect.collidepoint(posBlocco[0],posBlocco[1]-1):
            noCol=False
    if noCol:
        player.inAria=True

def collisioneBlocchiLati(player,Mondo):
    for posBlocco in Mondo.blocchi:
        if player.rect.collidepoint(posBlocco[0]-1,posBlocco[1]+1):
            player.StopDestra()

        elif player.rect.collidepoint(posBlocco[0]+51,posBlocco[1]+1):
            player.StopSinistra()

def collisioneBlocchiSotto(player,Mondo):
    for posBlocco in Mondo.blocchi:
        if player.rect.collidepoint(posBlocco[0],posBlocco[1]+50):
            player.StopSalto(posBlocco[1]+51)

while True:
    collisioneBlocchiSopra(player, Mondo)
    collisioneBlocchiSotto(player, Mondo)
    
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

    if keys[K_SPACE]:
        player.Salto()

    
    collisioneBlocchiLati(player, Mondo)
    screen.blit(sfondo,sfondorect)
    player.muovi()
    player.draw()
    Mondo.draw()
    pygame.display.update()
    clock.tick(fps)