import pygame

class Hueco(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image=archivo
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0
