import pygame, sys, math, random
from math import sqrt
from math import sin
from math import cos
from math import atan
from pygame.locals import *
from personaggio import Personaggio
from Mondo import MondoClass
from Inventario_Rapido import Inventario
from Riquadri import RiqScritto
from HP import VitaClass
from Sfondo import SfondoClass
from fantasma import FantasmaClass
from proiettile import ProiettileClass

#TI PREGO DIMMI CHE SEI LA VERSIONE GIUSTA!

pygame.init()

sizeWindow=(1000,700)
screen=pygame.display.set_mode(sizeWindow)
pygame.display.set_caption("TerraCraft2D")

sfondorect=pygame.Rect((0,0),(1000,700))
sfondoMenu=pygame.image.load("images/Minecraft2D.png")
sfondoMenu=pygame.transform.scale(sfondoMenu,sizeWindow)
YouDied=pygame.image.load("images/YouDied.png")
YouDied=pygame.transform.scale(YouDied,sizeWindow)


Sfondo = SfondoClass((-30,-30),(30,30),screen,sizeWindow)
Mondo = MondoClass((0,0), sizeWindow, screen,[-40,-50])

sizeMondi=(450,100)
sizeReset=(150,100)
sizeYouDied=(450,75)
sizeCreaMondi=(300,100)

Mondo1=RiqScritto(screen, (100,200), sizeMondi, "MONDO 1")
Mondo2=RiqScritto(screen, (100,325), sizeMondi, "MONDO 2")
Mondo3=RiqScritto(screen, (100,450), sizeMondi, "MONDO 3")
CreaMondo1=RiqScritto(screen,(600,200),sizeCreaMondi, "Crea Mondo 1")
CreaMondo2=RiqScritto(screen,(600,325),sizeCreaMondi, "Crea Mondo 2")
CreaMondo3=RiqScritto(screen,(600,450),sizeCreaMondi, "Crea Mondo 3")
MondoSize=RiqScritto(screen, (500,200),sizeCreaMondi, "Piccola")
Difficulty=RiqScritto(screen,(500,350),sizeCreaMondi, "Pacifica")
MondoSizeScritta=RiqScritto(screen, (150,230),sizeCreaMondi, "")
DifficultyScritta=RiqScritto(screen, (150,380),sizeCreaMondi, "")
CreaMondoTasto=RiqScritto(screen, (300,575), (400,100), "Crea Mondo")

QUITButton=RiqScritto(screen, (400,575), (200,100), "QUIT")

FpsF3=RiqScritto(screen,(50,100),(100,100),"Fps: ")
NdayF3=RiqScritto(screen,(50,130),(100,100),"Day: ")
PosXMF3=RiqScritto(screen,(50,160),(100,100),"XM:")
PosYMF3=RiqScritto(screen,(150,160),(100,100),"YM: ")
PosXPF3=RiqScritto(screen,(50,190),(100,100),"XP: ")
PosYPF3=RiqScritto(screen,(150,190),(100,100),"YP: ")
DiffF3=RiqScritto(screen,(50,220),(100,100),"Diff: ")

Respawn=RiqScritto(screen, (25,600), sizeYouDied,"Respawn")
TitleScreen=RiqScritto(screen,(525,600), sizeYouDied,"Title Screen")

vita=[]
vitaTmp=[VitaClass((120,30),(25,25),screen),0]
vita.append(vitaTmp)
vitaTmp=[VitaClass((150,30),(25,25),screen),0]
vita.append(vitaTmp)
vitaTmp=[VitaClass((180,30),(25,25),screen),0]
vita.append(vitaTmp)
vitaTmp=[VitaClass((210,30),(25,25),screen),0]
vita.append(vitaTmp)
vitaTmp=[VitaClass((240,30),(25,25),screen),0]
vita.append(vitaTmp)

clock = pygame.time.Clock()
fps = 60

sizeInventario=(60,60)

