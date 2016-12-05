import pygame
import random
import Colores
import FuncionesTerreno
import Jugador
import Enemigo
import Bala_enemigo
import Princesa
import Bloques
import Huecos
import Bala_Defen
import Vidas
import vidas_Juego
import Fuego
import Gravedad
import muerte_Dragon
import ConfigParser #

ContadorMap=0
ANCHO=1344
ALTO=704
Nro_VIDAS=5
listaBlo=[]

if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(Colores.eColor("TURQUESA"))
    interprete=ConfigParser.ConfigParser()
    interprete.read('nivel.map')
    ar_origen=interprete.get("nivel","origen") #Tomar de nivel, el origen
    mapa=interprete.get("nivel","mapa").split("\n") #Lee todo el mapa hasta encontrar un salto de linea
    al=int (interprete.get("nivel","corte_alto")) #Extraer el alto de nivel
    an=int (interprete.get("nivel","corte_ancho")) #Extraer el ancho de nivel
    fondo=FuncionesTerreno.Recortar(ar_origen,an,al)
    todos=pygame.sprite.Group()
    #jugador
    #Fondodel nivel
    fondoPriN=pygame.image.load('Fondonivel1.jpg')
    dim_fondoPriN=fondoPriN.get_rect()
    ventana=fondoPriN.subsurface(0,0, ANCHO, ALTO)
    var_f=0
    pos_f=0
    animal=FuncionesTerreno.Recortar('feca.png',60,64)
    feca=Jugador.Jugador(animal[0][0])
    #Princesa
    Princesa1=FuncionesTerreno.Recortar('Princesa.png',64,64)
    Pocahontas=Princesa.Princesa(Princesa1[0][2])
    #Dragon
    Dragon1=FuncionesTerreno.Recortar('Dragon1.png',80,80)
    Dragon=Enemigo.Enemigo(Dragon1[0][0])

    Me_Dragon=FuncionesTerreno.Recortar('Muerte_Dragon.png',50,50)
    muerte_Dragon1=muerte_Dragon.Muerte(Me_Dragon[0][0])

    muerte_Dragons=pygame.sprite.Group()
    muerte_Dragons.add(muerte_Dragon1)
    Tirar_Fuego=pygame.sprite.Group()
    Estrella=pygame.sprite.Group()
    Jugadores=pygame.sprite.Group()
    Jugadores.add(feca)
    Vidas_feca=FuncionesTerreno.Recortar('vidas.png',50,50)
    Feca_vidas=Vidas.Vida(Vidas_feca[0][0])

    Vida_j=FuncionesTerreno.Recortar('Vidas_juego.png',50,35)
    Aum_vida=vidas_Juego.Vid_juego(Vida_j[0][0])


    gru_Vidas_juego=pygame.sprite.Group
    Gro_Vidas=pygame.sprite.Group()
    Gro_Vidas.add(Aum_vida)
    todos.add(muerte_Dragon1)
    todos.add(Aum_vida)
    todos.add(Feca_vidas)
    todos.add(feca)
    #todos.add(Pocahontas)
    todos.add(Dragon)
    Bloqueadores=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    princes=pygame.sprite.Group()
    Caidas=pygame.sprite.Group()
    feca.Bloqueadores=Bloqueadores
    #princes.add(Pocahontas)
