# coding=utf-8
import Componentes
from Componentes import Boton
import pygame
import SystemTrivia
import Escenas
from Componentes import Robots
def main():
    #Inicializamos modulos de python
    pygame.init()
    #Tamaño de la pantalla
    pantalla= pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    #Dimensiones de la pantalla
    x,y = pantalla.get_size()
    #1824 984
    print(x,y)
    #Nombre que se refleja en la ventana
    pygame.display.set_caption("Trivia")
    #Fotogramaas por segundo a los que se ejecuta los update
    reloj = pygame.time.Clock()
    #Cargando Sonidos
    pygame.mixer.music.load("Musica/Musica.mp3")
    pygame.mixer.music.play(-1)
    correcto = pygame.mixer.Sound("Musica/Correcto.wav")
    incorrecto = pygame.mixer.Sound("Musica/Incorrecto.wav")
    #Cargando imagenes
    bRojoA = pygame.image.load("Img/botonRojoA.png")
    botonR = Boton(bRojoA,300,280)
    bVerdeA = pygame.image.load("Img/botonVerdeA.png")
    botonV = Boton(bVerdeA,300,480)
    bAmarilloA = pygame.image.load("Img/botonAmarilloA.png")
    botonA = Boton(bAmarilloA,300,680)
    fondo = pygame.image.load("Img/FondoA.png")
    robot1 = pygame.image.load("Img/robot1.png")
    robot1_1= pygame.image.load("Img/robot1.1.png")
    robot1_2= pygame.image.load("Img/robot1.2.png")
    robotA1 = Robots(robot1,robot1_1,robot1_2,50,30)
    robot2 = pygame.image.load("Img/robot2.png")
    robot2_1= pygame.image.load("Img/robot2.1.png")
    robot2_2= pygame.image.load("Img/robot2.2.png")
    robotA2 = Robots(robot2,robot2_1,robot2_2,50,1200)
    robot3 = pygame.image.load("Img/robot3.png")
    robot3_1= pygame.image.load("Img/robot3.1.png")
    robot3_2= pygame.image.load("Img/robot3.2.png")
    robotA3 = Robots(robot3,robot3_1,robot3_2,590,480)
    robot4 = pygame.image.load("Img/robot4.png")
    robot4_1= pygame.image.load("Img/robot4.1.png")
    robot4_2= pygame.image.load("Img/robot4.2.png")
    robotA4 = Robots(robot4,robot4_1,robot4_2,585,850)
    robotT= Robots(robot4,robot4_1,robot4_2,560,1100)
    robot1F = Robots(robot1,robot1_1,robot1_2,30,50)
    robot2F = Robots(robot2,robot2_1,robot2_2,30,1300)
    robot3F = Robots(robot3,robot3_1,robot3_2,590,280)
    robot4F = Robots(robot4,robot4_1,robot4_2,590,1000)
    #Color del bg
    bg=(199,174,180)
    #Superficie invisible para pueba de la respuesta
    t_f = pygame.Surface([0,0])
    gameOver = False
    num = 0
    inicio=-1
    correctas =0
    numQA = len(Componentes.quiz_ans)
    n=0

    #LoopPrincipal
    while gameOver !=True:

        pantalla.fill(bg)
        reloj.tick(60)
        #Componentes.dibujarBG(bg,pantalla,x,y)
        Componentes.dibujar_panel(fondo,pantalla)
        #Reproducir musica infinitamente
        #Escena del menu
        if (inicio == -1):
            robotA2.update(pantalla,n)
            robotA1.update(pantalla,n)
            robotA3.update(pantalla,n)
            robotA4.update(pantalla,n)
            Escenas.inicio(pantalla)
        #Escena finalizada
        if (num >= numQA):
            inicio = -2
            Escenas.fin(pantalla,correctas,numQA)
            robot1F.update(pantalla,n)
            robot2F.update(pantalla,n)
            robot3F.update(pantalla,n)
            robot4F.update(pantalla,n)
        #Escena de la trivia
        if (inicio >= 0 and num < numQA):
            robotT.update(pantalla,n)
            Escenas.trivia(num,pantalla)
        n+=1
        if n > 3:
            n=0
        #Eventos en ocurren a lo largo del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameOver = True
                if (event.key == pygame.K_q and inicio !=-1 and inicio != -2):
                    botonR.update(pantalla,130,130)
                    a = Componentes.respuestaT("q",num)
                    Componentes.sonCI(correcto,incorrecto,a,pantalla)
                    num +=1
                    if a == "T":
                        correctas +=1
                if event.key == pygame.K_w and inicio !=-1 and inicio != -2:
                    botonV.update(pantalla,130,130)
                    a = Componentes.respuestaT("w",num)
                    Componentes.sonCI(correcto,incorrecto,a,pantalla)
                    if a == "T":
                        correctas +=1
                    num+=1
                if event.key == pygame.K_e and inicio !=-1 and inicio != -2:
                    botonA.update(pantalla,130,130)
                    a = Componentes.respuestaT("e",num)
                    Componentes.sonCI(correcto,incorrecto,a,pantalla)
                    if a == "T":
                        correctas +=1

                    num+=1
                if (event.key == pygame.K_q and inicio == -1):
                    inicio = 0
                if event.key == pygame.K_q and inicio == -2:
                    inicio = -1
                    num =0
        #Actualizamos la pantalla
        pygame.display.update()
    pygame.quit()

main()
