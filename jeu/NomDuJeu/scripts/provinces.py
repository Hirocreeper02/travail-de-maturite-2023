import fonctions
import factions
import files

index = {}

class Province():

    def __init__(self, nom:str, faction:object):

        self.nom = nom
        self.faction = faction
        self.comtes = []

        index[self.nom] = self

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

def creation(noProvinces:int,noComtes:int,noFactions:int):

    for i in range(noProvinces):

        while True:
            nom = files.nomAleatoire(files.index["provinces"])

            if nom != index.keys():
                break

        faction = None

        index{nom} = Province(nom,faction)