#Fuentes
    fuente=pygame.font.SysFont("comicsansms",66) #Fuente para hacer el letrero(tipo de letra, tamano).
    fuente2=pygame.font.SysFont("comicsansms",36)
    fuente3=pygame.font.SysFont("comicsansms",26)
    pygame.display.flip()

    reloj=pygame.time.Clock()
    #Introduccion al Juego
    pag=0 #Pantallazos
    terminar=False
    parar=False

    while not terminar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag+=1

        if pag == 0:
            pantalla.fill(Colores.eColor("BLANCO"))
            imagen=pygame.image.load('dofus.png')
            pantalla.blit(imagen, [50,50])
            texto=fuente.render("BIENVENIDO AL MUNDO DE LOS DOCE...", True, Colores.eColor("VERDEBICHE")) #Lo que hay en el letrero.
            pantalla.blit(texto,[200,10]) #Posicion del letrero
            pygame.display.flip()

        if pag == 1:
            pantalla.fill(Colores.eColor("BLANCO"))
            texto=fuente2.render("En una tierra muy lejana existia un gran guerrero de clase feca, Su nombre era .. LEYENDA ..", True, Colores.eColor("NEGRO")) #Lo que hay en el letrero.
            pantalla.blit(texto,[10,10]) #Posicion del letrero
            imagen=pygame.image.load('MunecoFeca2.png')
            pantalla.blit(imagen, [20, 20])
            pygame.display.flip()

        if pag == 2:
            pantalla.fill(Colores.eColor("BLANCO"))
            texto=fuente2.render("En una tierra muy lejana existia un gran guerrero de clase feca, Su nombre era .. LEYENDA ..", True, Colores.eColor("NEGRO")) #Lo que hay en el letrero.
            pantalla.blit(texto,[10,10]) #Posicion del letrero
            imagen=pygame.image.load('MunecoFeca2.png')
            pantalla.blit(imagen, [20, 20])
            texto=fuente2.render("El cual tenia un amigo fiel llamado .. DRAGOPAVO ..", True, Colores.eColor("NEGRO")) #Lo que hay en el letrero.
            pantalla.blit(texto,[500,100]) #Posicion del letrero
            imagen=pygame.image.load('Dragopavo.png')
            pantalla.blit(imagen, [600, 300])
            pygame.display.flip()

        if pag == 3:
            pantalla.fill(Colores.eColor("BLANCO"))
            texto=fuente2.render("En una tierra muy lejana existia un gran guerrero de clase feca, Su nombre era .. LEYENDA ..", True, Colores.eColor("NEGRO")) #Lo que hay en el letrero.
            pantalla.blit(texto,[10,10]) #Posicion del letrero
            imagen=pygame.image.load('MunecoFeca2.png')
            pantalla.blit(imagen, [20, 20])
            texto=fuente2.render("El cual tenia un amigo fiel llamado .. DRAGOPAVO ..", True, Colores.eColor("NEGRO")) #Lo que hay en el letrero.
            pantalla.blit(texto,[500,100]) #Posicion del letrero
            imagen=pygame.image.load('Dragopavo.png')
            pantalla.blit(imagen, [600, 300])
            texto=fuente3.render("los dos juntos salvaran a su princesa que fue..", True, Colores.eColor("NEGRO")) #Lo que hay en el letrero.
            pantalla.blit(texto,[800,400]) #Posicion del letrero
            texto2=fuente3.render("raptada por seres malditos..", True, Colores.eColor("NEGRO")) #Lo que hay en el letrero.
            pantalla.blit(texto2,[850,420]) #Posicion del letrero
            imagen=pygame.image.load('fantasmas.png')
            pantalla.blit(imagen, [800, 400])
            pygame.display.flip()

        if pag == 4:
            pantalla.fill(Colores.eColor("BLANCO"))
            imagen=pygame.image.load('instrucciones.png')
            #fondo=pygame.image.load('Fondonivel1.png')
            pantalla.blit(imagen, [0, 0])
            pygame.display.flip()
        if pag == 5:
            terminar=True

    vary=0
    for fila in mapa:
        varx=0
        for div in fila:
            px=int (interprete.get(div,"x"))
            py=int (interprete.get(div,"y"))
            if(div == "#"):#lo cambie para hacer la prueba ojo
                Bloquea=FuncionesTerreno.Recortar('terrenogen.png',54,180)
                Bloquear=Bloques.Bloque(Bloquea[0][0])
                Bloquear.rect.x = varx
                Bloquear.rect.y = vary
                #if feca.rect.x>=100:
                Bloquear.var_x=-0.1
                #if feca.rect.x<100:
                #Bloquear.var_x=0.1
                Bloqueadores.add(Bloquear)
                todos.add(Bloquear)
            if(div == "H"):
                Hueco=FuncionesTerreno.Recortar('terrenogen.png',32,32)
                Caer=Huecos.Hueco(Hueco[19][11])
                Caer.rect.x = varx
                Caer.rect.y = vary
                Caidas.add(Caer)
                todos.add(Caer)
            pantalla.blit(fondo[px][py], (varx,vary))
            varx+=an
        vary+=al



    pos_X = 0
