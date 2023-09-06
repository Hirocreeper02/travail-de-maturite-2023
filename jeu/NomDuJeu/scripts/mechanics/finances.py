import provinces
import variables
import factions
import debug

def collecterImpots():

    for key in provinces.index:
            for element in provinces.index[key].comtes:

                comt = provinces.index[key].comtes[element]

                for strate in range(3):
                    comt.faction.finances += comt.population * comt.classes[strate] * variables.tauxImposition

    debug.afficherFinances()
                