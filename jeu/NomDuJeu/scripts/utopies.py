

index = {}
liste = []

class Utopie():

    def __init__(self, nom:str, structure:object, lois:list, positionnement:list):

        self.nom = nom
        self.structure = structure
        self.lois = lois
        self.positionnement = positionnement

        index[self.nom] = self

def creation():

    liste.append(Utopie("Technocratie",None,None,[50,-50,-100,-50]))