# aumentar vidas en el juego
    for i in range(15):
        Vida_j=FuncionesTerreno.Recortar('Vidas_juego.png',50,35)
        Aum_vida=vidas_Juego.Vid_juego(Vida_j[0][0])
        pos_X = random.randrange(5,15000)
        Aum_vida.rect.x=pos_X
        Aum_vida.var_x=-1.5
        Aum_vida.rect.y=random.randrange(540,640)

        Gro_Vidas.add(Aum_vida)
        todos.add(Aum_vida)

    #numero de fantasmas
    for i in range(0):
        fantasmasVarios1=FuncionesTerreno.Recortar('Fantasmas1.png',64,64)
        fantasmasVarios=Enemigo.Enemigo(fantasmasVarios1[0][1])
        pos_X = random.randrange(5,1100)
        if(pos_X % 2 == 0):
            fantasmasVarios.rect.x= pos_X
            fantasmasVarios.rect.y=random.randrange(59,600)
        else:
            fantasmasVarios.rect.x= pos_X + 1
            fantasmasVarios.rect.y=random.randrange(59,600)
        fantasmasVarios.var_x=-2
        #fantasmasVarios.var_y=1
        enemigos.add(fantasmasVarios)
        todos.add(fantasmasVarios)

    if(parar== False):
        MovimientoDragon= Dragon.rect.x
        parar=True

    fin= False
    colorear= 1
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    feca.var_x=-5
                    #feca.var_y=0
                    #feca.dir=1
                    #Pocahontas.dir=1
                if event.key == pygame.K_d:
                    #if feca.var_x == 0:
                    feca.var_x=5
                    #feca.var_y=0
                    #feca.dir=2
                    #Pocahontas.dir=3
                if event.key == pygame.K_w:
                    if feca.rect.y==640:
                    #if feca.rect.x == 0:
                        feca.rect.y += -10
                        feca.var_y=-16
                    #feca.dir=3
                    #Pocahontas.dir=2
                if event.key == pygame.K_s:
                    #feca.var_y=3
                    #feca.var_x=0
                    feca.dir=0
                    #Pocahontas.dir=3
                if event.key == pygame.K_SPACE:
                    feca.var_x=0
                    feca.var_y=0
                    Pocahontas.dir=2
                if event.key == pygame.K_p:
                    ContadorMap+=2
                    if feca.dir == 0:
                        b=Bala_Defen.Bala('Estrellaninja2.png')
                        b.rect.x=feca.rect.x
                        b.rect.y=feca.rect.y
                        b.var_x=0
                        b.var_y=10
                        Estrella.add(b)
                        todos.add(b)
                        #ContadorMap+=32
                    if feca.dir == 1:
                        b=Bala_Defen.Bala('Estrellaninja2.png')
                        b.rect.x=feca.rect.x
                        b.rect.y=feca.rect.y
                        b.var_x=-10
                        b.var_y=0
                        Estrella.add(b)
                        todos.add(b)
                    if feca.dir == 2:
                        b=Bala_Defen.Bala('Estrellaninja2.png')
                        b.rect.x=feca.rect.x
                        b.rect.y=feca.rect.y
                        b.var_x=10
                        b.var_y=0
                        Estrella.add(b)
                        todos.add(b)
                    if feca.dir == 3:
                        b=Bala_Defen.Bala('Estrellaninja2.png')
                        b.rect.x=feca.rect.x
                        b.rect.y=feca.rect.y
                        b.var_x=0
                        b.var_y=-10
                        Estrella.add(b)
                        todos.add(b)

        #lOGICA JUEGO            (VUELTA DE FANTASMAS)
        for J in Jugadores:
            ls_choque=pygame.sprite.spritecollide(J,Gro_Vidas,False)
            for V in ls_choque:
                Nro_VIDAS+=1
                todos.remove(V)
                Gro_Vidas.remove(V)


        for J in Jugadores:
            ls_choque=pygame.sprite.spritecollide(J,enemigos,False)
            for E in ls_choque:
                Nro_VIDAS-=1
                todos.remove(E)
                enemigos.remove(E)

        for Elimino in Bloqueadores:
            if Elimino.rect.x==0:
                todos.remove(Elimino)
                Bloqueadores.remove(Elimino)



        for JUG in Jugadores:
            ls_choque=pygame.sprite.spritecollide(JUG,Bloqueadores,False)
            for b in ls_choque:
                if JUG.var_x>0:
                    JUG.var_x=0
                    JUG.var_x=2
                    #JUG.var_y=0
                    JUG.rect.left=b.rect.right
                if JUG.var_x<0:
                    JUG.rect.left=b.rect.right
                    JUG.var_x=0
                    JUG.var_x=-2
                if JUG.var_y>0:
                    JUG.rect.bottom=b.rect.top
                    JUG.var_y=0
                if JUG.var_y<0:
                    #JUG.con=0
                    JUG.rect.top=b.rect.bottom
                    JUG.var_y=0


        if colorear == 1:
            #estrellas nijas
            for bl in Estrella:
                ls_impac=pygame.sprite.spritecollide(bl,Bloqueadores,False)
                for mu in ls_impac:
                    Estrella.remove(bl)
                    todos.remove(bl)
            for bl in Estrella:
                ls_impac=pygame.sprite.spritecollide(bl,enemigos,False)
                for im in ls_impac:
                    Estrella.remove(bl)
                    todos.remove(bl)
                    im.vida-=1
                    if im.vida==0:
                        enemigos.remove(im)
                        todos.remove(im)

            for Ene in enemigos:
                if ( 2 == Ene.rect.x):
                    Ene.var_x=2
                    Ene.dir=2
                    Ene.image=fantasmasVarios1[Ene.con][Ene.dir]
                if (1000 == Ene.rect.x ):
                    Ene.var_x=-2
                    Ene.dir=1
                    Ene.image=fantasmasVarios1[Ene.con][Ene.dir]


            image=pygame.image.load("gameover.jpg")
            for caer in Caidas:
                ls_impac=pygame.sprite.spritecollide(caer,Jugadores,False)
                for ju in ls_impac:
                    colorear=0

            image2=pygame.image.load("win.png")
            for prin in princes:
                ls_impac=pygame.sprite.spritecollide(prin,Jugadores,False)
                for ju in ls_impac:
                    colorear=3


                    #screen.blit(image,(0,0))
                    #fin=True
    #MovimientoDragon

