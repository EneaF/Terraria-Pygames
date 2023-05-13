import pygame, sys, math
from math import sqrt
from pygame.locals import *
from personaggio import Personaggio
from Mondo import MondoClass
from Inventario_Rapido import Inventario

pygame.init()

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

sizeInventario=(60,60)

box1=Inventario((300,25), sizeInventario, screen)
box2=Inventario((360,25), sizeInventario, screen)
box3=Inventario((420,25), sizeInventario, screen)
box4=Inventario((480,25), sizeInventario, screen)
box5=Inventario((540,25), sizeInventario, screen)

f=open("MondoOriginaleLarge.txt","r")
f1=open("Mondo.txt","w")
f1.truncate()
for riga in f:
    f1.write(riga)
f.close()
f1.close()


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
        Mondo.blocchiAria=[]
    if player.rect.left<=200 and player.muoviSinistra==True:
        if collisioneBlocchiLati(player, Mondo,6)==2:
            posMondox=posMondox-player.VelMovimento
        posMondox=posMondox+player.VelMovimento
        player.StopSinistra()
        Mondo.blocchi=[]
        Mondo.blocchiAria=[]
    return posMondox

def scorriMondoAlto(player,Mondo,posMondoy):
    if player.rect.top<=100:
        if player.vel[1]<0:
            player.rect.top=100
        
        posMondoy=posMondoy-player.vel[1]
        Mondo.blocchi=[]
        Mondo.blocchiAria=[]
    
    if player.rect.bottom>550:
        if player.vel[1]>0:
            player.rect.bottom=550
        posMondoy=posMondoy-player.vel[1]
        Mondo.blocchi=[]
        Mondo.blocchiAria=[]
    return posMondoy


nFoglie=0
nLegno=0
nPietra=0
nErba=0
nTerra=0
lum=0

posMondox=-550
posMondoy=-250
while True:
    collisioneBlocchiSopra(player, Mondo)
    collisioneBlocchiSotto(player, Mondo)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN and event.button==1:
            pos=pygame.mouse.get_pos()
            for blocco in Mondo.blocchi:
                rectTmp=pygame.Rect((blocco[0],blocco[1]),(50,50))
                if sqrt((rectTmp.centerx-player.rect.centerx)**2+(rectTmp.centery-player.rect.centery)**2)<=250:
                    if rectTmp.collidepoint(pos):
                        if blocco[2]==1 and nErba<999:
                            nErba+=1
                            Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                        elif blocco[2]==2 and nTerra<999:
                            nTerra+=1
                            Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                        elif blocco[2]==3 and nPietra<999:
                            nPietra+=1
                            Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                        elif blocco[2]==4 and nFoglie<999:
                            nFoglie+=1
                            Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                        elif blocco[2]==5 and nLegno<999:
                            nLegno+=1
                            Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))

        if event.type == MOUSEBUTTONDOWN and event.button==3:
            pos=pygame.mouse.get_pos()
            for bloccoAria in Mondo.blocchiAria:
                rectTmp=pygame.Rect((bloccoAria[0],bloccoAria[1]),(50,50))
                if rectTmp.collidepoint(pos):
                    if sqrt((rectTmp.centerx-player.rect.centerx)**2+(rectTmp.centery-player.rect.centery)**2)<=250:
                        if lum==1 and nFoglie>0:
                            nFoglie-=1
                            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)
                        elif lum==2 and nLegno>0:
                            nLegno-=1
                            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)
                        elif lum==3 and nPietra>0:
                            nPietra-=1
                            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)
                        elif lum==4 and nErba>0:
                            nErba-=1
                            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)
                        elif lum==5 and nTerra>0:
                            nTerra-=1
                            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)
                    
                        


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
    
    if keys[K_1]:
        lum=1
    if keys[K_2]:
        lum=2
    if keys[K_3]:
        lum=3
    if keys[K_4]:
        lum=4
    if keys[K_5]:
        lum=5
    if keys[K_e]:
        if lum==5:
            lum=1
        else:
            lum=lum+1
    if keys[K_q]:
        if lum==1:
            lum=5
        else:
            lum=lum-1

    screen.blit(sfondo,sfondorect)
    
    collisioneBlocchiLati(player, Mondo)
    posMondoy=scorriMondoAlto(player, Mondo, posMondoy)
    posMondox=scorriMondolati(player,Mondo,posMondox)

    Mondo.draw(posMondox,posMondoy)
    box1.draw(1,nFoglie)
    box2.draw(2,nLegno)
    box3.draw(3,nPietra)
    box4.draw(4,nErba)
    box5.draw(5,nTerra)

    if lum==1:
        box1.draw(1,nFoglie,True)
    elif lum==2:
        box2.draw(2,nLegno,True)
    elif lum==3:
        box3.draw(3,nPietra,True)
    elif lum==4:
        box4.draw(4,nErba,True)
    elif lum==5:
        box5.draw(5,nTerra,True)

    player.muovi()
    player.draw()
    
    pygame.display.update()
    clock.tick(fps)