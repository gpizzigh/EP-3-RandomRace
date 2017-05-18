import pygame as pyg
from pygame.locals import *
import time
import math
import os
from classes import *
#-------------------Class-------------------------------------------------------


#-------------------------------------------------------------------------------
pyg.init()


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"resourses\imagens")

screen = pyg.display.set_mode((500,500))
FPS = 40
#background = pyg.image.load(os.path.join(img_folder,"FundoDemo.png")).convert()
pista = pyg.image.load(os.path.join(img_folder,"track final.png"))
faixa = pyg.image.load(os.path.join(img_folder,"faixa.png"))
carro = pyg.image.load(os.path.join(img_folder,"carro vermelho Demo.png"))#.convert_alpha()
#carro_mask = pyg.mask.from_surface((os.path.join(img_folder,"carro vermelho mask.png")))
#carro_mask = carro_mask(15,24)
#pista_mask = pista_mask(1383,1448.4)
#bg_mask = bg_mask(1500,1500)
#pista_mask = pyg.image.load(os.path.join(img_folder,"track final pista mask black.png"))
bg_mask = pyg.image.load(os.path.join(img_folder,"track final mask white.png"))
#carro_mask = pyg.image.load(os.path.join(img_folder,"carro vermelho mask.png"))
pistax= 0
pistay= -1000
xpos = 275
ypos = 350
keys=[False,False,False,False]
direction = 0
forward = 0
WHITE = (255, 255, 255, 255)
YEllOW = (246,255,0,255)
BLACK = (0,0,0,0)
LAPS=0
TEMPO = 0
smallfont = pyg.font.SysFont("comicsansms",25)
def score(score):

	text = smallfont.render("Laps: "+str(score),True, YEllOW)
	#if faixa.get_at((int(xpos - pistax), int(ypos - pistay))) == YEllOW:
		#score += 1


	screen.blit(text, [0,0])
def tempo(Tempo):
    #text1 = smallfont.render("Tempo total: "+str(timer),True,YELLOW)
    text2 = smallfont.render("Tempo da volta: "+str(Tempo),True, BLACK)
    #screen.blit(text1,[,])
    screen.blit(text2,[250,0])

clock = pyg.time.Clock()

dt = 0
TEMPO = 0
timer2 =0
y = 0
running = True
while running:
    clock.tick(FPS)
    timer = pyg.time.get_ticks()/1000

    #timer = pyg.time.set
    #Y = timer
    pyg.display.set_caption('Random Race')
    screen.fill(0)
    # Verifica se o carro bateu na pista.
    print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))))
    print(faixa.get_at((int(xpos - pistax), int(ypos - pistay))))
    if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == WHITE:
        pyg.quit()
        exit(0)
    if faixa.get_at((int(xpos - pistax), int(ypos - pistay))) == YEllOW:
        timer2 = pyg.time.get_ticks()/40000
        timer = pyg.time.get_ticks()/1000
        if timer2 < 0.15:
            LAPS +=1
            TEMPO = timer - TEMPO



        #elif TEMPO > 40:
            #TEMPO = x

    print(timer)
    print(timer2)
    # lista_de_colisao = pyg.sprite.spritecollide(all_sprites_carros,all_sprites_extra,False)
    # for carro in lista_de_colisao:
    #     print("carro bateu")
    #     running = False
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
    screen.blit(faixa,(pistax,pistay))
    screen.blit(carro_rot, (xpos,ypos))

    score(LAPS)
    tempo(TEMPO)
    #screen.blit(carro_mask, (xpos,ypos))
    pyg.display.flip()
    time.sleep(0.02)

    for event in pyg.event.get():
        #da update no grupo de sprites:
        # all_sprites_list.update()
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
