# coding=utf-8
import pygame
import Componentes
from Componentes import Boton
from Componentes import Robots
pygame.init()
q0 = pygame.mixer.Sound("Musica/q1.ogg")
q1 = pygame.mixer.Sound("Musica/q2.ogg")
q2 = pygame.mixer.Sound("Musica/q3.ogg")
q3 = pygame.mixer.Sound("Musica/q4.ogg")
q4 = pygame.mixer.Sound("Musica/q5.ogg")
q5 = pygame.mixer.Sound("Musica/q6.ogg")
q6 = pygame.mixer.Sound("Musica/q7.ogg")
q7 = pygame.mixer.Sound("Musica/q8.ogg")
q8 = pygame.mixer.Sound("Musica/q9.ogg")
q9 = pygame.mixer.Sound("Musica/q10.ogg")
#Cargamos imagenes
bRojo = pygame.image.load("Img/botonRojo.png")
bVerde = pygame.image.load("Img/botonVerde.png")
bAmarillo = pygame.image.load("Img/botonAmarillo.png")
robot1 = pygame.image.load("Img/robot1.png")
robot2 = pygame.image.load("Img/robot2.png")
robot3 = pygame.image.load("Img/robot3.png")
robot4 = pygame.image.load("Img/robot4.png")

bInicio = pygame.image.load("Img/Inicio.png")
palanca1 = pygame.image.load("Img/palanca1.png")
palanca2 = pygame.image.load("Img/palanca2.png")
finish = pygame.image.load("Img/finish.png")

#Creacion de botones
botonR = Boton(bRojo,300,280)
botonV = Boton(bVerde,300,480)
botonA = Boton(bAmarillo,300,680)
botonI = Boton(bInicio,735,450)
palanca1 = Boton(palanca1,1400,470)
palanca2 = Boton(palanca2,200,450)
bfinish = Boton(finish,500,85)
botonF = Boton(bInicio,735,600)

#Sonidos
listaSP = [q0,q1,q2,q3,q4,q5,q6,q7,q8,q9]

def inicio(pantalla):
    botonI.update(pantalla,400,150)
    palanca1.update(pantalla,300,500)
    palanca2.update(pantalla,300,500)
    pantalla.blit(Componentes.fuente(100).render("Trivia De Robots",True,(0,0,0)),(520,100))
    pantalla.blit(Componentes.fuente(40).render("Empezar",True,(0,0,0)),(850,460))

def fin(pantalla,n,a):
    bfinish.update(pantalla,800,900)
    botonF.update(pantalla,300,150)
    pantalla.blit(Componentes.fuente(25).render("Volver a empezar",True,(0,0,0)),(777,615))
    pantalla.blit(Componentes.fuente(36).render("Obtuviste " + str(n) + " de " + str(a) + " aciertos",True,(0,0,0)),(675,460))

def trivia(numQA,pantalla,t,s):
    if t == True:
        listaSP[s].play(0,0,0)
    #Colocamos donde se mostrara el texto de la pregunta.
    pantalla.blit(Componentes.texto(numQA,"question"),(280,100))
    #Colocamos el texto de las posibles respuestas
    pantalla.blit(Componentes.texto(numQA,"ans1"),(475,300))
    pantalla.blit(Componentes.texto(numQA,"ans2"),(475,500))
    pantalla.blit(Componentes.texto(numQA,"ans3"),(475,700))
    #Botones
    botonR.update(pantalla,130,130)
    botonV.update(pantalla,130,130)
    botonA.update(pantalla,130,130)
