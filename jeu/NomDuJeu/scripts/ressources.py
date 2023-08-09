

index = {}
liste = []

class Ressource():

    def __init__(self, nom:str, type:str, valeur:int,prerequis:object=None):

        self.nom = nom
        self.valeur = valeur
        self.prerequis = prerequis
        self.type = {"Primaire":0,"Secondaire":1,"Luxe":2}[type]

        index[self.nom] = self

    def __repr__(self):
        return f"{self.nom}"

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

def creationDeterminee(infos):
    
    for i in range(len(infos)):

        nom = infos[i][0]
        type = infos[i][1]
        valeur = int(infos[i][2])

        if infos[i][3] == " None":
            prerequis = None
        else:
            prerequis = index[infos[i][3]]

        index[nom] = Ressource(nom,type,valeur,prerequis)

    print(index)


