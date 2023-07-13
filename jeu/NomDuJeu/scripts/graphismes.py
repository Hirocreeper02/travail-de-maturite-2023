import variables

import pygame
 
pygame.init()
X = 1450
Y = 800
 
scrn = pygame.display.set_mode((X, Y)) # Création de la Fenêtre
 
pygame.display.set_caption('Map') # Nom de la Fenêtre
 
imp = pygame.image.load("assets/map.png").convert() # Surface avec Image Dessinée
 
scrn.blit(imp, (0, 0))
 
pygame.display.flip()
status = True
while (status):
 
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
            status = False
 
        if event.type == pygame.KEYDOWN:
           
            for i in range(2):

                if event.key == variables.up[i]:

                    print("UP")

                if event.key == variables.down[i]:

                    print ("DOWN")

                if event.key == variables.right[i]:

                    print("RIGHT")

                if event.key == variables.left[i]:

                    print("LEFT") 
pygame.quit()

#https://www.geeksforgeeks.org/python-display-images-with-pygame/