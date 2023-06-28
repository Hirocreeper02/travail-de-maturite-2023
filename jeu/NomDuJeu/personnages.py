import factions

liste = []

class Personnage():

    def __init__(self, nom:str, faction:object, influence:int, age:int):

        self.nom = nom
        self.faction = faction
        self.influence = influence
        self.age = age

        faction.membres.append(self)