import utopies
import files
import fonctions

index = {}
liste = []

nameIndex = {utopies.index["Technocratie"]:"technocratie.txt"}
mottoIndex = {utopies.index["Technocratie"]:"mottos_technocratie.txt"}

class Faction():

    def __init__(self, nom:str, utopie:object, positionnement:list, motto:str):

        self.nom = nom
        self.positionnement = positionnement
        self.motto = motto
        self.membres = []
        self.utopie = utopie
        self.finances = 0

        index[self.nom] = self

def creation(nombreDeFactions):

    for i in range(nombreDeFactions):

        utopie = fonctions.elementAleatoire(index)

        while True:
            nom = files.nomAleatoire(nameIndex[utopie])

            if nom != index.keys():
                break

        positionnement = [0,0,0,0]

        motto = mottoIndex[utopie]

        index[nom] = Faction(nom,utopie,positionnement,motto)