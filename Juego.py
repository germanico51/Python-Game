# importación de paquetes
import pygame, sys

# Inicialización de Pygame
pygame.init()

# Creación de la pantalla
PANTALLA = pygame.display.set_mode((1000, 600))

#Fondo del juego
fondo = pygame.image.load("imagenes/fondo.png")
PANTALLA.blit(fondo,(0,0))


# Especificación de título
pygame.display.set_caption('Exterminator')
icono = pygame.image.load("imagenes/Exterminator.png")
pygame.display.set_icon(icono)

# Bucle de ejecución
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
