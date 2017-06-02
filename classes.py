import pygame as pyg
from pygame.locals import *
import time
import math
import os

BLUE = (0,30,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"resourses\imagens")


class carro_mask(pyg.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pyg.Surface([width, height]) #define condiçoes de tamanho
        #self.image.fill(BLUE) #Prenche o carro com a cor azul
        #self.image.set_colorkey(WHITE) #deixa a imgem como transaprente(por ser mask continuara assim!)
        self.image = pyg.image.load(os.path.join(img_folder,"carro vermelho mask.png"))
        self.rect = self.image.get_rect()# dimençoes de um retangluo sendo do mesmo tamanho que a imagem
        self.mask = pyg.mask.from_surface(self.image)# Cria a mask para o carro
        self.rect = self.image.get_rect() #cria um rectangulo no formato do carro para ser considerado uma Surface

class bg_mask(pyg.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pyg.Surface([width, height]) #define condiçoes de tamanho
        #self.image.fill(WHITE) #Prenche o carro com a cor azul
        #self.image.set_colorkey(WHITE) #deixa a imgem como transaprente(por ser mask continuara assim!)
        self.image = pyg.image.load(os.path.join(img_folder,"track final mask white.png"))
        self.rect = self.image.get_rect()# dimençoes de um retangluo sendo do mesmo tamanho que a imagem
        self.mask = pyg.mask.from_surface(self.image)# Cria a mask para o fundo
        self.rect = self.image.get_rect() #cria um rectangulo no formato do fundo para ser considerado uma Surface

class pista_mask(pyg.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pyg.Surface([width, height]) #define condiçoes de tamanho
        #self.image.fill(WHITE) #Prenche o carro com a cor azul
        #self.image.set_colorkey(WHITE) #deixa a imgem como transaprente(por ser mask continuara assim!)
        self.image = pyg.image.load(os.path.join(img_folder,"track final pista mask black.png"))
        self.rect = self.image.get_rect()# dimençoes de um retangluo sendo do mesmo tamanho que a imagem
        self.mask = pyg.mask.from_surface(self.image)# Cria a mask para a pista
        self.rect = self.image.get_rect() #cria um rectangulo no formato da pista para ser considerado uma Surface
