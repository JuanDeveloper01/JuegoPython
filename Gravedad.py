import pygame

def gravedad(self):
    if self.var_y ==0:
        self.var_y =1
    else:
        self.var_y+=0.35

    if self.rect.y >= (ALTO)-self.rect.height:
        self.rect.bottom = (ALTO)
        self.var_y=0

def update(self):
    self.gravedad()
    self.rect.x+=self.var_x
    if self.rect.right > ANCHO-100:
        self.rect.right=ANCHO-100
        self.var_x=0

    self.rect.y+=self.var_y
    if self.rect.left < 100:
        self.rect.left=100
        self.var_x=0
