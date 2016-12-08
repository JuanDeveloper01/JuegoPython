import pygame
import random

class Rayo_Ene(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=archivo
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.var_x=-10
        self.var_y=10

    def update(self):
        self.rect.x+=self.var_x
