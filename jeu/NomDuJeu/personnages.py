import factions

index = {}
liste = []

class Personnage():

    def __init__(self, nom:str, faction:str, influence:int, age:int):

        self.nom = nom
        self.faction = factions.index[faction]
        self.influence = influence
        self.age = age

        self.faction.membres.append(self)

        index[self.nom] = self