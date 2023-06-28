

liste = []

class Loi():

    def __init__(self, nom:str, effets:None, impact:list, positionnement:list):

        self.nom = nom
        self.effets = effets
        self.impact = impact
        self.positionnement = positionnement

def creation():

    liste.append(Loi("Ordre et Progrès",None,[[0,0,0],[5,10,-1],[3,5,-4]],[0,-50,0,0]))