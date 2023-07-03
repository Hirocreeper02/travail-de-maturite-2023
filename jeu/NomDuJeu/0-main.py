import initialisation
import factions
import gouvernements
import lois
import factions

initialisation.creationExemple()

def propositionLoi(loi:object):

    print("\n##########")

    if (gouvernements.propositionLegislatif(loi) and gouvernements.propositionExecutif(loi) and gouvernements.propositionJudiciaire(loi)):

        print("LOI", loi.nom,"ACCEPTEE")

        return True

    else:

        print("LOI", loi.nom,"REJETEE")

        return False   

def testLoi(nombreEssais:int):
    test = 0

    for i in range(nombreEssais):

        if(propositionLoi(lois.index["Ordre et Progrès"])):
            test += 1

    print(test / (nombreEssais / 100) , "%")

testLoi(1000)