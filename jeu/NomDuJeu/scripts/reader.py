"""""

import files
import ressources

file = open(files.index["ressources.txt"],"r")

fileData = file.readlines()


def getCells(file): # Division de la page en cellules

    stats = []
    temp = []

    for i in range(len(fileData)):

        if "}" not in fileData[0]:

            temp.append(fileData[0])

            fileData.remove(fileData[0])

        else:

            temp.append(fileData[0])

            fileData.remove(fileData[0])

            stats.append(temp)

            temp = []

    print("temp: ", temp)

    print("stats: ", stats)

    return stats

def basicEpuration(list):

    for i in range(len(list)):

        list[i] = list[i].replace("\n","")

    while True:
            try:
                list.remove("")
            except:
                break
        

def getTemplate(cells): # Extraction de la première cellule comme template de sélection
    
    cells[0][0] = " {"

    basicEpuration(cells[0])

    return cells[0]

def getInfo(cells, template): # Extraction des informations des autres cellules
    
    cells.remove(cells[0]) # Effaçage du template

    for i in range(len(cells)):

        basicEpuration(cells[i])

        for j in range(len(cells[i])):

            cells[i][j] = cells[i][j].replace(template[j],"")

            if cells[i][j] == "":
                cells[i].remove("")

    print(cells)

    return cells

def objectCreation(file,infos):

    if file == "ressources.txt":

        ressources.creationDeterminee(infos[0])

infos = []

objectCreationIndex = {files.index["ressources.txt"]:ressources.creationDeterminee}

def mainControll(file):
    
    cells = getCells(file)

    infos = getInfo(cells, getTemplate(cells))

    objectCreationIndex[file](infos)

mainControll("file.txt")

""""""
