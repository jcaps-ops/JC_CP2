import csv

def StorageSave(currentCreature):

    with open("Pet_simulator/Documentation/pet_info.csv", "a", newline = "") as csvfile:
        fieldnames = ["name","species","age","hunger","happiness","energy","timer","days","living","lifespan"]
        writer = csv.writer(csvfile)

    #writer.writerow(fieldnames)
        writer.writerow([currentCreature[0],currentCreature[1],currentCreature[2],currentCreature[3],currentCreature[4],currentCreature[5],currentCreature[6],currentCreature[7],currentCreature[8],currentCreature[9]])

def StorageLoad(Desired):
   with open("Pet_simulator/Documentation/pet_info.csv", "r", newline = "") as csvfile:
        for line in csvfile:
            name = []
            name = line.split(",")
            if name[0] == Desired:
                return(line)
    #writer.writerow(fieldnames)
def storageDisplay():
    with open("Pet_simulator/Documentation/pet_info.csv", "r", newline = "") as csvfile:
        count = 0
        for line in csvfile:
            count += 1
            name = []
            name = line.split(",")
            print(f"{count}:Name:{name[0]},Creature Type:{name[1]}")

        
"""
currentBeings = ["Doug","Human",23,8,10,10,0,0,True,24]
StorageSave(currentBeings)
currentBeings = ["james","owl",23,8,10,10,0,0,True,24]
StorageSave(currentBeings)
current = StorageLoad("Doug")
print(current)
"""

"storageDisplay()"
