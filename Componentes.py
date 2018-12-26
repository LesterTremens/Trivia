import pygame
import SystemTrivia
import os

tache = pygame.image.load("Img/tache.png")
palomita = pygame.image.load("Img/palomita.png")
#Lita de preguntas y respuestas
quiz_ans = SystemTrivia.get_QA(SystemTrivia.archivo)

#Tendremos un rectangulo que apunte al Cursor en todo momento.
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()



class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen,x = 200 , y = 200):
        self.imagen_actual = imagen
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def update(self,pantalla,x,y):
        pan = pygame.transform.scale(self.imagen_actual,(x,y))
        pantalla.blit(pan,self.rect)

class Robots(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,imagen3,x =200,y = 200):
        self.imagen_1 = imagen1
        self.imagen_2 = imagen2
        self.imagen_3 = imagen3
        self.imagenes= [self.imagen_1,self.imagen_2,self.imagen_1,self.imagen_3]
        self.imagen = self.imagenes[0]
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left= (x,y)

    def update(self,pantalla,n):
        for r in self.imagenes:
            pantalla.blit(self.imagenes[n],self.rect)

def dibujar_panel(imagen, pantalla):
    pan1 = pygame.transform.scale(imagen,(1600,900))
    pantalla.blit(pan1,(150,90))

def dibujarBG(imagen,pantalla,x,y):
    pan2 = pygame.transform.scale(imagen,(x,y))
    pantalla.blit(pan2,(0,0))

def fuente(len):
    #Ruta del tipo de fuente
    font_path = "Textos/Lucida.ttf"
    #Tamaño deseado de la fuente
    font_size = len
    #Regresamos el tipo de fuente creado
    return pygame.font.Font(font_path,font_size)
#Funcion que devuelve el texto correspondiente a una pregunta o una respuesta

def sonCI(correcto,incorrecto,v,pantalla):
    if v == "T":
        pantalla.blit(palomita,(1000,200))
        correcto.play()
    else:
        pantalla.blit(tache,(1000,200))
        incorrecto.play()

def respuestaT(opcion,num):
    if opcion == "q":
        return quiz_ans[num].ans1[1]
    if opcion == "w":
        return quiz_ans[num].ans2[1]
    if opcion == "e":
        return quiz_ans[num].ans3[1]

def textop(opcion):
    font1 = fuente(50)
    if opcion == "T":
        return font1.render("Correcto",True,(0,0,0))
    if opcion == "F":
        return font1.render("Incorrecto",True,(0,0,0))

def texto(n,opcion):
    #Tipos de fuente y asignamos el tamaño
    font = fuente(50)
    font1 = fuente(30)
    #Usamos la funcion render para obtener el texto correspondiente
    if opcion == "question":
        f = len(quiz_ans[n].question) -1
        return font.render(quiz_ans[n].question[1:f],True,(0,0,0))
    if opcion == "ans1":
        f = len(quiz_ans[n].ans1) -1
        return font1.render((quiz_ans[n].ans1[2:f]),True,(0,0,0))
    if opcion == "ans2":
        f = len(quiz_ans[n].ans2) -1
        return font1.render((quiz_ans[n].ans2[2:f]),True,(0,0,0))
    if opcion == "ans3":
        f = len(quiz_ans[n].ans3) -1
        return font1.render((quiz_ans[n].ans3[2:f]),True,(0,0,0))
