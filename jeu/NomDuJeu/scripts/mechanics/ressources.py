index = {}
liste = []

class Ressource():
    nom:str; type:str; valeur:int; prerequis:object

    def __init__(self, nom:str = "Nom de la ressource", type:str = "Luxe", valeur:int = 1,prerequis:object = None):

        self.nom = nom
        self.valeur = valeur
        self.prerequis = prerequis
        self.type = {"Primaire":0,"Secondaire":1,"Luxe":2}[type]

        index[self.nom] = self

    def __repr__(self):
        return f"{self.nom}"

class RouteCommerciale():
    
    def __init__(self,depart,arrivee):
        
        self.depart = depart
        self.arrivee = arrivee

def creation():
    
    global index
    
    index["Minerai"] = Ressource("Minerai","Primaire",10)
    index["Ficelle"] = Ressource("Ficelle","Primaire",5)
    index["Diamant"] = Ressource("Diamant","Primaire",50)
    index["Or"] = Ressource("Or","Primaire",90)
    index["Nourriture"] = Ressource("Nourriture","Primaire",5)
    
    index["Lingot"] = Ressource("Lingot","Secondaire",40,index["Minerai"])
    index["Tissu"] = Ressource("Tissu","Secondaire",15,index["Ficelle"])
    index["Bijoux"] = Ressource("Bijoux","Luxe",90,index["Diamant"])
    
    index["Armes"] = Ressource("Armes","Secondaire",80,index["Lingot"])
    index["Habits"] = Ressource("Habits","Secondaire",45,index["Tissu"])
    
    print("\033[0;32m",index,"<- in ressources.py","\033[0;37m")

def creationDeterminee(infos):
    
    for i in range(len(infos)):

        nom = infos[i][0]
        type = infos[i][1]
        valeur = int(infos[i][2])

        if infos[i][3] == " None":
            prerequis = None
        else:
            prerequis = index[infos[i][3]]

        index[nom] = Ressource(nom,type,valeur,prerequis)

    print(index)

def chercherRouteCommerciale(comte:object):
    """Utilise l'algorithme de Djikstra pour trouver le chemin le plus court entre le demandeur et le producteur"""
    
    pass

# def calculerRoutesCommerciales():
#     """Vérifie tous les comtés et leur production et redessine les routes commerciales"""
    
#     comtesCelibataires = []
    
#     for province in provinces.index.values():
        
#         for comte in province.indexComtes.values():
            
#             for comteAutres in provinces.indexComtes.values():
                
#                 if comte.prerequis == comteAutres.ressource:
                    
#                     print("Route Interne")
                
#                 else:
                    
#                     comtesCelibataires.append(comte)
    
#     for comte in comtesCelibataires:
        
#         chercherRouteCommerciale(comte)


# IRON ORE: https://www.rawpixel.com/search?page=1&similar=6791486&sort=curated&topic_group=_topics 
# STRING: https://www.google.com/search?q=string&tbm=isch&hl=fr&tbs=il:cl&client=firefox-b-d&sa=X&ved=0CAAQ1vwEahcKEwjQmY3U_-qBAxUAAAAAHQAAAAAQCA&biw=1440&bih=721#imgrc=-aosRoQVtUrlsM 
# DIAMANT: https://pixabay.com/no/photos/edelsten-diamant-brytning-glass-423428/ 
# OR ORE: https://ici.radio-canada.ca/nouvelle/1763411/mines-or-cochrane-hill-beaver-dam-fifteen-mile-stream-nouvelle-ecosse 
# NOURRITURE: https://pxhere.com/fr/photo/1347902
# ARMES: https://pxhere.com/fr/photo/450960
# FER: https://www.facebook.com/174020329413636/photos/a.319526851529649/1878145289001123/?type=3&theater
# LAINE: https://www.istockphoto.com/fr/search/2/image?phrase=morceau+de+tissu
# BIJOUX: https://www.couleurcameleon.ch/cours-1/cours-de-bijoux-de-visage/
# HABITS: https://www.etsy.com/ch/listing/1318180331/herrenhemd-mit-schnurung-xv-jahrhundert