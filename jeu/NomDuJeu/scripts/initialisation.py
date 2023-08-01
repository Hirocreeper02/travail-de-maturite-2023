import factions
import graphismes
import lois
import provinces
import ressources
import utopies
import gouvernements
import files

def creationPreetablies():

    ressources.creation()

    lois.creation()

    utopies.creation()

def creation(noFactions:int, noPersonnages:int, noProvinces:int, noComtes:int):
    if noFactions > noPersonnages or noProvinces > noComtes:
        return False
    
    creationPreetablies()

    factions.creation(noFactions,noPersonnages)

    provinces.creation(noProvinces,noComtes)
    


"""
def creationExemple():

    creationPreetablies()

    factions.liste.append(factions.Faction("Profs d'Informatique", utopies.index["Technocratie"], [-40,-75, -25, -80], "Il nous faut impérativement de nouvelles souris"))

    personnages.liste.append(personnages.Personnage("David DaSilva", "Profs d'Informatique", 72, 30))
    personnages.liste.append(personnages.Personnage("Raphaël Mérot", "Profs d'Informatique", 48, 30))

    factions.liste.append(factions.Faction("Profs de MEP", None, [40, 55, 75, 95],"On s’est remis à croire en Dieu à partir de Planck"))

    personnages.liste.append(personnages.Personnage("Jérémie Borel", "Profs de MEP", 54, 30))
    personnages.liste.append(personnages.Personnage("Jérôme DuFour", "Profs de MEP", 53, 30))
    personnages.liste.append(personnages.Personnage("Grégoire Favre", "Profs de MEP", 46, 30))
    
    factions.liste.append(factions.Faction("Profs de Français", None, [80, -75, -95, -25],"On veut juste lire en paix... tout le temps et partout..."))

    personnages.liste.append(personnages.Personnage("Vincent Verselles", "Profs de Français", 68, 30))
    personnages.liste.append(personnages.Personnage("Guillaume Schilt", "Profs de Français", 32, 30))
    personnages.liste.append(personnages.Personnage("Murielle Matthey", "Profs de Français", 57, 30))

    factions.liste.append(factions.Faction("Profs de Sport", None, [-70, -40, -95, -20],"Louis XIV ne faisait clairement pas assez de sport!"))

    personnages.liste.append(personnages.Personnage("Thomas Daetwyler", "Profs de Sport", 54, 30))
    personnages.liste.append(personnages.Personnage("Diana Mödder", "Profs de Sport", 27, 30))
    personnages.liste.append(personnages.Personnage("Léonard Berner", "Profs de Sport", 16, 30))

    for i in range(3):
        print("\n##########\n",factions.liste[i].nom,factions.liste[i].positionnement,":")
        for object in factions.liste[i].membres:
            print(object.nom)

    provinces.liste.append(provinces.Province("Bâtiment A",factions.index["Profs d'Informatique"]))

    provinces.index["Bâtiment A"].comtes.append(comtes.Comte("A11",factions.index["Profs d'Informatique"],ressources.index["Fer"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment A"].comtes.append(comtes.Comte("A12",factions.index["Profs d'Informatique"],ressources.index["Nourriture"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment A"].comtes.append(comtes.Comte("A13",factions.index["Profs d'Informatique"],ressources.index["Fer"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment A"].comtes.append(comtes.Comte("A14",factions.index["Profs d'Informatique"],ressources.index["Bijouterie"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment A"].comtes.append(comtes.Comte("A15",factions.index["Profs d'Informatique"],ressources.index["Ficelle"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment A"].comtes.append(comtes.Comte("A16",factions.index["Profs d'Informatique"],ressources.index["Or"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment A"].comtes.append(comtes.Comte("A17",factions.index["Profs d'Informatique"],ressources.index["Armes"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment A"].comtes.append(comtes.Comte("A18",factions.index["Profs d'Informatique"],ressources.index["Nourriture"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment A"].comtes.append(comtes.Comte("A1T",factions.index["Profs d'Informatique"],ressources.index["Nourriture"], 100,[33,33,33],[0,0,0,0]))

    provinces.liste.append(provinces.Province("Bâtiment B",factions.index["Profs de MEP"]))

    provinces.index["Bâtiment B"].comtes.append(comtes.Comte("B41",factions.index["Profs de MEP"],ressources.index["Fer"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment B"].comtes.append(comtes.Comte("B42",factions.index["Profs de MEP"],ressources.index["Laine"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment B"].comtes.append(comtes.Comte("B44",factions.index["Profs de MEP"],ressources.index["Armes"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment B"].comtes.append(comtes.Comte("B45",factions.index["Profs de MEP"],ressources.index["Or"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment B"].comtes.append(comtes.Comte("Local",factions.index["Profs de MEP"],ressources.index["Nourriture"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment B"].comtes.append(comtes.Comte("WC",factions.index["Profs de MEP"],ressources.index["Diamant"], 100,[33,33,33],[0,0,0,0]))

    provinces.liste.append(provinces.Province("Bâtiment C",factions.index["Profs de Français"]))

    provinces.index["Bâtiment C"].comtes.append(comtes.Comte("C21",factions.index["Profs de Français"],ressources.index["Laine"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment C"].comtes.append(comtes.Comte("C22",factions.index["Profs de Français"],ressources.index["Armes"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment C"].comtes.append(comtes.Comte("C23",factions.index["Profs de Français"],ressources.index["Fer"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment C"].comtes.append(comtes.Comte("C24",factions.index["Profs de Français"],ressources.index["Nourriture"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment C"].comtes.append(comtes.Comte("C25",factions.index["Profs de Français"],ressources.index["Habits"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment C"].comtes.append(comtes.Comte("Salle des Maîtres",factions.index["Profs de Français"],ressources.index["Ficelle"], 100,[33,33,33],[0,0,0,0]))

    provinces.liste.append(provinces.Province("Bâtiment de Sport",factions.index["Profs de Sport"]))

    provinces.index["Bâtiment de Sport"].comtes.append(comtes.Comte("Salle des Profs",factions.index["Profs de Sport"],ressources.index["Diamant"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment de Sport"].comtes.append(comtes.Comte("Salle I",factions.index["Profs de Sport"],ressources.index["Habits"], 100,[33,33,33],[0,0,0,0]))
    provinces.index["Bâtiment de Sport"].comtes.append(comtes.Comte("Salle II",factions.index["Profs de Sport"],ressources.index["Nourriture"], 100,[33,33,33],[0,0,0,0]))

    for i in provinces.liste:
        print("\n##########\n",i.nom,":")
        for j in i.comtes:
            print(j.nom,",",j.faction.nom,": ",j.ressource.nom)

    legislatif = gouvernements.Legislatif("Conseil de Direction",4,None)
    executif = gouvernements.Executif("Directeur",1,None)
    judiciaire = gouvernements.Judiciaire("Assemblée des Enseignants",6,None)

    gouvernements.creation(legislatif,executif,judiciaire)

    print("\n##########")
    for i in gouvernements.gouvernement.pouvoirs:
        print(i.nom,", pourvoyant ",i.poste,"postes, avec une nomination par",i.nomination)

    gouvernements.gouvernement.pouvoirs[0].membres.append(personnages.index["David DaSilva"])
    gouvernements.gouvernement.pouvoirs[0].membres.append(personnages.index["Vincent Verselles"])
    gouvernements.gouvernement.pouvoirs[0].membres.append(personnages.index["Guillaume Schilt"])
    gouvernements.gouvernement.pouvoirs[0].membres.append(personnages.index["Jérémie Borel"])

    gouvernements.gouvernement.pouvoirs[1].membres.append(personnages.index["Thomas Daetwyler"])

    gouvernements.gouvernement.pouvoirs[2].membres.append(personnages.index["Raphaël Mérot"])
    gouvernements.gouvernement.pouvoirs[2].membres.append(personnages.index["Murielle Matthey"])
    gouvernements.gouvernement.pouvoirs[2].membres.append(personnages.index["Diana Mödder"])
    gouvernements.gouvernement.pouvoirs[2].membres.append(personnages.index["Léonard Berner"])
    gouvernements.gouvernement.pouvoirs[2].membres.append(personnages.index["Jérôme DuFour"])
    gouvernements.gouvernement.pouvoirs[2].membres.append(personnages.index["Grégoire Favre"])

    #print("factions: ",factions.index)
    #print("lois: ",lois.index)
    #print("personnages ",personnages.index)
    #print("provinces: ",provinces.index)
    #print("ressources: ",ressources.index)
    #print("utopies: ",utopies.index)

"""
