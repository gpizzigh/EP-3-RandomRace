import math
import pygame as pyg
import os
#--------------------------------------------------Funçoes------------------------------------------------------------------------------------------

#--------------------------------------------------Programa Principal-------------------------------------------------------------------------------
pyg.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"arte_grafica")
fps = 30

pyg.display.set_caption("Random Race")
Display_largura = 400
Display_altura = 400
screen = pyg.display.set_mode((Display_largura,Display_altura))
#----------------------------------
#comprimento Pista-------------
Display_pista_larg = 900
Display_pista_alt = 350
#----------------------------
#comprimeto Faixa ---------------
Display_faixa_larg =20
Display_faixa_alt = 50
#-------------Variaveis-------------------
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
#----------------------------------------------
screen = pyg.display.set_mode((Display_largura,Display_altura))
pyg.display.set_caption("Random Race")

background = pyg.image.load(os.path.join(img_folder,"grama.png")).convert()
pista = pyg.image.load(os.path.join(img_folder,"pista2.0.png")).convert()
pista = pyg.image.set_colorkey(black)
faixa = pyg.image.load(os.path.join(img_folder,"linha_de_chegada.png")).convert()
carro  = pyg.image.load("carro.jpeg").convert()

clock = pyg.time.Clock()

class Player(pyg.sprite.Sprite):
        def __init__(self):
            pyg.sprite.Sprite.__init__(self)
            self.image = pyg.image.load("carro.jpeg").convert()
            self.image.set_colorkey(black) # deixa transparente as partes a mais do retancgulo

            self.rect = self.image.get_rect()
            self.rect.centerx = 300
            self.rect.bottom = 300
            self.speedx = 0


        def update(self):
            self.speedx = 0
            self.speedy = 0
            keystate = pyg.key.get_pressed()
            #if keystate[pyg.K_LEFT]:
            #if keystate[pyg.K_RIGHT]:


            if keystate[pyg.K_DOWN]:
                self.speedy = 5
            if keystate[pyg.K_UP]:
                self.speedy = -5
            if keystate[pyg.K_LEFT]:
                self

            self.rect.y += self.speedy
            if self.rect.right > Display_largura:
                self.rect.right = Display_largura
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > Display_altura:  # ERRRO
                self.rect.right = 0


class Oponente(pyg.sprite.Sprite):
        def __init__(self):
            pyg.sprite.Sprite.__init__(self)
            self.image = pyg.image.load("carro.jpeg").convert()
            self.image.set_colorkey(black) # deixa transparente as partes a mais do retancgulo

            self.rect = self.image.get_rect()
            self.rect.centerx = 600
            self.rect.bottom = 300
            self.speedx = 0


        def update(self):
            self.speedx = 0
            self.speedy = 0
            keystate = pyg.key.get_pressed()
            #if keystate[pyg.K_LEFT]:
            #if keystate[pyg.K_RIGHT]:


            if keystate[pyg.K_s]:
                self.speedy = 5
            if keystate[pyg.K_w]:
                self.speedy = -5
            if keystate[pyg.K_a]:
                self

            self.rect.y += self.speedy
            if self.rect.right > Display_largura:
                self.rect.right = Display_largura
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > Display_altura:  # ERRRO
                self.rect.right = 0


all_sprites = pyg.sprite.Group()
player = Player()
oponente = Oponente()
oponente_grupo = pyg.sprite.Group()
oponente_grupo.add(oponente)
all_sprites.add(player)
all_sprites.add(oponente)


running = True
while running:
    # keep loop runing at the right speed
    clock.tick(fps)
    #Process inout/(events)
    for event in pyg.event.get():
        #check for closing the window
        if event.type == pyg.QUIT:
            running = False
    #update
    all_sprites.update()
    screen.blit(background, (0,0, Display_altura, Display_largura))
    screen.blit(pista, (0,0, Display_pista_alt,Display_pista_larg))
    screen.blit(faixa,(0,0,Display_faixa_alt,Display_faixa_larg))
    screen.blit(pyg.transform.rotate(carro,angle),[lead_x, lead_y, 10, 10])
    all_sprites.draw(screen)


    # after drawing everything , flip the display
    pyg.display.flip()



pyg.quit()
