import factions
import fonctions
import files

import random

index = {}
liste = []

class Personnage():

    def __init__(self, nom:str, faction:str, influence:int, age:int):

        self.nom = nom
        self.faction = faction
        self.influence = influence
        self.age = age

        self.faction.membres.append(self)

        index[self.nom] = self

    def __repr__(self):
        return f"{self.nom} ({self.faction})"

def creation(nombreDeFactions,nombreDePersonnages):
    
    repartition = fonctions.repartitionInegale(nombreDePersonnages,nombreDeFactions)

    print("FACTIONS: ",factions.index,"| REPARTITION: ",repartition)

    i = 0

    for key in factions.index:

        for j in range(repartition[i]):

            while True:
                nom = files.nomAleatoire(files.index["prenoms_masculins.txt"])+" "+files.nomAleatoire(files.index["noms.txt"])

                if nom != index.keys:
                    break

            influence = random.randint(1,100)

            age = random.randint(20,80)

            factions.index[key].membres.append(Personnage(nom,factions.index[key],influence,age))

        i += 1

    for key in index:
        print(index[key])