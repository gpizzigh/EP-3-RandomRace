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

#background = pyg.image.load(os.path.join(img_folder,"FundoDemo.png")).convert()
pista = pyg.image.load(os.path.join(img_folder,"track final.png"))
faixa = pyg.image.load(os.path.join(img_folder,"faixa.png"))
carro = pyg.image.load(os.path.join(img_folder,"carro vermelho Demo.png"))#.convert_alpha()
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
<<<<<<< HEAD
BLACK = (255, 255, 255, 0)
=======

BLACK = (255, 255, 255, 0)
#BLACK =()

>>>>>>> 531c48b261b45ba73b110904e5a204f56ea10f69
YEllOW = (246,255,0,255)
LAPS=0
smallfont = pyg.font.SysFont("comicsansms",25)
def score(score):

	text = smallfont.render("Laps: "+str(score),True, YEllOW)
	#if faixa.get_at((int(xpos - pistax), int(ypos - pistay))) == YEllOW:
		#score += 1

	screen.blit(text, [0,0])

<<<<<<< HEAD
=======

>>>>>>> 531c48b261b45ba73b110904e5a204f56ea10f69
#lista de sprites:
#all_sprites_carros = pyg.sprite.Group()#sprites de carros
#all_sprites_extra = pyg.sprite.Group()#sprites da pista e BG
#adiciona ao grupo de sprites:
#all_sprites_carros.add(carro_mask)
#all_sprites_extra.add(pista_mask)
#all_sprites_extra.add(bg_mask)



running = True
while running:
    pyg.display.set_caption('Random Race')
    screen.fill(0)
    # Verifica se o carro bateu na pista.
<<<<<<< HEAD
    
#    print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))))
 #   print(pistax,pistay)
    if pistax >= 270: 
        pistax = pistax -5 
=======
<<<<<<< HEAD
    print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay)))) #(255,255,255,0)
    if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == WHITE:
        print("Colisao")
        #pyg.quit()
=======

#    print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))))
    print(pistax,pistay)
    if pistax >= 270:
        pistax = pistax -5
>>>>>>> 531c48b261b45ba73b110904e5a204f56ea10f69
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
#        if forward >2:
#            forward = 2
        if keys[2]==True:
            forward = 0
            forward = -2
        if keys[3]==True:
            forward = 0
            forward = 2

<<<<<<< HEAD
  #  print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))))
  #  print(faixa.get_at((int(xpos - pistax), int(ypos - pistay))))
 #   if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == WHITE:
  #      pyg.quit()
   #     exit(0)
    if faixa.get_at((int(xpos - pistax), int(ypos - pistay))) == YEllOW:
    	LAPS += 1

=======

#    print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))))
#    print(faixa.get_at((int(xpos - pistax), int(ypos - pistay))))
#    if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == WHITE:
#        pyg.quit()
#        exit(0)
    if faixa.get_at((int(xpos - pistax), int(ypos - pistay))) == YEllOW:
    	LAPS += 1
>>>>>>> 8d5ff9905e60ae9da0d28c27a874e0029ebe75cd

        #exit(0)
>>>>>>> 531c48b261b45ba73b110904e5a204f56ea10f69
    # lista_de_colisao = pyg.sprite.spritecollide(all_sprites_carros,all_sprites_extra,False)
    # for carro in lista_de_colisao:
    #     print("carro bateu")

#     running = False
    #if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == NO_COLOR:
    if keys[2]==True:
        forward-= 0.08
    if keys[3]==True and forward <= 0:
        forward+= 0.08
    if keys[0]==True:
        direction+= 2
    if keys[1]==True:
        direction-= 2
    movex=math.cos(direction/57.29)*forward
    movey=math.sin(direction/57.29)*forward
    pistax+=movex
    pistay-=movey


    carro_rot = pyg.transform.rotate(carro,direction)
    #screen.blit(background,(0,0))

    screen.blit(pista, (pistax,pistay))

<<<<<<< HEAD
    screen.blit(faixa,(pistax,pistay))

=======
#    screen.blit(pista_mask, (pistax,pistay))

    screen.blit(faixa,(pistax,pistay))
>>>>>>> 531c48b261b45ba73b110904e5a204f56ea10f69
    screen.blit(carro_rot, (xpos,ypos))

    score(LAPS)
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
                keys[2]=True
            elif event.key==K_DOWN:
                keys[3]=True
            elif event.key == pyg.K_ESCAPE:
                pyg.quit()
                exit(0)
        g = True
        if event.type == pyg.KEYUP:
            if event.key==pyg.K_LEFT:
                keys[0]=False
            elif event.key==pyg.K_RIGHT:
                keys[1]=False
            elif event.key==pyg.K_UP:
<<<<<<< HEAD
                forward = -2
#                while g:
#                    forward -= 1
#                    if forward == 0:
#                        g=False
=======
                forward = -5
>>>>>>> 531c48b261b45ba73b110904e5a204f56ea10f69
                keys[2]=False
            elif event.key==pyg.K_DOWN:
                keys[3]=False
