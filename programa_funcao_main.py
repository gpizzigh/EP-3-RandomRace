import math
import pygame as pyg
import os
#--------------------------------------------------Funçoes------------------------------------------------------------------------------------------
#--------------------------------------------------Programa Principal-------------------------------------------------------------------------------
pyg.init()

white = (255,255,255)


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"arte_grafica")


#comprimeto Fundo--------------------
Display_largura = 400
Display_altura = 400
#----------------------------------
#comprimento Pista-------------
Display_pista_larg = 200
Display_pista_alt = 200
#----------------------------
#comprimeto Faixa ---------------
Display_faixa_larg =7
Display_faixa_alt = 9
screen = pyg.display.set_mode((Display_largura,Display_altura))
pyg.display.set_caption("Random Race")

background = pyg.image.load(os.path.join(img_folder,"grama.png")).convert()
pista = pyg.image.load(os.path.join(img_folder,"pista2.0.png")).convert_alpha()
faixa = pyg.image.load(os.path.join(img_folder,"linha_de_chegada.png")).convert()
carro  = pyg.image.load(os.path.join(img_folder,"carrofinal2.png")).convert_alpha()

clock = pyg.time.Clock()

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0
global direction
direction = "right"
d_angle = 20
angle = 180
d_vel = 2
vel = 3
out = False
#global direction
if direction == "right":
    head = pyg.transform.rotate(carro,180)
if direction == "left":
    head = pyg.transform.rotate(carro,180)
if direction == "up":
    head = pyg.transform.rotate(carro,180)
if direction == "down":
    head = pyg.transform.rotate(carro,180)

#-----------------------------Game LOOP------------------------------------------------------------
while out != True:
    for event in pyg.event.get():
        #global direction
        if event.type == pyg.QUIT:
            out = True
        if event.type == pyg.KEYDOWN:

                if event.key == pyg.K_LEFT:
                    direction = "left"
                    angle += d_angle
                elif event.key == pyg.K_RIGHT:
                    direction = "right"
                    angle -= d_angle

                elif event.key == pyg.K_UP:
                    direction = "up"
                    vel += d_vel

                elif event.key == pyg.K_DOWN:
                    direction = "down"
                    vel -= d_vel


    lead_x += vel * math.cos(math.pi * angle / 180.0)
    lead_y -= vel * math.sin(math.pi * angle / 180.0)
    if lead_x >= Display_largura or lead_x < 0 or lead_y >= Display_altura or lead_y < 0:
        pass
    if lead_x >= 401 or lead_x < 1 or lead_y >= 401 or lead_y < 1:
        out = True
    screen.blit(background, (0,0, Display_altura, Display_largura))
    screen.blit(pista, (0,0, Display_pista_alt,Display_pista_larg))
    screen.blit(faixa,(0,0,Display_faixa_alt,Display_faixa_larg))
    screen.blit(pyg.transform.rotate(carro,angle),[lead_x, lead_y, 10, 10])
    pyg.display.update()
    clock.tick(27)

pyg.quit()
