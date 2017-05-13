import math
import pygame as pyg
import os
#--------------------------------------------------Funçoes------------------------------------------------------------------------------------------

#--------------------------------------------------Programa Principal-------------------------------------------------------------------------------
pyg.init()
# definicao das cores

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

angle = math.pi
variacao_angle =(math.pi/180)*10

Display_largura = 1152
Display_altura = 654
fps = 30

screen = pyg.display.set_mode((Display_largura,Display_altura))
pyg.display.set_caption("Random Race")
background = pyg.image.load("Pista.jpeg")
clock = pyg.time.Clock()

class Player(pyg.sprite.Sprite):
        def __init__(self):
            pyg.sprite.Sprite.__init__(self)
            self.image = pyg.image.load("carro.jpeg").convert()
            self.image.set_colorkey(black) # deixa transparente as partes a mais do retancgulo

            self.rect = self.image.get_rect()
            # onde muda a localizacao do carrinho
            self.rect.centerx = 300
            self.rect.bottom = 300  # parte inferior
            self.speedx = 0    # velocidade
            self.speedy = 0
            self.angle = 180






        def update(self):
            self.speedx = 0
            self.speedy = 0
            self.angle  = 180

            keystate = pyg.key.get_pressed()
            #if keystate[pyg.K_LEFT]:
            #if keystate[pyg.K_RIGHT]:

            if keystate[pyg.K_DOWN]:
                self.speedy = 5
                self.rect.y += self.speedy
                self.rect.x += self.speedx

            if keystate[pyg.K_UP]:
                self.speedy = -5
                self.rect.y += self.speedy
                self.rect.x += self.speedx

            if keystate[pyg.K_LEFT]:
                self.speedx = -10
                self.angle -= 45
                self.rect.y += self.speedy*math.sin(math.pi*self.angle/180)
                self.rect.x += self.speedx*math.cos(math.pi*self.angle/180)
            if keystate[pyg.K_RIGHT]:
                self.speedx= 10
                self.angle += 45
                self.rect.y += self.speedy*math.sin(math.pi*self.angle/180)
                self.rect.x += self.speedx*math.cos(math.pi*self.angle/180)






            if self.rect.right > Display_largura:
                self.rect.right = Display_largura
            if self.rect.left < 0:
                self.rect.left = 0

            if self.rect.bottom > Display_altura:  # ERRRO
                self.rect.bottom = 0




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
            if keystate[pyg.K_d]:
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
    # check to see if a mob hit player
    '''def collide (player, oponente):
        if hits = pyg.sprite.spritecollide(player,pista,False)
            if hits:
                player.speedy = player.speedy * 1/4
            speedy = speedy * 1/4


        if oponente == grama:
            hits2 = pyg.sprite.spritecollide(oponente,pista,False)
            speedy = speedy * 1/4

        if oponente == player:'''



    #screen.fill(blue)
        #Draw / render]
    screen.blit(background, (0,0,Display_altura,Display_largura))

    all_sprites.draw(screen)


    # after drawing everything , flip the display
    pyg.display.flip()



pyg.quit()
