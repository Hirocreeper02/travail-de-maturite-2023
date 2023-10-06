from PIL import Image
import random

dimensions = (501,501) # Doivent être impaires

class Labyrinthe():

    def __init__(self,dimensions:tuple,forbiddenWalls:list = set()):

        self.dimensions = dimensions
        self.image = Image.new("RGB",dimensions,(0,0,0))
        self.path = []
        self.start = (1,1)
        self.exit = (dimensions[0]-2,dimensions[1]-2)
        self.forbiddenWalls = forbiddenWalls

    def getNodes(self):
        """Retourne tous les noeuds d'intersection possible des labyrinthes"""

        for x in range(self.image.width):

            if x%2 == 1:

                for y in range(self.image.height):

                    if y%2 == 1:

                        self.image.putpixel((x,y),(137,137,137))

    def getRandomPoint(self):
        """Prend un foyer aléatoire pour le chemin"""

        randomPoint = (0,0)

        while randomPoint[0] % 2 == 0 or randomPoint[1] % 2 == 0:

            randomPoint = (random.randint(0,dimensions[0]-1),random.randint(0,dimensions[1]-1))

        self.image.putpixel(randomPoint,(255,255,255))
        self.path.append(randomPoint)

    def getNeighbourPoint(self):
        """Algorythme de pose des chemin du labyrinthe"""

        while True:

            currentPoint = self.path[-1]
            currentNeighbours = []

            currentNeighbours.append(((currentPoint[0]-2),currentPoint[1]))
            currentNeighbours.append(((currentPoint[0]+2),currentPoint[1]))
            currentNeighbours.append((currentPoint[0],(currentPoint[1]-2)))
            currentNeighbours.append((currentPoint[0],(currentPoint[1]+2)))

            removeList = []

            for point in currentNeighbours:
                
                if (point[0] < 0 or point[0] > dimensions[0] - 1) or (point[1] < 0 or point[1] > dimensions[1] - 1) or (self.image.getpixel(point) == (255,255,255)) or point in self.forbiddenWalls:
                    
                    removeList.append(point)

            for point in removeList:

                currentNeighbours.remove(point)

            if len(currentNeighbours) != 0:

                selectedPoint = currentNeighbours[random.randint(0,len(currentNeighbours)-1)]

                self.path.append(selectedPoint)
                self.image.putpixel(selectedPoint,(255,255,255))
                self.image.putpixel((int((selectedPoint[0] + currentPoint[0]) / 2),int((selectedPoint[1] + currentPoint[1]) / 2)),(255,255,255))

            else:

                self.path.pop()

                if len(self.path) == 0:

                    return False

    def getPossibleWays(self,position:tuple):

        x,y = position

        possibleWays = []

        for xPos in range(x-1,x+2):

            for yPos in range(y-1,y+2):

                if yPos <= self.image.height or yPos <= self.image.width:

                    if self.image.getpixel((xPos,yPos)) == (255,255,255):

                        possibleWays.append((xPos,yPos))

        return possibleWays

    def createLabyrinthe(self):

        self.getNodes()
        self.getRandomPoint()
        self.getNeighbourPoint()



class Explorer():

    def __init__(self,labyrinthe:Labyrinthe,prenom:str = "Guendoline"):

        self.prenom = prenom
        self.labyrinthe = labyrinthe
        self.position = self.labyrinthe.start
        self.path = [self.position]
        

    def explorationArianne(self):

        while True:

            if self.position == self.labyrinthe.exit:

                print("YAY", self.prenom, "MANAGED TO GET OUT OF MY BASEMENT")

                # for i,element in enumerate(self.path):

                #     labyrinthe.image.putpixel(element,(0, 200, 0))
                    
                #     if element != self.path[-1]:

                #         labyrinthe.image.putpixel((int((element[0]+self.path[i+1][0])/2),int((element[1]+self.path[i+1][1])/2)),(0, 200, 0))

                return True
            
            self.labyrinthe.image.putpixel(self.position,(112,112,112))

            possibleWays = self.labyrinthe.getPossibleWays(self.position)

            if len(possibleWays) == 0:

                self.position = self.path.pop()
                
            else:

                xPos, yPos = possibleWays[0]
                x,y = self.position

                self.labyrinthe.image.putpixel(possibleWays[0],(112,112,112))

                self.path.append(self.position)

                self.position = (x+(xPos-x)*2,y+(yPos-y)*2)

def labyrintheNature(dimensions:tuple)-> Labyrinthe:
    labyrinthe = Labyrinthe(dimensions)
    labyrinthe.createLabyrinthe()

    return labyrinthe

def format(labyrinthe:Labyrinthe):

    # labyrinthe.image = labyrinthe.image.resize((10 * dimensions[0],10*dimensions[1]),Image.BOX)
    labyrinthe.image.save("scripts/engine/temp_img/labyrinthe.png")

def labyrintheToTerrain(labyrinthe:Labyrinthe):

    for x in range(1,labyrinthe.image.width-2):
        for y in range(1,labyrinthe.image.height-2):

            if labyrinthe.image.getpixel((x,y)) == (0,0,0):

                majority = 0

                for neighbourX in range(x-1,x+2):
                    for neighbourY in range(y-1,y+2):

                        if labyrinthe.image.getpixel((neighbourX,neighbourY)) == (255,255,255):

                            majority += 1
                
                if majority > 2:
                    
                    labyrinthe.image.putpixel((x,y),(255,255,255))
                
                else:
                    
                    labyrinthe.image.putpixel((x,y),(112,112,112))

### CREATE LABYRINTHE ###

def createNewLabyrinthe():

    labyrinthe = labyrintheNature(dimensions)

    ### EXPLORE LABYRINTHE WITH GUENDOLINE ###

    explorer = Explorer(labyrinthe)

    explorer.explorationArianne()

    labyrintheToTerrain(labyrinthe)

    format(labyrinthe)

# createNewLabyrinthe()