box1=Inventario((300,25), sizeInventario, screen)
box2=Inventario((360,25), sizeInventario, screen)
box3=Inventario((420,25), sizeInventario, screen)
box4=Inventario((480,25), sizeInventario, screen)
box5=Inventario((540,25), sizeInventario, screen)
box6=Inventario((600,25), sizeInventario, screen)
box7=Inventario((660,25), sizeInventario, screen)
box8=Inventario((720,25), sizeInventario, screen)
box9=Inventario((780,25), sizeInventario, screen)






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
        if player.rect.collidepoint(posBlocco[0]+49,posBlocco[1]-1):
            player.StopBasso(posBlocco[1]-1)
            noCol=False
    if noCol:
        player.inAria=True
    else:
        return True

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
        player.nextDestra()
        Mondo.blocchi=[]
        Mondo.blocchiAria=[]
        Mondo.blocchiDietro=[]
        Mondo.scale=[]
    if player.rect.left<=200 and player.muoviSinistra==True:
        if collisioneBlocchiLati(player, Mondo,6)==2:
            posMondox=posMondox-player.VelMovimento
        posMondox=posMondox+player.VelMovimento
        player.StopSinistra()
        player.nextSinistra()
        Mondo.blocchi=[]
        Mondo.blocchiAria=[]
        Mondo.blocchiDietro=[]
        Mondo.scale=[]
    return posMondox

def scorriMondoAlto(player,Mondo,posMondoy):
    if player.rect.top<=200:
        if player.vel[1]<0:
            player.rect.top=200
        
        posMondoy=posMondoy-player.vel[1]
        Mondo.blocchi=[]
        Mondo.blocchiAria=[]
        Mondo.blocchiDietro=[]
        Mondo.scale=[]
    
    if player.rect.bottom>550:
        if player.vel[1]>0:
            player.rect.bottom=550
        posMondoy=posMondoy-player.vel[1]
        Mondo.blocchi=[]
        Mondo.blocchiAria=[]
        Mondo.blocchiDietro=[]
        Mondo.scale=[]
    return posMondoy

def DisegnaMenu():
    Mondo1.draw()
    Mondo2.draw()
    Mondo3.draw()
    CreaMondo1.draw()
    CreaMondo2.draw()
    CreaMondo3.draw()
    QUITButton.draw()
    pos=pygame.mouse.get_pos()
    if Mondo1.rect.collidepoint(pos):
        Mondo1.draw(0,1)
    if Mondo2.rect.collidepoint(pos):
        Mondo2.draw(0,1)
    if Mondo3.rect.collidepoint(pos):
        Mondo3.draw(0,1)
    if CreaMondo1.rect.collidepoint(pos):
        CreaMondo1.draw(0,1)
    if CreaMondo2.rect.collidepoint(pos):
        CreaMondo2.draw(0,1)
    if CreaMondo3.rect.collidepoint(pos):
        CreaMondo3.draw(0,1)
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

def dannoDaCaduta(player):

    danno=0
    if player.velMax>=20.1:
        danno=10
    elif player.velMax>=19.2:
        danno=9
    elif player.velMax>=18.3:
        danno=8
    elif player.velMax>=17.4:
        danno=7
    elif player.velMax>=16.5:
        danno=6
    elif player.velMax>=15.9:
        danno=5
    elif player.velMax>=15:
        danno=4
    elif player.velMax>=13.7:
        danno=3
    elif player.velMax>=12.8:
        danno=2
    elif player.velMax>=11.8:
        danno=1
    
    return danno    

def saleScala(player,Mondo):
    for scala in Mondo.scale:
        scalaRect=pygame.Rect((scala[0],scala[1]),(50,53))
        if scalaRect.collidepoint(player.rect.bottomleft)==True or scalaRect.collidepoint(player.rect.bottomright)==True :
            player.SaleScala()
            player.inAria=False
            player.velMax=0

def scendeScala(player,Mondo):
    for scala in Mondo.scale:
        scalaRect=pygame.Rect((scala[0],scala[1]),(50,53))
        if scalaRect.collidepoint(player.rect.bottomleft)==True or scalaRect.collidepoint(player.rect.bottomright)==True :
            player.ScendeScala()
            player.inAria=False
            player.velMax=0

def suScala(player,Mondo):
    for scala in Mondo.scale:
        scalaRect=pygame.Rect((scala[0],scala[1]),(50,51))
        if scalaRect.collidepoint(player.rect.bottomleft)==True or scalaRect.collidepoint(player.rect.bottomright)==True :
            player.SuScala()
            player.inAria=False
            player.velMax=0

