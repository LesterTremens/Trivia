# coding=utf-8
import Componentes
from Componentes import Boton
import pygame
import SystemTrivia
import Escenas
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
    #Cargando Sonidos
    correcto = pygame.mixer.Sound("Correcto.wav")
    incorrecto = pygame.mixer.Sound("Incorrecto.wav")
    #Cargando imagenes
    fondo = pygame.image.load("FondoA.png")
    #Color del bg
    bg=(199,174,180)
    #Superficie invisible para pueba de la respuesta
    t_f = pygame.Surface([0,0])
    gameOver = False
    num = 0
    inicio=-1
    correctas =0
    numQA = len(Componentes.quiz_ans)
    #LoopPrincipal
    while gameOver !=True:

        pantalla.fill(bg)
        reloj.tick(60)
        #Componentes.dibujarBG(bg,pantalla,x,y)
        Componentes.dibujar_panel(fondo,pantalla)
        #Reproducir musica infinitamente
        #Escena del menu
        if (inicio == -1):
            Escenas.inicio(pantalla)
        #Escena finalizada
        if (num >= numQA):
            inicio = -2
            Escenas.fin(pantalla,8,numQA)
        #Escena de la trivia
        if (inicio >= 0 and num < numQA):
            Escenas.trivia(num,pantalla)

        #Eventos en ocurren a lo largo del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameOver = True
                if (event.key == pygame.K_q and inicio !=-1 and inicio != -2):
                    Componentes.sonCI(correcto,incorrecto,"q",pantalla)
                    pygame.time.wait(1500)
                    num +=1
                if event.key == pygame.K_w and inicio !=-1 and inicio != -2:
                    Componentes.sonCI(correcto,incorrecto,"w",pantalla)
                    pygame.time.wait(1500)
                    num+=1
                if event.key == pygame.K_e and inicio !=-1 and inicio != -2:
                    Componentes.sonCI(correcto,incorrecto,"e",pantalla)
                    pygame.time.wait(1500)
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
