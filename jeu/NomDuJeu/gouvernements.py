
liste = []

class Pouvoir():

    def __init__(self,nom:str,poste:int,nomination:str):
        self.nom = nom
        self.poste = poste
        self.nomination = nomination
        self.nominationmembres = []

class Legislatif(Pouvoir):

    pass

class Executif(Pouvoir):

    pass

class Judiciaire(Pouvoir):

    pass

class Gouvernement():

    def __init__(self,legislatif:object,executif:object,judiciaire:object):
        self.legislatif = legislatif
        self.executif = executif
        self.judiciaire = judiciaire

def creation():
    
    liste.append(Legislatif("Dictateur",1,None))

    liste.append(Executif("Dictateur",1,None))

    liste.append(Judiciaire("Dictateur",1,None))