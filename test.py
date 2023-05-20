import pygame
from pygame.locals import *
pygame.init()

pygame.mixer.music.load("Sounds/MainMusic.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
danno=pygame.mixer.Sound("Sounds/Damage.mp3")

r=True
while r:
    x=input("ciao")
    if x=="1":
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.load("Sounds/MenuMusic.mp3")
        pygame.mixer.music.play(0,1)
