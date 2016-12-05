import pygame
import Jugador
import Principaljuego

class Bloque(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=archivo
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0

    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
