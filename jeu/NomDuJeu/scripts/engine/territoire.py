import labGen

import sys
sys.path.append("scripts/mechanics")
import provinces
import ressources

from PIL import Image,ImageFile
import random
import math

ImageFile.LOAD_TRUNCATED_IMAGES = True

labyrintheMap = Image.open("scripts/engine/temp_img/labyrinthe.png")
frontieresMap = None
ressourcesMap = None

quantityOfZooms = 5

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

    global couleurComtes
    couleurComtes = dict(zip(dictionnaire.values(),provinces.indexComtes.values()))

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

                transparence = 255 if len(couleurs) != 1 else 50
                colour = territoireMap.getpixel((x,y))
                transparentColour = (colour[0],colour[1],colour[2],transparence)

                frontieresMap.putpixel((x,y),transparentColour)

# colourChange()

# repartirTerritoire(randomPoints(25))

# extraireFrontieres()

# labyrintheMap.save("scripts/engine/temp_img/labyrintheMap.png")
# territoireMap.save("scripts/engine/temp_img/territoireMap.png")
# frontieresMap.save("scripts/engine/temp_img/frontieresMap.png")

def creerCarteRessources(listeFoyers:list):

    global frontieresMap
    global couleurComtes
    global ressourcesMap
    
    ressourcesImages = {
    ressources.index["Armes"]:Image.open("assets/graphic/ressources/armes.png"),
    ressources.index["Bijoux"]:Image.open("assets/graphic/ressources/bijou.png"),
    ressources.index["Diamant"]:Image.open("assets/graphic/ressources/diamant.png"),
    ressources.index["Ficelle"]:Image.open("assets/graphic/ressources/ficelle.png"),
    ressources.index["Habits"]:Image.open("assets/graphic/ressources/habits.png"),
    ressources.index["Lingot"]:Image.open("assets/graphic/ressources/lingot.png"),
    ressources.index["Minerai"]:Image.open("assets/graphic/ressources/minerai.png"),
    ressources.index["Nourriture"]:Image.open("assets/graphic/ressources/nourriture.png"),
    ressources.index["Or"]:Image.open("assets/graphic/ressources/or.png"),
    ressources.index["Tissu"]:Image.open("assets/graphic/ressources/tissu.png")
}

    ressourcesMap = Image.new("RGBA",(labGen.dimensions[0],labGen.dimensions[1]),(0,0,0,0))

    for point in listeFoyers:

        pixel = frontieresMap.getpixel(point)
        pixel = (pixel[0],pixel[1],pixel[2],255)

        print(couleurComtes[pixel],"|",couleurComtes[pixel].ressource)

        mask = ressourcesImages[couleurComtes[pixel].ressource].convert("L")
        mask = mask.point(lambda p: p > 0 and 255) # ThanksGPT

        ressourcesMap.paste(ressourcesImages[couleurComtes[pixel].ressource],(point[0]-16,point[1]-16),mask)



def creation(noProvinces:int,noComtes:int,dimensions:tuple=(100,100)):
    """Création des Provinces, Comtés, et Territoires"""
    
    provinces.creation(noProvinces,noComtes)

    global labyrintheMap
    global frontieresMap
    global ressourcesMap

    global territoire
    global frontieres

    labyrintheMap = Image.open("scripts/engine/temp_img/labyrinthe.png")

    colourChange()
    listeFoyers = randomPoints(noComtes)
    repartirTerritoire(listeFoyers)
    extraireFrontieres()

    creerCarteRessources(listeFoyers)

    labyrintheMap.save("scripts/engine/temp_img/labyrintheMap.png")
    #territoireMap.save("scripts/engine/temp_img/territoireMap.png")
    frontieresMap.save("scripts/engine/temp_img/frontieresMap.png")
    ressourcesMap.save("scripts/engine/temp_img/ressourcesMap.png")

    # global quantityOfZooms

    # for i in range(1,quantityOfZooms+1):

    #     labyrintheMap = labyrintheMap.resize((labyrintheMap.width*2,labyrintheMap.height*2))
    #     frontieresMap = frontieresMap.resize((frontieresMap.width*2,frontieresMap.height*2))

    #     labyrintheMap.save(f"scripts/engine/temp_img/labyrintheMap{i}.png")
    #     frontieresMap.save(f"scripts/engine/temp_img/frontieresMap{i}.png")

    print("New map processed ended with a success")