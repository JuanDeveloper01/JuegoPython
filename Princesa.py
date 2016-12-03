import pygame

class Princesa(pygame.sprite.Sprite):
    def __init__(self, img_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image=img_sprite
        self.rect=self.image.get_rect()
        self.rect.x=1300
        self.rect.y=600
        self.var_x=0
        self.var_y=0
        self.con=0
        self.dir=2
        self.DetecionHueco=False


    def update(self):
        if self.DetecionHueco==False:
            self.rect.x+=self.var_x
            self.rect.y+=self.var_y
            if self.con<2:
                self.con+=1
            else:
                self.con=0
        else:
            self.var_x=0
            self.var_y=0
