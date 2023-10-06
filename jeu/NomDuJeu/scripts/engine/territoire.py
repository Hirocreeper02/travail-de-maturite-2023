import random
import math

import labGen

import sys
sys.path.append("scripts/mechanics")
import provinces

#################### INITIALISATION ####################

# terrain = []
# territoire = []
# frontieres = []

# terrain = [
#     "-------AAAA--------AAA",
#     "~~~~~----A---~~------A",
#     "-~~~-------~~~~-------",
#     "-----AA-----~~--------",
#     "---AAAAA-------------A",
#     "------AAA---------AAAA", 
#     "-------A-----------AAA",
#     "---A------~---------AA",
#     "AAAAA-----~~~---------",
#     "AA---------~~-------AA",
#     "~~~--------------AAAAA",
#     "~~~~-------------AAAAA"]

# #################### DEFINITIONS ####################

# def createGrid(dimensions:tuple = (25,25)) -> list:
#     """Créé une grille vide avec les dimensions données (utile pour créer les terrains et territoires)"""
    
#     grid = []
    
#     tailleX,tailleY = dimensions
    
#     for y in range(tailleY):
        
#         grid.append([])
        
#         for _ in range(tailleX):
#             grid[y].append("-")
    
#     return grid

# def getRandomPoints(numberOfPoints:int,grid:list) -> list:
#     """Donne n points aléatoires sur la grille donnée"""
    
#     listOfPoints = []
    
#     for point in range(numberOfPoints):
        
#         while True:
            
#             point = [random.randint(0,len(grid[0])-1),random.randint(0,len(grid[1]))]
            
#             if point not in listOfPoints:
                
#                 listOfPoints.append(point)
                
#                 break
    
#     return listOfPoints


# def divideStates(listOfPoints:list,grid:list) -> list:
#     """Divise une grille en n territoires"""
    
#     print("provinces.indexComtes",provinces.indexComtes)
    
#     print(len(provinces.indexComtes)," =? ",len(listOfPoints))
    
#     # colors = {
#     #     str(point): provinces.indexComtes[key]
#     #     for key, point in zip(provinces.indexComtes, listOfPoints)
#     # }
    
#     colors = {}
    
#     for comte,point in zip(provinces.indexComtes.values(),listOfPoints):
#         colors[str(point)] = comte
#         comte.foyer = point
    
#     for y,column in enumerate(grid):
        
#         for x,row in enumerate(column):
            
#             distance = 10**20
            
#             for point in listOfPoints:
                
#                 if math.sqrt(abs(x-point[0]) + abs(y-point[1])) < distance: # Pythagore
                    
#                     distance = math.sqrt(abs(x-point[0]) + abs(y-point[1]))
#                     grid[y][x] = colors[str(point)]

#     return grid

# def createTerritoire(listOfPoints:int,grid:list) -> list:
#     """Divise la grille donnée en n territoires aléatoires"""
    
#     grid = divideStates(listOfPoints,grid)
    
#     return grid

# def getFrontieres(grid:list) -> list:
#     """Crée une grille comprenant uniquement les coordonnées des frontières"""
    
#     borderGrid = createGrid((len(grid[0]),len(grid)))
    
#     for y,yPosition in enumerate(grid):
        
#         for x,xPosition in enumerate(yPosition):
            
#             territoiresVoisins = set()
            
#             for yVoisin in grid[y-1:y+2]:
                
#                 for xVoisin in yVoisin[x-1:x+2]:
                    
#                     territoiresVoisins.add(xVoisin)
            
#             if len(territoiresVoisins) > 1:
                
#                 borderGrid[y][x] = grid[y][x]
    
#     print("\033[0;31m",borderGrid,"<- in territoire.getFrontieres.py","\033[0;37m")
    
#     return borderGrid

# def assignProvinces(noProvinces:int,foyers:list):
#     """Répartis les comtés dans des provinces aléatoirement"""
    
#     randomPoints = []
    
#     for _ in range(noProvinces):
        
#         while True:
            
#             foyerProvince = foyers[random.randint(0,len(foyers)-1)]
            
#             if foyerProvince not in randomPoints:
                
#                 randomPoints.append(foyerProvince)
                
#                 break
    
#     for point,province in zip(randomPoints,provinces.index.values()):
        
#         province.foyer = point
#         print("PROVINCE.FOYER : ", province.foyer)
    
#     for comte in provinces.indexComtes.values():
        
#         distance = 10**10
        
#         for province in provinces.index.values():
            
