

liste = []

class Comte():

    def __init__(self, nom:str, faction:object, ressource:object, population:int, classes:list, positionnement:list):

        self.nom = nom
        self.faction = faction
        self.ressource = ressource
        self.population = population
        self.classes = classes
        self.positionnement = positionnement

        liste.append(self)