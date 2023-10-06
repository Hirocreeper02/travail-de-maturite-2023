import fonctions
import factions
import files

index = {}
indexComtes = {}

class Province():
    
    def __init__(self, nom:str, faction:object):
        
        self.nom = nom
        self.faction = faction
        self.comtes = {}
        self.voisins = []
        self.foyer = []
        
        #index[self.nom] = self
    
    def __repr__(self):
        return f"{self.nom}"

class Comte():
    
    def __init__(self, nom:str, faction:object, ressource:object, population:int, classes:list, positionnement:list):
        
        self.nom = nom
        self.faction = faction
        self.ressource = ressource
        self.population = population
        self.classes = classes
        self.positionnement = positionnement
        self.voisins = set()
        self.foyer = []
        
        for i in self.classes:
            i = i / 100
    
    def __repr__(self):
        return f"{self.nom}"
    
    def verifierAllegance(self):
        
        print("")
        choix = [self.faction,fonctions.comparerGraphes(self.faction,self)]
        print("")
        
        for faction in factions.liste:
            difference = fonctions.comparerGraphes(faction,self)
            if difference < choix[1]:
                choix = [faction,difference]
        
        self.faction = choix[0]
        
        print("\nLe comté",self.nom,"a décidé d'accorder sa fidélité à la faction:",self.faction.nom,"\n")

def creation(noProvinces:int,noComtes:int):

    global index
    global indexComtes
    
    for _ in range(noProvinces):
        
        while True:
            nom = files.nomAleatoire(files.index["provinces.txt"])
            
            if nom != index.keys():
                break
        
        print("\033[0;31m",factions.index,"<- in provinces.py","\033[0;37m")
        
        faction = fonctions.elementAleatoire(factions.index)
        
        index[nom] = Province(nom,faction)
    
    for _ in range(noComtes):
            
        while True:
            nomComte = files.nomAleatoire(files.index["comtes.txt"])
                
            if nomComte not in indexComtes.keys():
                break
        
        ressource = None
        
        population = 100
        
        classes = [33,33,33]
        
        positionnement = [0,0,0,0]
        
        indexComtes[nomComte] = Comte(nomComte,faction,ressource,population,classes,positionnement)
    
    print("indexComtes:",indexComtes)