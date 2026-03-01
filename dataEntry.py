"""file to enter data into database files
"""

import sys
from database import fields

def writeData(name):
    with open(f"data/{name}.txt") as f:
        counter = f.readlines()
        nextID = len(counter)

    with open(f"data/{name}.txt", "a") as f:
        while True:
            print("\nNEW ITEM")
            entry = []
            for item in fields[name]:
                if type(item) is list:
                    ite = item[1]
                else:
                    ite = item
                
                new = input(f"{ite}: ")
                if not new:
                    break
                entry.append(new)
            if not new:
                break
            write = ",".join(entry)
            print(f"{nextID},{write} written to file")
            f.write(f"{nextID},{write}\n")
            nextID += 1

print("Which database would you like to add to? \n1 for skins, 2 for stickers, 3 for collections, 4 for cases, 5 for collectionCases.")
try:
    choice = int(input("Enter a number: "))
except:
    sys.exit()

if choice == 1:
    print("int id (pk), str name, int weaponid (fk), int quality (fk), float minFloat, float maxFloat, bool stattrak, bool souvenir, bool hasRarePattern, int collectionid (fk)")
    writeData("skins")

elif choice == 2:
    print("int id (pk), str name, int quality (fk), int collectionid (fk)")
    writeData("stickers")

elif choice == 3:
    print("int collectionid (pk), str name")
    writeData("collections")

elif choice == 4:
    print("int caseid (pk), str name")
    writeData("cases")

else:
    print("int id (pk), int collectionid (fk), int caseid (fk)")
    writeData("collectionCases")
