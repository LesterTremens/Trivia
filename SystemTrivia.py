import pygame
#Archivo que contiene la trivia
archivo = "/home/orlando/Escritorio/Trivia/Trivia.txt"
class QuizAndAns():
    def __init__(self,question,ans1,ans2,ans3):
        self.question = question
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3


def get_QA(archivo):
    lista = []
    g = open(archivo)
    q=""
    u=""
    d=""
    t=""
    with g:
        linea = g.readline()
        while linea:
            linea.strip()
            if linea[0] == "*":
                q = linea
            if linea[0] == "1":
                u = linea
            if linea[0] == "2":
                d = linea
            if linea[0] == "3":
                t = linea
                if q != "" and u != "" and d != "" and t != "":
                    trivia = QuizAndAns(q,u,d,t)
                    lista.append(trivia)
                    q=""
                    u=""
                    d=""
                    t=""
                else:
                    print( "Revisa tu archivo de texto")
            linea = g.readline()
    return lista
