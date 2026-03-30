import csv
import random
def StorageSave(students):

    with open("Grade_book/Documenation/Student_Storgae.csv", "w", newline = "") as csvfile:
        writer = csv.writer(csvfile)
    #writer.writerow(fieldnames)
        writer.writerows(students)

def StorageLoad():
   with open("Grade_book/Documenation/Student_Storgae.csv", "r", newline = "") as csvfile:
        tempList = []
        for line in csvfile:
            linesplit = line.split(",")
            linesplit[2] = linesplit[2] +"," + linesplit[3]
            tempList.append(linesplit)
        return tempList
            

            
    #writer.writerow(fieldnames)

"""
currentBeings = ["Doug","Human",23,8,10,10,0,0,True,24]
StorageSave(currentBeings)
currentBeings = ["james","owl",23,8,10,10,0,0,True,24]
StorageSave(currentBeings)
current = StorageLoad("Doug")
print(current)
"""

"storageDisplay()"
