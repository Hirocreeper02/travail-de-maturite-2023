
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

def creation():

    liste.append(Loi("Ordre et Progrès",None,[[0,0,0],[5,10,-1],[3,5,-4]],-50,3))