def CresceSapling(Mondo,posMondox,posMondoy):
    for bloccoDietro in Mondo.blocchiDietro:
        if bloccoDietro[2]=="S":
            # Servirebbe un if per controllare che i blocchi dove piazzare foglie e legno siano liberi
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0],bloccoDietro[1]),2)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0],bloccoDietro[1]-50),2)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0],bloccoDietro[1]-100),2)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0],bloccoDietro[1]-150),2)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]-100,bloccoDietro[1]-100),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]-100,bloccoDietro[1]-150),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]-50,bloccoDietro[1]-100),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]-50,bloccoDietro[1]-150),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]-50,bloccoDietro[1]-200),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]-50,bloccoDietro[1]-250),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0],bloccoDietro[1]-200),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0],bloccoDietro[1]-250),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]+50,bloccoDietro[1]-100),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]+50,bloccoDietro[1]-150),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]+50,bloccoDietro[1]-200),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]+50,bloccoDietro[1]-250),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]+100,bloccoDietro[1]-100),1)
            Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoDietro[0]+100,bloccoDietro[1]-150),1)

def disegnaYouDied():
    Respawn.draw()
    TitleScreen.draw()

def fantasmaSpawn(Velocita):
    lato=random.randint(0,3)
    if lato==0:
        X=-50
        Y=random.randint(0,700)
    elif lato==1:
        X=random.randint(0,1000)
        Y=700
    elif lato==2:
        X=1000
        Y=random.randint(0,700)
    else:
        X=random.randint(0,1000)
        Y=-50
    Fantasma=FantasmaClass((X,Y),(50,50),screen,Velocita)
    return Fantasma

def fantasmaMove(fantasma,player):
    if (fantasma.rect.centerx-player.rect.centerx)==0:
        velFantasmax=0
        velFantasmay=fantasma.Vel
    else:
        m=(fantasma.rect.centery-player.rect.centery)/(fantasma.rect.centerx-player.rect.centerx)
        ang=atan(m)
        velFantasmax=fantasma.Vel*cos(ang)
        velFantasmay=fantasma.Vel*sin(ang)
    
        if fantasma.rect.left>player.rect.left:
            velFantasmax*=-1
            velFantasmay*=-1
    fantasma.muovi(velFantasmax,velFantasmay)

def ProiettileSpara(X,Y):
    Proiettile=ProiettileClass((X,Y),(5,5),screen)
    return Proiettile

Soundtrack=["Sounds/MainTheme/Soundtrack (1).mp3","Sounds/MainTheme/Soundtrack (2).mp3",
            "Sounds/MainTheme/Soundtrack (3).mp3","Sounds/MainTheme/Soundtrack (4).mp3",
            "Sounds/MainTheme/Soundtrack (5).mp3","Sounds/MainTheme/Soundtrack (6).mp3",
            "Sounds/MainTheme/Soundtrack (7).mp3","Sounds/MainTheme/Soundtrack (8).mp3",
            "Sounds/MainTheme/Soundtrack (9).mp3","Sounds/MainTheme/Soundtrack (10).mp3",
            "Sounds/MainTheme/Soundtrack (11).mp3","Sounds/MainTheme/Soundtrack (12).mp3",
            "Sounds/MainTheme/Soundtrack (13).mp3","Sounds/MainTheme/Soundtrack (14).mp3",
            "Sounds/MainTheme/Soundtrack (15).mp3","Sounds/MainTheme/Soundtrack (16).mp3",
            "Sounds/MainTheme/Soundtrack (17).mp3","Sounds/MainTheme/Soundtrack (18).mp3",
            "Sounds/MainTheme/Soundtrack (19).mp3","Sounds/MainTheme/Soundtrack (20).mp3",
            "Sounds/MainTheme/Soundtrack (21).mp3","Sounds/MainTheme/Soundtrack (22).mp3",
            "Sounds/MainTheme/Soundtrack (23).mp3","Sounds/MainTheme/Soundtrack (24).mp3",
            "Sounds/MainTheme/Soundtrack (25).mp3","Sounds/MainTheme/Soundtrack (26).mp3",]


