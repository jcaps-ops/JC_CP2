from Booking import *
from Saving import *

def main_menu(book1):
    answer = True
    while answer == True:
        respince = input("Main menu 1 to add a student")
        if respince == "1":
            name = input("What is the students name")
            stuID = input("What is the students ID")
            Currentstudent = student(name,stuID,[0])
            book1.add_student(Currentstudent.name,Currentstudent.id,Currentstudent.grades,Currentstudent.avargeGrade,Currentstudent.letter)
        if respince == "2":
            book1.display_students()
                


book1 = Book("Book1")    
tempstorage = StorageLoad()
for x in tempstorage:
    Currentstudent = student(x[0],x[1],[int(x[2][1] + x[2][2]),int(x[2][5] + x[2][6])])
    book1.add_student(Currentstudent.name,Currentstudent.id,Currentstudent.grades,Currentstudent.avargeGrade,Currentstudent.letter)
main_menu(book1)