import math
import pygame as pyg
#import classeplayer.py
#--------------------------------------------------Funçoes------------------------------------------------------------------------------------------
#--------------------------------------------------Programa Principal-------------------------------------------------------------------------------
pyg.init()

white = (255,255,255)
Display_largura = 1152
Display_altura = 654

screen = pyg.display.set_mode((Display_largura,Display_altura))
pyg.display.set_caption("Random Race")

background = pyg.image.load("Pista.jpeg")
car  = pyg.image.load("carro.jpeg")

clock = pyg.time.Clock()
FPS=15
lead_x = 520
lead_y = 580
lead_x_change = 0
lead_y_change = 0
#global direction
#direction = "right"
d_angle = 20
angle = 0
d_vel = 5
vel = 0

out = False
#global direction
#if direction == "right":
    #head = pyg.transform.rotate(car,180)
#if direction == "left":
    #head = pyg.transform.rotate(car,180)
#if direction == "up":
    #head = pyg.transform.rotate(car,180)
#if direction == "down":
    #head = pyg.transform.rotate(car,180)

#-----------------------------Game LOOP------------------------------------------------------------
while out != True:
    for event in pyg.event.get():
        #global direction
        if event.type == pyg.QUIT:
            out = True

        if event.type == pyg.KEYDOWN:

                if event.key == pyg.K_LEFT:
                    #direction = "left"
                    angle +=d_angle
                elif event.key == pyg.K_RIGHT:
                   # direction = "right"
                    angle -= d_angle

                elif event.key == pyg.K_UP:
                   # direction = "up"
                    vel += d_vel

                elif event.key == pyg.K_DOWN:
                   # direction = "down"
                    vel -= d_vel
        #if event.type == pyg.KEYUP:
                #if event.key == pyg.K_LEFT:
                    #direction = "left"
                    #angle = angle
                #elif event.key == pyg.K_RIGHT:
                   # direction = "right"
                    #angle -= angle




    lead_x += vel * math.cos(math.pi * angle / 180.0)
    lead_y -= vel * math.sin(math.pi * angle / 180.0)

    if lead_x >= Display_largura or lead_x < 0 or lead_y >= Display_altura or lead_y < 0:
        out = True
    
    screen.blit(background, (0,0, Display_altura, Display_largura))

    screen.blit(pyg.transform.rotate(car,angle+90),[lead_x, lead_y, 10, 10])

    #screen.blit(car,[lead_x,lead_y,10,10])


    pyg.display.update()
    clock.tick(FPS)

pyg.quit()
