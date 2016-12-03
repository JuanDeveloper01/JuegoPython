import pygame
import random

class Fuego_Dragons(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=archivo
        self.rect=self.image.get_rect()
        self.rect.x=900
        self.rect.y=600
        self.var_x=-10
        self.var_y=10

    def update(self):
        self.rect.x+=self.var_x
