# coding=utf-8
import Componentes
from Componentes import Boton
import pygame
import SystemTrivia
def main():
    #Inicializamos modulos de python
    pygame.init()
    #Tamaño de la pantalla
    pantalla= pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    #Dimensiones de la pantalla
    x,y = pantalla.get_size()
    #Nombre que se refleja en la ventana
    pygame.display.set_caption("Trivia")
    #Fotogramaas por segundo a los que se ejecuta los update
    reloj = pygame.time.Clock()
    #Cargando imagenes
    bRojo = pygame.image.load("botonRojo.png")
    bVerde = pygame.image.load("botonVerde.png")
    bAmarillo = pygame.image.load("botonAmarillo.png")
    finish = pygame.image.load("finish.png")
    fondo = pygame.image.load("fondo6.png")
    blanco=(112,150,163)

    botonR = Boton(bRojo,300,750)
    botonV = Boton(bVerde,800,750)
    botonA = Boton(bAmarillo,1300,750)
    #Superficie invisible para pueba de la respuesta
    t_f = pygame.Surface([0,0])
    gameOver = False
    num = 0
    numQA = 0
    #LoopPrincipal
    while gameOver !=True:

        pantalla.fill(blanco)
        reloj.tick(30)
        Componentes.dibujar_panel(fondo,pantalla,x,y)
        if (num >= len(Componentes.quiz_ans)):
            pantalla.blit(finish,(700,243))
        elif (num < len(Componentes.quiz_ans)):
            numQA = num
            #Colocamos donde se mostrara el texto de la pregunta.
            pantalla.blit(Componentes.texto(numQA,"question"),(280,100))
            #Colocamos el texto de las posibles respuestas
            pantalla.blit(Componentes.texto(numQA,"ans1"),(350,250))
            pantalla.blit(Componentes.texto(numQA,"ans2"),(350,400))
            pantalla.blit(Componentes.texto(numQA,"ans3"),(350,550))
            #Botones
            botonR.update(pantalla)
            botonV.update(pantalla)
            botonA.update(pantalla)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameOver = True
                if event.key == pygame.K_q:
                    t_f = Componentes.textop(Componentes.respuestaT("q"))
                    pantalla.blit(t_f,(1000,250))
                    pygame.time.delay(400)
                    t_f = pygame.Surface([0,0])
                    num +=1
                if event.key == pygame.K_w:
                    t_f = Componentes.textop(Componentes.respuestaT("w"))
                    pantalla.blit(t_f,(1000,250))
                    pygame.time.delay(400)
                    t_f = pygame.Surface([0,0])
                    num +=1

                if event.key == pygame.K_e:
                    t_f = Componentes.textop(Componentes.respuestaT("e"))
                    pantalla.blit(t_f,(1000,250))
                    pygame.time.delay(400)
                    t_f = pygame.Surface([0,0])
                    num +=1


        #Actualizamos la pantalla
        pygame.display.update()
    pygame.quit()

main()
