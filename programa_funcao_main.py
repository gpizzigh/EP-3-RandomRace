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

background = pyg.image.load("Pista.jpeg")
carro  = pyg.image.load("carro.jpeg")

clock = pyg.time.Clock()

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

d_angle = 20
angle = 180
d_vel = 2
vel = 3


out = False
while out != True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            out = True
<<<<<<< HEAD
            
=======
        if event.type == pyg.KEYDOWN:

                if event.key == pyg.K_LEFT:
                    angle += d_angle
                elif event.key == pyg.K_RIGHT:
                    angle -= d_angle
                elif event.key == pyg.K_UP:
                    vel += d_vel
                elif event.key == pyg.K_DOWN:
                    vel -= d_vel
>>>>>>> 0da5df51e9ee1b5629a6ffac5e3e73fa8e42d7b5

    lead_x += vel * math.cos(math.pi * angle / 180.0)
    lead_y -= vel * math.sin(math.pi * angle / 180.0)
    if lead_x >= Display_largura or lead_x < 0 or lead_y >= Display_altura or lead_y < 0:
        pass
    if lead_x >= 1152 or lead_x < 0 or lead_y >= 654 or lead_y < 0:
        out = True
    screen.blit(background, (0,0, Display_altura, Display_largura))
    screen.blit(carro,[lead_x,lead_y,10,10])

    pyg.display.update()
    clock.tick(27)

pyg.quit()
