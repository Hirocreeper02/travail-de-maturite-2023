

index = {}
liste = []

class Ressource():

    def __init__(self, nom:str, type:str, valeur:int,prerequis:object=None):

        self.nom = nom
        self.valeur = valeur
        self.prerequis = prerequis
        self.type = {"Primaire":0,"Secondaire":1,"Luxe":2}[type]

        index[self.nom] = self

def creation():

    liste.append(Ressource("Fer","Primaire",1))
    liste.append(Ressource("Ficelle","Primaire",1))
    liste.append(Ressource("Diamant","Primaire",1))
    liste.append(Ressource("Or","Primaire",1))
    liste.append(Ressource("Nourriture","Primaire",1))

    liste.append(Ressource("Armes","Secondaire",1,liste[0]))
    liste.append(Ressource("Laine","Secondaire",1,liste[1]))
    liste.append(Ressource("Bijouterie","Luxe",1,liste[2]))

    liste.append(Ressource("Habits","Secondaire",1,liste[6]))
