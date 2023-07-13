import lois

index = {}
liste = []

class Utopie():

    def __init__(self, nom:str, structure:list, lois:list, positionnement:list):

        self.nom = nom
        self.structure = structure # [[N° Postes, Election],[N° Postes, Election],[N° Postes, Election]]
        self.lois = lois
        self.positionnement = positionnement

        index[self.nom] = self

def creation():

    liste.append(Utopie("Technocratie",[[100,None],[20,None],[12,None]],[lois.index["Ordre et Progrès"]],[50,-50,-100,-50]))