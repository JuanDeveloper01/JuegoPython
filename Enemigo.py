import pygame
import random

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=archivo
        self.rect=self.image.get_rect()
        self.rect.x=1200
        self.rect.y=600
        self.var_x=-2
        self.var_y=0
        self.disparar=False
        self.vida=2
        self.con=0
        self.dir=1
        self.tiempo=random.randrange(100)

    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        self.tiempo-=1
        if self.tiempo==0:
            self.disparar=True
            self.tiempo=random.randrange(20)
