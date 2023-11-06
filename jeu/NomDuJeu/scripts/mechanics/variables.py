import pygame
import sys

### MAIN ###

tickSpeed = 1
facteurFonctionsB = 4
facteurFonctionsC = 10


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

seuilProgressionRecherche = 100
seuilProgressionPolitique = 100
seuilProgressionLobbying = 100
seuilProgressionPublicite = 100
seuilProgressionManifestations = 100

### FINANCES ###
tauxImposition = 1

### PERSONNAGES ###
seuilAssassinat = 10
seuilInfluenceRapprochement = 10
seuilInfluenceCorruption = 10
seuilArgentCorruption = 10