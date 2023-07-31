import factions
import variables

debug = True

### START ###

def afficherFactions():
    if debug != True:
        return
    
    print("  F\u0332a\u0332c\u0332t\u0332i\u0332o\u0332n\u0332s\u0332:\u0332")

    display = ""

    for key in factions.index:
        display = display + "   - " + factions.index[key].nom +": "+ str(factions.index[key].utopie.nom) + ", " + str(len(factions.index[key].membres)) + " membres \n"

    print(display)

def afficherPersonnages():
    if debug != True:
        return
    
    print("  P\u0332e\u0332r\u0332s\u0332o\u0332n\u0332n\u0332a\u0332g\u0332e\u0332s\u0332:\u0332")

    display = ""

    for key in factions.index:
        for i in range(len(factions.index[key].membres)):
            display = display + "   - [" + factions.index[key].nom +"] "+ factions.index[key].membres[i].nom + ", " + str(factions.index[key].membres[i].influence) + " d'influence \n"

    print(display)

def afficherProvinces():
    if debug != True:
        return

def afficherComtes():
    if debug != True:
        return

def afficherStart():
    if debug != True:
        return
    
    print("\n\nSTART| PHASE D'INITIALISATION \n")
    
    afficherFactions()

    afficherPersonnages()

    afficherProvinces()

    afficherComtes()

### ROUTINE ###

def afficherFonctions(tick):
    if debug != True:
        return
        
    display = str(tick)+"| FONCTIONS A"

    if tick % variables.facteurFonctionsB == 0:

        display = display + ", FONCTIONS B"
        
    if tick % variables.facteurFonctionsC == 0:

        display = display + ", FONCTIONS C"

    print(display + "\n")

def afficherFinances():
    if debug != True:
        return
    
    print("  F\u0332i\u0332n\u0332a\u0332n\u0332c\u0332e\u0332s\u0332:\u0332")

    display = ""

    for key in factions.index:
        display = display + "   - " + factions.index[key].nom +": "+ str(factions.index[key].finances) + " $ \n"

    print(display)