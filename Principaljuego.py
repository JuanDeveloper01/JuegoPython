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
NumEstrellas=10
Presen=0

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
    fondoPriN=pygame.image.load('Fondonivel1.jpg')
    dim_fondoPriN=fondoPriN.get_rect()
    ventana=fondoPriN.subsurface(0,0, ANCHO, ALTO)
    var_f=0
    pos_f=0
    animal=FuncionesTerreno.Recortar('pucca.png',62,66)
    pucca=Jugador.Jugador(animal[0][0])
    Rayos=pygame.sprite.Group()
    Estrella=pygame.sprite.Group()
    Jugadores=pygame.sprite.Group()
    Jugadores.add(pucca)
    Vidas_pucca=FuncionesTerreno.Recortar('vidas.png',100,110)
    pucca_vidas=Vidas.Vida(Vidas_pucca[0][0])

    gru_Vidas_juego=pygame.sprite.Group
    Gro_Vidas=pygame.sprite.Group()
    todos.add(pucca_vidas)
    todos.add(pucca)
    Bloqueadores=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    princes=pygame.sprite.Group()
    Caidas=pygame.sprite.Group()
    pucca.Bloqueadores=Bloqueadores
    fuente=pygame.font.SysFont("comicsansms",66) #Fuente para hacer el letrero(tipo de letra, tamano).
    fuente2=pygame.font.SysFont("comicsansms",36)
    fuente3=pygame.font.SysFont("comicsansms",26)
    pygame.display.flip()

    reloj=pygame.time.Clock()
    #Introduccion al Juego
    pag=0 #Pantallazos
    terminar=False
    parar=False
    Inicio=pygame.mixer.Sound("CancioInicio.ogg")



    while not terminar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag+=1

        if pag == 0:
            if Presen ==0:
                    Inicio.play(loops=0)
                    Presen=1
            pantalla.fill(Colores.eColor("BLANCO"))
            imagen=pygame.image.load('Primero.jpg')
            pantalla.blit(imagen, [150,50])
            texto=fuente.render("TODOS LOS DERECHOS RESERVADOS...", True, Colores.eColor("ROJO")) #Lo que hay en el letrero.
            pantalla.blit(texto,[200,10]) #Posicion del letrero
            pygame.display.flip()

        if pag == 1:
            pantalla.fill(Colores.eColor("BLANCO"))
            imagen=pygame.image.load('segundo.png')
            pantalla.blit(imagen, [0, 0])
            pygame.display.flip()

        if pag == 2:
            pantalla.fill(Colores.eColor("BLANCO"))
            imagen=pygame.image.load('tercero.png')
            pantalla.blit(imagen, [0, 0])
            pygame.display.flip()

        if pag == 3:
            pantalla.fill(Colores.eColor("BLANCO"))
            texto=fuente2.render("En una tierra muy lejana existia un gran guerrero de clase pucca, Su nombre era .. LEYENDA ..", True, Colores.eColor("NEGRO")) #Lo que hay en el letrero.
            pantalla.blit(texto,[10,10]) #Posicion del letrero
            imagen=pygame.image.load('Munecopucca2.png')
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
            Inicio.stop()
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
                Bloquear.var_x=-1.5
                Bloqueadores.add(Bloquear)
                todos.add(Bloquear)
            if(div == "H"):
                Hueco=FuncionesTerreno.Recortar('terrenogen.png',60,32)
                Caer=Huecos.Hueco(Hueco[1][0])
                Caer.rect.x = varx
                Caer.rect.y = vary
                Caer.var_x=-1.5
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
        pos_X = random.randrange(5,10000)
        Aum_vida.rect.x=pos_X
        Aum_vida.var_x=-1.5
        Aum_vida.rect.y=random.randrange(540,640)

        Gro_Vidas.add(Aum_vida)
        todos.add(Aum_vida)
    pos_X=400
    #numero de fantasmas
    for i in range(15):
        NinjaVarios1=FuncionesTerreno.Recortar('Ninja.png',120,120)
        NinjaVarios=Enemigo.Enemigo(NinjaVarios1[0][0])
        NinjaVarios.rect.x= pos_X
        NinjaVarios.rect.y=550
        NinjaVarios.var_x=-3
        pos_X+=800
        enemigos.add(NinjaVarios)
        todos.add(NinjaVarios)



    fin= False
    colorear= 1
    MusicFon=pygame.mixer.Sound("Fondo.ogg")
    no=0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pucca.con=1
                    pucca.var_x=-3
                if event.key == pygame.K_d:
                    pucca.var_x=3
                    pucca.con=0
                    pucca.dir=1
                if event.key == pygame.K_w:
                    if pucca.rect.y==638:
                        pucca.rect.y +=-10
                        pucca.var_y=-16
                if event.key == pygame.K_s:
                    pucca.dir=0
                if event.key == pygame.K_SPACE:
                    pucca.var_x=0
                    pucca.var_y=0
                if event.key == pygame.K_p:
                    if pucca.var_x<0 and NumEstrellas != 0:
                        EstrellaN=pygame.mixer.Sound("SonidoEstrella.ogg")
                        b=Bala_Defen.Bala('Estrellaninja2.png')
                        EstrellaN.play(loops=2)
                        b.rect.x=pucca.rect.x
                        b.rect.y=pucca.rect.y
                        b.var_x=-10
                        b.var_y=0
                        #NumEstrellas-=1
                        Estrella.add(b)
                        todos.add(b)
                    if pucca.var_x>=0 and NumEstrellas != 0:
                        EstrellaN=pygame.mixer.Sound("SonidoEstrella.ogg")
                        b=Bala_Defen.Bala('Estrellaninja2.png')
                        EstrellaN.play(loops=2)
                        b.rect.x=pucca.rect.x
                        b.rect.y=pucca.rect.y
                        b.var_x=10
                        b.var_y=0
                        #NumEstrellas-=1
                        Estrella.add(b)
                        todos.add(b)
                #if event.key == pygame.K_l:
                #    pygame.time.wait()
                #if event.key == pygame.K_k:
                #    pygame.time.delay()




        if no== 0:
            MusicFon.play(loops=50)
            no=1

        #lOGICA JUEGO            (VUELTA DE FANTASMAS)

        for J in Jugadores:
            ls_choque=pygame.sprite.spritecollide(J,Gro_Vidas,False)
            for V in ls_choque:
                if Nro_VIDAS<5:
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
                todos.remove(b)
                Bloqueadores.remove(b)
                Nro_VIDAS-=1


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
                if (  0 == Ene.rect.x ):
                    enemigos.remove(Ene)
                    todos.remove(Ene)
                if Ene.dir==14 and Ene.rect.x<=1144 and Ene.rect.x>=1104:
                    Rayol=FuncionesTerreno.Recortar('rayo.png',60,60)
                    Rayo=Fuego.Rayo_Ene(Rayol[0][0])
                    Rayo.rect.x=Ene.rect.x
                    Rayo.rect.y=Ene.rect.y+90
                    Rayos.add(Rayo)
                    todos.add(Rayo)

            for J in Jugadores:
                ls_choque=pygame.sprite.spritecollide(J,Rayos,False)
                for E in ls_choque:
                    Nro_VIDAS-=1
                    todos.remove(E)
                    Rayos.remove(E)

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




            if Nro_VIDAS == 5:
                pucca_vidas.image=Vidas_pucca[0+pucca_vidas.con][0]
            if Nro_VIDAS == 4:
                pucca_vidas.image=Vidas_pucca[0+pucca_vidas.con][1]
            if Nro_VIDAS == 3:
                pucca_vidas.image=Vidas_pucca[0+pucca_vidas.con][2]
            if Nro_VIDAS == 2:
                pucca_vidas.image=Vidas_pucca[0+pucca_vidas.con][3]
            if Nro_VIDAS == 1:
                pucca_vidas.image=Vidas_pucca[0+pucca_vidas.con][4]
                colorear=0

            pucca.image=animal[pucca.dir][pucca.con]
            for Ninja in enemigos:
                Ninja.image=NinjaVarios1[NinjaVarios.dir][NinjaVarios.con]




            if pucca.rect.right >=100:
                pos_f+=6
            if pucca.rect.left <100:
                pos_f-=6
            if pos_f>=0 and pos_f < (dim_fondoPriN.width - ANCHO):
                #enemigos=pygame.sprite.Group()
                #Caidas=pygame.sprite.Group()                                
                ventana=fondoPriN.subsurface(pos_f,0, ANCHO, ALTO)
            pantalla.blit(ventana, (0,0))


            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(15)
        if colorear == 0:
            pantalla.blit(image,(0,0))
            MusicFon.stop()
            pygame.display.flip()
            reloj.tick(15)
        if colorear == 3:
            pantalla.fill(Colores.eColor("BLANCO"))
            pantalla.blit(image2,(0,0))
            pygame.display.flip()
            reloj.tick(15)