pygame.mixer.music.load("Sounds/MainTheme/MainMenu.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
LegnoSuono = [pygame.mixer.Sound("Sounds/WoodBreak.mp3"),pygame.mixer.Sound("Sounds/Woodplacing2.mp3"),pygame.mixer.Sound("Sounds/Woodplacing3.mp3")]
ErbaSuono=[pygame.mixer.Sound("Sounds/GrassBreak.mp3"),pygame.mixer.Sound("Sounds/GrassBreak2.mp3"),pygame.mixer.Sound("Sounds/Grassbreak3.mp3"),pygame.mixer.Sound("Sounds/Grassbreak4.mp3")]
PietraSuono=[pygame.mixer.Sound("Sounds/StoneBreak.mp3"),pygame.mixer.Sound("Sounds/StoneBreak2.mp3"),pygame.mixer.Sound("Sounds/StoneBreak3.mp3")]
dannoSuono=pygame.mixer.Sound("Sounds/Damage.mp3")
FoglieSuono=pygame.mixer.Sound("Sounds/foglie.mp3")
TerraSuono=pygame.mixer.Sound("Sounds/DirtBreak.mp3")
RespawnSuono=pygame.mixer.Sound("Sounds/Respawn.mp3")
YouDiedSuono=pygame.mixer.Sound("Sounds/YouDiedSound.mp3")
SparoSuono=pygame.mixer.Sound("Sounds/Gunshot.mp3")
FantasmaSuono=pygame.mixer.Sound("Sounds/Ghostdeath.mp3")
Fantasmarisata=pygame.mixer.Sound("Sounds/Ghostlaugh.mp3")
SparoSuono.set_volume(0.1)

lum=0
fase=1
regen=0
tempo=0
F3=False
fantasmaPres=0
fantasmaLim=0
Fantasma=[]
cooldown=0
ProPres=False
tipo=1
Diff=None
FantasmaSpeed=1
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
                
                if CreaMondo1.rect.collidepoint(pos):
                    nomeMondo="FileTXT/Mondo1.txt"
                    nomeSalvataggio="FileTXT/salvataggio1.txt"
                    fase=5
                    Diff=0
                if CreaMondo2.rect.collidepoint(pos):
                    nomeMondo="FileTXT/Mondo2.txt"
                    nomeSalvataggio="FileTXT/salvataggio2.txt"
                    fase=5
                    Diff=0
                if CreaMondo3.rect.collidepoint(pos):
                    nomeMondo="FileTXT/Mondo3.txt"
                    nomeSalvataggio="FileTXT/salvataggio3.txt"
                    fase=5
                    Diff=0     

    elif fase==3:
        nFoglie=dati[0]
        nLegno=dati[1]
        nPietra=dati[2]
        nErba=dati[3]
        nTerra=dati[4]
        posMondox=dati[5]
        posMondoy=dati[6]
        posPlayer=(dati[7],dati[8])
        vitaTot=dati[9]
        tempo=dati[10]
        nOakPlanks=dati[11]
        nScale=dati[12]
        nSaplings=dati[13]
        nDay=dati[14]
        nDay1=dati[15]
        if Diff==None:
            Diff=dati[16]
        if dati[17]==0:
            Sfondo.notte=True
        else:
            Sfondo.notte=False
        Mondo.blocchi=[]
        Mondo.blocchiAria=[]
        Mondo.blocchiDietro=[]
        Mondo.scale=[]
        player=Personaggio(screen, posPlayer,(45,90))
        fase=2
        regen=0

        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.load(random.choice(Soundtrack))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(0,1)

    elif fase==5:
        screen.blit(sfondoMenu,sfondorect)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                pos=pygame.mouse.get_pos()
                if MondoSize.rect.collidepoint(pos):
                    if MondoSize.testo=="Piccola":
                        MondoSize.testo="Grande"
                        tipo=2
                    else:
                        MondoSize.testo="Piccola"
                        tipo=1
                if Difficulty.rect.collidepoint(pos):
                    if Difficulty.testo=="Pacifica":
                        Difficulty.testo="Facile"
                        Diff=1
                    elif Difficulty.testo=="Facile":
                        Difficulty.testo="Normale"
                        Diff=2
                    elif Difficulty.testo=="Normale":
                        Difficulty.testo="Difficile"
                        Diff=3
                    else:
                        Difficulty.testo="Pacifica"
                        Diff=0
                
                if CreaMondoTasto.rect.collidepoint(pos):
                    CreaMondo(nomeMondo,nomeSalvataggio,tipo)
                    fase=1

        MondoSize.draw()
        Difficulty.draw()
        CreaMondoTasto.draw()
        MondoSizeScritta.drawNormal("Dimensione Mondo: ",50)
        DifficultyScritta.drawNormal("Difficoltà: ",50)
        




    elif fase==4:

        screen.blit(YouDied,sfondorect)
        disegnaYouDied()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                pos=pygame.mouse.get_pos()
                if Respawn.rect.collidepoint(pos):
                    nFoglie=round(nFoglie/2)
                    nLegno=round(nLegno/2)
                    nErba=round(nErba/2)
                    nOakPlanks=round(nOakPlanks/2)
                    nTerra=round(nTerra/2)
                    nScale=round(nScale/2)
                    nSaplings=round(nSaplings/2)
                    nPietra=round(nPietra/2)
                    posMondox=-550
                    posMondoy=-200
                    player.rect.left=500
                    player.rect.top=350
                    vitaTot=10
                    fase=2
                    pygame.mixer.music.fadeout(1000)
                    RespawnSuono.play()
                    Mondo.blocchi=[]
                    Mondo.blocchiAria=[]
                    Mondo.blocchiDietro=[]
                    Mondo.scale=[]
                    Fantasma=[]
                    fantasmaPres=0

                if TitleScreen.rect.collidepoint(pos):
                    fase=1
                    dati=[]
                    dati.append(nFoglie)
                    dati.append(nLegno)
                    dati.append(nPietra)
                    dati.append(nErba)
                    dati.append(nTerra)
                    dati.append(posMondox)
                    dati.append(posMondoy)
                    dati.append(player.rect.left)
                    dati.append(player.rect.top)
                    dati.append(vitaTot)
                    dati.append(tempo)
                    dati.append(nOakPlanks)
                    dati.append(nScale)
                    dati.append(nSaplings)
                    dati.append(nDay)
                    dati.append(nDay1)
                    dati.append(Diff)
                    if Sfondo.notte==True:
                        dati.append(0)
                    else:
                        dati.append(1)
                    SalvaDati(dati,nomeSalvataggio,nomeMondo)
                    Diff=None

                    pygame.mixer.music.fadeout(1000)
                    pygame.mixer.music.load("Sounds/MainTheme/MainMenu.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1,1)
                    
        
        keys = pygame.key.get_pressed()
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
            dati.append(player.rect.left)
            dati.append(player.rect.top)
            dati.append(vitaTot)
            dati.append(tempo)
            dati.append(nOakPlanks)
            dati.append(nScale)
            dati.append(nSaplings)
            dati.append(nDay)
            dati.append(nDay1)
            dati.append(Diff)
            if Sfondo.notte==True:
                dati.append(0)
            else:
                dati.append(1)
            SalvaDati(dati,nomeSalvataggio,nomeMondo)
            Fantasma=[]
            fantasmaPres=0
            Diff=None

            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load("Sounds/MainTheme/MainMenu.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1,1)
            
        if keys[K_r]:
            nFoglie=0
            nLegno=0
            nErba=0
            nOakPlanks=0
            nTerra=0
            nScale=0
            nSaplings=0
            nPietra=0
            posMondox=-550
            posMondoy=-200
            player.rect.left=500
            player.rect.top=350
            vitaTot=10
            fase=2
            Mondo.blocchi=[]
            Mondo.blocchiAria=[]
            Mondo.blocchiDietro=[]
            Mondo.scale=[]
            Fantasma=[]
            fantasmaPres=0


    elif fase==2:
        if Diff==1:
            FantasmaSpeed=1
        elif Diff==2:
            FantasmaSpeed=2
        elif Diff==3:
            FantasmaSpeed=3
        if pygame.mixer.music.get_busy()==False:
            pygame.mixer.music.unload()
            pygame.mixer.music.load(random.choice(Soundtrack))
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(0,1)
        caduto=False
        danno=0
        
        caduto=collisioneBlocchiSopra(player, Mondo)
        collisioneBlocchiSotto(player, Mondo)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                pos=pygame.mouse.get_pos()
                if box1.rectBox.collidepoint(pos):
                    lum=1
                if box2.rectBox.collidepoint(pos):
                    lum=2
                if box3.rectBox.collidepoint(pos):
                    lum=3
                if box4.rectBox.collidepoint(pos):
                    lum=4
                if box5.rectBox.collidepoint(pos):
                    lum=5
                if box6.rectBox.collidepoint(pos):
                    lum=6
                if box7.rectBox.collidepoint(pos):
                    lum=7
                if box8.rectBox.collidepoint(pos):
                    lum=8
                if box9.rectBox.collidepoint(pos):
                    lum=9
                    cooldown=0
                
                if lum==9 :
                    if cooldown==7:
                        cooldown=0
                        ProPres=True
                        Proiettile=ProiettileSpara(player.rect.centerx,player.rect.centery)
                        SparoSuono.play()
                        if (pos[0]-player.rect.centerx)==0:
                            velProX=0
                            velProY=Proiettile.vel
                            
                        else:
                            m=(pos[1]-player.rect.centery)/(pos[0]-player.rect.centerx)
                            ang=atan(m)
                            velProX=Proiettile.vel*sin(ang)
                            velProY=Proiettile.vel*cos(ang)
                        
                        if pos[0]<player.rect.centerx:
                            velProX*=-1
                            velProY*=-1
                else:
                    for blocco in Mondo.blocchi:
                        rectTmp=pygame.Rect((blocco[0],blocco[1]),(50,50))
                        if sqrt((rectTmp.centerx-player.rect.centerx)**2+(rectTmp.centery-player.rect.centery)**2)<=250:
                            if rectTmp.collidepoint(pos):
                                if blocco[2]=="E" and nErba<999:
                                    nErba+=1
                                    choice = random.choice(ErbaSuono)
                                    choice.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="T" and nTerra<999:
                                    nTerra+=1
                                    TerraSuono.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="P" and nPietra<999:
                                    nPietra+=1
                                    choice = random.choice(PietraSuono)
                                    choice.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="F" and nFoglie<999:
                                    nFoglie+=1
                                    FoglieSuono.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="L" and nLegno<999:
                                    nLegno+=1
                                    choice = random.choice(LegnoSuono)
                                    choice.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="O" and nOakPlanks<999:
                                    nOakPlanks+=1
                                    choice = random.choice(LegnoSuono)
                                    choice.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))

                    for blocco in Mondo.blocchiDietro:
                        rectTmp=pygame.Rect((blocco[0],blocco[1]),(50,50))
                        if sqrt((rectTmp.centerx-player.rect.centerx)**2+(rectTmp.centery-player.rect.centery)**2)<=250:
                            if rectTmp.collidepoint(pos):
                                if blocco[2]=="e" and nErba<999:
                                    nErba+=1
                                    choice = random.choice(ErbaSuono)
                                    choice.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="t" and nTerra<999:
                                    nTerra+=1
                                    TerraSuono.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="p" and nPietra<999:
                                    nPietra+=1
                                    choice = random.choice(PietraSuono)
                                    choice.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="f" and nFoglie<999:
                                    nFoglie+=1
                                    FoglieSuono.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="l" and nLegno<999:
                                    nLegno+=1
                                    choice = random.choice(LegnoSuono)
                                    choice.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="o" and nOakPlanks<999:
                                    nOakPlanks+=1
                                    choice = random.choice(LegnoSuono)
                                    choice.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="s" and nScale<999:
                                    nScale+=1
                                    choice = random.choice(LegnoSuono)
                                    choice.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))
                                elif blocco[2]=="S" and nSaplings<999:
                                    nSaplings+=1
                                    FoglieSuono.play()
                                    Mondo.RimuoviBlocco(posMondox,posMondoy,(blocco[0],blocco[1]))

            if event.type == MOUSEBUTTONDOWN and event.button==3:
                pos=pygame.mouse.get_pos()
                for bloccoAria in Mondo.blocchiAria:
                    rectTmp=pygame.Rect((bloccoAria[0],bloccoAria[1]),(50,50))
                    if rectTmp.collidepoint(pos)==True and player.rect.collidepoint(rectTmp.topleft)==False and player.rect.collidepoint(rectTmp.topright)==False and player.rect.collidepoint(rectTmp.bottomleft)==False and player.rect.collidepoint(rectTmp.bottomright)==False and player.rect.collidepoint(rectTmp.center)==False:
                        if sqrt((rectTmp.centerx-player.rect.centerx)**2+(rectTmp.centery-player.rect.centery)**2)<=250:
                            if lum==1 and nFoglie>0:
                                nFoglie-=1
                                FoglieSuono.play()
                                Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==2 and nLegno>0:
                                nLegno-=1
                                choice = random.choice(LegnoSuono)
                                choice.play()
                                Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==3 and nPietra>0:
                                nPietra-=1
                                choice = random.choice(PietraSuono)
                                choice.play()
                                Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==4 and nErba>0:
                                nErba-=1
                                choice = random.choice(ErbaSuono)
                                choice.play()
                                Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==5 and nTerra>0:
                                nTerra-=1
                                TerraSuono.play()
                                Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==6 and nOakPlanks>0:
                                nOakPlanks-=1
                                choice = random.choice(LegnoSuono)
                                choice.play()
                                Mondo.AggiungiBlocco(posMondox,posMondoy,(bloccoAria),lum)

            if event.type == MOUSEBUTTONDOWN and event.button==2:
                pos=pygame.mouse.get_pos()
                for bloccoAria in Mondo.blocchiAria:
                    rectTmp=pygame.Rect((bloccoAria[0],bloccoAria[1]),(50,50))
                    if rectTmp.collidepoint(pos):
                        if sqrt((rectTmp.centerx-player.rect.centerx)**2+(rectTmp.centery-player.rect.centery)**2)<=250:
                            if lum==1 and nFoglie>0:
                                nFoglie-=1
                                FoglieSuono.play()
                                Mondo.AggiungiBloccoDietro(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==2 and nLegno>0:
                                nLegno-=1
                                choice = random.choice(LegnoSuono)
                                choice.play()
                                Mondo.AggiungiBloccoDietro(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==3 and nPietra>0:
                                nPietra-=1
                                choice = random.choice(PietraSuono)
                                choice.play()
                                Mondo.AggiungiBloccoDietro(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==4 and nErba>0:
                                nErba-=1
                                choice = random.choice(ErbaSuono)
                                choice.play()
                                Mondo.AggiungiBloccoDietro(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==5 and nTerra>0:
                                nTerra-=1
                                TerraSuono.play()
                                Mondo.AggiungiBloccoDietro(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==6 and nOakPlanks>0:
                                nOakPlanks-=1
                                choice = random.choice(LegnoSuono)
                                choice.play()
                                Mondo.AggiungiBloccoDietro(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==7 and nScale>0:
                                nScale-=1
                                choice = random.choice(LegnoSuono)
                                choice.play()
                                Mondo.AggiungiBloccoDietro(posMondox,posMondoy,(bloccoAria),lum)
                            elif lum==8 and nSaplings>0:
                                for blocco in Mondo.blocchi:
                                    if blocco==(bloccoAria[0],bloccoAria[1]+50,"E") or blocco==(bloccoAria[0],bloccoAria[1]+50,"T"):
                                        nSaplings-=1
                                        FoglieSuono.play()
                                        Mondo.AggiungiBloccoDietro(posMondox,posMondoy,(bloccoAria),lum)

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c and lum==6 and nLegno>0:
                    nLegno-=1
                    nOakPlanks+=4
                if event.key==pygame.K_c and lum==7 and nOakPlanks>1:
                    nOakPlanks-=2
                    nScale+=1
                if event.key==pygame.K_c and lum==8 and nFoglie>0:
                    nFoglie-=1
                    if random.randint(0,4)==2:
                        nSaplings+=1

                if event.key==pygame.K_e:
                    if lum==9:
                        lum=1
                    elif lum==8:
                        lum=9
                        cooldown=0
                    else:
                        lum=lum+1
                if event.key==pygame.K_q:
                    if lum==1:
                        lum=9
                        cooldown=0
                    else:
                        lum=lum-1
                
                if event.key==pygame.K_F3:
                    if F3:
                        F3=False
                    else:
                        F3=True


        keys = pygame.key.get_pressed()
        if keys[K_d]:
            player.muovi_Destra()
        else:
            player.StopDestra()
        
        if keys[K_a]:
            player.muovi_Sinistra()
        else:
            player.StopSinistra()
        
        if keys[K_a]==False and keys[K_d]==False and player.inAria==False:
            player.stopAll()

        if keys[K_SPACE]:
            player.Salto()
        
        if keys[K_w]:
            saleScala(player,Mondo)
        if keys[K_s]:
            scendeScala(player,Mondo)
        if keys[K_LSHIFT]:
            suScala(player,Mondo)

        
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
        if keys[K_6]:
            lum=6
        if keys[K_7]:
            lum=7
        if keys[K_8]:
            lum=8
        if keys[K_9]:
            lum=9
            cooldown=0

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
            dati.append(player.rect.left)
            dati.append(player.rect.top)
            dati.append(vitaTot)
            dati.append(tempo)
            dati.append(nOakPlanks)
            dati.append(nScale)
            dati.append(nSaplings)
            dati.append(nDay)
            dati.append(nDay1)
            dati.append(Diff)
            if Sfondo.notte==True:
                dati.append(0)
            else:
                dati.append(1)
            SalvaDati(dati,nomeSalvataggio,nomeMondo)
            Diff=None

            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.load("Sounds/MainTheme/MainMenu.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1,1)
            Fantasma=[]
            fantasmaPres=0

        
        
        collisioneBlocchiLati(player, Mondo)
        posMondoy=scorriMondoAlto(player, Mondo, posMondoy)
        posMondox=scorriMondolati(player,Mondo,posMondox)
        if tempo>=100 and tempo<=200 and Sfondo.notte==False:
            CresceSapling(Mondo,posMondox,posMondoy)
        tempo*=Sfondo.draw(tempo,posMondoy)
        
        Mondo.draw(posMondox,posMondoy)
        box1.draw(1,nFoglie)
        box2.draw(2,nLegno)
        box3.draw(3,nPietra)
        box4.draw(4,nErba)
        box5.draw(5,nTerra)
        box6.draw(6,nOakPlanks)
        box7.draw(7,nScale)
        box8.draw(8,nSaplings)
        box9.draw(9,"")

        player.calcolaVelMax()
        if caduto==True and player.velMax>=11.8:
            danno+=dannoDaCaduta(player)
            player.velMax=0
            dannoSuono.play()

        if Sfondo.notte==True and fantasmaLim>fantasmaPres:
            Fantasma.append(fantasmaSpawn(FantasmaSpeed))
            #aggiungi audio fantasma
            fantasmaPres+=1

        if fantasmaPres>0:
            i=0
            for entita in Fantasma:
                
                fantasmaMove(entita,player)
                entita.draw()
                if player.rect.collidepoint(entita.rect.topleft) or player.rect.collidepoint(entita.rect.bottomleft) or player.rect.collidepoint(entita.rect.topright) or player.rect.collidepoint(entita.rect.bottomright):
                    danno+=2
                    dannoSuono.play()
                    Fantasmarisata.play()
                    fantasmaPres-=1
                    Fantasma.pop(i)
                if ProPres==True:
                    if entita.rect.collidepoint(Proiettile.rect.center):
                        fantasmaPres-=1
                        FantasmaSuono.play()
                        Fantasma.pop(i)

                i=i+1

        if regen >= 300 and vitaTot < 10:
            vitaTot+=1
            regen = 0
        
        if vitaTot==0:
            pygame.mixer.music.stop()
            fase=4
            YouDiedSuono.play()
            pygame.mixer.music.load("Sounds/MainTheme/YouDiedMusic.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)

        vitaTot-=danno
        if vitaTot<0:
            vitaTot=0
        vitaTmp=vitaTot
        for i in range(len(vita)):
            if vitaTmp==1:
                vita[i][1]=1
                vitaTmp-=1
            elif vitaTmp>=2:
                vita[i][1]=0
                vitaTmp-=2
            else:
                vita[i][1]=2
        if vitaTot<10:
            regen+=1
        
        for cuore in vita:
            cuore[0].draw(cuore[1])

        if ProPres:
            Proiettile.muovi(velProX,velProY)
            if Proiettile.rect.centerx>1000 or Proiettile.rect.centerx<0 or Proiettile.rect.centery>700 or Proiettile.rect.centery<0:
                ProPres=False
            Proiettile.draw()
        
        
        if F3:
            FpsF3.drawNormal(str(round(clock.get_fps())))
            NdayF3.drawNormal(str(nDay))
            PosXMF3.drawNormal(str(round(posMondox)))
            PosYMF3.drawNormal(str(round(posMondoy)))
            PosXPF3.drawNormal(str(round(player.rect.left)))
            PosYPF3.drawNormal(str(round(player.rect.bottom)))
            DiffF3.drawNormal(str(Diff))

        player.muovi()
        player.draw()
        if Sfondo.notte==True and nDay1<nDay:
            nDay1=nDay
            fantasmaLim=int(round(nDay/2))
        elif Sfondo.notte==False and nDay1==nDay:
            nDay=nDay1+1
        if Sfondo.notte==True:
            fantasmaLim=int(round(nDay/2))
        
        if tempo%7==0 and cooldown<7:
            cooldown+=1

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
        elif lum==6:
            box6.draw(6,nOakPlanks,True)
        elif lum==7:
            box7.draw(7,nScale,True)
        elif lum==8:
            box8.draw(8,nSaplings,True)
        elif lum==9:
            box9.draw(9,"",True,cooldown)
        
        tempo+=1
    pygame.display.update()
    clock.tick(fps)