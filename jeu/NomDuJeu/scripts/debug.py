import factions
import provinces
import variables
import files

from datetime import datetime

debug = True
log = False

### MAIN ###

def logStart():

    if log:

        display = "\n\n######################################################\n########## = [" + str(datetime.now()) + "] = ##########\n#####################################################"

        f = open(files.index["log.txt"], "a")

        f.write(display)

        f.close()

def afficher(display):
    
    if debug:

        print(display)

    if log:

        f = open(files.index["log.txt"], "a")

        f.write(display)

        f.close()

### START ###

def afficherFactions():
    
    
    print("  F\u0332a\u0332c\u0332t\u0332i\u0332o\u0332n\u0332s\u0332:\u0332")

    display = ""

    for key in factions.index:
        display = display + "   - " + factions.index[key].nom +": "+ str(factions.index[key].utopie.nom) + ", " + str(len(factions.index[key].membres)) + " membres \n"

    afficher(display)

def afficherPersonnages():
    
    display = "  P\u0332e\u0332r\u0332s\u0332o\u0332n\u0332n\u0332a\u0332g\u0332e\u0332s\u0332:\u0332\n"

    for key in factions.index:
        for i in range(len(factions.index[key].membres)):
            display = display + "   - [" + factions.index[key].nom +"] "+ factions.index[key].membres[i].nom + ", " + str(factions.index[key].membres[i].influence) + " d'influence \n"

    afficher(display)

def afficherProvinces():

    display = "  P\u0332r\u0332o\u0332v\u0332i\u0332n\u0332c\u0332e\u0332s\u0332:\u0332\n"

    for key in provinces.index:
        display = display + "   - " + provinces.index[key].nom +" ["+ provinces.index[key].faction.nom + "]\n"

    afficher(display)

def afficherComtes():
    
    display = "  C\u0332o\u0332m\u0332t\u0332é\u0332s\u0332:\u0332\n"

    for key in provinces.index:
        for element in provinces.index[key].comtes:
            display = display + "   - "+ provinces.index[key].comtes[element].nom + " de " + provinces.index[key].nom + ": " + str(provinces.index[key].comtes[element].population) + " habitants \n"

    afficher(display)

def afficherStart():
    
    logStart()
    
    afficher("\n\nSTART| PHASE D'INITIALISATION \n")
    
    afficherFactions()

    afficherPersonnages()

    afficherProvinces()

    afficherComtes()

### ROUTINE ###

def afficherFonctions(tick):
    
        
    display = str(tick)+"| FONCTIONS A"

    if tick % variables.facteurFonctionsB == 0:

        display = display + ", FONCTIONS B"
        
    if tick % variables.facteurFonctionsC == 0:

        display = display + ", FONCTIONS C"

    afficher(display + "\n")

def afficherFinances():
    
    display = "  F\u0332i\u0332n\u0332a\u0332n\u0332c\u0332e\u0332s\u0332:\u0332\n"

    for key in factions.index:
        display = display + "   - " + factions.index[key].nom +": "+ str(factions.index[key].finances) + " $ \n"

    afficher(display)