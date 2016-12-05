import pygame
import random

class Vid_juego(pygame.sprite.Sprite):
    def __init__(self, img_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image=img_sprite
        self.rect=self.image.get_rect()
        self.rect.x=800
        self.rect.y=600
        self.var_x=0
        self.var_y=0
                
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
