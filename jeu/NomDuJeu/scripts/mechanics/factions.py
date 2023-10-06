import utopies
import files
import fonctions
import lois
import variables

import random

index = {}

nameIndex = {}
mottoIndex = {}

class Faction():

    def __init__(self, nom:str, utopie:object, positionnement:list, motto:str, finances:int = 0, membres:list = []):
        
        self.nom = nom
        self.positionnement = positionnement
        self.motto = motto
        self.membres = membres
        self.utopie = utopie
        self.finances = finances
    
    def __repr__(self):
        return f"{self.nom}"
    
    def AI(self):
        """Procédure de décision autonome des factions pouvant...
            - Proposer une Loi
            - Proposer un Changement de la Constitution
            - Investir dans une Région
        """
        
        pass

class Personnage():
    
    def __init__(self, nom:str, faction:str, influence:int, age:int):
        
        self.nom = nom
        self.positionnement = []
        self.opinions = {}
        self.votes = {}
        self.faction = faction
        self.influence = influence
        self.age = age
    
    def __repr__(self):
        return f"{self.nom}"
    
    def assassiner(self,cible:object):
        """Tuer... aïe..."""
        print("AAAAAAAAAHHHHH")

    def AI(self):
        """Procédure de décision autonome des personnages pouvant...
            - Assassiner un Personnage
            - Se Rapprocher d'un Personnage
            - Corrompre un Personnage
            - Convaincre un Personnage
            - Changer sa Loyauté
        """
        
        for loi in lois.activeIndex():
            
            distance = 10**100
            
            # PROGESSER LOI #
            if fonctions.comparerGraphes(self.positionnement,loi.positionnement,loi.axe) * (loi.positionnement + 1) < distance:
                
                loi.progresser(self.influence)
        
        for faction in index: 
            
            for cible in faction.membres:
                
                # ASSASSINER #
                if self.opinions[cible] < variables.seuilAssassinat:
                    
                    self.assassiner(cible)
                
                # SE RAPPROCHER #
                if abs(cible.influence - self.influence) <= variables.seuilInfluenceRapprochement:
                    
                    self.rapprocher(cible)
                
                # CORROMPRE #
                if abs(cible.influence - self.influence) <= variables.seuilInfluenceCorruption and faction.argent >= variables.seuilArgentCorruption:
                    
                    self.corrompre(cible)
                
                # CHANGE LOYALTY #
                if fonctions.comparerGraphes(self.positionnement,cible.positionnement):
                    
                    self.faction = cible.faction

def creation(nombreDeFactions,nombreDePersonnages):
    
    # CREATION FACTIONS #
    
    nameIndex = {utopies.index["Technocratie"]:files.index["technocratisme.txt"]}
    mottoIndex = {utopies.index["Technocratie"]:"mottos_technocratisme.txt"}
    
    for _ in range(nombreDeFactions):
        
        utopie = fonctions.elementAleatoire(utopies.index)
        
        while True:
            nom = files.nomAleatoire(nameIndex[utopie])
            
            if nom != index.keys():
                break
        
        positionnement = [0,0,0,0]
        
        motto = mottoIndex[utopie]
        
        index[nom] = Faction(nom,utopie,positionnement,motto)
    
    print("\033[0;31m",index,"<- in factions.py","\033[0;37m")
    
    # CREATION PERSONNAGES #
    
    repartition = fonctions.repartitionInegale(nombreDePersonnages,nombreDeFactions)
    
    for i, key in enumerate(index):
        
        for _ in range(repartition[i]):
            while True:
                nom = files.nomAleatoire(files.index["prenoms_masculins.txt"])+" "+files.nomAleatoire(files.index["noms.txt"])
                
                if nom != index.keys:
                    break
            
            influence = random.randint(1,100)
            
            age = random.randint(20,80)
            
            index[key].membres.append(Personnage(nom,index[key],influence,age))

def creationDeterminee(infos):
    
    for i in range(len(infos)):
        
        nom = infos[i][0]
        positionnement = infos[i][1]
        motto = infos[i][2]
        membres = infos[i][3]
        utopie = utopies.index[infos[i][4]]
        finances = int(infos[i][5])
        
        index[nom] = Faction(nom,utopie,positionnement,motto,finances,membres)