import variables

def sgn(x):

    return x/abs(x)

def CalculsProbabilites(x:int,L:int):

    d = L - sgn(L) * variables.distancePointNul
    S = variables.seuilMaximumAcceptation

    #print("Chance Succès: ",min(S, ((S*(x-d)) / (L - d))  *  ((L - sgn(L)*101) / (x - sgn(L)*101))))

    return min(S, ((S*(x-d)) / (L - d))  *  ((L - sgn(L)*101) / (x - sgn(L)*101)))

print(CalculsProbabilites(9,10))