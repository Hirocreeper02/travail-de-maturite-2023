import factions
import gouvernements
import lois
import provinces
import ressources
import utopies

import os

from typing import get_type_hints # Permet de savoir le Type Hinting de chaque attribut ou variable

#createObjects = {"file.txt":ressources.creationDeterminee}

createObjects = {"factions.txt":factions.creationDeterminee,"lois.txt":lois.creationDeterminee,"provinces.txt":provinces.creationDeterminee,"ressources.txt":ressources.creationDeterminee,"utopies.txt":utopies.creationDeterminee}

def openFile(file:str):

    f = open(file,"r")
    fileData = f.readlines()

    return fileData

def divideCells(fileData:list):

    stats = []
    temp = []

    for i in range(len(fileData)):

        temp.append(fileData[0])
        fileData.remove(fileData[0])

        if "}\n" in temp:

            stats.append(temp)
            temp = []

    return stats

def cellEpuration(liste:list):

    for i in range(len(liste)):

        liste[i] = liste[i].replace("\n","")

    while True:
        if "" in liste:
            liste.remove("")
        else:
            return liste

def extractTemplate(cells:list):
    
    cells[0][0] = " {"

    cells[0] = cellEpuration(cells[0])

    return cells[0]

def readInfo(cells:list,template:list):

    cells.remove(cells[0]) # Effaçage du template

    for i in range(len(cells)):

        cellEpuration(cells[i])

        for j in range(len(cells[i])):

            cells[i][j] = cells[i][j].replace(template[j],"")

            if cells[i][j] == "":
                cells[i].remove("")

            # Soustraction de variables: celluleCible - celluleTemplate

    return cells

def load(file:str):

    fileData = openFile(file)

    cells = divideCells(fileData)
    template = extractTemplate(cells)

    infos = readInfo(cells,template)

    fileIndex = file.split("/")[-1] # Ignorer le chemin d'accès, juste garder le nom du fichier

    createObjects[fileIndex](infos)

#####

def loadGame(saveName:str):

    saveName = "saves/" + saveName

    for root, dirs, files in os.walk(saveName):  
             
	    for file in files:

            load(saveName + "/" + os.path.basename(file))