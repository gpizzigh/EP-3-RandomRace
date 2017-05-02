import pygame as pyg

#---------------------------------------------------------------------------------------------------------------------------------------------------
#def main():
pyg.init()
Display_largura = 1152
Display_altura = 684
screen = pyg.display.set_mode((Display_largura,Display_altura))
img = pyg.image.load("Pista.jpeg").convert()
pyg.display.set_caption("Random Race")
clock = pyg.time.Clock()
background = pyg.image.load("Pista.jpeg")
out = False
while out != True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            out = True

    screen.blit(background, (0,0, Display_altura, Display_largura))
    pyg.display.update()
    clock.tick(27)
pyg.quit()


'''if __name__ == '__main__':
    main()
def BG(x,y):
    img.blit("Pista.jpeg",(w,y))'''
