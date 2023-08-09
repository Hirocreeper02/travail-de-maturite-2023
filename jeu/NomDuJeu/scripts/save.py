import factions
import gouvernements
import lois
import provinces
import ressources
import terrain
import utopies
import load

import inspect
import os
from datetime import datetime

parentFolder = "saves"

listOfClassFolders = {"factions":factions.index,"factions":factions.index,"lois":lois.index,"provinces":provinces.index,"ressources":ressources.index,"utopies":utopies.index}

def appendToFile(file,appendMessage):

    f = open(file,"a")

    f.write(appendMessage)

    f.close()

def getClassVariables(object:object):

    varList = []

    for i in inspect.getmembers(object):
    
        if not i[0].startswith('_'): # Enlève les potentielles fonctions privées

            if not inspect.ismethod(i[1]): # Enlever les méthodes
                
                varList.append(i)

    return varList

def format(classIndex:dict):

    appendMessage = ""

    for key in classIndex:

        varList = getClassVariables(classIndex[key])

        tempMessage = ""

        for i in range(len(varList)):

            if varList[i][0] != "nom": #Check if not name 

                tempMessage = tempMessage + "   " + str(varList[i][0]) + " = " + str(varList[i][1]) + "\n"

            else:

                tempMessage = str(varList[i][1]) + " {\n" + tempMessage

        tempMessage = tempMessage + "}\n\n"

        appendMessage = appendMessage + tempMessage

    print(appendMessage)

    return appendMessage

def save(file:str,classIndex:dict):

    appendMessage = format(classIndex)

    appendToFile(file,appendMessage)

#####

def createFolder(folderName:str):

    path = os.path.join(parentFolder, folderName)

    os.mkdir(path)

    return path

def createFile(path:str,fileName:str):
    
    open(path,"x")
  
def saveGame(saveName:str = "Savegame - " + str(datetime.now())):

    path = createFolder(saveName)

    for key in listOfClassFolders:

        filePath = path + "/" + key + ".txt"

        createFile(filePath,key)
        save(filePath,listOfClassFolders[key])

# Created the files, now have to fill them

# https://www.geeksforgeeks.org/create-a-directory-in-python/