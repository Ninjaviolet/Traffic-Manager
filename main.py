import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1920, 1000))

continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

pygame.quit()