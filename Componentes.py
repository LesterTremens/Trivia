import pygame
import SystemTrivia

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
    def update(self,pantalla):
        pantalla.blit(self.imagen_actual,self.rect)

def dibujar_panel(imagen, pantalla,x,y):
    panel = pygame.transform.scale(imagen,(1400,675))
    pantalla.blit(panel,(265,75))


def fuente(len):
    #Ruta del tipo de fuente
    font_path = "Lucida.ttf"
    #Tamaño deseado de la fuente
    font_size = len
    #Regresamos el tipo de fuente creado
    return pygame.font.Font(font_path,font_size)
#Funcion que devuelve el texto correspondiente a una pregunta o una respuesta
def respuestaT(opcion):
    if opcion == "q":
        return quiz_ans[0].ans1[1]
    if opcion == "w":
        return quiz_ans[0].ans2[1]
    if opcion == "e":
        return quiz_ans[0].ans3[1]

def textop(opcion):
    font1 = fuente(50)
    if opcion == "T":
        return font1.render("Correcto",True,(0,0,0))
    if opcion == "F":
        return font1.render("Incorrecto",True,(0,0,0))

def texto(n,opcion):
    #Tipos de fuente y asignamos el tamaño
    font = fuente(100)
    font1 = fuente(50)
    #Usamos la funcion render para obtener el texto correspondiente
    if opcion == "question":
        return font.render(quiz_ans[n].question,True,(0,0,0))
    if opcion == "ans1":
        return font1.render((quiz_ans[n].ans1[2:]),True,(0,0,0))
    if opcion == "ans2":
        return font1.render((quiz_ans[n].ans2[2:]),True,(0,0,0))
    if opcion == "ans3":
        return font1.render((quiz_ans[n].ans3[2:]),True,(0,0,0))