import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, img_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image=img_sprite
        self.rect=self.image.get_rect()
        self.rect.x=40
        self.rect.y=80
        self.var_x=0
        self.var_y=0
        self.con=0
        self.dir=0
        self.DetecionHueco=False
        self.Vida=5


    def gravedad(self):
        if self.var_y ==0:
            self.var_y =0.2
        else:
            self.var_y+=1

        if self.rect.y >= (704)-self.rect.height:
            self.rect.bottom = (704)
            self.var_y=0

    def update(self):
        self.gravedad()
        self.rect.x+=self.var_x
        if self.rect.right > 1344:
            self.rect.right=1344
            self.var_x=0
        if self.rect.left < 0:
            self.rect.left=0
            self.var_x=0
        self.rect.y+=self.var_y
        if self.dir<2:
            self.dir+=1
        else:
            self.dir=0
