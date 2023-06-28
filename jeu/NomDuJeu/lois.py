

liste = []

class Loi():

    def __init__(self, effets:None, impact:list, positionnement:list):

        self.effets = effets
        self.impact = impact
        self.positionnement = positionnement

        liste.append(self)