#             print(comte.foyer, type(comte.foyer),":",province.foyer, type(province.foyer))
            
#             if math.sqrt(abs(comte.foyer[0]-province.foyer[0]) + abs(comte.foyer[1]-province.foyer[1])) < distance:
                
#                 distance = math.sqrt(abs(comte.foyer[0]-province.foyer[0]) + abs(comte.foyer[1]-province.foyer[1])) < distance
#                 provinceParente = province
        
#         provinceParente.comtes[comte.nom] = comte
    
    
#     for province in provinces.index.values():
        
#         print(province.comtes)

from PIL import Image,ImageFile
import random
import math

ImageFile.LOAD_TRUNCATED_IMAGES = True

labyrintheMap = Image.open("scripts/engine/temp_img/labyrinthe.png")

def colourChange():

    global labyrintheMap

    for x in range(labGen.dimensions[0]):
        for y in range(labGen.dimensions[1]):

            if labyrintheMap.getpixel((x,y)) == (112,112,112):

                labyrintheMap.putpixel((x,y),(112,200,112))

            else:

                labyrintheMap.putpixel((x,y),(112,112,200))

def randomPoints(noOfPoints:int):

    randomPoints = []

    for _ in range(noOfPoints):

        while True:

            randPoint = (random.randint(0,labGen.dimensions[0]-1),random.randint(0,labGen.dimensions[1]-1))

            if labyrintheMap.getpixel(randPoint) != (112,112,200):

                randomPoints.append(randPoint)

                break

    return randomPoints

def repartirTerritoire(randomPoints:list):

    global labyrintheMap
    global territoireMap

    territoireMap = Image.new("RGBA",(labGen.dimensions[0],labGen.dimensions[1]),(0,0,0,0))

    dictionnaire = {
        point: (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            255
        )
        for point in randomPoints
    }

    for x in range(labGen.dimensions[0]):
        for y in range(labGen.dimensions[1]):

            if labyrintheMap.getpixel((x,y)) != (112,112,200):

                distance = 10**10

                for point in randomPoints:

                    tempDistance = math.sqrt(abs(x-point[0])**2+abs(y-point[1])**2)

                    if tempDistance < distance:

                        territoireMap.putpixel((x,y),dictionnaire[point])
                        distance = tempDistance

def extraireFrontieres():

    global territoireMap
    global frontieresMap

    frontieresMap = Image.new("RGBA",(labGen.dimensions[0],labGen.dimensions[1]),(0,0,0,0))

    for x in range(1,labGen.dimensions[0]-1):
        for y in range(1,labGen.dimensions[1]-1):
            
            if territoireMap.getpixel((x,y)) != (0,0,0,0):
            
                couleurs = set()

                for xVoisin in range(x-1,x+2):
                    for yVoisin in range(y-1,y+2):

                        couleurs.add(territoireMap.getpixel((xVoisin,yVoisin)))

                if len(couleurs) != 1:

                    transparence = 255

                else:

                    transparence = 50
                    
                colour = territoireMap.getpixel((x,y))
                transparentColour = (colour[0],colour[1],colour[2],transparence)
                
                frontieresMap.putpixel((x,y),transparentColour)

# colourChange()

# repartirTerritoire(randomPoints(25))

# extraireFrontieres()

# labyrintheMap.save("scripts/engine/temp_img/labyrintheMap.png")
# territoireMap.save("scripts/engine/temp_img/territoireMap.png")
# frontieresMap.save("scripts/engine/temp_img/frontieresMap.png")

def creation(noProvinces:int,noComtes:int,dimensions:tuple=(100,100)):
    """Création des Provinces, Comtés, et Territoires"""
    
    # provinces.creation(noProvinces,noComtes)
    global labyrintheMap
    global territoire
    global frontieres

    labyrintheMap = Image.open("scripts/engine/temp_img/labyrinthe.png")
    
    colourChange()
    repartirTerritoire(randomPoints(noComtes))
    extraireFrontieres()

    labyrintheMap.save("scripts/engine/temp_img/labyrintheMap.png")
    territoireMap.save("scripts/engine/temp_img/territoireMap.png")
    frontieresMap.save("scripts/engine/temp_img/frontieresMap.png")

    print("New map processed ended with a success")

    # territoire = createGrid(dimensions)
    # listOfPoints = getRandomPoints(noComtes,territoire)
    # territoire = createTerritoire(listOfPoints,territoire)
    
    # assignProvinces(noProvinces,listOfPoints)
    
    # frontieres = getFrontieres(territoire)

# creation(5,30)