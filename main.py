import random
import database
import numpy as np
import pandas as pd

# create container class
class container:
    def __init__(self, caseType, name, cost, itemDict, stat, minQ, maxQ):
        self.name = f"{name.capitalize} {caseType.capitalize}"
        self.type
        self.cost = cost
        self.items = itemDict
        self.stat = stat
        self.minQ = minQ
        self.maxQ = maxQ

# test = container("case", "test", 1.5, {2 : [1, 49], 3 : [2], 4 : [111], 5 : [1111], 6 : [69]}, 1, 2, 6)

skins = pd.DataFrame.from_dict(database.skins, orient='index')
stickers = pd.DataFrame.from_dict(database.stickers, orient='index')
collections = pd.DataFrame.from_dict(database.collections, orient='index')
cases = pd.DataFrame.from_dict(database.cases, orient='index')
collectionCases = pd.DataFrame.from_dict(database.collectionCases, orient='index')

def getSkinsFromCase(name):
    cNumber = cases[cases["name"] == name].index[0]
    col = collectionCases.loc[collectionCases["caseid"] == cNumber]["collectionid"].iloc[0]
    s = skins[skins["collectionid"] == col]
    statOrSouv = "stat" if s["stattrak"].iloc[0] else "souv" if s["souvenir"].iloc[0] else False
    s = s[["name", "quality", "minFloat", "maxFloat", "hasRarePattern"]]

    return s, statOrSouv
