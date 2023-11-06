import provinces
import variables

index = {}
activeIndex = {}
liste = []

class Loi():
    
    def __init__(self, nom:str, effets:None, impact:list, positionnement:int,axe:int):
        
        self.nom = nom
        self.effets = effets
        self.impact = impact
        self.positionnement = positionnement
        self.progression = 0
        self.influence = 0
        self.axe = axe - 1
        
        index[self.nom] = self
    
    def __repr__(self):
        return f"{self.nom}"
    
    def application(self):
        
        for prov in provinces.liste:
            for comt in prov.comtes:
                for strate in range(3):
                    print("\n##########\n",comt.nom,"[",comt.ressource.type,"] :\n",comt.positionnement[self.axe])
                    comt.positionnement[self.axe] += self.impact[comt.ressource.type][strate] * comt.population * comt.classes[strate] * variables.facteurDeDeriveDesComtes
                    print("Devenu:",comt.positionnement[self.axe])
                    comt.verifierAllegance()
    
    def checkProgression(self,seuil:int) -> bool:
        
        if self.progression > seuil:
            
            self.progression += 1
            
            return True
        
        return False
    
    def recherche(self,influence:int):
        """Phase de recherche pour débloquer la loi sur l'arbre"""
        
        self.influence += influence
        
        self.checkProgression(variables.seuilProgressionRecherche)
    
    def soutienPolitique(self,influence:int):
        """Assignation des avis des personnages vis-à-vis de la loi et influence sur ceux-ci"""
        
        self.influence += influence
        
        self.checkProgression(variables.seuilProgressionPolitique)
    
    def lobbying(self,influence:int):
        """Compromis et changement de loi pour les groupes d'intérêts"""
        
        self.influence += influence
        
        self.checkProgression(variables.seuilProgressionLobbying)
    
    def publicite(self,influence:int):
        """Tenatives d'amélioration de l'impact des lois sur la population afin de changer les opinions des factions"""
        
        self.influence += influence
        
        self.checkProgression(variables.seuilProgressionPublicite)
    
    def manifestations(self,influence:int):
        """Solution extrême si la loi ne fonctionne pas"""
        
        self.influence += influence
        
        self.checkProgression(variables.seuilProgressionManifestations)
    
    def progresser(self,influence:int):
        
        progressionIndex = [self.recherche,self.soutienPolitique,self.lobbying,self.publicite,self.manifestations]
        
        progressionIndex[self.progression](influence)

def creation():
    
    liste.append(Loi("Ordre et Progrès",None,[[0,0,0],[5,10,-1],[3,5,-4]],-50,3))


