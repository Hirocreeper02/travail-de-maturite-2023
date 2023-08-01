import variables

import random

def sgn(x):

    return x/abs(x)

def CalculsProbabilites(x:int,L:int):

    d = L - sgn(L) * variables.distancePointNul
    S = variables.seuilMaximumAcceptation

    #print("Chance Succès: ",min(S, ((S*(x-d)) / (L - d))  *  ((L - sgn(L)*101) / (x - sgn(L)*101))))

    return min(S, ((S*(x-d)) / (L - d))  *  ((L - sgn(L)*101) / (x - sgn(L)*101)))

#print("Chances de Succès de la Loi: ",CalculsProbabilites(9,10))

def comparerGraphes(a,b):

    difference = 0

    for i in range(4):

        difference += abs(a.positionnement[i] - b.positionnement[i])

    #print("La différence entre", a.nom, "et", b.nom,"est:",difference)

    return difference

def elementAleatoire(index:dict):

    res = random.choice(list(index.items()))

    return(index[res[0]])

def repartitionInegale(dividende:int,diviseur:int):

    quotients = []

    for i in range(diviseur):

        while True:

            #Important de garder la condition de NoFaction > NoPersonnages dans initialisiation.py

            quotientTemporaire = random.randint(1,dividende)

            if quotientTemporaire not in quotients:
                
                quotients.append(quotientTemporaire)

                break

    quotients = sorted(quotients,reverse=True) #Organisation en ordre décroissant

    for i in range(len(quotients)): #Calcul du ∂ entre chacune des valeurs
        if i < (len(quotients) - 1):
            quotients[i] -= quotients[i+1]

    return quotients

