import factions
import lois
import provinces
import ressources
import utopies
import gouvernements
import files

import sys
sys.path.append('scripts/engine')
import territoire

def creationPreetablies():

    ressources.creation()

    lois.creation()

    utopies.creation()

def creation(noFactions:int, noPersonnages:int, noProvinces:int, noComtes:int):
    if noFactions > noPersonnages or noProvinces > noComtes:
        return False
    
    creationPreetablies()

    factions.creation(noFactions,noPersonnages)

    territoire.creation(noProvinces,noComtes)
