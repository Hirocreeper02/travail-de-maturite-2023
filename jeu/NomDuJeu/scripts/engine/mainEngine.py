import pygame
import math
import territoire
import random

resolution = (1280,800)

tileSize = 64
buttonSize = 64

buttons = {}
dictionnaireFonctionsBoutons = {}

renderWindow = None

#################### INITIALISATION ####################

#pygame.init()

def Setup():

    pygame.init()

    global display
    global horloge
    global textfont
    global mouse

    display = pygame.display.set_mode(resolution) # Display fenêtre
    horloge = pygame.time.Clock()
    textfont = pygame.font.SysFont("Corbel",35)
    mouse = pygame.mouse.get_pos()

Setup()

# IMAGE #

def createImage(path,dimensions):

    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (dimensions[0],dimensions[1]))

    return image

windowBackground = createImage("assets/graphic/interface/window_background.png", [resolution[0] - 50, resolution[1] - 50])

grassTile = createImage("assets/graphic/tiles/grass_tile.png", (tileSize,tileSize))
mountainTile = createImage("assets/graphic/tiles/mountain_tile.png", (tileSize,tileSize))
waterTile = createImage("assets/graphic/tiles/water_tile.png", (tileSize,tileSize))

buttons["politics"] = {"released":createImage("assets/graphic/buttons/politics_released.png", (buttonSize,buttonSize)),"pressed":createImage("assets/graphic/buttons/politics_pressed.png",(buttonSize,buttonSize))}
buttons["character"] = {"released":createImage("assets/graphic/buttons/character_released.png", (buttonSize,buttonSize)),"pressed":createImage("assets/graphic/buttons/character_pressed.png",(buttonSize,buttonSize))}
buttons["faction"] = {"released":createImage("assets/graphic/buttons/faction_released.png", (buttonSize,buttonSize)),"pressed":createImage("assets/graphic/buttons/faction_pressed.png",(buttonSize,buttonSize))}
buttons["economy"] = {"released":createImage("assets/graphic/buttons/economy_released.png", (buttonSize,buttonSize)),"pressed":createImage("assets/graphic/buttons/economy_pressed.png",(buttonSize,buttonSize))}
buttons["utopie"] = {"released":createImage("assets/graphic/buttons/utopie_released.png", (buttonSize,buttonSize)),"pressed":createImage("assets/graphic/buttons/utopie_pressed.png",(buttonSize,buttonSize))}

# MAP CREATION #

territoire.divisionTerritoire()
mappa = pygame.Surface((len(territoire.terrain[0])*tileSize,len(territoire.terrain)*tileSize)) 


#################### DEFINITIONS ####################

# CLASS DEFINITIONS #

class PlayerController:
    """Objet gérant la souris et ses actions"""

    def __init__(self):
        
        self.image = pygame.Surface((32,32)).fill((255,0,0))
        self.rect = pygame.Rect((284,284),(32,32))
        self.mapPos = (0,0)
        self.moveBox = (10,10,resolution[0]-10,resolution[1]-10) # Cadre de l'écran

    def move(self) -> None:
        """Fonction traitant de la souris et de l'écran"""

        mx,my = self.mapPos

        if playerCursor.rect.x <= self.moveBox[0]:
            self.rect.x += 8
            mx += 8
        elif playerCursor.rect.x >= self.moveBox[2]-32:
            self.rect.x -= 8
            mx -= 8
        if playerCursor.rect.y <= self.moveBox[1]:
            self.rect.y += 8
            my += 8
        elif playerCursor.rect.y >= self.moveBox[3]-32:
            self.rect.y -= 8
            my -= 8

        self.rect.x,self.rect.y = mouse
        self.mapPos = (mx,my)

    def render(self,display:object) -> None:
        """Affichage du curseur"""

        display.blit(self.image(self.rect.x-16,self.rect.y-16))

