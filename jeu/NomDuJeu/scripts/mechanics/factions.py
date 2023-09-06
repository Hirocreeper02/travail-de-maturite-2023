import utopies
import files
import fonctions

import random

index = {}

nameIndex = {}
mottoIndex = {}

class Faction():

    def __init__(self, nom:str, utopie:object, positionnement:list, motto:str, finances:int = 0, membres:list = []):

        self.nom = nom
        self.positionnement = positionnement
        self.motto = motto
        self.membres = membres
        self.utopie = utopie
        self.finances = finances
    
    def __repr__(self):
        return f"{self.nom}"
    
class Personnage():

    def __init__(self, nom:str, faction:str, influence:int, age:int):

        self.nom = nom
        self.faction = faction
        self.influence = influence
        self.age = age

    def __repr__(self):
        return f"{self.nom}"

def creation(nombreDeFactions,nombreDePersonnages):

    # CREATION FACTIONS #

    nameIndex = {utopies.index["Technocratie"]:files.index["technocratisme.txt"]}
    mottoIndex = {utopies.index["Technocratie"]:"mottos_technocratisme.txt"}


    for i in range(nombreDeFactions):

        utopie = fonctions.elementAleatoire(utopies.index)

        while True:
            nom = files.nomAleatoire(nameIndex[utopie])

            if nom != index.keys():
                break

        positionnement = [0,0,0,0]

        motto = mottoIndex[utopie]

        index[nom] = Faction(nom,utopie,positionnement,motto)

    # CREATION PERSONNAGES #

    repartition = fonctions.repartitionInegale(nombreDePersonnages,nombreDeFactions)

    i = 0

    for key in index:

        for j in range(repartition[i]):

            while True:
                nom = files.nomAleatoire(files.index["prenoms_masculins.txt"])+" "+files.nomAleatoire(files.index["noms.txt"])

                if nom != index.keys:
                    break

            influence = random.randint(1,100)

            age = random.randint(20,80)

            index[key].membres.append(Personnage(nom,index[key],influence,age))

        i += 1

def creationDeterminee(infos):
    
    for i in range(len(infos)):

        nom = infos[i][0]
        positionnement = infos[i][1]
        motto = infos[i][2]
        membres = infos[i][3]
        utopie = utopies.index[infos[i][4]]
        finances = int(infos[i][5])

        index[nom] = Faction(nom,utopie,positionnement,motto,finances,membres)
