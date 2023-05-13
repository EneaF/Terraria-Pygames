import pygame, sys, math
from math import sqrt
from pygame.locals import *
from personaggio import Personaggio
from Mondo import MondoClass
from Inventario_Rapido import Inventario
from Riquadri import RiqScritto

pygame.init()

sizeWindow=(1000,700)
screen=pygame.display.set_mode(sizeWindow)
pygame.display.set_caption("TerraCraft2D")

sfondorect=pygame.Rect((0,0),(1000,700))
sfondoGioco=pygame.image.load("images/Sfondo.png")
sfondoMenu=pygame.image.load("images/Minecraft2D.png")
sfondoMenu=pygame.transform.scale(sfondoMenu,sizeWindow)
sfondoGioco=pygame.transform.scale(sfondoGioco,sizeWindow)

Mondo = MondoClass((0,0), sizeWindow, screen,[-40,-50])

sizeMondi=(450,100)
sizeReset=(150,100)

Mondo1=RiqScritto(screen, (100,200), sizeMondi, "MONDO 1")
Mondo2=RiqScritto(screen, (100,325), sizeMondi, "MONDO 2")
Mondo3=RiqScritto(screen, (100,450), sizeMondi, "MONDO 3")
Reset1S=RiqScritto(screen, (600,200), sizeReset, "Map S")
Reset1L=RiqScritto(screen, (800,200), sizeReset, "Map L")
Reset2S=RiqScritto(screen, (600,325), sizeReset, "Map S")
Reset2L=RiqScritto(screen, (800,325), sizeReset, "Map L")
Reset3S=RiqScritto(screen, (600,450), sizeReset, "Map S")
Reset3L=RiqScritto(screen, (800,450), sizeReset, "Map L")

QUITButton=RiqScritto(screen, (400,575), (200,100), "QUIT")




clock = pygame.time.Clock()
fps = 60



sizeInventario=(60,60)

box1=Inventario((300,25), sizeInventario, screen)
box2=Inventario((360,25), sizeInventario, screen)
box3=Inventario((420,25), sizeInventario, screen)
box4=Inventario((480,25), sizeInventario, screen)
box5=Inventario((540,25), sizeInventario, screen)

# f=open("MondoOriginaleLarge.txt","r")
# f1=open("Mondo.txt","w")
# f1.truncate()
# for riga in f:
#     f1.write(riga)
# f.close()
# f1.close()


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

def DisegnaMenu():
    Mondo1.draw()
    Mondo2.draw()
    Mondo3.draw()
    Reset1L.draw()
    Reset1S.draw()
    Reset2L.draw()
    Reset2S.draw()
    Reset3L.draw()
    Reset3S.draw()
    QUITButton.draw()
    pos=pygame.mouse.get_pos()
    if Mondo1.rect.collidepoint(pos):
        Mondo1.draw(0,1)
    if Mondo2.rect.collidepoint(pos):
        Mondo2.draw(0,1)
    if Mondo3.rect.collidepoint(pos):
        Mondo3.draw(0,1)
    if Reset1L.rect.collidepoint(pos):
        Reset1L.draw(0,1)
    if Reset1S.rect.collidepoint(pos):
        Reset1S.draw(0,1)
    if Reset2L.rect.collidepoint(pos):
        Reset2L.draw(0,1)
    if Reset3L.rect.collidepoint(pos):
        Reset3L.draw(0,1)
    if Reset2S.rect.collidepoint(pos):
        Reset2S.draw(0,1)
    if Reset3S.rect.collidepoint(pos):
        Reset3S.draw(0,1)
    if QUITButton.rect.collidepoint(pos):
        QUITButton.draw(0,1)

def CaricaMondo(nomeMondo,saveFile):
    f=open(nomeMondo,"r+")
    f1=open("fileTXT/Mondo.txt","w")
    f1.truncate()
    for riga in f:
        f1.write(riga)
    f.close()
    f1.close()

    f=open(saveFile,"r+")
    dati=[]
    for riga in f:
        dati.append(int(riga))
    f.close()
    return dati

def CreaMondo(nomeMondo,saveFile,tipo):
    if tipo==0:
        f=open("FileTXT/MondoOriginale.txt","r+")
        f1=open("fileTXT/Mondo.txt","w")
        f1.truncate()
        for riga in f:
            f1.write(riga)
        f.close()
        f1.close()

    elif tipo==1:
        f=open("FileTXT/MondoOriginaleLarge.txt","r+")
        f1=open("fileTXT/Mondo.txt","w")
        f1.truncate()
        for riga in f:
            f1.write(riga)
        f.close()
        f1.close()

    f=open("fileTXT/Mondo.txt","r+")
    f1=open(nomeMondo,"w")
    f1.truncate()
    for riga in f:
        f1.write(riga)
    f.close()
    f1.close()


    f=open("FileTXT/SalvataggioBase.txt","r+")
    f1=open(saveFile,"w")
    f1.truncate()
    for riga in f:
        f1.write(riga)
    f.close()
    f1.close()

