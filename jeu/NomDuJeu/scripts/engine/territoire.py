import random
import math

terrain = [
    "-------AAAA--------AAA",
    "~~~~~----A---~~------A",
    "-~~~-------~~~~-------",
    "-----AA-----~~--------",
    "---AAAAA-------------A",
    "------AAA---------AAAA", 
    "-------A-----------AAA",
    "---A------~---------AA",
    "AAAAA-----~~~---------",
    "AA---------~~-------AA",
    "~~~--------------AAAAA",
    "~~~~-------------AAAAA"]

"""territoire = [
    "----------------------",
    "----------------------",
    "----------------------",
    "----------------------",
    "----------------------",
    "----------------------",
    "----------------------",
    "----------------------",
    "----------------------",
    "----------------------",
    "----------------------",
    "----------------------",
]
"""

def createTerritoire(dimensions:tuple = (25,25)):
    """Create empty territory with dimensions"""

    territoire = []

    for y in range(dimensions[1]):

        territoire.append("")

        for x in range(dimensions[0]):

            territoire[y] = territoire[y] + "-"

    for i in range(len(territoire)):
        territoire[i] = [*territoire[i]]

    return territoire

territoire = createTerritoire((200,100))

borders = territoire.copy()

def display():
    """Display the territory map"""

    for i in range(len(territoire)):
        #terrain[i] = "".join(terrain[i])
        territoire[i] = "".join(territoire[i])
        borders[i] = "".join(borders[i])

    for i in range(len(territoire)):
    
        print(territoire[i])

    print("\n\n\n\n")

    for i in range(len(borders)):
    
        print(borders[i])

    #for i in range(len(territoire)):
    #
    #    print(" ",territoire[i])

    for i in range(len(territoire)):
        #terrain[i] = [*terrain[i]]
        borders[i] = [*borders[i]]
        territoire[i] = [*territoire[i]]

def getRandomPoint(numberOfPoints:int,terrain)->list:
    """Set the random points that will be the center of the states"""

    listOfPoints = []

    for i in range(numberOfPoints):

        while True:

            randomPoint = [random.randint(0,len(terrain[0])-1),random.randint(0,len(terrain)-1)]

            if randomPoint not in listOfPoints:

                listOfPoints.append(randomPoint)

                break

    return listOfPoints

def divideStates(listOfPoints:list):
    """Divide the territory among the states"""

    for y in range(len(territoire)):

        for x in range(len(territoire[0])):

            distance = 10*10000000000

            for i in range(len(listOfPoints)):

                if math.sqrt(abs(x-listOfPoints[i][0])+abs(y-listOfPoints[i][1])) < distance:

                    distance = math.sqrt(abs(x-listOfPoints[i][0])+abs(y-listOfPoints[i][1]))
                    territoire[y][x] = colors[str(listOfPoints[i])]

def getBorders():

    for y in range(len(territoire)):

        for x in range(len(territoire)):

            listeTerritoires = []
            
            listeTerritoires.append(territoire[y][x])

            for i in range(y-1,y+1):

                for j in range(x-1,x+1):

                    if territoire[i][j] not in listeTerritoires:

                        listeTerritoires.append(territoire[i][j])

            if len(listeTerritoires) != 1:

                borders[y][x] = territoire[y][x]




def divisionTerritoire():

    territoire = createTerritoire((100,100))

    display()

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]

    listOfPoints = getRandomPoint(35,territoire)

    global colors
    colors = {}

    for i in range(len(listOfPoints)):

        letter = alphabet[random.randint(0,len(alphabet)-1)]

        alphabet.remove(letter)

        colors[str(listOfPoints[i])] = alphabet[random.randint(0,len(alphabet)-1)]

    divideStates(listOfPoints)

    print(len(territoire))

    getBorders()

    display()