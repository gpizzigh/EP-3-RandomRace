import pygame as pyg
from pygame.locals import *
import time
import math
import os

pyg.init()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"arte_grafica")



screen = pyg.display.set_mode((500,500))

#background = pyg.image.load(os.path.join(img_folder,"FundoDemo.png")).convert()
pista = pyg.image.load(os.path.join(img_folder,"track final.png"))
carro = pyg.image.load(os.path.join(img_folder,"carro vermelho Demo1.0.png"))#.convert_alpha()
pistax= 0
pistay= -1000
xpos = 275
ypos = 350
keys=[False,False,False,False]
direction = 0
forward = 0


running = 1
while running:
    pyg.display.set_caption('Random Race')
    screen.fill(0)

    if keys[0]==True:
        direction+= 2
    if keys[1]==True:
        direction-= 2
    if keys[2]==True:
        forward-= 0.2
    if keys[3]==True and forward <= 0:
        forward+= 0.2

    movex=math.cos(direction/57.29)*forward
    movey=math.sin(direction/57.29)*forward
    pistax+=movex
    pistay-=movey

    carro_rot = pyg.transform.rotate(carro,direction)
    #screen.blit(background,(0,0))
    screen.blit(pista, (pistax,pistay))
    screen.blit(carro_rot, (xpos,ypos))
    pyg.display.flip()
    time.sleep(0.02)

    for event in pyg.event.get():
    # checa se sai do jogo
        if event.type==pyg.QUIT:
            # SAida do jogo
            pyg.quit()
            exit(0)

        if event.type == pyg.KEYDOWN:
            if event.key==K_LEFT:
                keys[0]=True
            elif event.key==K_RIGHT:
                keys[1]=True
            elif event.key==K_UP:
                keys[2]=True
            elif event.key==K_DOWN:
                keys[3]=True

        if event.type == pyg.KEYUP:
            if event.key==pyg.K_LEFT:
                keys[0]=False
            elif event.key==pyg.K_RIGHT:
                keys[1]=False
            elif event.key==pyg.K_UP:
                keys[2]=False
            elif event.key==pyg.K_DOWN:
                keys[3]=False
