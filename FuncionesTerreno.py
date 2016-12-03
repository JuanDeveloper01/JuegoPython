import random
import pygame

def Recortar(archivo, anc, alc): #anc:ancho de corte, alc:alto de corte
    matriz=[]
    imagen=pygame.image.load(archivo).convert_alpha()
    i_ancho, i_alto=imagen.get_size()
    for x in range(0, i_ancho/anc):
        linea=[]
        for y in range(0, i_alto/alc):
            cuadro=(x*anc, y*alc, anc, alc) #Recortar la imagen
            linea.append(imagen.subsurface(cuadro))
        matriz.append(linea)
    return matriz
