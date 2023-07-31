import os
import random

index = {}

def collectFiles():

    for root, dirs, files in os.walk("values"):
	    for file in files:
                 index[os.path.basename(file)] = os.path.join(root,file)

def read(filePath):

    file = open(filePath,"r")

    fileData = file.readlines()

    for i in range(len(fileData)):
        fileData[i] = fileData[i].replace("\n","")

    return fileData

def nomAleatoire(filePath):
     
    return random.choice(read(filePath))

collectFiles()

print(read(index["noms.txt"]))

#"noms.txt":open("values/noms/personnages/noms.txt","r")

#https://pythonexamples.org/python-get-list-of-all-files-in-directory-and-sub-directories/