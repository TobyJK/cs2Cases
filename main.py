import random
import database

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
