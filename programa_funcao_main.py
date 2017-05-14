import math
import pygame as pyg
import classeplayer.py
#--------------------------------------------------Funçoes------------------------------------------------------------------------------------------
#--------------------------------------------------Programa Principal-------------------------------------------------------------------------------
pyg.init()

white = (255,255,255)
Display_largura = 1152
Display_altura = 654

screen = pyg.display.set_mode((Display_largura,Display_altura))
pyg.display.set_caption("Random Race")

background = pyg.image.load("pista2.png")
carro  = pyg.image.load("carro.jpeg")
set_colorkey(white, flags=0)
set_colorkey(None)
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
    head = pyg.transform.rotate(car,180)
if direction == "left":
    head = pyg.transform.rotate(car,180)
if direction == "up":
    head = pyg.transform.rotate(car,180)
if direction == "down":
    head = pyg.transform.rotate(car,180)

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
    if lead_x >= 1152 or lead_x < 0 or lead_y >= 654 or lead_y < 0:
        out = True
    screen.blit(background, (0,0, Display_altura, Display_largura))
    screen.blit(pyg.transform.rotate(car,angle),[lead_x, lead_y, 10, 10])
    screen.blit(carro,[lead_x,lead_y,10,10])

    pyg.display.update()
    clock.tick(27)

pyg.quit()
