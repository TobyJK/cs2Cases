"""database of weapons, skins and stickers
"""

qualities = {
    0 : "grey",
    1 : "light blue",
    2 : "blue",
    3 : "purple",
    4 : "pink",
    5 : "red",
    6 : "gold"
}

stattrak = {
    0 : None,
    1 : "StatTrak",
    2 : "Souvenir"
}

"""int id (pk), str name
"""

weapons = {
    0: 'CZ75-Auto', 1: 'Desert Eagle', 2: 'Dual Berettas', 3: 'Five-SeveN', 
    4: 'Glock-18', 5: 'P2000', 6: 'P250', 7: 'R8 Revolver', 8: 'Tec-9', 
    9: 'USP-S', 10: 'AK-47', 11: 'AUG', 12: 'AWP', 13: 'FAMAS', 14: 'G3SG1', 
    15: 'Galil AR', 16: 'M4A1-S', 17: 'M4A4', 18: 'SCAR-20', 19: 'SG 553', 
    20: 'SSG 08', 21: 'MAC-10', 22: 'MP5-SD', 23: 'MP7', 24: 'MP9', 
    25: 'PP-Bizon', 26: 'P90', 27: 'UMP-45', 28: 'MAG-7', 29: 'Nova', 
    30: 'Sawed-Off', 31: 'XM1014', 32: 'M249', 33: 'Negev', 34: 'Bayonet', 
    35: 'Bowie Knife', 36: 'Butterfly Knife', 37: 'Classic Knife', 
    38: 'Falchion Knife', 39: 'Flip Knife', 40: 'Gut Knife', 
    41: 'Huntsman Knife', 42: 'Karambit', 43: 'Kukri Knife', 44: 'M9 Bayonet', 
    45: 'Navaja Knife', 46: 'Nomad Knife', 47: 'Paracord Knife', 
    48: 'Shadow Daggers', 49: 'Skeleton Knife', 50: 'Stiletto Knife', 
    51: 'Survival Knife', 52: 'Talon Knife', 53: 'Ursus Knife'
}

"""[0, x] means int, [1, x] means float, [2, x] means bool"""

fields = {
    "skins" : ["name", [0, "weaponid"], [0, "quality"], [1, "minFloat"], [1, "maxFloat"], [2, "stattrak"], [2, "souvenir"], [2, "hasRarePattern"], [0, "collectionid"]],
    "knives" : ["name", [0, "weaponid"], [1, "minFloat"], [1, "maxFloat"], [2, "hasRarePattern"], [0, "knifeCollectionid"]],
    "stickers" : ["name", [0, "quality"], [0, "collectionid"]],
    "collections" : ["name"],
    "knifeCollections" : ["name"],
    "cases" : ["name", "type"],
    "collectionCases" : [[0, "collectionid"], [0, "caseid"]],
    "knifeCollectionCases" : [[0, "knifeCollectionid"], [0, "caseid"]]
}

def dataValidation(fields, data):
    ret = []
    for i in range(len(fields)):
        a, b = fields[i], data[i]
        if type(a) is list:
            if a[0] == 0:
                b = int(b)
            elif a[0] == 1:
                b = float(b)
            else:
                b = eval(b)
            a = a[1]
        ret.append([a, b])
    return ret

# database files are in the data/ folder
# create a function to read data from text file
def readData(name):
    with open(f"data/{name}.txt") as f:
        d = {}
        for line in f:
            l = line.strip()
            data = l.split(",")
            key = int(data.pop(0))
            d[key] = {x[0] : x[1] for x in dataValidation(fields[name], data)}
    return d


"""int id (pk), str name, int weaponid (fk), int quality (fk), float minFloat, float maxFloat, bool stattrak, bool souvenir, bool hasRarePattern, int collectionid (fk)
"""
skins = readData("skins")

"""int id (pk), str name, int quality (fk), int collectionid (fk)
"""
stickers = readData("stickers")

"""int collectionid (pk), str name
"""
collections = readData("collections")

"""int caseid (pk), str name, str type
"""
cases = readData("cases")

"""int id (pk), int collectionid (fk), int caseid (fk)
"""
collectionCases = readData("collectionCases")

"""int id (pk), str name, int weaponid (fk), float minFloat, float maxFloat, bool hasRarePattern, int knifeCollectionid (fk)
"""
knives = readData("knives")

"""int knifeCollectionid (pk), str name
"""
knifeCollections = readData("knifeCollections")

"""int id (pk), int knifeCollectionid (fk), int caseid (fk)
"""
knifeCollectionCases = readData("knifeCollectionCases")
