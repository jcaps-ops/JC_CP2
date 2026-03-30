from Booking import *
from Saving import *

def main_menu(book1):
    answer = True
    while answer == True:
        respince = input("Main menu 1 to add a student, 2 to view the students 3 to add a grade")
        if respince == "1":
            name = input("What is the students name")
            stuID = input("What is the students ID")
            Currentstudent = student(name,stuID,[0])
            book1.add_student(Currentstudent.name,Currentstudent.id,Currentstudent.grades,Currentstudent.avargeGrade,Currentstudent.letter)
        if respince == "2":
            book1.display_students()
        if respince == "3":
            book1.display_students()
            tempId = input("What is the id of the student")
            tempstudent = book1.finder(tempId)
            grading = True
            while grading:
                newgrade = input("What is the grade (0-100):")
                if newgrade.isnumaric():
                    newgrade = int(newgrade)
                    if newgrade > 0 and newgrade < 101:
                        grading = False
            tempindex = book1.students.index(tempstudent)
            book1.students[tempindex][2].append(newgrade)
            
        


book1 = Book("Book1")    
tempstorage = StorageLoad()
for x in tempstorage:
    Currentstudent = student(x[0],x[1],[int(x[2][1] + x[2][2]),int(x[2][5] + x[2][6])])
    book1.add_student(Currentstudent.name,Currentstudent.id,Currentstudent.grades,Currentstudent.avargeGrade,Currentstudent.letter)
main_menu(book1)