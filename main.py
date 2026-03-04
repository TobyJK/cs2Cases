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
knives = pd.DataFrame.from_dict(database.knives, orient='index')
knifeCollections = pd.DataFrame.from_dict(database.knifeCollections, orient='index')
knifeCollectionCases = pd.DataFrame.from_dict(database.knifeCollectionCases, orient='index')

def getSkinsFromCase(name):
    cNumber = cases[cases["name"] == name].index[0]
    col = collectionCases.loc[collectionCases["caseid"] == cNumber]["collectionid"].iloc[0]
    s = skins[skins["collectionid"] == col]
    s = s[["name", "weaponid", "quality", "minFloat", "maxFloat", "hasRarePattern"]]

    return s

def getKnivesFromCase(name):
    cNumber = cases[cases["name"] == name].index[0]
    col = knifeCollectionCases.loc[knifeCollectionCases["caseid"] == cNumber]["knifeCollectionid"].iloc[0]
    k = knives[knives["knifeCollectionid"] == col]
    k = k[["name", "weaponid", "minFloat", "maxFloat", "hasRarePattern"]]

    return k

# get odds for case
def getOdds(minQ, maxQ):
    qualities = [x for x in range(maxQ, minQ - 1, -1)]
    
    if maxQ == 6:
        return qualities, [2] + [5 ** (x+1) for x in range(maxQ - minQ)]
    
    if minQ <= 1:
        odds = []
        last = None
        for i in range(len(qualities)):
            if not last:
                odds.append(1)
                last = 1
                continue

            if qualities[i] == 1:
                last = (last // 5) * 24
                odds.append(last)
                continue

            last *= 5
            odds.append(last)
        
        return qualities, odds
    
    return qualities, [5 ** x for x in range(maxQ - minQ + 1)]

# assign float to opened skin
def assignFloat(skin):
    wear = random.choices([0, 1, 2, 3, 4], [0.03, 0.24, 0.33, 0.24, 0.16])[0]
    endPoint = database.wears[wear][0]
    startPoint = 0 if wear == 0 else database.wears[wear - 1][0] + 0.01
    basicFloat = random.uniform(startPoint, endPoint)

    minFloat, maxFloat = float(skin["minFloat"].iloc[0]), float(skin["maxFloat"].iloc[0])

    if minFloat == 0 and maxFloat == 1:
        return [basicFloat, wear]

    finalFloat = (basicFloat * (maxFloat - minFloat)) + minFloat
    for w in database.wears:
        if finalFloat < database.wears[w][0]:
            finalWear = w
            break

    return [finalFloat, finalWear]

# open a given case
def caseOpenFromName(name):
    cType = cases[cases["name"] == name]["type"].iloc[0].lower()
    skinsPossible = getSkinsFromCase(name)
    if cType == "case":
        quals, odds = getOdds(2, 6)
        knivesPossible = getKnivesFromCase(name)

    elif cType == "souvenir":
        quals, odds = getOdds(min(skinsPossible["quality"]), max(skinsPossible["quality"]))
    
    qualityChosen = random.choices(quals, odds)[0]

    if cType == "case":
        if qualityChosen == 6:
            chosen = knivesPossible.sample()
        else:
            chosen = skinsPossible[skinsPossible["quality"] == qualityChosen].sample()

    elif cType == "souvenir":
        chosen = skinsPossible[skinsPossible["quality"] == qualityChosen].sample()

    skinFloat, wear = assignFloat(chosen)
