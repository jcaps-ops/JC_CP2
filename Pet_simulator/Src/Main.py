from storage import *
from actions import *

def main_menu(CurrentCreature):
    answer = True
    while answer == True:
        ply_repon = input(f"[1] Feed Pet\n[2] Play with Pet\n[3] Put Pet to Sleep\n[4] Check Status\n[5] Save Game\n[6] Load Game/Manage creatures\n[7] Quit\n Which option:")
        if ply_repon == "1":
            CurrentCreature.eat(1)
        elif ply_repon == "2":
            CurrentCreature.play(1)
        elif ply_repon == "3":
            CurrentCreature.sleep()
            input("")
        elif ply_repon == "4":
            print(CurrentCreature.stat_screen())
            input("")
        elif ply_repon == "5":
            StorageSave(CurrentCreature)
            print("These are your saved creatures")
            storageDisplay()
        elif ply_repon == "6":
            subAnswer = True
            while subAnswer == True:
                subResponce = (f"[1].Load game\n[2].Create New pet\n[3]Delete a pet\n[4] to exit")
                if subResponce == "1":
                    temp_counter = storagecounter()
                    if temp_counter != 1:
                        storageDisplay()
                        an = input("What is the name of the creature you want to load")
                        CurrentCreature = StorageLoad(an)
                if subResponce == "2":
                    StorageSave(CurrentCreature)
                    CurrentCreature = Genisis()
                if subResponce == "3":
                    temp_counter = storagecounter()
                    if temp_counter != 1:
                        storageDisplay()
                        ply = input("What is the name of the creature you want to kill:")
                        ply = ply.capitalize()
                        storageDeletion(ply)
                        print("These are the current pets")
                        storageDisplay()
                if subResponce == "4":
                    subAnswer = False
                
temp_counter = storagecounter()
if temp_counter == 0:
    creatureStats = Genisis()
    StorageSave(creatureStats)
else:
    storageDisplay()
    an = input("What is the name of the creature you want to load")
    CurrentCreature = StorageLoad(an)
CurrentCreature = creature(creatureStats[0],creatureStats[1],creatureStats[2],creatureStats[3],creatureStats[4],creatureStats[5],creatureStats[6],creatureStats[7],creatureStats[8],creatureStats[9])
main_menu(CurrentCreature)