import math
import pygame as pyg
#--------------------------------------------------Funçoes------------------------------------------------------------------------------------------

#--------------------------------------------------Programa Principal-------------------------------------------------------------------------------
pyg.init()

white = (255,255,255)
Display_largura = 1152
Display_altura = 684

screen = pyg.display.set_mode((Display_largura,Display_altura))
pyg.display.set_caption("Random Race")

background = pyg.image.load("Pista.jpeg")

clock = pyg.time.Clock()

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

d_angle = 20
angle = 180
d_vel = 2
vel = 5

out = False
while out != True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            out = True
        if event.type == pyg.KEYDOWN:

                if event.key == pyg.K_LEFT:
                    angle += d_angle
                elif event.key == pyg.K_RIGHT:
                    angle -= d_angle
                elif event.key == pyg.K_UP:
                    vel += d_vel
                elif event.key == pyg.K_DOWN:
                    vel -= d_vel

    lead_x += vel * math.cos(math.pi * angle / 180.0)
    lead_y -= vel * math.sin(math.pi * angle / 180.0)
    if lead_x >= Display_largura or lead_x < 0 or lead_y >= Display_altura or lead_y < 0:
        out = True


    screen.blit(background, (0,0, Display_altura, Display_largura))
    pyg.draw.rect(screen, white, [lead_x, lead_y, 10, 10])
    pyg.display.update()
    clock.tick(27)

pyg.quit()
