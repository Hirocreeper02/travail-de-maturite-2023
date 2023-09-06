import factions
import gouvernements
import lois
import provinces
import ressources
import utopies

import os

from typing import get_type_hints # Permet de savoir le Type Hinting de chaque attribut ou variable

objects = {"factions.txt":factions.Faction,"lois.txt":lois.Loi,"provinces.txt":provinces.Province,"ressources.txt":ressources.Ressource,"utopies.txt":utopies.Utopie}

def openFile(file:str) -> str: # Opens file

    f = open(file,"r")
    fileData = f.readlines()

    return fileData

def divideCells(fileData:list) -> str: 

    stats = []
    temp = []

    for i in range(len(fileData)):

        temp.append(fileData[0])
        fileData.remove(fileData[0])

        if "}\n" in temp:

            stats.append(temp)
            temp = []

    return stats

def cellEpuration(liste:list) -> str:

    for i in range(len(liste)):

        liste[i] = liste[i].replace("\n","")

    while True:
        if "" in liste:
            liste.remove("")
        else:
            return liste

def extractTemplate(cells:list) -> str:
    
    cells[0][0] = " {"

    cells[0] = cellEpuration(cells[0])

    return cells[0]

def readInfo(cells:list,template:list) -> str:

    infos = []

    cells.remove(cells[0]) # Effaçage du template

    for i in range(len(cells)):

        tempInfo = {}

        cellEpuration(cells[i])

        for j in range(len(cells[i])):

            

            if " {"  in cells[i][j]: #Element "nom"

                tempInfo["nom"] = cells[i][j].replace(" {","")

            elif cells[i][j].replace(template[j],"") != "": #Si l'élément similaire n'est pas égal à celui dans le template

                cells[i][j] = cells[i][j].split(" = ") #Crée une liste [nomDeLaVariable, variable]

                tempInfo[cells[i][j][0].replace("   ","")] = cells[i][j][1] #Enlève les "tabs"

            else:
                cells[i][j] = ""

        while True:
        
            if "" in cells[i]:
                cells[i].remove("")

            else:

                break

        infos.append(tempInfo)
    
    print(infos)

    return infos

def createObjects(infos,fileIndex):

    #Solution at https://stackoverflow.com/questions/4290178/why-cant-i-change-another-modules-variable-in-python

    classObject = objects[fileIndex]
    index = classObject.__module__.index

    for i in range(len(infos)):
        
        objectInfo = infos[i]

        print("objectInfo",objectInfo)

        print(index)

        key = objectInfo["nom"]

        index[key] = classObject()

        print(index[objectInfo["nom"]])
        

def load(file:str):

    fileData = openFile(file)

    cells = divideCells(fileData)
    template = extractTemplate(cells)

    infos = readInfo(cells,template)

    fileIndex = file.split("/")[-1] # Ignorer le chemin d'accès, juste garder le nom du fichier

    createObjects(infos,fileIndex)

load("saves/Savegame - 2023-08-10 14:14:08.651758/ressources.txt")

#####

def loadGame(saveName:str):

    saveName = "saves/" + saveName

    for root, dirs, files in os.walk(saveName):  
             
	    for file in files:
                load(saveName + "/" + os.path.basename(file))