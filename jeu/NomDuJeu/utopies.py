

liste = []

class Utopie():

    def __init__(self, nom:str, structure:object, lois:list, positionnement:list):

        self.nom = nom
        self.structure = structure
        self.lois = lois
        self.positionnement = positionnement

        liste.append(self)