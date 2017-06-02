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
#tela = pyg.display.set_mode((500,500),pyg.FULLSCREEN)

#background = pyg.image.load(os.path.join(img_folder,"FundoDemo.png")).convert()
pista = pyg.image.load(os.path.join(img_folder,"track final.png"))
faixa = pyg.image.load(os.path.join(img_folder,"faixa.png"))
fakeline = pyg.image.load(os.path.join(img_folder,"fake line.png"))
carro = pyg.image.load(os.path.join(img_folder,"RED_INDEX.png"))#.convert_alpha()
#carro_mask = pyg.mask.from_surface((os.path.join(img_folder,"carro vermelho mask.png")))
#carro_mask = carro_mask(15,24)
#pista_mask = pista_mask(1383,1448.4)
#bg_mask = bg_mask(1500,1500)
#pista_mask = pyg.image.load(os.path.join(img_folder,"track final pista mask black.png")).convert_alpha()
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
red = (255,0,0)
black =(0,0,0)
BLUE = (0,39,255,255)
BLACK = (255, 255, 255, 0)
#BLACK =()
FPS = 60
YEllOW = (246,255,0,255)
LAPS=0
TEMPO = 0  # Variavel que recebera o tempo da volta
y = 0
key = 0
key2=0
smallfont = pyg.font.SysFont("comicsansms",20)  #  Fonte da letra usada no Lap e timer.
fonte_titulo = pyg.font.SysFont("comicsansms",60)
fonte_instrucoes = pyg.font.SysFont("comicsansms",15)
def score(score):

	text = smallfont.render("Laps: "+str(score),True, BLACK)
	#if faixa.get_at((int(xpos - pistax), int(ypos - pistay))) == YEllOW:
		#score += 1

	screen.blit(text, [0,0])
def tempo(Tempo):
    text1 = smallfont.render("Tempo total: "+str(timer),True,BLACK)
    text2 = smallfont.render("Tempo da volta: "+str(Tempo),True, BLACK)
    screen.blit(text1,[250,0])
    screen.blit(text2,[250,24])


clock = pyg.time.Clock()

#click do jogador
click = pyg.mixer.Sound(os.path.join("musicas","click.wav"))
click.set_volume(0.4)
#click.play(0)

#musica 1
m_1 = pyg.mixer.Sound(os.path.join("musicas","parte1.wav"))
m_1.set_volume(0.2)
#m_1.play(-1)

#musica 2
m_2 = pyg.mixer.Sound(os.path.join("musicas", "parte2.wav"))
m_2.set_volume(0.2)
#m_2.play(-1)

#musica 3
m_3 = pyg.mixer.Sound(os.path.join("musicas","parte3.wav"))
m_3.set_volume(0.2)
m_3.play(-1)

#carro acelerando
carro_acelerando = pyg.mixer.Sound(os.path.join("musicas","carro_acelerando.wav"))
carro_acelerando.set_volume(0.2)

#carro na grama
grama = pyg.mixer.Sound(os.path.join("musicas","grama.wav"))
grama.set_volume(0.3)

#carro de re
re=pyg.mixer.Sound(os.path.join("musicas","re.wav"))
re.set_volume(0.3)
def show_game_over():
    screen.fill(black)
    text_title = fonte_titulo.render("Game Over",True,red)
    screen.blit(text_title,[150,100])
    pyg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                exit(0)

def score(score):  # Funçao que mostra o numero de Laps dadas , na tela do jogador.
    text = smallfont.render("Laps: "+str(score),True, BLACK)
    screen.blit(text, [0,0])

def tempo(Tempo):  # Funçao que mostra o tempo totatl e o tempo da volta na tela do jogador.

    text1 = smallfont.render("Tempo total: "+str(timer),True,BLACK)
    text2 = smallfont.render("Tempo da volta: "+str(Tempo),True, BLACK)
    screen.blit(text1,[250,0])
    screen.blit(text2,[250,24])
#lista de sprites:
#all_sprites_carros = pyg.sprite.Group()#sprites de carros
#all_sprites_extra = pyg.sprite.Group()#sprites da pista e BG
#adiciona ao grupo de sprites:
#all_sprites_carros.add(carro_mask)
#all_sprites_extra.add(pista_mask)
#all_sprites_extra.add(bg_mask)
z = 0
timer = 0
running = True
while running:
    pyg.display.set_caption('Random Race')
    screen.fill(0)
    clock.tick(FPS)
    timer = pyg.time.get_ticks()/1000
