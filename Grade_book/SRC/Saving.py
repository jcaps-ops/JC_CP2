import csv
from Booking import *
def StorageSave(BookName,students):

    with open("Grade_book/Documenation/Student_Storgae.csv", "w", newline = "") as csvfile:
        fieldnames = ["name","species","age","hunger","happiness","energy","timer","days","living","lifespan"]
        writer = csv.writer(csvfile)

    #writer.writerow(fieldnames)
        writer.writerows([BookName],students)

def StorageLoad(bookSave):
   with open("Grade_book/Documenation/Student_Storgae.csv", "r", newline = "") as csvfile:
        for line in csvfile:
            
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
