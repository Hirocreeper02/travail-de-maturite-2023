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

    def __repr__(self):
        return f"{self.nom}"

def creation():

    liste.append(Utopie(
        nom = "Technocratie",
        structure = [[100,None],[20,None],[12,None]],
        lois = [lois.index["Ordre et Progrès"]],
        positionnement = [50,-50,-100,-50]
        )
    )