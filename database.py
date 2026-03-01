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

"""int id (pk), name, weaponid (fk), int quality (fk), float minFloat, float maxFloat, bool stattrak, bool souvenir, bool hasRarePattern, int collectionid (fk)
"""
skins = {

}

"""int id (pk), int quality (fk), int collectionid (fk)
"""
stickers = {

}

"""int collectionid (pk), str name
"""
collections = {

}

"""int caseid (pk), str name
"""
cases = {
    
}

"""int collectionid (fk ck), int caseid (fk ck)
"""
collectionCases = {

}