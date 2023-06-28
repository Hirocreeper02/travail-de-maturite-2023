import comtes
import factions
import graphismes
import lois
import personnages
import province
import ressource
import utopies

def creationUtopies():

    utopies.liste.append(utopies.Utopie("Technocratie",None,None,[50,-50,-100,-50]))

def creation(noFactions:int, noPersonnages:int, noProvinces:int, noComtes:int):
    if noFactions > noPersonnages or noProvinces > noComtes:
        return False
    
    creationUtopies

    # Créer des factions et comtés aléatoires #

def creationExemple():

    creationUtopies()

    factions.liste.append(factions.Faction("Profs d'Informatique", utopies.liste[0], [-75, -25, -80, 40],"Il nous faut impérativement de nouvelles souris"))

    print("########## ",factions.liste[0].nom, " ##########")

    personnages.liste.append(personnages.Personnage("David DaSilva", factions.liste[0], 72, 30))
    personnages.liste.append(personnages.Personnage("Raphael Merot", factions.liste[0], 48, 30))
    
    factions.liste.append(factions.Faction("Profs de Français", None, [-75, -95, -25, -80],"On veut juste lire en paix... tout le temps et partout..."))

    print("########## ",factions.liste[1].nom, " ##########")

    personnages.liste.append(personnages.Personnage("Vincent Verselles", factions.liste[1], 68, 30))
    personnages.liste.append(personnages.Personnage("Guillaume Schilt", factions.liste[1], 32, 30))
    personnages.liste.append(personnages.Personnage("Murielle Matthey", factions.liste[1], 57, 30))

    factions.liste.append(factions.Faction("Profs de Sport", None, [-40, -95, -20, 70],"Louis XIV ne faisait clairement pas assez de sport!"))

    print("########## ",factions.liste[2].nom, " ##########")

    personnages.liste.append(personnages.Personnage("Thomas Daetwyler", factions.liste[2], 54, 30))
    personnages.liste.append(personnages.Personnage("Diana Mödder", factions.liste[2], 27, 30))
    personnages.liste.append(personnages.Personnage("Léonard Berner", factions.liste[2], 16, 30))

    factions.liste.append(factions.Faction("Profs de MEP", None, [55, 75, 95, -40],"On s’est remis à croire en Dieu à partir de Planck"))

    print("########## ",factions.liste[3].nom, " ##########")

    personnages.liste.append(personnages.Personnage("Jérémie Borel", factions.liste[3], 54, 30))
    personnages.liste.append(personnages.Personnage("Jérôme DuFour", factions.liste[3], 53, 30))
    personnages.liste.append(personnages.Personnage("Grégoire Favre", factions.liste[3], 46, 30))

    print("########## ",factions.liste[4].nom, " ##########")
    print("########## ",factions.liste[6].nom, " ##########")

    print("\n\n\n")

    for i in range(len(factions.liste)):
        print(factions.liste[i].nom)

    #for i in range(3):
    #    print("\n##########\n",factions.liste[i].nom,":")
    #    for object in factions.liste[i].membres:
    #        print(object.nom)