class Button:
    """Objet pouvant être cliqué et qui effectue une action donnée"""

    def __init__(self,dimensions:tuple,position:tuple,text:str,fonction:str,parametresFonction:list = [],isRender:bool = True,imageReleased:object = None, imagePressed:object = None):
        
        if imageReleased != None and imagePressed != None:

            self.image = [imageReleased,imagePressed]

        else:

            self.image = [pygame.Surface(dimensions),pygame.Surface(dimensions)]
            self.image[0].fill((30,30,30))
            self.image[1].fill((20,20,20))        

        self.dimensions = dimensions
        self.position = position
        self.text = text
        self.isRender = isRender

        self.fonction = fonction
        self.parametresFonction = parametresFonction

    def action(self) -> None:
        """Action performée par la pression du bouton"""

        dictionnaireFonctionsBoutons[self.fonction](self.parametresFonction)

    def render(self,display:object) -> None:
        """Affichage du bouton"""

        ax,ay = pygame.mouse.get_pos()

        if (self.position[0] <= ax <= (self.position[0] + self.dimensions[0])) and (self.position[1] <= ay <= self.position[1] + self.dimensions[1]):

            display.blit(self.image[1],(self.position[0],self.position[1]))

        else:

            display.blit(self.image[0],(self.position[0],self.position[1]))

class Window:
    """Objet affichant une fenêtre donnant diverses informations sur l'écran de jeu"""

    def __init__(self,nom:str):
        
        self.nom = nom
        self.text = ""

    def render(self,display:object) -> None:
        """Affichage de la fenêtre"""

        display.blit(windowBackground,(25,25))
        windowExitButton.isRender = True

        textBox = textfont.render(self.text, True, (0,0,0))
        textRect = textBox.get_rect()
        textRect.center = (resolution[0] // 2, resolution[1] // 2)

        display.blit(textBox, textRect)

# CLASS DECLARATION #

playerCursor = PlayerController()

windowExitButton = Button((buttonSize,buttonSize),(80,80),"X",False)
politicsButton = Button((buttonSize,buttonSize),(10,10),"politicsButton","openCloseWindow","POLITIQUE",True,buttons["politics"]["released"],buttons["politics"]["pressed"])
characterButton = Button((buttonSize,buttonSize),(10,110),"characterButton","openCloseWindow","PERSONNAGES",True,buttons["character"]["released"],buttons["character"]["pressed"])
factionButton = Button((buttonSize,buttonSize),(10,210),"factionButton","openCloseWindow","FACTIONS",True,buttons["faction"]["released"],buttons["faction"]["pressed"])
economyButton = Button((buttonSize,buttonSize),(10,310),"economyButton","openCloseWindow","ECONOMIE",True,buttons["economy"]["released"],buttons["economy"]["pressed"])
utopieButton = Button((buttonSize,buttonSize),(10,410),"utopieButton","openCloseWindow","UTOPIE",True,buttons["utopie"]["released"],buttons["utopie"]["pressed"])

buttonIndex = {"windowExitButton":windowExitButton,"politicsButton":politicsButton,"characterButton":characterButton,"factionButton":factionButton,"economyButton":economyButton,"utopieButton":utopieButton}

mainWindow = Window("mainWindow")
leftInfoWindow = Window("leftInfoWindow")
rightInfoWindow = Window("leftInfoWindo")

windowIndex = {"mainWindow":mainWindow}

# BUTTON FUNCTION DEFINITION #

def openCloseWindow(windowText:str = None):
    """Inverse l'état de la fenêtre (Ouvert -> Fermé ou Fermé -> Ouvert)"""

    global renderWindow

    if windowText:

        openWindow(windowText)

        print("OPEN WINDOW")

    else:

        renderWindow = None

        print("CLOSE WINDOW")

dictionnaireFonctionsBoutons = {"openCloseWindow":openCloseWindow}

# MINOR FUNCTION DEFINITION #

def openWindow(info:object):
    """Affiche la fenêtre et y ajoute le texte donné"""

    global renderWindow

    renderWindow = mainWindow

    mainWindow.text = info

def displayTerrain(terrain:list):
    """Affiche le terrain et les territoires"""

    x,y = 0,0

   # TERRAIN # 

    for row in terrain:
        for tile in row:
            if tile in "-":
                mappa.blit(grassTile,(x,y))
            elif tile in "A":
                mappa.blit(mountainTile,(x,y))
            elif tile in "~":
                mappa.blit(waterTile,(x,y))
            else:
                pygame.draw.rect(mappa,(255,128,122),((x,y),(tileSize,tileSize)))
            x += tileSize
        y += tileSize
        x = 0

    # TERRITOIRE #

    borders = territoire.borders

    colorDict = {}

    colors = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]

    borderTileSize = [math.ceil(len(terrain[0]) * tileSize / len(borders[0])),math.ceil(len(terrain) * tileSize / len(borders))]

    if len(terrain[0]) > len(terrain):

        borderTileSize[0] = borderTileSize[0] * math.ceil(len(terrain[0]) / len(terrain))

    else: 

        borderTileSize[1] = borderTileSize[1] * math.ceil(len(terrain) / len(terrain[0]))
 
    for i in range(len(colors)):

        colorDict[colors[i]] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    x,y = 0,0

    for row in borders:
        for tile in row:
            if tile not in "-":

                pygame.draw.rect(mappa,colorDict[tile],((x,y),(borderTileSize[0],borderTileSize[1])))

            x += borderTileSize[0]
        y += borderTileSize[1]
        x = 0

