import pygame as pyg
#from MoverObjetos.py import MoverCarrinho

#---------------------------------------------------------------------------------------------------------------------------------------------------
#def main():

pyg.init()

white = (153,255,255)
black = (0,0,0)
red = (255,0,0)
Display_largura = 1152
Display_altura = 684

screen = pyg.display.set_mode((Display_largura,Display_altura))
pyg.display.set_caption("Random Race")

# img = pyg.image.load("Pista.jpeg").convert()
background = pyg.image.load("Pista.jpeg")

clock = pyg.time.Clock()

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

out = False
while out != True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            out = True
#----------------------------------------------------------MoverCarrinho()------------------------------------------------------------------------------

        if event.type == pyg.KEYDOWN:
                # lead_y_change = 0 para zerar a muddança no eixo y e mante somento no eixo x
                # se permanecer lead_x_change = + ou - 10 ele mudara no x e no y (diagonal)
                if event.key == pyg.K_LEFT:
                    lead_x_change = - 10
                    lead_y_change = 0
                elif event.key == pyg.K_RIGHT:
                    lead_x_change = + 10
                    lead_y_change = 0
                elif event.key == pyg.K_UP:
                    lead_y_change = - 10
                    lead_x_change = 0
                elif event.key == pyg.K_DOWN:
                    lead_y_change = + 10
                    lead_x_change = 0

#ao parar de pressionar a tecla para de mecher
#if event.type == pygame.KEYUP:
    #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #lead_x_change=0
#if event.type == pygame.KEYDOWN:
    #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #lead_x_change=0


    lead_x += lead_x_change
    lead_y += lead_y_change
    if lead_x >= Display_largura or lead_x < 0 or lead_y >= Display_altura or lead_y < 0:
        out = True

    lead_x_change = 0
    lead_y_change = 0
            #screen.fill(background)
    screen.blit(background, (0,0, Display_altura, Display_largura))
    pyg.draw.rect(screen, white, [lead_x, lead_y, 10, 10])
    #screen.blit(background, (0,0, Display_altura, Display_largura))
    pyg.display.update()
    clock.tick(27)

pyg.quit()


'''if __name__ == '__main__':
    main()
def BG(x,y):
    img.blit("Pista.jpeg",(w,y))'''
