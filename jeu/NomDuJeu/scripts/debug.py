import factions

main = __import__("0-main") # Import de fichier avec des chiffres à l'intérieur

debug = True

def afficherFonctions(tick):
    if debug != True:
        return
        
    display = str(tick)+"| FONCTIONS A"

    if tick % main.facteurFonctionsB == 0:

        display = display + ", FONCTIONS B"
        
    if tick % main.facteurFonctionsC == 0:

        display = display + ", FONCTIONS C"

    print(display)

def afficherFinances():
    if debug != True:
        return
        
    display = ""

    for key in factions.index:
        display = factions.index[key].nom + str(factions.index[key].finances) + "$ \n"

    print(display)