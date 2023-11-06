import tkinter as tk
from PIL import Image,ImageTk,ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


import labGen
import territoire
import dependencies

import sys
sys.path.append("scripts/mechanics")
import factions
import provinces
import utopies

print(factions.index.values(),"<- in mainEngine.py")

rootWidth,rootHeight = 1000,600

root = dependencies.root
# root = tk.Tk()
root.title("Utopia")
root.geometry(f"{rootWidth}x{rootHeight}")
root.configure(bg="yellow")

################################################################################################
######################### ELEMENT DEFINTITION ##################################################
################################################################################################

### MAP CANVAS ###

mapImagePos = [0,0]

mapCanvas = tk.Canvas(root,width=rootWidth-100,height=rootHeight-50)
mapCanvas.place(x=rootWidth//2-((rootWidth-100)//2), y=rootHeight//2-((rootHeight-10)//2))

mapImage = Image.open("scripts/engine/temp_img/labyrintheMap.png")
mapImage = ImageTk.PhotoImage(mapImage)
mapImageId = mapCanvas.create_image(mapImagePos[0],mapImagePos[1],image=mapImage,anchor=tk.NW)
# mapCanvas.mapImage = mapImage

preFrontierImage = Image.open("scripts/engine/temp_img/frontieresMap.png")
frontierImage = ImageTk.PhotoImage(preFrontierImage)
frontierImageId = mapCanvas.create_image(mapImagePos[0],mapImagePos[1],image=frontierImage,anchor=tk.NW)
# mapCanvas.frontierImage = frontierImage

ressourcesImage = Image.open("scripts/engine/temp_img/ressourcesMap.png")
ressourcesImage = ImageTk.PhotoImage(ressourcesImage)
ressourcesImageId = mapCanvas.create_image(mapImagePos[0],mapImagePos[1],image=ressourcesImage,anchor=tk.NW)
mapCanvas.itemconfig(ressourcesImageId, state="hidden")

# territoryImage = Image.open("scripts/engine/temp_img/territoireMap.png")


### SIDE BUTTONS ###

buttonFrame = tk.Frame(root)

buttonPolitique = tk.Button(buttonFrame,text="G",command=lambda:windowInteraction("Structure Politique","a"))
buttonPersonnages = tk.Button(buttonFrame,text="P",command=lambda:windowInteraction("Personnages",showPersonnagesWindow()))
buttonFaction = tk.Button(buttonFrame,text="F",command=lambda:windowInteraction("Factions",showFactionsWindow()))
buttonEconomie = tk.Button(buttonFrame,text="E",command=lambda:windowInteraction("Economie","d"))
buttonUtopie = tk.Button(buttonFrame,text="U",command=lambda:windowInteraction("Utopies & Lois","\n".join(map(str, utopies.index.values()))))

def showFrameButton():
    buttonFrame.pack(side=tk.LEFT)
    buttonPolitique.pack(side=tk.TOP,padx=0,pady=20)
    buttonPersonnages.pack(side=tk.TOP,padx=0,pady=20)
    buttonFaction.pack(side=tk.TOP,padx=0,pady=20)
    buttonEconomie.pack(side=tk.TOP,padx=0,pady=20)
    buttonUtopie.pack(side=tk.TOP,padx=0,pady=20)

showFrameButton()


### MENU ###

boutonMenu = tk.Button(root,text="Menu",command=lambda:menuInteraction())
boutonMenu.pack(side=tk.TOP)

menuFrame = tk.Frame(root)

newGameButton = tk.Button(menuFrame,text="New Game",command=lambda:newGame())
settingsButton = tk.Button(menuFrame,text="Settings",command=lambda:None)
quitButton = tk.Button(menuFrame,text="Quit Game",command=lambda:quit())

def showFrameMenu():
    menuFrame.pack(side=tk.TOP)
    newGameButton.pack()
    settingsButton.pack()
    quitButton.pack()


### WINDOW ###

window = tk.Frame(root,width=1000,height=1000,)

windowExitButton = tk.Button(window,text="X",command=lambda:closeWindow())
windowTitle = tk.Label(window, text="New Window")

windowInfos = tk.Label(window, text="Default Text")

# WINDOW CARACTERS #

personnagesWindowIndex = {
    caracter: {
        "frame": (frame := tk.Frame(window)),
        "text": (label := tk.Label(frame, text=caracter.nom)),
        "bouton": (button := tk.Button(
            frame,
            text="Voir",
            command=lambda c=caracter: showPersonnagesFrameWindow(f"Personnage - {c}", f"Positionnement: {c.positionnement}\nFaction: {c.faction}\nInfluence: {c.influence}\nÂge: {c.age}")
        )),
    }
    for caracterListe in factions.index.values()
    for caracter in caracterListe.membres
}

# WINDOW FACTIONS #

factionsWindowIndex = {
    faction: {
        "frame": (frame := tk.Frame(window)),
        "text": (label := tk.Label(frame, text=faction.nom)),
        "bouton": (button := tk.Button(frame, text="Voir",command=lambda:showFactionsFrameWindow(f"Faction - {faction}",f"Positionnement: {faction.positionnement}\nMotto: {faction.motto}\nFinances: {faction.finances}\nUtopies:{faction.utopie}") )),
    }
    for faction in factions.index.values()
}
#windowInteraction("Personnages","\n".join(map(str, factions.index.values())))

for element in (factionsWindowIndex | personnagesWindowIndex).values(): # Parcours de deux dictionnaires simultanément

    element["text"].pack()
    element["bouton"].pack()
    element["frame"].pack()

    element["text"].pack_forget()
    element["bouton"].pack_forget()
    element["frame"].pack_forget()


def createWindow(title:str):

    window.place(x=(rootWidth//2)-200,y=(rootHeight//2)-200)

    windowExitButton.pack(anchor=tk.W,padx=0,pady=0)
    windowTitle.pack(padx=30,pady=0)

    windowTitle.config(text=title)

def showFactionsWindow():

    createWindow("Factions")

    windowInfos.config(text="")

    for element in factionsWindowIndex.values():
        
        element["frame"].pack(side="top")
        
        element["text"].pack(side="left", padx=0, pady=10)
        element["bouton"].pack(side="left", padx=50, pady=0)

def showPersonnagesWindow():

    createWindow("Personnages")

    windowInfos.config(text="")

    for element in personnagesWindowIndex.values():
        
        element["frame"].pack(side="top")
        
        element["text"].pack(side="left", padx=0, pady=10)
        element["bouton"].pack(side="left", padx=50, pady=0)

def showFrameWindow(title:str,text:str):

    createWindow(title)
    
    windowInfos.pack(padx=0,pady=10)
    windowInfos.config(text=text)

def showFactionsFrameWindow(title:str,text:str):

    for element in factionsWindowIndex.values(): 

        element["text"].pack_forget()
        element["bouton"].pack_forget()
        element["frame"].pack_forget()

    showFrameWindow(title,text)

def showPersonnagesFrameWindow(title:str,text:str):

    for element in personnagesWindowIndex.values(): 

        element["text"].pack_forget()
        element["bouton"].pack_forget()
        element["frame"].pack_forget()

    showFrameWindow(title,text)

### INFO BAR ###

infoFrame = tk.Frame(root)

infoLabel1 = tk.Label(infoFrame,text="hi")

def showFrameInfo():
    infoFrame.pack(side=tk.RIGHT)
    infoLabel1.pack(side=tk.TOP,padx=0,pady=0)

showFrameInfo()

### CHECKBOXES ###

checkTerritory = tk.IntVar(value=1)
checkRessources = tk.IntVar(value=0)

showTerritory = True
showRessources = True

checkBoxFrame = tk.Frame(root)
checkBoxFrame.pack(side="right", anchor="se")

checkboxTerritory = tk.Checkbutton(checkBoxFrame, text="Territory", variable=checkTerritory, command=lambda:toggle_image_visibility(frontierImageId))
checkboxTerritory.pack()

mapCanvas.itemconfig(frontierImageId, state="normal")

checkboxRessources = tk.Checkbutton(checkBoxFrame, text="Ressources", variable=checkRessources, command=lambda:toggle_image_visibility(ressourcesImageId))
checkboxRessources.pack()

def toggle_image_visibility(imageId):
    current_state = mapCanvas.itemcget(imageId, "state")
    if current_state == "normal":
        mapCanvas.itemconfig(imageId, state="hidden")
    else:
        mapCanvas.itemconfig(imageId, state="normal")


    

    

################################################################################################
######################### FUNCTIONS ############################################################
################################################################################################

### NEW GAME ###

def newGame():

    print("New game sequence initiated")

    labGen.createNewLabyrinthe()
    territoire.creation(5,30)

    global mapImage
    global mapImageId
    global frontierImage
    global frontierImageId
    global mapImagePos

    mapImagePos = [0,0]
    
    mapImage = Image.open("scripts/engine/temp_img/labyrintheMap.png")
    mapImage = ImageTk.PhotoImage(mapImage)
    mapImageId = mapCanvas.create_image(mapImagePos[0],mapImagePos[1],image=mapImage,anchor=tk.NW)
    
    frontierImage = Image.open("scripts/engine/temp_img/frontieresMap.png")
    frontierImage = ImageTk.PhotoImage(frontierImage)
    frontierImageId = mapCanvas.create_image(mapImagePos[0],mapImagePos[1],image=frontierImage,anchor=tk.NW)

    print("Well, with real success this time")

### MAP CLICK ###

def map_click(event):

    x, y = event.x, event.y

    pixel = preFrontierImage.getpixel((x,y))

    pixel = (pixel[0],pixel[1],pixel[2],255)

    if pixel not in {(112, 112, 200, 255), (236, 236, 236, 255), (0,0,0,255)}:

        _extracted_from_map_click_11(pixel)
    # You can add logic to execute a function based on the clicked location (x, y)
    print(f"Clicked on map at ({x}, {y})")


# TODO Rename this here and in `map_click`
def _extracted_from_map_click_11(pixel):
    print(territoire.couleurComtes)
    print(pixel)
    print(territoire.couleurComtes[pixel])
    print(territoire.couleurComtes[pixel].faction)

    comte = territoire.couleurComtes[pixel]
    windowInteraction(f"Comté - {comte}",f"Faction: {comte.faction}\nRessource: {comte.ressource}\nPopulation: {comte.population}\nClasses: {comte.classes}")




### WINDOW INTERACTIONS ###

windowOpened = False
menuOpened = False

def closeWindow():
    global windowOpened
    windowOpened = False
    
    window.place_forget()
    
    for element in window.winfo_children():
        element.pack_forget()

def openWindow(title:str,text:str):
    global windowOpened
    windowOpened = True
    
    showFrameWindow(title,text)

def windowInteraction(title:str,text:str):
    global windowOpened
    
    if windowOpened:
        closeWindow()
    else:
        openWindow(title,text)


### MENU INTERACTIONS ###

def menuInteraction():
    global menuOpened
    
    if menuOpened:
        menuFrame.pack_forget()
        menuOpened = False
    else:
        showFrameMenu()
        menuOpened = True


### MOVEMENT & ZOOM ###

moveSpeed = 1

def moveMap(moveVector:tuple):
    global mapImagePos
    
    mapImagePos[0], mapImagePos[1] = mapImagePos[0] + moveVector[0], mapImagePos[1] + moveVector[1]
    
    mapCanvas.coords(mapImageId, mapImagePos[0], mapImagePos[1])
    mapCanvas.coords(frontierImageId, mapImagePos[0], mapImagePos[1])

def setMapZoom(value:str):
    global moveSpeed
    global frontierImage
    global mapImage
    global ressourcesImage
    global frontierImageId
    global mapImageId
    global ressourcesImageId
    
    value = int(value)
    moveSpeed = value
    
    mapImage = setImageZoom("scripts/engine/temp_img/labyrintheMap.png", value)
    mapImageId = mapCanvas.create_image(mapImagePos[0],mapImagePos[1],image=mapImage,anchor=tk.NW)
    # mapCanvas.mapImage = mapImage   
    
    frontierImage = setImageZoom("scripts/engine/temp_img/frontieresMap.png", value)
    frontierImageId = mapCanvas.create_image(mapImagePos[0],mapImagePos[1],image=frontierImage,anchor=tk.NW)
    # mapCanvas.frontierImage = frontierImage

    ressourcesImage = setImageZoom("scripts/engine/temp_img/ressourcesMap.png", value)
    ressourcesImageId = mapCanvas.create_image(mapImagePos[0],mapImagePos[1],image=frontierImage,anchor=tk.NW)

def setImageZoom(inputImage:str, zoom):
    """By Chat-GPT"""
    global mapImagePos

    mapImagePos = mapImagePos * zoom
    moveMap((0,0))
    
    image = Image.open(inputImage)
    image = image.resize(
        (zoom * image.width, zoom * image.height), Image.BOX
    )
    image = ImageTk.PhotoImage(image)
    return image


### KEYBOARD INPUTS GESTION ###

def handle_key_w(event):

    moveMap((0,10*moveSpeed))

def handle_key_a(event):
    
    moveMap((10*moveSpeed,0))

def handle_key_s(event):
    
    moveMap((0,-10*moveSpeed))

def handle_key_d(event):
    
    moveMap((-10*moveSpeed,0))


################################################################################################
######################### INPUTS ###############################################################
################################################################################################

### ZOOM SLIDER ###

slider = tk.Scale(root, from_=1.0, to=5.0, orient="horizontal", command=setMapZoom,length=200)
slider.set(1.0)
slider.pack(side="bottom")


### MOVEMENT ###

root.bind("<w>", handle_key_w)
root.bind("<a>", handle_key_a)
root.bind("<s>", handle_key_s)
root.bind("<d>", handle_key_d)


### MENU ###

root.bind("<Escape>", menuInteraction)


### MAP ###

mapCanvas.bind("<Button-1>", map_click)


################################################################################################
################################################################################################

root.mainloop()