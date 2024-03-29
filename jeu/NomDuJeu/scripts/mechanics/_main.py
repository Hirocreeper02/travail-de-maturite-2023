import initialisation
import provinces
import gouvernements
import lois
import factions
import finances
import debug
import variables

import save

import time


def propositionLoi(loi:object):

    print("\n##########")

    if (gouvernements.propositionLegislatif(loi) and gouvernements.propositionExecutif(loi) and gouvernements.propositionJudiciaire(loi)):

        print("LOI", loi.nom,"ACCEPTEE")

        loi.application()

        return True

    else:

        print("LOI", loi.nom,"REJETEE")

        return False   

def testLoi(nombreEssais:int):

    test = sum(
        1
        for _ in range(nombreEssais)
        if (propositionLoi(lois.index["Ordre et Progrès"]))
    )
    print(test / (nombreEssais / 100) , "%")

#propositionLoi(lois.index["Ordre et Progrès"])


#lois.index["Ordre et Progrès"].application()

#finances.collecterImpots()

#for i in factions.liste:
#    print(i.nom,":",i.finances,"$")

#comtes.list[0].verifierAllegance()

def routine():

    tick = 0

    #while True:
    while True:

        time.sleep(variables.tickSpeed)

        debug.afficherFonctions(tick)
        
        # FONCTIONS A # 

        # FONCTIONS B #

        if tick % variables.facteurFonctionsB == 0:

            pass

        # FONCTIONS C #

        if tick % variables.facteurFonctionsC == 0:

            finances.collecterImpots()

        tick += 1

def start():

    initialisation.creation(4,15,5,20)

    debug.afficherStart()

    # save.save()

    import sys
    sys.path.append('scripts/engine')
    import mainEngine

start()