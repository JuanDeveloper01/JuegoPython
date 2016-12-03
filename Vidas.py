import pygame

class Vida(pygame.sprite.Sprite):
    def __init__(self, img_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image=img_sprite
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.con=0
        self.dir=0
