import pygame
import sys

### GOUVENEMENTS ###
seuilDeReussiteLegislatif = 1
seuilDeReussiteExecutif = 1
seuilDeReussiteJudiciare = 1

facteurAcceptationLegislatif = 1 # [0;1]
facteurAcceptationExecutif = 1 # [0;1]
facteurAcceptationJudiciaire = 1 # [0;1]

### FONCTIONS ###
seuilMaximumAcceptation = 80 # [0;100]
distancePointNul = 1000

### LOIS ###
facteurDeDeriveDesComtes = 1 / 10000

### FINANCES ###
tauxImposition = 1

### KEYBINDS ###
left = [pygame.K_a,pygame.K_LEFT]
right = [pygame.K_d,pygame.K_RIGHT]
up = [pygame.K_w,pygame.K_UP]
down = [pygame.K_s,pygame.K_DOWN]
