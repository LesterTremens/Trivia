pygame.init() #Inciamos todos los modulos de pygame
pantalla = pygame.display.set_mode((0,0),pygame.FULLSCREEN) # Tamanio de la pantalla.
salir= False #Finaliza el evento principal.
reloj1 = pygame.time.Clock() #Reloj para actualizar los frames por segundo
blanco =(255,255,255) #Color en formato RGB
#Tipo de fuente a usar
fuente1 = pygame.font.Font(None,100)
#Texto que se mostrara
texto1= fuente1.render("Hola",0,(0,0,0))
#Evento principal
while salir != True:
    #Decide cada cuando se actualizara
    reloj1.tick(20)
    #Color de la pantalla
    pantalla.fill(blanco)
    #Colocamos donde se mostrara el texto colocando una nueva superficie
    pantalla.blit(texto1,(150,150))
    #actualiza la ventaba constantemente
    pygame.display.update()
    #Evento que permite cerrar la ventana.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                salir = True
            salir = True

pygame.quit()
