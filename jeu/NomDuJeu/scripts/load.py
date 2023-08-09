import ressources

createObjects = {"file.txt":ressources.creationDeterminee}

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

def Load(file:str):

    fileData = openFile(file)

    cells = divideCells(fileData)
    template = extractTemplate(cells)

    infos = readInfo(cells,template)

    createObjects[file](infos)