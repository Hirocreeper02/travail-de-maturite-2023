import provinces
import comtes
import variables
import factions

def collecterImpots():

    for prov in provinces.liste:
            for comt in prov.comtes:
                for strate in range(3):
                    comt.faction.finances += comt.population * comt.classes[strate] * variables.tauxImposition
                