#           if ( MovimientoDragon-250 == Dragon.rect.x):
#                Fuego_Drago=FuncionesTerreno.Recortar('Fuego_Dragon.png',50,29)
#                Dragon_Fuego=Fuego.Fuego_Dragons(Fuego_Drago[0][0])
#                Dragon_Fuego.rect.x=Dragon.rect.x
#                Dragon.var_x=2
#                Dragon.dir=0
#                Dragon.image=Dragon1[0+Dragon.con][Dragon.dir]
#                Tirar_Fuego.add(Dragon_Fuego)
#                todos.add(Dragon_Fuego)
#            if (MovimientoDragon == Dragon.rect.x ):
#                Fuego_Drago=FuncionesTerreno.Recortar('Fuego_Dragon.png',50,29)
#                Dragon_Fuego=Fuego.Fuego_Dragons(Fuego_Drago[0][0])
#                Dragon_Fuego.rect.x=Dragon.rect.x
#                Tirar_Fuego.add(Dragon_Fuego)
#                todos.add(Dragon_Fuego)
#                Dragon.image=Dragon1[0+Dragon.con][Dragon.dir]
#                Dragon.var_x=-2
#                Dragon.dir=1
#            if (MovimientoDragon-100 == Dragon.rect.x ):
#                Fuego_Drago=FuncionesTerreno.Recortar('Fuego_Dragon.png',50,29)
#                Dragon_Fuego=Fuego.Fuego_Dragons(Fuego_Drago[0][0])
#                Dragon_Fuego.rect.x=Dragon.rect.x
#                Dragon.image=Dragon1[0+Dragon.con][Dragon.dir]
#                Tirar_Fuego.add(Dragon_Fuego)
#                todos.add(Dragon_Fuego)
#                Dragon.var_x=-2
#                Dragon.dir=2

            for J in Jugadores:
                ls_choque=pygame.sprite.spritecollide(J,Tirar_Fuego,False)
                for T in ls_choque:
                    Nro_VIDAS-=1
                    todos.remove(T)
                    Tirar_Fuego.remove(T)

            for J in Jugadores:
                ls_choque=pygame.sprite.spritecollide(J,muerte_Dragons,False)
                for T in ls_choque:
                    Dragon.image=Dragon1[0+Dragon.con][3]
                    Dragon.var_x=0
                    Dragon.var_y=-10


            if Nro_VIDAS == 5:
                Feca_vidas.image=Vidas_feca[0+Feca_vidas.con][0]
            if Nro_VIDAS == 4:
                Feca_vidas.image=Vidas_feca[0+Feca_vidas.con][1]
            if Nro_VIDAS == 3:
                Feca_vidas.image=Vidas_feca[0+Feca_vidas.con][2]
            if Nro_VIDAS == 2:
                Feca_vidas.image=Vidas_feca[0+Feca_vidas.con][3]
            if Nro_VIDAS == 1:
                Feca_vidas.image=Vidas_feca[0+Feca_vidas.con][4]
                colorear=0


            #Pocahontas.image=Princesa1[0+Pocahontas.con][Pocahontas.dir]
            #feca.image=animal[feca.con][feca.dir]  Para cambiar cuando este cambiando la imgane de pucca


            #ContadorMap+=1
            #carga o refresco

#            varia=0
#            if varia == 0:
#                vary=0
#                varia+=1
#
#            for fila in mapa:
#                varx=0
#                for div in fila:
#                    px=int (interprete.get(div,"x"))
#                    py=int (interprete.get(div,"y"))
#                    pantalla.blit(fondo[px][py], (varx,vary))
#                    varx+=an
#                vary+=al






            if feca.rect.right >=100:
                ContadorMap+=5
                pos_f+=5
            if feca.rect.left <100:
                ContadorMap-=5
                pos_f-=5
            if pos_f>=0 and pos_f < (dim_fondoPriN.width - ANCHO):
                ventana=fondoPriN.subsurface(pos_f,0, ANCHO, ALTO)
                #print pos_x
            pantalla.blit(ventana, (0,0))


            print Nro_VIDAS

            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(15)
        if colorear == 0:
            pantalla.blit(image,(0,0))
            pygame.display.flip()
            reloj.tick(15)
        if colorear == 3:
            pantalla.fill(Colores.eColor("BLANCO"))
            pantalla.blit(image2,(0,0))
            pygame.display.flip()
            reloj.tick(15)
