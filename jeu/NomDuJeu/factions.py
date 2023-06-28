

liste = []

class Faction():

    def __init__(self, nom:str, utopie:object, positionnement:list, motto:str):

        self.nom = nom
        self.utopie = utopie
        self.positionnement = positionnement
        self.motto = motto
        self.membres = []

        liste.append(self)