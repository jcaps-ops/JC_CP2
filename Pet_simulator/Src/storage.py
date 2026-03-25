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
def storageDeletion(Desired):
    wanted = []
    with open("Pet_simulator/Documentation/pet_info.csv", "r", newline = "") as csvfile:
        for line in csvfile:
            name = []
            name = line.split(",")
            if name[0] == Desired:
                pass
            else:
                temp_wanted = []
                temp_wanted.append(name[0])
                temp_wanted.append(name[1])
                temp_wanted.append(name[2])
                temp_wanted.append(name[3])
                temp_wanted.append(name[4])
                temp_wanted.append(name[5])
                temp_wanted.append(name[6])
                temp_wanted.append(name[7])
                temp_wanted.append(name[8])
                temp_9 = int(name[9])
                temp_wanted.append(temp_9)
                wanted.append(temp_wanted)
    with open("Pet_simulator/Documentation/pet_info.csv", "w", newline = "") as csvfile:
        fieldnames = ["name","species","age","hunger","happiness","energy","timer","days","living","lifespan"]
        writer = csv.writer(csvfile)

    #writer.writerow(fieldnames)
        print(wanted)
        writer.writerows(wanted)
def storagecounter():
    count = 0
    with open("Pet_simulator/Documentation/pet_info.csv", "r", newline = "") as csvfile:
        for line in csvfile:
            count += 1
        return(count)

        
"""
currentBeings = ["Doug","Human",23,8,10,10,0,0,True,24]
StorageSave(currentBeings)
currentBeings = ["james","owl",23,8,10,10,0,0,True,24]
StorageSave(currentBeings)
current = StorageLoad("Doug")
print(current)
"""

"storageDisplay()"
