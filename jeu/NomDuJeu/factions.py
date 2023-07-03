import utopies

index = {}
liste = []

class Faction():

    def __init__(self, nom:str, utopie:object, positionnement:list, motto:str):

        self.nom = nom
        self.positionnement = positionnement
        self.motto = motto
        self.membres = []
        self.utopie = utopie

        index[self.nom] = self