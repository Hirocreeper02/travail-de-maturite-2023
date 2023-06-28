

liste = []

class Ressource():

    def __init__(self, nom:str, type:str, valeur:int):

        self.nom = nom
        self.type = type
        self.valeur = valeur

        liste.append(self)