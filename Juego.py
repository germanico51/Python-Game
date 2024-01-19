import pygame, sys
from pygame.locals import *

pygame.init()

PANTALLA = pygame.display.set_mode((500,400))
pygame.display.set_caption('Mi primer Juego')

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

C710E4 = (199,16,228)
C602DC1 = (96, 45, 193)

PANTALLA.fill(BLANCO)

rectangulo1 = pygame.draw.rect(PANTALLA,ROJO,(100,50,100,50))
print(rectangulo1)

pygame.draw.line(PANTALLA,VERDE,(100,101),(199,101),10)
pygame.draw.circle(PANTALLA,NEGRO,(122,250),(20),0)
pygame.draw.ellipse(PANTALLA,AZUL,(265,200,40,70))

puntos=[(100,300),(100,100),(150,100)]
pygame.draw.polygon(PANTALLA,C710E4,puntos,8)
#Bucle del game
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()