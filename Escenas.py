# coding=utf-8
import pygame
import Componentes
from Componentes import Boton

#Cargamos imagenes
bRojo = pygame.image.load("botonRojo.png")
bVerde = pygame.image.load("botonVerde.png")
bAmarillo = pygame.image.load("botonAmarillo.png")
robot1 = pygame.image.load("robot1.png")
robot2 = pygame.image.load("robot2.png")
robot3 = pygame.image.load("robot3.png")
robot4 = pygame.image.load("robot4.png")
bInicio = pygame.image.load("Inicio.png")
palanca1 = pygame.image.load("palanca1.png")
palanca2 = pygame.image.load("palanca2.png")
finish = pygame.image.load("finish.png")

#Creacion de botones
botonR = Boton(bRojo,300,280)
botonV = Boton(bVerde,300,480)
botonA = Boton(bAmarillo,300,680)
botonI = Boton(bInicio,735,450)
palanca1 = Boton(palanca1,1400,470)
palanca2 = Boton(palanca2,200,450)
bfinish = Boton(finish,500,85)
botonF = Boton(bInicio,735,600)

def inicio(pantalla):
    pantalla.blit(robot1,(50,30))
    pantalla.blit(robot2,(1400,30))
    pantalla.blit(robot3,(550,590))
    pantalla.blit(robot4,(1000,585))
    botonI.update(pantalla,400,150)
    palanca1.update(pantalla,300,500)
    palanca2.update(pantalla,300,500)
    pantalla.blit(Componentes.fuente(100).render("Trivia De Robots",True,(0,0,0)),(520,100))
    pantalla.blit(Componentes.fuente(40).render("Empezar",True,(0,0,0)),(850,460))


def fin(pantalla,n,a):
    bfinish.update(pantalla,800,900)
    pantalla.blit(robot1,(50,30))
    pantalla.blit(robot2,(1400,30))
    pantalla.blit(robot3,(450,590))
    pantalla.blit(robot4,(1050,585))
    botonF.update(pantalla,300,150)
    pantalla.blit(Componentes.fuente(25).render("Volver a empezar",True,(0,0,0)),(777,615))
    pantalla.blit(Componentes.fuente(36).render("Obtuviste " + str(n) + " de " + str(a) + " aciertos",True,(0,0,0)),(675,460))

def trivia(numQA,pantalla):
    #Colocamos donde se mostrara el texto de la pregunta.
    pantalla.blit(Componentes.texto(numQA,"question"),(280,100))
    #Colocamos el texto de las posibles respuestas
    pantalla.blit(Componentes.texto(numQA,"ans1"),(475,300))
    pantalla.blit(Componentes.texto(numQA,"ans3"),(475,500))
    pantalla.blit(Componentes.texto(numQA,"ans2"),(475,700))
    #Botones
    botonR.update(pantalla,130,130)
    botonV.update(pantalla,130,130)
    botonA.update(pantalla,130,130)
