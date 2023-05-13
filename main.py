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

Mondo = MondoClass((0,0), sizeWindow, screen,[-40,-50])


clock = pygame.time.Clock()
fps = 60

player=Personaggio(screen, (500,350),(45,90))


def collisioneBlocchiSopra(player,Mondo):
    noCol=True
    for posBlocco in Mondo.blocchi:
        if player.rect.collidepoint(posBlocco[0]+49,posBlocco[1]):
            player.StopBasso(posBlocco[1]-1)
            noCol=False
        if player.rect.collidepoint(posBlocco[0],posBlocco[1]):
            player.StopBasso(posBlocco[1]-1)
            noCol=False
        if player.rect.collidepoint(posBlocco[0],posBlocco[1]-1):
            player.StopBasso(posBlocco[1]-1)
            noCol=False
    if noCol:
        player.inAria=True

def collisioneBlocchiLati(player,Mondo,mode=1):
    for posBlocco in Mondo.blocchi:
        if player.rect.collidepoint(posBlocco[0]-mode,posBlocco[1]+1):
            player.StopDestra()
            return 1
        if player.rect.collidepoint(posBlocco[0]-mode,posBlocco[1]+49):
            player.StopDestra()
            return 1
        if player.rect.collidepoint(posBlocco[0]+50+mode,posBlocco[1]+1):
            player.StopSinistra()
            return 2
        if player.rect.collidepoint(posBlocco[0]+50+mode,posBlocco[1]+49):
            player.StopSinistra()
            return 2

def collisioneBlocchiSotto(player,Mondo):
    for posBlocco in Mondo.blocchi:
        if player.rect.collidepoint(posBlocco[0],posBlocco[1]+50):
            player.StopSalto(posBlocco[1]+51)
        if player.rect.collidepoint(posBlocco[0]+49,posBlocco[1]+50):
            player.StopSalto(posBlocco[1]+51)

def scorriMondolati(player,Mondo,posMondox):
    if player.rect.right>=800 and player.muoviDestra==True:
        if collisioneBlocchiLati(player, Mondo,6)==1:
            posMondox=posMondox+player.VelMovimento
        posMondox=posMondox-player.VelMovimento
        player.StopDestra()
        Mondo.blocchi=[]
    if player.rect.left<=200 and player.muoviSinistra==True:
        if collisioneBlocchiLati(player, Mondo,6)==2:
            posMondox=posMondox-player.VelMovimento
        posMondox=posMondox+player.VelMovimento
        player.StopSinistra()
        Mondo.blocchi=[]
    return posMondox

def scorriMondoAlto(player,Mondo,posMondoy):
    if player.rect.top<=100:
        if player.vel[1]<0:
            player.rect.top=100
        
        posMondoy=posMondoy-player.vel[1]
        Mondo.blocchi=[]
    
    if player.rect.bottom>550:
        if player.vel[1]>0:
            player.rect.bottom=550
        posMondoy=posMondoy-player.vel[1]
        Mondo.blocchi=[]
    return posMondoy


posMondox=-50
posMondoy=-100
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

    screen.blit(sfondo,sfondorect)
    collisioneBlocchiLati(player, Mondo)
    posMondoy=scorriMondoAlto(player, Mondo, posMondoy)
    posMondox=scorriMondolati(player,Mondo,posMondox)
    
    
    player.muovi()
    player.draw()
    Mondo.draw(posMondox,posMondoy)

    pygame.display.update()
    clock.tick(fps)