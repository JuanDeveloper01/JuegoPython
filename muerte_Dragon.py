import pygame

class Muerte(pygame.sprite.Sprite):
    def __init__(self, img_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image=img_sprite
        self.rect=self.image.get_rect()
        self.rect.x=920
        self.rect.y=470
        self.con=0
        self.dir=0