def getTerrainCoordinates():
    """Donne la position sur le terrain en fonction de la position de la souris sur l'écran"""
    
    ax,ay = pygame.mouse.get_pos()
    bx,by = playerCursor.mapPos

    x = math.ceil((ax - bx) / tileSize) - 1
    y = math.ceil((ay - by) / tileSize) - 1

    return([x,y])

def getTerritoireCoordinates():
    """Donne la position sur le territoire en fonction de la position de la souris"""

    ax,ay = pygame.mouse.get_pos()
    bx,by = playerCursor.mapPos

    x = math.ceil((ax - bx) / 16) - 1
    y = math.ceil((ay - by) / 8) - 1

    return([x,y])

def buttonCheck():
    """Vérifie si le click concerne un bouton ou non"""

    global renderWindow

    ax,ay = pygame.mouse.get_pos()

    for key in buttonIndex:

        button = buttonIndex[key]
    
        if button.position[0] <= ax <= (button.position[0] + button.dimensions[0]) and button.position[1] <= ay <= (button.position[1] + button.dimensions[1]):
            
            return button

    return False

# MAJOR FUNCTION DEFINITION #

def Render():
    """Activation de toutes les fonction Render() des objets"""
    
    for key in buttonIndex:
        
        buttonIndex[key].render(display)

    for key in windowIndex:

        windowIndex[key].render(display)

def Click():
    """Instructions lors d'un click sur l'écran"""

    coordinates = getTerrainCoordinates()
    tCoordinates = getTerritoireCoordinates()

    button = buttonCheck()

    if button:

        button.action()

    elif 0 <= tCoordinates[0] <= len(territoire.territoire[0]) and 0 <= tCoordinates[1] <= len(territoire.territoire):

        tile = territoire.territoire[tCoordinates[1]][tCoordinates[0]]

        openWindow(tile)

        print(tile)


terrain = territoire.terrain
displayTerrain(terrain)

text = textfont.render('quit' , True , (255,255,255))
pygame.display.set_caption('TM - NomDuJeu')

def Run():
    """Boucle principale du moteur et du jeu en entier"""
    
    Setup()


    RUNNING = True

    while RUNNING:

        horloge.tick(60)

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                Click()
        
        playerCursor.move()
    
        display.fill((0,0,0))
        display.blit(mappa,playerCursor.mapPos)
    
        Render()
    
        pygame.display.flip()

    pygame.quit()

