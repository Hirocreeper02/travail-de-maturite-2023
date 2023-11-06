
import tkinter as tk

root = tk.Tk()

windowDimensions = 300, 1000

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

windowCanvas = tk.Canvas(frame)
windowCanvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame, orient="vertical", command=windowCanvas.yview)
scrollbar.pack(side="right", fill="y")

windowCanvas.config(yscrollcommand=scrollbar.set)

window = tk.Frame(windowCanvas)

windowCanvas.create_window((0, 0), window=window, anchor="nw")


def on_configure(event):
    windowCanvas.configure(scrollregion=windowCanvas.bbox("all"))

windowCanvas.bind("<Configure>", on_configure)

#### FONCTIONNEMENT FENÊTRES #####
#                                #
#   Window(title,dependencies =  #
#                                #
#       ajouter les éléments qu'il faut afficher dans la fenêtre
#                                # 
#   )                            #
#                                #
##################################

class Window():
    """
        Append elements to display in the window
    """

    def shareLength(self):
        """
            Decides how to share the elements according to the right handle position
        """

        tempDependencies = self.dependencies.copy()
        tempLength = 0
        tempDisplay = []

        while len(tempDependencies) > 0:

            for element in tempDependencies:
                
                if tempLength+element.length <= 20:

                    tempDisplay.append(element)
                    tempLength += element.length

                    if element is tempDependencies[-1]:

                        tempLength += 20

                else:

                    self.display.append(tempDisplay)

                    tempLength = 0
                    tempDisplay = []

                    tempDependencies.pop(0)

                    break

    def displayDependencies(self):
        """
            Display the elements according to the shareLength() function
        """

        for element in window.winfo_children():

            element.pack_forget()

        # for element in windowEssentials:

        #     element.pack()
        
        for element in self.dependencies:
            
            element.display()

    def __init__(self,title:str,dependencies:list):
        
        self.title = title
        self.dependencies = dependencies
        self.display = []
        
        self.progressBar = 0

        # self.shareLength()

class WindowInfos():
    """
        text = f"Var1:{var1}/nVar2:{var2}..."

        -----

        Var1: var1
        Var2: var2
        ...
    """

    def __init__(self,text):

        self.text = text

        self.length = (text.count("\n")+1)
        self.displayList = []

    def display(self):
        """
            Displays the element
        """

        self.displayList = [tk.Label(window,text=self.text)]
        self.displayList[0].pack()

class WindowListing():
    """
        iterable = {key1:____,key2:_____,key3: ...}
        windowTarget = Window(...)
        -----
        Nom 1 [VOIR] \n
        Nom 2 [VOIR] \n
        Nom 3 [VOIR]
    """

    def __init__(self,iterable:dict,windowTarget:Window):

        self.iterable = iterable
        self.windowTarget = windowTarget

        self.length = len(iterable)

    def display(self):
        """
            Displays the element
        """

        self.displayList = []

        for element in self.iterable.values():

            self.displayList.append([
                frame := tk.Frame(window),
                tk.Label(frame,text=element.nom),
                tk.Button(frame,text="Voir",command=lambda:self.windowTarget.displayDependencies())
            ])

            for displayElement in self.displayList[-1]:

                displayElement.pack()

class WindowInteractibles():
    """
        actions = [lambda:fonction1(arguments),lambda:fonction2(arguments),lambda: ...]
        actionNames = ["Fonction 1","Fonction 2", ...]
        -----
        [Fonction 1] \n
        [Fonction 2] \n
        [...]
    """

    def __init__(self,actions:list,actionNames:list):

        self.actions = actions
        self.actionNames = actionNames
        
        self.length = len(actions)

    def display(self):
        """
            Displays the element
        """

        self.displayList = []

        for i,(action,actionName) in enumerate(zip(self.actions,self.actionNames)):

            self.displayList.append(tk.Button(window,text=actionName,command=action))
            self.displayList[i].pack()

class WindowCustomizables():

    def __init__(self,options:list,outputList:list):

        self.options = options 
        self.outputList = outputList
        
        self.length = len(options)

    def display(self):
        """
            Displays the element
        """

        self.displayList = [tk.OptionMenu(window, self.options[0], *self.options, command=lambda:print("Hello"))]
        self.displayList[0].pack()

class WindowOpinions():

    def __init__(self,positionnement):
        
        self.positionnement = positionnement
        
        self.length = 10

class WindowSliders():

    def __init__(self,variable,intervalle):
        
        self.variable = variable
        self.intervalle = intervalle
        
        self.length = 2

# outputLists = []

# class ville():
#     def __init__(self,nom):
#         self.nom = nom

# dictionnaire = {"lausanne":ville("Lausanne"),"genève":ville("Genève"),"zürich":ville("Zürich")}

# targetWindow = Window(
#     title = "Nay!",
#     dependencies = [
#         WindowInfos("YOUHOUHOU"),
#         WindowInfos ("Warum nichts?")
#     ]
# )

# newWindow = Window(
#     title = "Yay!",
#     dependencies = [
#         WindowInfos(f"Var1:var1\nVar2:var2\nVar3:var3"),
#         WindowInteractibles([lambda:print("1"),lambda:print("2"),lambda:print("3")],[1,2,3]),
#         WindowCustomizables(["A","B","C","D","E"],outputLists),
#         WindowListing(dictionnaire,targetWindow)

#     ]
# )

# # newWindow.shareLength()
# newWindow.displayDependencies()

# root.mainloop()
