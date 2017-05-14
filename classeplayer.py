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

<<<<<<< HEAD
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"arte_grafica")
=======
'''d_angle = 20
angle = 0'''

Display_largura = 1152
Display_altura = 654
>>>>>>> 8749e75190ffafad66c5aadb68b6159f888baea0
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
<<<<<<< HEAD

background = pyg.image.load(os.path.join(img_folder,"grama.png")).convert()
pista = pyg.image.load(os.path.join(img_folder,"pista2.0.png")).convert()
pista = pyg.image.set_colorkey(black)
faixa = pyg.image.load(os.path.join(img_folder,"linha_de_chegada.png")).convert()
carro  = pyg.image.load("carro.jpeg").convert()

=======
background = pyg.image.load("pista2.png")
>>>>>>> 8749e75190ffafad66c5aadb68b6159f888baea0
clock = pyg.time.Clock()

class Player(pyg.sprite.Sprite):
        def __init__(self):
<<<<<<< HEAD
            pyg.sprite.Sprite.__init__(self)
            self.image = pyg.image.load("carro.png").convert()
            self.image = pyg.tranform.scale(pygame.image.load(gamegame.img_dir)).convert_alpha(), (TILESIZE,TILESIZE)
            self.image.set_colorkey(black) # deixa transparente as partes a mais do retancgulo
            self.rect = self.image.get_rect()
            self.rect.centerx = 300
            self.rect.bottom = 300
=======
            pyg.sprite.Sprite.__init__(self)  #  Parte que e necessaria para utilizar as funcoes do sprite
            self.image = pyg.image.load("carro.jpeg").convert()  # da load na imgem
            self.image.set_colorkey(black) # deixa transparente as partes a mais do retancgulo

            self.rect = self.image.get_rect()  #  Cria um retangulo em volta da imgem
            # onde muda a localizacao do carrinho
            self.rect.centerx = 520  # localizacao do carrinho eixo x
            self.rect.bottom = 580  # Localizacao da  parte inferior da imgem
>>>>>>> a6d84decc7a3b49127b13555a3edd0c4a7d47964
            self.speedx = 0
            self.speedy = 0
            #self.angle = -90   # teste


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
                self.speedx = 5
                #self.angle += 20
            if keystate[pyg.K_RIGHT]:
                self.speedx = -5
                #self.angle -= 20

            self.rect.y += self.speedy
            self.rect.x += self.speedx

            '''self.rect.y -= self.speedy*math.sin(math.pi*self.angle/180)
            self.rect.x += self.speedy*math.cos(math.pi*self.angle/180)
            self.rect.center(pyg.transform.rotate(self.image,self.angle+90),[self.rect.x,self.rect.y, 10, 10])'''


            if self.rect.right > Display_largura or self.rect.left > Display_largura or self.rect.bottom > Display_largura or self.rect.top > Display_largura :
                self.rect.right = Display_largura
            if self.rect.left < 0 or self.rect.right <0 or self.rect.bottom <0 or self.rect.top <0:
                self.rect.left = 0

            if self.rect.bottom > Display_altura or self.rect.right > Display_altura or self.rect.left > Display_altura  or self.rect.top > Display_altura:  # ERRRO
                self.rect.bottom = Display_altura




'''class Oponente(pyg.sprite.Sprite):
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
<<<<<<< HEAD
=======
                self
            if keystate[pyg.K_d]:
>>>>>>> 8749e75190ffafad66c5aadb68b6159f888baea0
                self

            self.rect.y += self.speedy
            if self.rect.right > Display_largura:

                self.rect.right = Display_largura
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > Display_altura:  # ERRRO
                self.rect.right = 0
'''

<<<<<<< HEAD
all_sprites = pyg.sprite.Group()
player = Player()
all_sprites.add(player)

=======
all_sprites = pyg.sprite.Group()  # Cria um grupo para sprite
player = Player()  # Player
oponente = Oponente()
oponente_grupo = pyg.sprite.Group()   # Cria um grupo chamado oponente_grupo
oponente_grupo.add(oponente)   # Adiciona o opnente ao grupo oponente_grupo
all_sprites.add(player)   #
all_sprites.add(oponente)
>>>>>>> a6d84decc7a3b49127b13555a3edd0c4a7d47964

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
<<<<<<< HEAD
    screen.blit(background, (0,0, Display_altura, Display_largura))
    screen.blit(pista, (0,0, Display_pista_alt,Display_pista_larg))
    screen.blit(faixa,(0,0,Display_faixa_alt,Display_faixa_larg))
    screen.blit(pyg.transform.rotate(carro,angle),[lead_x, lead_y, 10, 10])
=======
    # check to see if a mob hit player
    '''bateu
    bateu_player = pyg.sprite.spritecollide(player,oponente,False)
    bateu_oponente = pyg.sprite.spritecollide(oponente,player,False)
    if bateu_player:
        player1.rect.centery = bateu

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

>>>>>>> 8749e75190ffafad66c5aadb68b6159f888baea0
    all_sprites.draw(screen)


    # after drawing everything , flip the display
    pyg.display.flip()



pyg.quit()
