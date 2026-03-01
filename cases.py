if __name__ == "main":
    pass

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

class container:
    def __init__(self, caseType, name, cost, itemDict, stat, minQ, maxQ):
        self.name = f"{name.capitalize} {caseType.capitalize}"
        self.type
        self.cost = cost
        self.items = itemDict
        self.stat = stat
        self.minQ = minQ
        self.maxQ = maxQ

test = container("case", "test", 1.5, {2 : [1, 49], 3 : [2], 4 : [111], 5 : [1111], 6 : [69]}, 1, 2, 6)
