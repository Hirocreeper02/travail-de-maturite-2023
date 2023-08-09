import fonctions
import factions
import files

index = {}

class Province():

    def __init__(self, nom:str, faction:object):

        self.nom = nom
        self.faction = faction
        self.comtes = {}

        #index[self.nom] = self

    def __repr__(self):
        return f"{self.nom}"

class Comte():

    def __init__(self, nom:str, faction:object, ressource:object, population:int, classes:list, positionnement:list):

        self.nom = nom
        self.faction = faction
        self.ressource = ressource
        self.population = population
        self.classes = classes
        self.positionnement = positionnement
        self.voisins = []

        for i in self.classes:
            i = i / 100

    def __repr__(self):
        return f"{self.nom}"

    def verifierAllegance(self):

        print("")
        choix = [self.faction,fonctions.comparerGraphes(self.faction,self)]
        print("")

        for faction in factions.liste:
            difference = fonctions.comparerGraphes(faction,self)
            if difference < choix[1]:
                choix = [faction,difference]

        self.faction = choix[0]

        print("\nLe comté",self.nom,"a décidé d'accorder sa fidélité à la faction:",self.faction.nom,"\n")

def creation(noProvinces:int,noComtes:int):

    repartitionComtes = fonctions.repartitionInegale(noComtes,noProvinces)

    print("REPARTITION COMTES : ", repartitionComtes)

    for i in range(noProvinces):

        while True:
            nom = files.nomAleatoire(files.index["provinces.txt"])

            if nom != index.keys():
                break

        faction = fonctions.elementAleatoire(factions.index)

        index[nom] = Province(nom,faction)

        for j in range(repartitionComtes[i]):

            while True:

                nomComte = files.nomAleatoire(files.index["comtes.txt"])

                if nomComte != index.keys():
                    break

            ressource = None

            population = 100

            classes = [33,33,33]

            positionnement = [0,0,0,0]

            index[nom].comtes[nomComte] = Comte(nomComte,faction,ressource,population,classes,positionnement)