import comtes
import factions
import graphismes
import lois
import personnages
import provinces
import ressources
import utopies
import gouvernements

def creationPreetablies():

    utopies.creation()

    ressources.creation()

    lois.creation()

    gouvernements.creation()

def creation(noFactions:int, noPersonnages:int, noProvinces:int, noComtes:int):
    if noFactions > noPersonnages or noProvinces > noComtes:
        return False
    
    creationPreetablies()

    # Créer des factions et comtés aléatoires #

def creationExemple():

    creationPreetablies()

    factions.liste.append(factions.Faction("Profs d'Informatique", utopies.liste[0], [-75, -25, -80, 40],"Il nous faut impérativement de nouvelles souris"))

    personnages.liste.append(personnages.Personnage("David DaSilva", factions.liste[0], 72, 30))
    personnages.liste.append(personnages.Personnage("Raphael Merot", factions.liste[0], 48, 30))

    factions.liste.append(factions.Faction("Profs de MEP", None, [55, 75, 95, -40],"On s’est remis à croire en Dieu à partir de Planck"))

    personnages.liste.append(personnages.Personnage("Jérémie Borel", factions.liste[1], 54, 30))
    personnages.liste.append(personnages.Personnage("Jérôme DuFour", factions.liste[1], 53, 30))
    personnages.liste.append(personnages.Personnage("Grégoire Favre", factions.liste[1], 46, 30))
    
    factions.liste.append(factions.Faction("Profs de Français", None, [-75, -95, -25, -80],"On veut juste lire en paix... tout le temps et partout..."))

    personnages.liste.append(personnages.Personnage("Vincent Verselles", factions.liste[2], 68, 30))
    personnages.liste.append(personnages.Personnage("Guillaume Schilt", factions.liste[2], 32, 30))
    personnages.liste.append(personnages.Personnage("Murielle Matthey", factions.liste[2], 57, 30))

    factions.liste.append(factions.Faction("Profs de Sport", None, [-40, -95, -20, 70],"Louis XIV ne faisait clairement pas assez de sport!"))

    personnages.liste.append(personnages.Personnage("Thomas Daetwyler", factions.liste[3], 54, 30))
    personnages.liste.append(personnages.Personnage("Diana Mödder", factions.liste[3], 27, 30))
    personnages.liste.append(personnages.Personnage("Léonard Berner", factions.liste[3], 16, 30))

    for i in range(3):
        print("\n##########\n",factions.liste[i].nom,":")
        for object in factions.liste[i].membres:
            print(object.nom)

    provinces.liste.append(provinces.Province("Bâtiment A",factions.liste[0]))

    provinces.liste[0].comtes.append(comtes.Comte("A11",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("A12",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("A13",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("A14",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("A15",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("A16",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("A17",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("A18",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("A1T",factions.liste[0],None, 100,[],[0,0,0,0]))

    provinces.liste.append(provinces.Province("Bâtiment B",factions.liste[1]))

    provinces.liste[0].comtes.append(comtes.Comte("B41",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("B42",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("B44",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("B45",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("Local",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("WC",factions.liste[0],None, 100,[],[0,0,0,0]))

    provinces.liste.append(provinces.Province("Bâtiment C",factions.liste[2]))

    provinces.liste[0].comtes.append(comtes.Comte("C21",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("C22",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("C23",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("C24",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("C25",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("Salle des Maîtres",factions.liste[0],None, 100,[],[0,0,0,0]))

    provinces.liste.append(provinces.Province("Bâtiment de Sport",factions.liste[3]))

    provinces.liste[0].comtes.append(comtes.Comte("Salle des Profs",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("Salle I",factions.liste[0],None, 100,[],[0,0,0,0]))
    provinces.liste[0].comtes.append(comtes.Comte("Salle II",factions.liste[0],None, 100,[],[0,0,0,0]))