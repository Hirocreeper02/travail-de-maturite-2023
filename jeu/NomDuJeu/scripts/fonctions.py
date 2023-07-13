import variables
import comtes
import factions

def sgn(x):

    return x/abs(x)

def CalculsProbabilites(x:int,L:int):

    d = L - sgn(L) * variables.distancePointNul
    S = variables.seuilMaximumAcceptation

    #print("Chance Succès: ",min(S, ((S*(x-d)) / (L - d))  *  ((L - sgn(L)*101) / (x - sgn(L)*101))))

    return min(S, ((S*(x-d)) / (L - d))  *  ((L - sgn(L)*101) / (x - sgn(L)*101)))

print("Chances de Succès de la Loi: ",CalculsProbabilites(9,10))

def comparerGraphes(a,b):

    difference = 0

    for i in range(4):

        difference += abs(a.positionnement[i] - b.positionnement[i])

    print("La différence entre", a.nom, "et", b.nom,"est:",difference)

    return difference