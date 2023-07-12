import provinces
import comtes
import variables

index = {}
liste = []

class Loi():

    def __init__(self, nom:str, effets:None, impact:list, positionnement:int,axe:int):

        self.nom = nom
        self.effets = effets
        self.impact = impact
        self.positionnement = positionnement
        self.axe = axe - 1

        index[self.nom] = self

    def application(self):

        for prov in provinces.liste:
            for comt in prov.comtes:
                for strate in range(3):
                    print("\n##########\n",comt.nom,"[",comt.ressource.type,"] :\n",comt.positionnement[self.axe])
                    comt.positionnement[self.axe] += self.impact[comt.ressource.type][strate] * comt.population * comt.classes[strate] * variables.facteurDeDeriveDesComtes
                    print("Devenu:",comt.positionnement[self.axe])
                    comt.verifierAllegance()

def creation():

    liste.append(Loi("Ordre et Progrès",None,[[0,0,0],[5,10,-1],[3,5,-4]],-50,3))