def SalvaDati(dati,saveFile,nomeMondo):
    f=open("fileTXT/Mondo.txt","r+")
    f1=open(nomeMondo,"w")
    f1.truncate()
    for riga in f:
        f1.write(riga)
    f.close()
    f1.close()

    f=open(saveFile,"w")
    f.truncate()
    for dato in dati:
        f.write(str(int(dato)))
        f.write("\n")
    f.close()


# nFoglie=0
# nLegno=0
# nPietra=0
# nErba=0
# nTerra=0
lum=0
# posPlayer=(500,350)


# posMondox=-550
# posMondoy=-250
fase=1
while True:
    if fase==1:
        screen.blit(sfondoMenu,sfondorect)
        DisegnaMenu()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                pos=pygame.mouse.get_pos()
                if QUITButton.rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
                if Mondo1.rect.collidepoint(pos):
                    nomeSalvataggio="FileTXT/salvataggio1.txt"
                    nomeMondo="FileTXT/Mondo1.txt"
                    dati= CaricaMondo(nomeMondo,nomeSalvataggio)
                    fase=3
                if Mondo2.rect.collidepoint(pos):
                    nomeSalvataggio="FileTXT/salvataggio2.txt"
                    nomeMondo="FileTXT/Mondo2.txt"
                    dati= CaricaMondo(nomeMondo,nomeSalvataggio)
                    fase=3
                if Mondo3.rect.collidepoint(pos):
                    nomeSalvataggio="FileTXT/salvataggio3.txt"
                    nomeMondo="FileTXT/Mondo3.txt"
                    dati= CaricaMondo(nomeMondo,nomeSalvataggio)
                    fase=3
                if Reset1L.rect.collidepoint(pos):
                    nomeMondo="FileTXT/Mondo1.txt"
                    nomeSalvataggio="FileTXT/salvataggio1.txt"
                    dati=CreaMondo(nomeMondo,nomeSalvataggio,1)

                if Reset1S.rect.collidepoint(pos):
                    nomeMondo="FileTXT/Mondo1.txt"
                    nomeSalvataggio="FileTXT/salvataggio1.txt"
                    dati=CreaMondo(nomeMondo,nomeSalvataggio,0)

                if Reset2L.rect.collidepoint(pos):
                    nomeMondo="FileTXT/Mondo2.txt"
                    nomeSalvataggio="FileTXT/salvataggio2.txt"
                    dati=CreaMondo(nomeMondo,nomeSalvataggio,1)

                if Reset2S.rect.collidepoint(pos):
                    nomeMondo="FileTXT/Mondo2.txt"
                    nomeSalvataggio="FileTXT/salvataggio2.txt"
                    dati=CreaMondo(nomeMondo,nomeSalvataggio,0)

                if Reset3L.rect.collidepoint(pos):
                    nomeMondo="FileTXT/Mondo3.txt"
                    nomeSalvataggio="FileTXT/salvataggio3.txt"
                    dati=CreaMondo(nomeMondo,nomeSalvataggio,1)

                if Reset3S.rect.collidepoint(pos):
                    nomeMondo="FileTXT/Mondo3.txt"
                    nomeSalvataggio="FileTXT/salvataggio3.txt"
                    dati=CreaMondo(nomeMondo,nomeSalvataggio,0)

                

        if fase==3:
            nFoglie=dati[0]
            nLegno=dati[1]
            nPietra=dati[2]
            nErba=dati[3]
            nTerra=dati[4]
            posMondox=dati[5]
            posMondoy=dati[6]
            posPlayer=(dati[7],dati[8])
            player=Personaggio(screen, posPlayer,(45,90))
            fase=2

    elif fase==2:
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
        if keys[K_ESCAPE]:
            fase=1
            dati=[]
            dati.append(nFoglie)
            dati.append(nLegno)
            dati.append(nPietra)
            dati.append(nErba)
            dati.append(nTerra)
            dati.append(posMondox)
            dati.append(posMondoy)
            dati.append(player.rect.right)
            dati.append(player.rect.top)
            SalvaDati(dati,nomeSalvataggio,nomeMondo)

        screen.blit(sfondoGioco,sfondorect)
        
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