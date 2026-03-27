import csv
import random
def StorageSave(students):

    with open("Grade_book/Documenation/Student_Storgae.csv", "w", newline = "") as csvfile:
        writer = csv.writer(csvfile)
    #writer.writerow(fieldnames)
        writer.writerows(students)

def StorageLoad():
   with open("Grade_book/Documenation/Student_Storgae.csv", "r", newline = "") as csvfile:
        temp = []
        for line in csvfile:
            print(line[0])
            temp.append[line]
        return line
            

            
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

StorageSave([["john",random.randrange(0,2000),[random.randrange(0,100),random.randrange(0,100)]],["john",random.randrange(0,2000),[random.randrange(0,100),random.randrange(0,100)]]])
print(StorageLoad())