import variables as keybind

import pygame
import sys

### PREPARATION ###

pygame.init()
X = 1400
Y = 800

A = 0
B = 0

scrn = pygame.display.set_mode((X, Y)) # Dimensions

pygame.display.set_caption('Map') # Nom

imp = pygame.image.load("assets/map.png").convert() # Préparation Image

scrn.blit(imp, (0, 0)) # Impression du Contenu

### ACTIVATION ###

pygame.display.flip()
status = True

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            for i in range(2):

                if event.key == keybind.left[i]:
                    print("LEFT!")
                    A += 10
            
                if event.key == keybind.right[i]:
                    print("RIGHT!")
                    A -= 10

                if event.key == keybind.up[i]:
                    print("UP!")
                    B += 10

                if event.key == keybind.down[i]:
                    print("DOWN!")
                    B -= 10

### FIN ###

pygame.quit()



# https://www.geeksforgeeks.org/python-display-images-with-pygame/