import random
import fonctions
import variables

liste = []

class Pouvoir():

    def __init__(self,nom:str,poste:int,nomination:str):
        self.nom = nom
        self.poste = poste
        self.nomination = nomination
        self.membres = []

class Legislatif(Pouvoir):

    pass

class Executif(Pouvoir):

    pass

class Judiciaire(Pouvoir):

    pass

class Gouvernement():

    def __init__(self,legislatif:object,executif:object,judiciaire:object):
        self.pouvoirs = [legislatif,executif,judiciaire]

def creation(legislatif:object,executif:object,judiciaire:object):

    global gouvernement
    
    gouvernement = Gouvernement(legislatif,executif,judiciaire)

def propositionLegislatif(loi:object):

    acceptance = 0

    for i in gouvernement.pouvoirs[0].membres:
        #print("Personnage:",i.faction.positionnement[loi.axe],", Loi:",loi.positionnement)
        if random.randint(0,100) <= fonctions.CalculsProbabilites(i.faction.positionnement[loi.axe],loi.positionnement) * variables.facteurAcceptationLegislatif:
            acceptance += 1
        else:
            acceptance -= 1

    if acceptance > 0:
        print("LAW APPROVED BY LEGISLATIVE POWER : ", acceptance)
        return(True)
    else:
        print("LAW REJECTED BY LEGISLATIVE POWER : ", acceptance)
        return(False)

def propositionExecutif(loi:object):

    acceptance = 0

    for i in gouvernement.pouvoirs[0].membres:
        #print("Personnage:",i.faction.positionnement[loi.axe],", Loi:",loi.positionnement)
        if random.randint(0,100) <= fonctions.CalculsProbabilites(i.faction.positionnement[loi.axe],loi.positionnement) * variables.facteurAcceptationExecutif:
            acceptance += 1
        else:
            acceptance -= 1

    if acceptance > 0:
        print("LAW APPROVED BY EXECUTIVE POWER : ", acceptance)
        return(True)
    else:
        print("LAW REJECTED BY EXECUTIVE POWER : ", acceptance)
        return(False)

def propositionJudiciaire(loi:object):

    acceptance = 0

    for i in gouvernement.pouvoirs[0].membres:
        #print("Personnage:",i.faction.positionnement[loi.axe],", Loi:",loi.positionnement)
        if random.randint(0,100) <= fonctions.CalculsProbabilites(i.faction.positionnement[loi.axe],loi.positionnement) * variables.facteurAcceptationJudiciaire:
            acceptance += 1
        else:
            acceptance -= 1

    if acceptance > 0:
        print("LAW APPROVED BY JUDICIARY POWER : ", acceptance)
        return(True)
    else:
        print("LAW REJECTED BY JUDICIARY POWER : ", acceptance)
        return(False)