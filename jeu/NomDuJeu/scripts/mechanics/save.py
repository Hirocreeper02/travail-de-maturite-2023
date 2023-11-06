import factions
import provinces

import pickle
from datetime import datetime

def save():

    path = f"saves/Savegame - {str(datetime.now())}.pkl"

    with open(path, "wb") as file:
        pickle.dump(factions.index, file)
        pickle.dump(provinces.index, file)

def load(path:str):

    with open(path, "rb") as file:
        factions.index = pickle.load(file)
        provinces.index = pickle.load(file)