#    print(pistax,pistay)
#    print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))))

    #limite exterior
    if pistax >= 270:
        pistax = pistax -5
        forward = 0.01
    if pistax <= -1200:
        pistax = pistax + 5
        forward = 0.01
    if pistay >= 350:
        pistay= pistay - 5
        forward = 0.01
    if pistay <= -1125:
        pistay = pistay + 5
        forward = 0.01

    if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == WHITE:
        if forward >2:
            forward = 2
        if forward < -2:
        	forward = -2
        if keys[2]==True:
            forward = -2
        if keys[3]==True:
            forward = 2

    if fakeline.get_at((int(xpos - pistax), int(ypos - pistay))) == BLUE:  # Precisa passar por essa faixa para conseguir comprletar a volta.
        key = 1  #  Chave para poder contabilizar a Lap.
        key2 = 1
#    print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))))
#    print(faixa.get_at((int(xpos - pistax), int(ypos - pistay))))
#    if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == WHITE:
#        pyg.quit()
#        exit(0)
    if faixa.get_at((int(xpos - pistax), int(ypos - pistay))) == YEllOW:  #  Linha de chegada .
        if LAPS == 0 and TEMPO == 0 and key==0:
            LAPS = 0
            TEMPO = timer - timer
            x = TEMPO
            y = timer

        elif LAPS == 0 and TEMPO>=0 and timer-y>10 and key == 1:
            LAPS = 1
            TEMPO = timer
            y = timer  #  y e igual ao timer naquele instante.
            x= TEMPO  # Tempo da volta.
            key = 0  # Zera a chave.


        elif LAPS >=1 and TEMPO >=0 and timer-y >10 and key == 1:
            LAPS += 1
            TEMPO = timer - y  #  Tempo total - tempo da volta anterior.
            x = TEMPO
            y = timer  #  y e igual ao timer naquele instante.
            key =  0


        elif LAPS == 1 and key2 ==1 :
            show_game_over()




## nao pode sair do jogo mais sim retornar fin do jogo e o player ganhador
#    if LAPS == 1:

#     running = False
    #if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == NO_COLOR:

    if keys[2]==True:
        if forward > -10:
            forward-= 0.08
        if forward < -10:
            forward = forward
    if keys[3]==True:
        if forward < 7:
            forward += 0.20
        if forward > 5:
            forward = 5
    if keys[0]==True:
        direction+= 2.5
    if keys[1]==True:
        direction-= 2.5
    
    movex=math.cos(direction/57.29)*forward
    movey=math.sin(direction/57.29)*forward
    pistax+=movex
    pistay-=movey


    carro_rot = pyg.transform.rotate(carro,direction)
    #screen.blit(background,(0,0))
    screen.blit(fakeline,(pistax,pistay))
    screen.blit(pista, (pistax,pistay))
    screen.blit(faixa,(pistax,pistay))
    screen.blit(carro_rot, (xpos,ypos))
   
    score(LAPS)
    tempo(TEMPO)

    #screen.blit(carro_mask, (xpos,ypos))
    pyg.display.flip()
    time.sleep(0.02)
    '''if pistax >= 280 or pistax <= -1200 and pistay >= 360 or pistay <= -1130:
        forward
        xpos -= 5
        ypos -= 5
        pistay += movey
        pistax -= movex
'''
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
#                if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == BLACK:
                carro_acelerando.play(-1)
        #        if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == WHITE:
        #            grama.play(-1)
                keys[2]=True
            
            elif event.key==K_DOWN:
                re.play(-1)
                keys[3]=True
            
            elif event.key == pyg.K_F10:
            	pyg.display.toggle_fullscreen()
           
            elif event.key == pyg.K_ESCAPE:
                pyg.quit()
                exit(0)

        if event.type == pyg.KEYUP:
            if event.key==pyg.K_LEFT:
                keys[0]=False
            
            elif event.key==pyg.K_RIGHT:
                keys[1]=False
            
            elif event.key==pyg.K_UP:
                carro_acelerando.stop()
                grama.stop()
                n=0
                if forward < 0 :
                    for i in range(n):
                        if forward < 0:
                            forward= forward +( 0.02* i)
                        if forward > 0:
                            forward = 0
                if forward > 0:
                    forward = 0
                keys[2]=False
            
            elif event.key==pyg.K_DOWN:
                re.stop()
                keys[3]=False
